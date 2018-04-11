#!/usr/bin/env python
import random
import time
from zwift import Client
import RPi.GPIO as GPIO
import subprocess
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
timeout = 200
from yeelight import Bulb
bulb = Bulb("192.168.0.76", auto_on=True, effect="smooth", duration=timeout)
bulb.set_brightness(50)
bulb.start_music()
 
RELAIS_4_GPIO = 21
RELAIS_3_GPIO = 20
RELAIS_2_GPIO = 26
RELAIS_1_GPIO = 19
GPIO.setup(RELAIS_4_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen

#GPIO.output(RELAIS_4_GPIO, GPIO.LOW) # an
GPIO.output(RELAIS_4_GPIO, GPIO.HIGH) # aus
#GPIO.output(RELAIS_3_GPIO, GPIO.LOW) # an
GPIO.output(RELAIS_3_GPIO, GPIO.HIGH) # aus
#GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # aus
GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # aus
#GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus

Herzfrequenz=0
Herzschwelle1=70
Herzschwelle2=90
Herzschwelle3=100
Herz_Hyst=2

cli = Client('mudda@quakeit.de','Recall1234')
world = cli.get_world()
players = world.players
friends= players['friendsInWorld']
friend = random.choice(friends)
#player_id = friend['playerId']

# find Player_id
profile = cli.get_profile()
your_player_id = profile.latest_activity['profile']['id']
player_id = your_player_id
# end find player_id

player_state = world.player_status(player_id)
print(player_state.player_state)
print(player_state.heartrate)
while True:
    player_state = world.player_status(player_id)
    print"Herzfrequenz=",(player_state.heartrate)
    Herzfrequenz=(player_state.heartrate)
    #print"Leistung=",(player_state.power)
    #print"Trittfrequenz=",(player_state.cadence)
    #print"Speed=",(player_state.speed)
    if Herzfrequenz >= Herzschwelle1:
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
	bulb.set_rgb(0, 255, 0)
        #subprocess.call("php /var/www/html/relais.php")
    #else: 
       # if Herzfrequenz <= (Herzschwelle1-Herz_Hyst):
       #     GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus
       #    bulb.set_rgb(255, 0, 0)
       #     time.sleep(1)
    if Herzfrequenz >= Herzschwelle2:
        GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # an
	bulb.set_rgb(255, 255, 0)
	time.sleep(1)
    #else: 
    #    if Herzfrequenz <= (Herzschwelle2-Herz_Hyst):
    #        GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # aus       
    #	    bulb.set_rgb(255, 128, 0)
    #	    time.sleep(1)        
    if Herzfrequenz >= Herzschwelle3:
        GPIO.output(RELAIS_3_GPIO, GPIO.LOW) # an
	bulb.set_rgb(255, 0, 0)
	time.sleep(1)
    #else: 
     #   if Herzfrequenz <= (Herzschwelle3-Herz_Hyst):
      #      GPIO.output(RELAIS_3_GPIO, GPIO.HIGH) # aus       
        

