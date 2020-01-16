import requests
import random


def weatherMood(overall, temperature, description, useTemperature):

    SUN = ["Happy", "Glad", "Thankful", "Excited", "Funky"]
    CLOUD = ["Self-Reflective", "Wandering", "Thoughtful"]
    RAIN = ["Sad", "Upset", "Cry", "Grief", "Brooding"]
    STORM = ["Anger", "Intense", "Violent", "Destructive"]
    FOG = ["Ominous", "Mysterious", "Silent"]

    moodDict = {"sun": SUN, "cloud": CLOUD, "rain": RAIN, "storm": STORM, "fog": FOG}

    atmosphereMood = ''

    if "sun" in overall or "clear" in overall:
        atmosphereMood = "sun"
    elif "cloud" in overall:
        atmosphereMood = "cloud"
    elif "rain" in overall:
        atmosphereMood = "rain"
    elif "storm" in overall:
        atmosphereMood = "storm"
    elif "fog" in overall:
        atmosphereMood = "fog"

    moodWeather = ''

    if atmosphereMood != '':
        moodWeather = random.choice(moodDict[atmosphereMood])

    EXTREME_COLD = ["freezing", "ice", "antarctica", "frozen"]
    COLD = ["snow", "chills", "chilly", "ice"]
    WARM = ["happy", "flying", "good", "calm"]
    HOT = ["sweat", "panting", "red", "sun"]
    EXTREME_HEAT = ["Exhausted", "burning", "fire", "dry"]

    tempDict = {"extreme cold": EXTREME_COLD, "cold": COLD, "warm": WARM, "hot": HOT, "extreme heat": EXTREME_HEAT}

    temperatureMood = ''
    temp = int(temperature)

    if temp < -10:
        temperatureMood = "extreme cold"
    elif temp >= -10 and temp <= 5:
        temperatureMood = "cold"
    elif temp > 5 and temp <= 15:
        temperatureMood = "warm"
    elif temp > 15 and temp <= 30:
        temperatureMood = "hot"
    elif temp > 30:
        temperatureMood = "extreme heat"

    if temperatureMood != '':
        moodTemp = random.choice(tempDict[temperatureMood])

    if not useTemperature:
        return moodWeather
    else:
        return moodTemp


def GetWeatherData(currentCity, key, useTemperature, unitSystem = "metric", country = ""):

    location = currentCity

    if country != "":
        location = currentCity + "," + country

    url = "https://api.openweathermap.org/data/2.5/weather"
    inputs = {'q': location, 'appid': key, 'units': unitSystem}

    weatherData = requests.get(url=url, params=inputs)

    weatherData.raise_for_status()

    jsonData = weatherData.json()

    weatherData = jsonData["weather"]
    mainData = jsonData["main"]

    description = weatherData[0]["description"]
    weatherStatus = weatherData[0]["main"]
    temperature = mainData["temp"]

    return weatherMood(overall=description, useTemperature=useTemperature, description=weatherStatus,
                       temperature=temperature)



