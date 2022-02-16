import requests
import json
from PIL import Image
# import urllib
import io 
import mido
from mido import Message
import random
from time import sleep

outport = mido.open_output('IAC Driver randymidi') 



# https://collectionapi.metmuseum.org/public/collection/v1/search?isOnView=true&q=sunflower

# x = requests.get("https://images.metmuseum.org/CRDImages/ep/original/DT1567.jpg")

# dict = json.loads(x.text)

im = Image.open("van-gogh.jpeg")

vangogh = list(im.getdata())


# urllib.urlretrieve("https://images.metmuseum.org/CRDImages/ep/original/DT1567.jpg", "van-gogh.jpg")

def make_note(channel, note):
    return Message('note_on', channel=channel, note=note, velocity=127, time=1)

def make_note_off(channel, note):
    return Message('note_off', channel=channel, note=note, velocity=127, time=1)    



# j = make_note(0, 100)
# i = make_note_off(0, 100)
# outport.send(j)
# sleep(.2)
# outport.send(i)


# for r,g,b in vangogh[170000:180000]:
#     r_note = make_note(1, r >> 1)
#     print(r >> 1)
#     r_off = make_note_off(1, r >> 1)
#     g_note = make_note(1, g >> 1)
#     g_off = make_note_off(1, g >> 1)
#     b_note = make_note(1, b >> 1)
#     b_off = make_note_off(1, b >> 1)
#     outport.send(r_note)
#     outport.send(g_note)
#     outport.send(b_note)
#     sleep(random.randint(1,4))
#     outport.send(r_off)
#     outport.send(g_off)
#     outport.send(b_off)
#     sleep(.2)


import math
def countBits(number):
    return int((math.log(number) / math.log(2)) + 1)
 

num = 127
print(countBits(num))
