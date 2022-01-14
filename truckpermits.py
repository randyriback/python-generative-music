import pandas as pd
import numpy as np
import mido
from mido import Message
from time import sleep
import random
from utils import LFO, loop, Switch_on
from datetime import datetime

df = pd.read_csv('permits.csv')
df = df.astype(str)

lat = []
long_ = []
dates = []
dt = []
time_diff = []

lat_column = df["lat"]
long_column = df["long"]

date_format = '%Y-%m-%d %H:%M:%S'
date_time = df['issued_date'].apply(lambda x: datetime.strptime(x, date_format))


outport = mido.open_output('IAC Driver randymidi')

param1 = Message('control_change', channel=1, control=100, value=1)
param2 = Message('control_change', channel=1, control=101, value=1)


for i in date_time.values:
    dt.append(i)

prev_date = date_time[0]
for date in dt:
    current_date = date
    diff = abs(int((current_date-prev_date) / np.timedelta64(1, 's')))
    time_diff.append(float("." + str(diff)))
    prev_date = current_date

print(time_diff)


# for i in lat_column.values:
#     if i == "nan":
#         pass
#     else:
#         i = i.replace(',','')
#         lat.append(int(i[3:5]))

# for i in long_column.values:
#     if i == "nan":
#         pass
#     else:
#         i = i.replace(',','')
#         long_.append(int(i[4:6]))

# lat_max = max(lat)
# lat_midi = lat_max / 127

# long_max = max(long_)
# long_midi = long_max / 127

# print(lat_midi)

# for i in lat:
#     x =  i // lat_midi  
#     param1.value = round(x)
#     outport.send(param1)   
#     sleep(.2)

