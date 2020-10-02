#Import Statements

from pygame import mixer
from math import floor as f
import datetime
import time as t

name = input("Enter your Name").capitalize()
print(f"{name}, Welcome to Healthy Programmer!")
print("We will keep reminding you to do your basic tasks again and again.")


def play(sound):
    """
    This function is used to play different sounds.
    This function takes the name of the file as a string
    """
    mixer.init()
    mixer.music.load(sound)
    mixer.music.set_volume(50)
    mixer.music.play(-1)


def time():
    """This function returns us the current time."""
    return t.time()


def water():
    """
    This function is used to deal with all the work related to water drinking.
    This plays the song.
    Then, log the time of drinking water.
    """
    play("water.mp3")
    a = input("Type Drank if you have drank the water").lower()
    while a != "drank":
        a = input("Wrong input type Drank to stop").lower()
    if a == "drank":
        mixer.music.stop()
    file = open("water_log.txt", "a")
    wr = f"{name} drank water at: {datetime.datetime.now()} \n"
    file.write(wr)
    file.close()


def eye():
    """
    This function is used to deal with all the work related to eye exercise.
    This plays the song.
    Then, log the time of doing eye exercise.
    """
    play("eyes.mp3")
    a = input("Type eye if you have done the exercise").lower()
    while a != "eye":
        a = input("Wrong input type eye to stop").lower()
    if a == "eye":
        mixer.music.stop()
    file = open("eye_log.txt", "a")
    wr = f"{name} did eye exercise at: {datetime.datetime.now()} \n"
    file.write(wr)
    file.close()


def exercise():
    """
    This function is used to deal with all the work related to exercise.
    This plays the song.
    Then, log the time of doing exercise.
    """
    play("exercise.mp3")
    a = input("Type done if you have done the exercise").lower()
    while a != "done":
        a = input("Wrong input type done to stop").lower()
    if a == "done":
        mixer.music.stop()
    file = open("exercise_log.txt", "a")
    wr = f"{name} did exercise at: {datetime.datetime.now()} \n"
    file.write(wr)
    file.close()


# Customizable Variables
water_after = 1200  # 20 minutes
eye_after = 1800  # 30 minutes
ex_after = 2700  # 45 minutes

# Non-customizable Variables
start_time = time()
water_time = start_time
eye_time = start_time
ex_time = start_time


''' This while loop does all the work. 
Now sometimes all the activities will need to execcute at the same time.
So, we use different if statements that will execute the processes one by one.  
'''
while True:
    x = f(time() - water_time) > water_after
    y = f(time() - eye_time) > eye_after
    z = f(time() - ex_time) > ex_after
    if x and y and z:
        water()
        water_time = time()
        eye()
        eye_time = time()
        exercise()
        ex_time = time()

    elif x and y:
        water()
        water_time = time()
        eye()
        eye_time = time()

    elif y and z:
        eye()
        eye_time = time()
        exercise()
        ex_time = time()

    elif x and z:
        water()
        water_time = time()
        exercise()
        ex_time = time()

    elif x:
        water()
        water_time = time()

    elif y:
        eye()
        eye_time = time()

    elif z:
        exercise()
        ex_time = time()
