from WeatherData import GetWeatherData
from MoodToSong import credentials, getArtistURI, musicSearch, selectSong


def WeatherToSong(currentCity, key, useTemp, unitSystem="metric", country=""):

    mood = GetWeatherData(currentCity=currentCity, key=key, useTemperature=useTemp, unitSystem=unitSystem,
                          country=country)

    spotify = credentials()

    playlist = musicSearch(searchInput=mood, spotify=spotify)
    song, imageLink = selectSong(playlist=playlist, spotify=spotify)

    song = str(song)
    songUri = song.split(":")
    songUri = songUri[-1]

    return songUri, imageLink

def getSong(cityAndCountry, useTemp, key):

    cityCountry = cityAndCountry.split()

    city = None
    country = None

    if city != "" and cityAndCountry is not None:
        city = cityCountry[0]

        if len(cityCountry) > 1:
            country = cityCountry[1]

    if useTemp != "Y" and useTemp != "N" and useTemp != "n" and useTemp != "y":
        exit()

    if country is None:
        country = ""

    return WeatherToSong(currentCity=city, key=key, country=country, useTemp=useTemp)
