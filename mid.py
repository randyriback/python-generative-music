import mido
import random
import threading
from utils import LFO, loop, Switch_on
from time import sleep, time  
from mido import Message
import numpy as np

outport = mido.open_output('IAC Driver randymidi') 
TIME_LIMIT = 1000

def make_note(channel, note):
    return Message('note_on', channel=channel, note=note, velocity=1, time=1)

def make_cc(channel, control, value):
    return Message('control_change', channel=channel, control=control, value=value)

shaker = make_note(1, 123)
shaker2 = make_note(1, 124)
tom = make_note(1, 68)
tom2 = make_note(1,69)
tabla = make_note(1, 71)
tabla2 = make_note(1, 72)
tabla3 = make_note(1, 74)
kit = [tom, tom2, tabla]

stab = make_note(3, 77)
stab2 = make_note(3, 79)
sub = [stab, stab2]

filter = make_cc(1, 55, 1)
on = make_cc(2, 51, 1)
convolution = make_cc(1, 56, 1)
grainwetdry = make_cc(1, 57, 1)
reaktor = make_cc(1, 60, 1)
looperator = make_cc(1, 90, 1)

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
    sleep(8)

def play_func(i):
    on.value = i
    outport.send(on)

def looperator_mix(i):
    looperator.value = i
    outport.send(looperator)
    sleep(.4)  

if __name__ == '__main__': 
    lfo = LFO(sweep, 20, 70)
    lfo2 = LFO(con, 70, 90)
    lfo3 = LFO(grain, 25, 100)
    lfo4 = LFO(reaktor_filter, 1, 127)
    lfo5 = LFO(looperator_mix, 20, 80)
    play = Switch_on(play_func, TIME_LIMIT) 

    t1 = threading.Thread(target=loop, args=(lfo.step, TIME_LIMIT))
    t2 = threading.Thread(target=loop, args=(drums, TIME_LIMIT))
    t3 = threading.Thread(target=loop, args=(lfo2.step, TIME_LIMIT))
    t4 = threading.Thread(target=loop, args=(bass, TIME_LIMIT))
    t5 = threading.Thread(target=loop, args=(lfo3.step, TIME_LIMIT))
    t5 = threading.Thread(target=loop, args=(lfo3.step, TIME_LIMIT))
    t6 = threading.Thread(target=loop, args=(lfo4.step, TIME_LIMIT))
    t7 = threading.Thread(target=play.toggle_on)
    t8 = threading.Thread(target=loop, args=(lfo5.step, TIME_LIMIT))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()