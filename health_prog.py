from pygame import mixer
from math import floor as f
import datetime
import time as t
print("Welcome to Healthy Programmer!")
print("We will keep reminding you to do your basic tasks again and again.")


def play(sound):
    mixer.init()
    mixer.music.load(sound)
    mixer.music.set_volume(50)
    mixer.music.play(-1)


def time():
    return t.time()


def water():
    play("water.mp3")
    a = input("Type Drank if you have drank the water").lower()
    while a != "drank":
        a = input("Wrong input type Drank to stop").lower()
    if a == "drank":
        mixer.music.stop()
    file = open("water_log.txt", "a")
    wr = "Drank water at: " + str(datetime.datetime.now()) + "\n"
    file.write(wr)
    file.close()


def eye():
    play("eyes.mp3")
    a = input("Type eye if you have done the exercise").lower()
    while a != "eye":
        a = input("Wrong input type eye to stop").lower()
    if a == "eye":
        mixer.music.stop()
    file = open("eye_log.txt", "a")
    wr = "Done eye Exercise at: " + str(datetime.datetime.now()) + "\n"
    file.write(wr)
    file.close()


def exercise():
    play("exercise.mp3")
    a = input("Type done if you have done the exercise").lower()
    while a != "done":
        a = input("Wrong input type done to stop").lower()
    if a == "done":
        mixer.music.stop()
    file = open("exercise_log.txt", "a")
    wr = "Done exercise at: " + str(datetime.datetime.now()) + "\n"
    file.write(wr)
    file.close()


start_time = time()
water_after = 1200 #20 minutes
eye_after = 1800 #30 minutes
ex_after = 2700 #45 minutes
water_time = start_time
eye_time = start_time
ex_time = start_time


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
