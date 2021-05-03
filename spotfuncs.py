import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
import spotipy as sp
import pandas as pd
from datetime import timedelta
from pprint import pprint
import urllib.request
import requests
import PIL.Image

setup = pd.read_csv("assets/reqs.txt", sep="=", index_col=0, squeeze=True, header=None)
client_id = setup['client_id']
client_secret = setup['client_secret']
device_name = setup['device_name']
redirect_uri = setup['redirect_uri']
scope = setup['scope']
username = setup['username']


def authenticate_app():
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        username=username)
    spotify = sp.Spotify(auth_manager=auth_manager)
    return spotify


def get_device_id(spot):
    devices = spot.devices()
    deviceID = None
    for d in devices['devices']:
        d['name'] = d['name'].replace('’', '\'')
        if d['name'] == device_name:
            deviceID = d['id']
            return deviceID


spotify = authenticate_app()
deviceID = get_device_id(spotify)


def get_song_name():
    try:
        a = spotify.current_playback()['item']['name']
    except TypeError:
        a = "No Song Playing!"
    return a


def get_album_name():
    return spotify.current_playback()['item']['album']['name']


def get_artists():
    sname = get_song_name()
    if sname == "No Song Playing!":
        return ""
    else:
        try:
            length = len(spotify.current_playback()['item']['album']['artists'])
            if length > 1:
                names = []
                for i in range(length):
                    names.append(spotify.current_playback()['item']['album']['artists'][i]['name'])
            else:
                names = spotify.current_playback()['item']['album']['artists'][0]['name']
            if 'feat. ' in sname:
                x = sname.index('feat. ')
                if sname[x + 6:len(sname) - 1] not in names:
                    names.append(sname[x + 6:len(sname) - 1])
            return names
        except:
            return ""


def get_volume():
    return spotify.current_playback()['device']['volume_percent']


def get_all_info():
    name = get_song_name()
    artist = get_artists()
    album = get_album_name()
    print(f"Song:\t\t{name}\nArtist:\t\t{artist}\nAlbum:\t\t{album}")


def get_progress_percent():
    try:
        p = spotify.current_playback()['progress_ms']
        d = spotify.current_playback()['item']['duration_ms']
        return round(p / d * 100).__floor__()
    except:
        return 0


def get_duration():
    try:
        t = str(timedelta(milliseconds=spotify.current_playback()['progress_ms']))
    except TypeError:
        return "0:00"
    return t[2:7]


def get_album_img():
    try:
        url = spotify.current_playback()['item']['album']['images'][0]['url']
        a = urllib.request.urlopen(url).read()
        return a
    except TypeError:
        return None
    except IndexError:
        return None


def skip():
    spotify.next_track()


def back():
    spotify.previous_track()


def shuffle(state):
    spotify.shuffle(state)


def repeat(state):
    spotify.repeat(state)
