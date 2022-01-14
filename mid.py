import mido
import random
import threading
from utils import LFO, loop, Switch_on
from time import sleep, time  
from mido import Message
import numpy as np

outport = mido.open_output('IAC Driver randymidi') 
TIME_LIMIT = 1000

tom = Message('note_on', channel=1, note=68, velocity=1, time=1)
tom2 = Message('note_on', channel=1, note=69, velocity=1, time=1)
tabla = Message('note_on', channel=1, note=71, velocity=1, time=1)
tabla2 = Message('note_on', channel=1, note=72, velocity=1, time=1)
tabla3 = Message('note_on', channel=1, note=74, velocity=1, time=1)
kit = [tom, tom2, tabla]

stab = Message('note_on', channel=3, note=77, velocity=100, time=0)
stab2 = Message('note_on', channel=3, note=79, velocity=100, time=0)
sub = [stab, stab2]

filter = Message('control_change', channel=1, control=55, value=1)
stretch = Message('control_change', channel=2, control=51, value=1) 
convolution = Message('control_change', channel=1, control=56, value=1)
grainwetdry = Message('control_change', channel=1, control=57, value=1)
reaktor = Message('control_change', channel=1, control=60, value=1)

def sweep(i):
    filter.value = i
    outport.send(filter)
    sleep(.1)

def reaktor_filter(i): 
    reaktor.value = i
    outport.send(reaktor)
    sleep(.1)

def con(i):
    convolution.value = i
    outport.send(convolution)
    sleep(.1)  

def grain(i):
    grainwetdry.value = i
    outport.send(grainwetdry)
    sleep(.3) 

def drums():
    msg = random.choice(kit)
    msg.velocity = random.randint(70,105)
    outport.send(msg) 
    sleep(random.uniform(0.08, 0.2))  

def bass():
    outport.send(random.choice(sub))
    sleep(random.uniform(8.0, 16.7))

def stretchfunc(i):
    stretch.value = i
    outport.send(stretch)



if __name__ == '__main__': 
    lfo = LFO(sweep, 20, 70)
    lfo2 = LFO(con, 98, 120)
    lfo3 = LFO(grain, 25, 100)
    lfo4 = LFO(reaktor_filter, 1, 127)
    # on = Switch_on(stretchfunc, TIME_LIMIT) 
    # on.toggle_on

    t1 = threading.Thread(target=loop, args=(lfo.step, TIME_LIMIT))
    t2 = threading.Thread(target=loop, args=(drums, TIME_LIMIT))
    t3 = threading.Thread(target=loop, args=(lfo2.step, TIME_LIMIT))
    t4 = threading.Thread(target=loop, args=(bass, TIME_LIMIT))
    t5 = threading.Thread(target=loop, args=(lfo3.step, TIME_LIMIT))
    t5 = threading.Thread(target=loop, args=(lfo3.step, TIME_LIMIT))
    t6 = threading.Thread(target=loop, args=(lfo4.step, TIME_LIMIT))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
