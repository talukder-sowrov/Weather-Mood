import spotipy
import spotipy.oauth2 as ouath2
import requests
from bs4 import BeautifulSoup
import re
import random

def credentials():
    credentials = ouath2.SpotifyClientCredentials(
        client_id='c038b169a3c449cca7929e588cbfba17',
        client_secret='a95ec49a358e4426ad04c700210b2b04'
    )

    token = credentials.get_access_token()

    spotify = spotipy.Spotify(auth=token)
    return spotify


def getArtistURI(artist):

    page = requests.get(f"https://www.google.com/search?q={artist}+Spotify")
    soup = BeautifulSoup(page.content, features="html.parser")

    links = soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)"))

    urlPosition = None
    uriLink = None

    for item in links:
        string = str(item)
        if 'open.spotify.com' in string:
            urlPosition = links.index(item)

    if urlPosition is not None:
        uriLink = re.split(":(?=http)", links[urlPosition]["href"].replace("/url?q=", ""))

    if uriLink is not None:
        print(uriLink)


def musicSearch(searchInput, spotify):

    results = spotify.search(q=searchInput, type='playlist', limit=10)
    playlistId = []

    playlistsJSON = results['playlists']['items']

    for playlist in playlistsJSON:
        playlistId.append(playlist['uri'])

    for i in range(0, 4):
        returnedPlaylist = random.choice(playlistId)

    return returnedPlaylist


def selectSong(playlist, spotify):

    results = spotify.user_playlist(user='223nuu6dnoutwvdngp3b3eudy', playlist_id=playlist, fields='tracks')
    tracksJSON = results['tracks']['items']

    tracksId = []
    imageLinks = []

    for track in tracksJSON:
        tracksId.append(track['track']['uri'])
        imageLinks.append(track['track']['album']['images'][1])

    for i in range(0, 10):
        returnedTrack = random.choice(tracksId)

    index = tracksId.index(returnedTrack)
    image = imageLinks[index]["url"]

    return returnedTrack, image
