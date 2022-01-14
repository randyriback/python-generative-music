import mido
import random
from time import sleep
from mido import Message, MidiTrack

outport = mido.open_output('IAC Driver Bus 1')

shaker = Message('note_on', channel=1, note=64, velocity=random.randint(70,105), time=1)
shaker2 = Message('note_on', channel=1, note=65, velocity=random.randint(70,105), time=1)
tom = Message('note_on', channel=1, note=68, velocity=random.randint(70,127), time=1)
tom2 = Message('note_on', channel=1, note=69, velocity=random.randint(70,127), time=1)
tabla = Message('note_on', channel=1, note=71, velocity=random.randint(70,127), time=1)
tabla2 = Message('note_on', channel=1, note=72, velocity=random.randint(70,127), time=1)
tabla3 = Message('note_on', channel=1, note=74, velocity=random.randint(70,127), time=1)

kit = [shaker, shaker2, tom, tom2, tabla, tabla3, tabla2]

pitch = Message('control_change', channel=2, control=50, value=55)
pitch2 = Message('control_change', channel=2, control=50, value=60)
pitch3 = Message('control_change', channel=2, control=50, value=65)
pitch4 = Message('control_change', channel=2, control=50, value=70)

synth = [pitch, pitch2, pitch3, pitch4]

while True:
    outport.send(random.choice(synth))
    sleep(random.uniform(1.00, 3.2))

