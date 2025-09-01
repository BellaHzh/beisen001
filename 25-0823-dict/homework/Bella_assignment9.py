import urllib.request
import ssl
import os
dir = os.path.dirname(__file__)
ssl._create_default_https_context = ssl._create_unverified_context
print("Your Weather Report")
print()
print("Current observations are available for: \n- New York \n- Cape May\n- San Francisco\n- Los Angeles")
print()
available_choice = ["New York", "Cape May", "San Francisco", "Los Angeles"]
choice = input("Enter the city you would like a weather report for: ").title()
while choice not in available_choice:
    choice = input("No data available. Please try another city: ").title()
print("Accessing weather data . . .")
print()
if choice == "New York":
    abbreviation = "KLGA"
elif choice == "Cape May":
    abbreviation = "KWWD"
elif choice == "San Francisco":
    abbreviation = "KSFO"
elif choice == "Los Angeles":
    abbreviation = "KLAX"
url = 'https://forecast.weather.gov/xml/current_obs/'+abbreviation+'.xml'
try:
    page = urllib.request.urlopen(url)
except:
    print("Problem accessing the URL")
else:
    info = {}
    source_code = page.read()
    print(f"The current weather has been accessed for {choice}")
    print()
    source_code = source_code.decode('utf-8')
    index_location_start = source_code.find("<location>")
    length_location = len("<location>")
    index_location_end = source_code.find("</location>")
    index_weather_start = source_code.find("<weather>")
    length_weather = len("<weather>")
    index_weather_end = source_code.find("</weather>")
    index_temperature_start = source_code.find("<temp_f>")
    length_temperature = len("<temp_f>")
    index_temperature_end = source_code.find("</temp_f>")
    index_humidity_start = source_code.find("<relative_humidity>")
    length_humidity = len("<relative_humidity>")
    index_humidity_end = source_code.find("</relative_humidity>")
    index_wind_start = source_code.find("<wind_string>")
    length_wind = len("<wind_string>")
    index_wind_end = source_code.find("</wind_string>")
    index_wind_start = source_code.find("<wind_string>")
    length_wind_dir = len("<wind_string>")
    index_wind_end = source_code.find("</wind_string>")
    index_visibility_start = source_code.find("<visibility_mi>")
    length_visibility = len("<visibility_mi>")
    index_visibility_end = source_code.find("</visibility_mi>")
    location = source_code[index_location_start +
                           length_location:index_location_end]
    weather = source_code[index_weather_start +
                          length_weather:index_weather_end]
    temperature = source_code[index_temperature_start +
                              length_temperature:index_temperature_end]
    humidity = source_code[index_humidity_start +
                           length_humidity:index_humidity_end]
    wind = source_code[index_wind_start +
                       length_wind:index_wind_end]
    visibility = source_code[index_visibility_start +
                             length_visibility:index_visibility_end]
    info['location'] = location
    info['weather'] = weather
    info['temperature'] = temperature+" degrees Fahrenheit"
    info['humidity'] = humidity+"%"
    info['wind'] = wind
    info['visibility'] = visibility+" miles"
    print("Information available:\n- (l)ocation\n- (w)eather\n- (t)emperature\n- (h)umidity\n- (wi)nd\n- (v)isibility")
    infoShortcutMap = {'l': 'location', 'w': 'weather',
                       't': 'temperature', 'h': 'humidity', 'wi': 'wind', 'v': 'visibility'}
    print()
    info_choice = input("What weather information would you like? ")
    while info_choice not in info and info_choice not in infoShortcutMap:
        info_choice = input(
            "No data available, please try another information: ")
    while info_choice in info or info_choice in infoShortcutMap:
        if info_choice in infoShortcutMap:
            info_choice = infoShortcutMap[info_choice]
        print(f"The {info_choice} in {choice} is {info[info_choice]}")
        print()
        info_choice = input(
            "What weather information would you like? Or, to end, enter \"done\". ")
        while (info_choice not in info) and (info_choice != "done") and (info_choice not in infoShortcutMap):
            print("That data is not available")
            print()
            info_choice = input(
                "What weather information would you like? Or, to end, enter \"done\". ")
        if info_choice == "done":
            report = input(
                "Would you like to export the full weather report? (yes/no) ")
            while report != "yes" and report != "no":
                report = input("Please enter \"yes\" or \"no\": ")
            if report == "yes":
                file_name = (f"{choice}_weather_report.txt")
                file_to_write = open(os.path.join(dir, file_name), 'a')
                file_to_write.write(
                    f"Weather for {choice}\n\nLocation: {info['location']}\nWeather: {info['weather']}\nVisibility: {info['visibility']}\nTemperature: {info['temperature']}\nWind: {info['wind']}\nHumidity: {info['humidity']}")
                print("The full weather report has been exported.")
                file_to_write.close()
                break
            elif report == "no":
                break


# Print out the source code of the web page
# print(source_code)
