import pyowm

user = str(input("Enter a city\n")).capitalize()
api_key = "6070f9abd8ee8d257d73d437c9bfff4e"
owm = pyowm.OWM(api_key)
observation = owm.weather_at_place(user)                                                                                            
w = observation.get_weather()





