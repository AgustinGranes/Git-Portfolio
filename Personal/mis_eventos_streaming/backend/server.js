const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3001; // Puerto para el backend

app.use(cors());

const TARGET_URL = 'https://streamtp4.com/eventos.html';

function parseEventDateTime(rawDateStr, rawTimeStr) {
    const now = new Date();
    let eventDate = new Date(now);

    const timeMatch = rawTimeStr.match(/(\d{1,2}:\d{2})/);
    if (!timeMatch) {
        console.warn(`Formato de hora no reconocido: ${rawTimeStr} para fecha ${rawDateStr}`);
        return null;
    }
    const [hours, minutes] = timeMatch[1].split(':').map(Number);

    rawDateStr = rawDateStr.toUpperCase();

    if (rawDateStr.includes('HOY')) {
        // Hoy
    } else if (rawDateStr.includes('MAÑANA')) {
        eventDate.setDate(now.getDate() + 1);
    } else {
        const dateParts = rawDateStr.match(/(\d{1,2})\/(\d{1,2})/);
        if (dateParts) {
            const day = parseInt(dateParts[1], 10);
            const month = parseInt(dateParts[2], 10) - 1;

            const currentYear = now.getFullYear();
            eventDate.setFullYear(currentYear, month, day);

            const todayForComparison = new Date(currentYear, now.getMonth(), now.getDate());
            const parsedDateForComparison = new Date(currentYear, month, day);

            if (parsedDateForComparison < todayForComparison) {
                eventDate.setFullYear(currentYear + 1);
            }
        } else {
            console.warn(`Formato de fecha no reconocido: ${rawDateStr}, usando fecha actual como base.`);
        }
    }

    eventDate.setHours(hours, minutes, 0, 0);

    const year = eventDate.getFullYear();
    const month = String(eventDate.getMonth() + 1).padStart(2, '0');
    const day = String(eventDate.getDate()).padStart(2, '0');
    const hourStr = String(hours).padStart(2, '0');
    const minuteStr = String(minutes).padStart(2, '0');

    return `<span class="math-inline">\{year\}\-</span>{month}-<span class="math-inline">\{day\}T</span>{hourStr}:${minuteStr}:00-03:00`; // Asumiendo GMT-3 para Argentina
}

app.get('/api/eventos', async (req, res) => {
    try {
        console.log(`[${new Date().toLocaleString('es-AR')}] Iniciando scraping de ${TARGET_URL}`);
        const { data } = await axios.get(TARGET_URL, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            }
        });

        const $ = cheerio.load(data);
        const scrapedEvents = [];
        let eventIdCounter = 0;

        $('.card-evento').each((index, element) => {
            const card = $(element);
            const name = card.find('h3').text().trim();
            let rawDateTimeText = card.find('p').first().text().trim();
            const linkElement = card.find('.botones-evento a.btn-ver');
            let link = linkElement.attr('href');

            if (link && !link.startsWith('http')) {
                try {
                    const baseUrl = new URL(TARGET_URL);
                    link = new URL(link, baseUrl.origin).href;
                } catch (e) {
                    console.warn(`No se pudo formar URL absoluta para: ${link}`);
                    link = null;
                }
            }

            if (name && rawDateTimeText && link) {
                const dateTimeParts = rawDateTimeText.split(' - ');
                let datePart = "HOY"; 
                let timePart = "";

                if (dateTimeParts.length >= 2) {
                    datePart = dateTimeParts[0].trim();
                    timePart = dateTimeParts.slice(1).join(' - ').trim();
                } else if (dateTimeParts.length === 1) {
                    timePart = dateTimeParts[0].trim();
                }

                const isoDateTime = parseEventDateTime(datePart, timePart);

                if (isoDateTime) {
                    scrapedEvents.push({
                        id: `bkd_evt_${eventIdCounter++}`,
                        name: name,
                        time: isoDateTime,
                        link: link,
                        rawTimeDetails: rawDateTimeText
                    });
                } else {
                    console.warn(`No se pudo parsear fecha/hora para evento: <span class="math-inline">\{name\} con texto "</span>{rawDateTimeText}"`);
                }
            } else {
                // Log si falta alguna información esencial
                 if(!name && !rawDateTimeText && !link) { /* Probablemente un card-evento vacío o separador */ }
                 else { console.warn(`Evento incompleto: Nombre='<span class="math-inline">\{name\}', HoraRaw\='</span>{rawDateTimeText}', Link='${link}'`); }
            }
        });

        console.log(`[${new Date().toLocaleString('es-AR')}] Scraping finalizado. Eventos encontrados: ${scrapedEvents.length}`);
        res.json(scrapedEvents);

    } catch (error) {
        console.error(`[${new Date().toLocaleString('es-AR')}] Error durante el scraping:`, error.message);
        res.status(500).json({ 
            message: 'Error al obtener los eventos del sitio de origen.', 
            error: error.message 
        });
    }
});

app.listen(PORT, () => {
    console.log(`Servidor backend escuchando en http://localhost:${PORT}`);
    console.log(`Endpoint de eventos: http://localhost:${PORT}/api/eventos`);
});