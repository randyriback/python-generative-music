
# if sys.argv[1] == 'drone': 
#     drone() 
# elif sys.argv[1] == 'drums':
#     drums()
# else:
#     bass()


# loop(saw(sleep))

# def drums():
#     start = time() #init timer
#     elapsed = 0
#     while elapsed < TIME_LIMIT: #end loop once TIME_LIMIT has been reached
#         msg = random.choice(kit) #create variable for random drum hit
#         msg.velocity = random.randint(70,105) #randomly assign value to drum's velocity attribut
#         outport.send(msg) #send midi message to Ableton
#         sleep(random.uniform(0.08, 0.2)) #randomly set delay in loop execution for "improvised feel"
#         elapsed = time() - start #check current time status

# def sweep():
#     start = time() #init timer
#     elapsed = 0
#     while elapsed < TIME_LIMIT: #end loop once TIME_LIMIT has been reached
#         for i in values:
#             if elapsed < TIME_LIMIT:
#                 filter.value = i
#                 outport.send(filter)
#                 sleep(.1)
#                 elapsed = time() - start
#             else:
#                 break

# song = Song(outport=mido.open_output('IAC Driver randymidi'), time_limit=60)
# t = Thread(target=song.onoff(synth))
# t = Thread(target=song.lfo(filter, ...))