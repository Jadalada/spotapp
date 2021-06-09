from spotipy.oauth2 import SpotifyOAuth
from datetime import timedelta
from pprint import pprint

import spotipy as sp
import pandas as pd
import numpy as np

import urllib.request
import subprocess
import imageio

import requests.exceptions

setup = pd.read_csv("assets/reqs.txt", sep="=", index_col=0, squeeze=True, header=None)
client_id = setup['client_id']
client_secret = setup['client_secret']
device_name = setup['device_name']
redirect_uri = setup['redirect_uri']
scope = setup['scope']
username = setup['username']

s_STATE = None
r_STATE = None


def authenticate_app():
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        username=username)
    spotify = sp.Spotify(auth_manager=auth_manager)
    return spotify


# Code to check for app running taken from Hugo on Stackoverflow
# https://stackoverflow.com/users/724176/hugo
def check_spotify():
    return int(subprocess.check_output(["osascript",
                                        "-e", "tell application \"System Events\"",
                                        "-e", "count (every process whose name is \"Spotify""\")",
                                        "-e", "end tell"]).strip()) > 0


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
        if len(a) > 27:
            a = f"{a[:25]}..."
        return a
    except TypeError:
        return "No Song Playing!"
    except requests.exceptions.ReadTimeout:
        print("Unable to connect to internet!")


def get_song_name_raw():
    try:
        return spotify.current_playback()['item']['name']
    except TypeError:
        return "No Song Playing!"
    except requests.exceptions.ReadTimeout:
        print("Unable to connect to internet!")


def get_artists():
    sname = get_song_name_raw()
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
            return ", ".join(names) if type(names) == list else names
        except Exception:
            return ""
        except requests.exceptions.ReadTimeout:
            print("Unable to connect to internet!")


def get_volume():
    return spotify.current_playback()['device']['volume_percent']


def get_progress_percent():
    try:
        p = spotify.current_playback()['progress_ms']
        d = spotify.current_playback()['item']['duration_ms']
        return round(p / d * 100).__floor__()
    except Exception:
        return 0


def get_duration():
    try:
        t = str(timedelta(milliseconds=spotify.current_playback()['progress_ms']))
        return t[2:7]
    except TypeError:
        return "0:00"
    except requests.exceptions.ReadTimeout:
        print("Unable to connect to internet!")


def get_album_img():
    try:
        url = spotify.current_playback()['item']['album']['images'][0]['url']
        a = urllib.request.urlopen(url).read()
        return a
    except requests.exceptions.ReadTimeout:
        print("Unable to connect to internet!")


def check_levels(img):
    try:
        f = imageio.imread(img, as_gray=True)
        is_light = np.mean(f) > 127
        return 1 if is_light else 0
    except OSError:
        return -1


def check_state():
    try:
        return spotify.current_playback()['is_playing']
    except TypeError:
        return -1
    except requests.exceptions.ReadTimeout:
        print("Unable to connect to internet!")


def skip():
    try:
        spotify.next_track()
    except requests.exceptions.ReadTimeout:
        print("Unable to connect to internet!")


def back():
    try:
        spotify.previous_track()
    except requests.exceptions.ReadTimeout:
        print("Unable to connect to internet!")


def shuffle():
    try:
        global s_STATE
        s_STATE = True
        if s_STATE:
            spotify.shuffle(False)
            s_STATE = False
        elif not s_STATE:
            spotify.shuffle(True)
            s_STATE = True
    except requests.exceptions.ReadTimeout:
        print("Unable to connect to internet!")


def repeat():
    try:
        global r_STATE
        r_STATE = True
        if r_STATE:
            spotify.repeat(False)
            r_STATE = False
        elif not r_STATE:
            spotify.repeat(True)
            r_STATE = True
    except requests.exceptions.ReadTimeout:
        print("Unable to connect to internet!")


def pause():
    try:
        spotify.pause_playback()
    except requests.exceptions.ReadTimeout:
        print("Unable to connect to internet!")


def resume():
    spotify.start_playback()
