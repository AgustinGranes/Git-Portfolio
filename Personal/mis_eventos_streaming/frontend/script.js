document.addEventListener('DOMContentLoaded', () => {
    const currentTimeElement = document.getElementById('current-time');
    const eventsContainer = document.getElementById('events-container');
    const notificationElement = document.getElementById('notification');
    let allEvents = [];

    function updateTime() {
        const now = new Date();
        const optionsTime = { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false, timeZone: 'America/Argentina/Buenos_Aires' }; // Mostrar en hora AR
        const optionsDate = { weekday: 'long', day: 'numeric', month: 'long', timeZone: 'America/Argentina/Buenos_Aires' };

        const formattedTime = now.toLocaleTimeString('es-AR', optionsTime);
        const formattedDate = now.toLocaleDateString('es-AR', optionsDate);

        const displayString = `${formattedDate} | ${formattedTime} (ARG)`;
        if (currentTimeElement) {
            currentTimeElement.textContent = displayString;
        }
        document.title = `Eventos Streaming - ${formattedTime}`;

        if (allEvents.length > 0) {
            displayEvents(allEvents); // Re-renderiza para actualizar estados si es necesario
        }
    }

    function copyToClipboard(text) {
        navigator.clipboard.writeText(text)
            .then(() => showNotification('¡Enlace copiado!'))
            .catch(err => {
                console.error('Error al copiar: ', err);
                showNotification('Error al copiar enlace.');
            });
    }

    let notificationTimeout;
    function showNotification(message) {
        if (notificationTimeout) clearTimeout(notificationTimeout);
        notificationElement.textContent = message;
        notificationElement.classList.add('show');
        notificationTimeout = setTimeout(() => {
            notificationElement.classList.remove('show');
        }, 2500);
    }

    function determineEventStatus(eventTimeISO) {
        const now = new Date();
        const eventTime = new Date(eventTimeISO); // La fecha del backend ya tiene el offset -03:00
                                               // new Date() la convertirá a la zona horaria local del navegador,
                                               // pero la comparación de tiempos absolutos será correcta.

        // Duración estimada de un evento: 2.5 horas (150 minutos)
        const EVENT_DURATION_MS = 150 * 60 * 1000; 
        const eventEndTime = new Date(eventTime.getTime() + EVENT_DURATION_MS);

        if (now < eventTime) {
            return { text: 'Próximo', class: 'status-proximo' };
        } else if (now >= eventTime && now < eventEndTime) {
            return { text: 'En Vivo', class: 'status-en-vivo' };
        } else {
            return { text: 'Finalizado', class: 'status-finalizado' };
        }
    }

    function displayEvents(events) {
        if (!eventsContainer) return;
        eventsContainer.innerHTML = ''; 

        if (events.length === 0) {
            eventsContainer.innerHTML = '<p class="loading-text">No hay eventos disponibles o no se pudieron cargar.</p>';
            return;
        }

        events.sort((a, b) => new Date(a.time) - new Date(b.time));

        events.forEach(event => {
            const card = document.createElement('div');
            card.className = 'event-card';

            const nameElement = document.createElement('h3');
            nameElement.textContent = event.name;

            const eventDate = new Date(event.time);
            const timeElement = document.createElement('p');
            timeElement.className = 'event-time';
            timeElement.textContent = eventDate.toLocaleString('es-AR', {
                weekday: 'short', day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit', hour12: false, timeZone: 'America/Argentina/Buenos_Aires'
            }) + ' hs (ARG)';

            const statusInfo = determineEventStatus(event.time);
            const statusElement = document.createElement('div');
            statusElement.className = `event-status ${statusInfo.class}`;
            statusElement.textContent = statusInfo.text;

            const actionsWrapper = document.createElement('div');
            actionsWrapper.className = 'event-actions';

            const viewLink = document.createElement('a');
            viewLink.href = event.link;
            viewLink.textContent = 'Ver Transmisión';
            viewLink.className = 'button button-primary';
            viewLink.target = '_blank';
            viewLink.rel = 'noopener noreferrer';

            const copyButton = document.createElement('button');
            copyButton.textContent = 'Copiar Enlace';
            copyButton.className = 'button button-secondary';
            copyButton.addEventListener('click', (e) => {
                e.stopPropagation(); // Evitar que se active otro click si el botón está dentro de un enlace
                copyToClipboard(event.link);
            });

            actionsWrapper.appendChild(viewLink);
            actionsWrapper.appendChild(copyButton);

            card.appendChild(nameElement);
            card.appendChild(timeElement);
            card.appendChild(statusElement);
            card.appendChild(actionsWrapper);

            eventsContainer.appendChild(card);
        });
    }

    async function fetchEventsFromServer() {
        const backendUrl = 'http://localhost:3001/api/eventos';
        try {
            const response = await fetch(backendUrl);
            if (!response.ok) {
                const errorData = await response.json().catch(() => ({ message: `Error del servidor: ${response.status}` }));
                throw new Error(errorData.message || `Error del servidor: ${response.status}`);
            }
            const events = await response.json();
            return events;
        } catch (error) {
            console.error("Error al obtener eventos del backend:", error);
            throw error; 
        }
    }

    async function loadAndDisplayEvents() {
        try {
            if (eventsContainer) { // Solo muestra "Actualizando" si el contenedor ya está vacío o con mensaje previo
               const currentContent = eventsContainer.querySelector('p.loading-text');
               if(currentContent) currentContent.textContent = 'Actualizando eventos...';
            }
            allEvents = await fetchEventsFromServer();
            displayEvents(allEvents);
        } catch (error) {
            console.error("Error al cargar eventos:", error);
            if (eventsContainer) eventsContainer.innerHTML = `<p class="loading-text">Error al cargar eventos: ${error.message}. <br>Asegúrate de que el servidor backend (Node.js) esté funcionando.</p>`;
        }
    }

    updateTime(); 
    setInterval(updateTime, 1000); 

    loadAndDisplayEvents(); 
    setInterval(loadAndDisplayEvents, 60000); // Actualizar eventos cada 1 minuto (60000 ms)
});