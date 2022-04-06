import urllib.request
import urllib.parse
import json
import requests
import datetime
import os

CLIENT_ID = "lppkkduzilm1efhb2wsyxnug6r3940"
CLIENT_SECRET = "1cnce8j7yh1a6og51639adf66x5tw0"



def make_request(URL):
    header = {"Client-ID": CLIENT_ID, "Authorization": f"Bearer {get_access_token()}"}

    req = urllib.request.Request(URL, headers=header)
    recv = urllib.request.urlopen(req)

    data = json.loads(recv.read().decode("utf-8"))
    #print(data)
    return(data)


def get_access_token():
    x = requests.post(
        f"https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials")

    return json.loads(x.text)["access_token"]

def stream_request(login):
    global streamer
    streamer = login
    URL = "https://api.twitch.tv/helix/users?login=" + str(streamer)
    data = [make_request(URL)]

    for i, d in enumerate(data, 0):
        id = d["data"][0]["id"]

    d = datetime.datetime.now()
    time = d + datetime.timedelta(minutes = -6)
    rfc_time = time.isoformat('T') + "Z"
    clip_data = [make_request("https://api.twitch.tv/helix/clips?broadcaster_id=" + str(id) + "&started_at=" + str(rfc_time) + "&first=1")] #100max
    print(clip_data)

    for i, c_d in enumerate(clip_data):
        if c_d["data"]:

            clip_link = c_d["data"][0]["url"]
            return clip_link

def name():
    return streamer



