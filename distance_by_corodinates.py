import geopy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pyowm

def distance_bot():
    
    api_key = "6070f9abd8ee8d257d73d437c9bfff4e"
    
    city1 = str(input("Enter a city\n")).capitalize()
    city2 = str(input("Enter a city\n")).capitalize()

    geolocator = Nominatim(user_agent = "Distancebot!")
    geolocator1 = Nominatim(user_agent = "Distancebot!")
    
    
    owm = pyowm.OWM(api_key)
    observation1 = owm.weather_at_place(city1)
    observation2 = owm.weather_at_place(city2)
    weather1 = observation1.get_weather()
    weather2 = observation2.get_weather()
    

    def weather01():
        weather01_wind = weather1.get_wind()
        weather01_humidity = weather1.get_humidity()
        weather01_temperature = weather1.get_temperature()
        weather01_cloud = weather1.get_clouds()
        weather01_rain = weather1.get_rain()
        weather01_snow = weather1.get_snow()
        weather01_pressure = weather1.get_pressure()
        weather01_status = weather1.get_status()
        weather01_detailed_status = weather1.get_detailed_status()
        weather01_sunrise_time = weather1.get_sunrise_time()
        
        print(f"Wind = {weather01_wind}\nHumidity = {weather01_humidity}\nTemperature = {weather01_temperature}\nCloud = {weather01_cloud}\nRain = {weather01_rain}\nSnow = {weather01_snow}\nPressure = {weather01_pressure}\nStatus = {weather01_status}\nDetailed Status = {weather01_detailed_status}\nSunrise Time = {weather01_sunrise_time}\n")

    
    location = geolocator.geocode(city1)
    print(location)
    city1_corodinates = (location.latitude, location.longitude)
    print(city1_corodinates)
    weather01()
    
    
    def weather02():
        weather02_wind = weather2.get_wind()
        weather02_humidity = weather2.get_humidity()
        weather02_temperature = weather2.get_temperature()
        weather02_cloud = weather2.get_clouds()
        weather02_rain = weather2.get_rain()
        weather02_snow = weather2.get_snow()
        weather02_pressure = weather2.get_pressure()
        weather02_status = weather2.get_status()
        weather02_detailed_status = weather2.get_detailed_status()
        weather02_sunrise_time = weather2.get_sunrise_time()
        
        print(f"Wind = {weather02_wind}\nHumidity = {weather02_humidity}\nTemperature = {weather02_temperature}\nCloud = {weather02_cloud}\nRain = {weather02_rain}\nSnow = {weather02_snow}\nPressure = {weather02_pressure}\nStatus = {weather02_status}\nDetailed Status = {weather02_detailed_status}\nSunrise Time = {weather02_sunrise_time}\n")

    
    location2 = geolocator1.geocode(city2)
    print(location2)
    city2_corodinates = (location2.latitude, location2.longitude)
    print(city2_corodinates)
    weather02()
    


    result = geodesic(city1_corodinates, city2_corodinates).miles
    return result


print(distance_bot(), "miles")
