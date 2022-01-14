import pandas as pd
import mido
from mido import Message
from time import sleep
import random
from utils import LFO, loop, Switch_on

df = pd.read_csv('btc.csv')

prices = []

prices_column = df["Price"]

for i in prices_column.values:
    i = i.replace(',','')
    prices.append(round(float(i)))
    
btcmax = max(prices)
midi_value = btcmax // 127
outport = mido.open_output('IAC Driver randymidi')

note = Message('note_on', channel=0, note=77, velocity=100, time=0)
param = Message('control_change', channel=1, control=100, value=1)
filter = Message('control_change', channel=1, control=101, value=1)
stretch = Message('control_change', channel=1, control=101, value=1)

# for i in prices[500::-1]: 
#     x =  i // midi_value  
#     print(x)
#     param.value = x
#     stretch.value = 127 - x
#     outport.send(note)
#     note.velocity = int(random.uniform(70, 127))
#     outport.send(param)
#     outport.send(stretch)    
#     sleep(random.uniform(1.5, 1.8))


print(prices)
# 
# def whitenoise():
#     max = 10
#     counter = 0

#     while counter < max:
#         print(prices)
#         sleep(.2)
#         counter += 1

# whitenoise()

# def sweep(i):
#     filter.value = i
#     outport.send(filter)
#     sleep(.01)


# new_lfo = LFO(sweep, 1, 127)

# sweep(124)


# file = open('btc.csv', 'r')
# lines = file.readlines()[1:]
 
# for line in lines[::-1]:
#     # print(line)
#     x = line.split(',')
#     # if round(float(x[2])) > 999:
#     #     y = x[2]
#     print(x)
#     # else: 
#     #     y = round(float(x[2])) + round(float(x[3]))
    
#     # j = float(y)
#     # print(y)
#     # i = int(x // 14.6)
#     # param.value = x
#     # outport.send(note)
#     # outport.send(param)
#     # print(x)        
#     # sleep(.16)

