# Write your code here :-)
from microbit import *
import randint

while True:
    display.scroll('roll your die')
    if accelerometer.was_gesture('shake'):
        # drum roll?
        roll_outcome = roll_die(6)
        music_outcome = ''
        if roll_outcome == 1:
            music_outcome = music.WAWAWAWAA
        elif roll_outcome == 6:
            music_outcome = music.POWER_UP
        else: music_outcome = music.BA_DING
        display.show(roll_outcome + '!')
        music.play(music_outcome)


def roll_die(die_size):
    return random.randint(1, die_size)


