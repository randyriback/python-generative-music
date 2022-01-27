import pandas as pd
import json
import vlc
from time import sleep
import random
import requests
import os
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("wages.csv")
jobs = df['OCC_TITLE']
new = []

token = os.getenv("TOKEN")	
query = ""

for title in jobs:
    query = title
    print(title)
    x = requests.get(f"https://freesound.org/apiv2/search/text/?query={query}&fields=previews&token={token}")
    x_dict = json.loads(x.text)
    j = x_dict["results"]
    for i in j:
        new.append(i["previews"]["preview-hq-mp3"])
    p = vlc.MediaPlayer(random.choice(new))
    print(new)
    p.play()
    sleep(3)
