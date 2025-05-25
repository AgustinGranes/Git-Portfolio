def weather_calculator(weather):
    if weather <= 0:
        return "Freezing"
    elif weather <= 10:
        return "Cold"  
    elif weather <= 20:
        return "Warm"  
    elif weather <= 30:  
        return "Hot"
    else:
        return "Very Hot"

if __name__ == "__main__":
    temperature = int(input("Enter the temperature in Celsius: "))
    print(weather_calculator(temperature))