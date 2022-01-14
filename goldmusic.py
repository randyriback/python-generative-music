import pandas as pd
import mido
from mido import Message
from time import sleep
import random
import threading

outport = mido.open_output('IAC Driver randymidi')

note = Message('note_on', channel=0, note=60, velocity=100, time=0)
param = Message('control_change', channel=1, control=100, value=1)
console1 = Message('control_change', channel=1, control=105, value=1)

file = open('gold.csv', 'r')
lines = file.readlines()[1:]

new = []

for line in lines:
    x = line.split(",")
    x = round(float(x[1][:-2]))
    new.append(x)

goldmax = max(new)
gold2midi = max(new) // 127
print(max(new))


def drums():
    for line in lines:
        outport.send(note)
        sleep(random.uniform(.06, .8))  
        file.close()

def cc():
    for line in lines:
        x = line.split(',')
        y = round(float(x[1][:-2]))
        z = int(y // gold2midi)
        console1.value = 127 - z
        param.value = z
        outport.send(param)
        outport.send(console1)
        print(console1.value)        
        sleep(random.uniform(0.1, 0.8))  
        file.close()



if __name__ == '__main__': 
    t1 = threading.Thread(target=drums)
    t2 = threading.Thread(target=cc)

    t1.start()
    t2.start()

