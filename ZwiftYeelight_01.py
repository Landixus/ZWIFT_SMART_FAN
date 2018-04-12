#!/usr/bin/env python
from yeelight import Bulb
import random
import time
from zwift import Client
import subprocess
timeout = 200

bulb = Bulb("192.168.0.76", auto_on=True, effect="smooth", duration=timeout) #IP Address of your bulb have to be replaced
bulb.set_brightness(50)
bulb.start_music()

#replace your Heart Rate Zone here
Herzfrequenz = 0
Herzschwelle1 = 70
Herzschwelle2 = 90
Herzschwelle3 = 100
Herz_Hyst = 2

cli = Client('YourMailAdress', 'YourPassword')
world = cli.get_world()
players = world.players
friends = players['friendsInWorld']
friend = random.choice(friends)
profile = cli.get_profile()
your_player_id = profile.latest_activity['profile']['id']
player_id = your_player_id


player_state = world.player_status(player_id)
print(player_state.player_state)
print(player_state.heartrate)
while True:
    player_state = world.player_status(player_id)
    print "Herzfrequenz =", (player_state.heartrate)
    Herzfrequenz = (player_state.heartrate)
    if Herzfrequenz >= Herzschwelle1:
        bulb.set_rgb(0, 255, 0)
        time.sleep(1)

    if Herzfrequenz >= Herzschwelle2:
        bulb.set_rgb(255, 255, 0)
        time.sleep(1)

    if Herzfrequenz >= Herzschwelle3:
        bulb.set_rgb(255, 0, 0)
        time.sleep(1)
