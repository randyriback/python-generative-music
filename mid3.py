import mido
import random
from threading import Thread
from utils import LFO, loop, Switch_on
from time import sleep, time
from mido import Message
import numpy as np

outport = mido.open_output('IAC Driver randymidi') 
TIME_LIMIT = 600 

sample_a = Message('note_on', channel=1, note=33, velocity=1, time=1)
sample_b = Message('note_on', channel=1, note=34, velocity=1, time=1)
sample_c = Message('note_on', channel=1, note=35, velocity=1, time=1)
sample_d = Message('note_on', channel=1, note=36, velocity=1, time=1)
sample_e = Message('note_on', channel=1, note=37, velocity=1, time=1)
sample_f = Message('note_on', channel=1, note=38, velocity=1, time=1)
sample_g = Message('note_on', channel=1, note=39, velocity=1, time=1)

kit = [sample_a, sample_b, sample_b, sample_c, sample_d, sample_e, sample_f, sample_g]


def drums():
    outport.send(Message('note_on', channel=0, note=60, velocity=125, time=200))
    sleep(3)



def samples():
    msg = random.choice(kit)
    msg.velocity = random.randint(70,105)
    print(msg)
    outport.send(msg) 
    sleep(random.uniform(2.08, 10.2)) 

if __name__ == '__main__': 
    t1 = Thread(target=loop, args=(drums, TIME_LIMIT))

    t1.start()