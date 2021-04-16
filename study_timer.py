#UTF-8
#Made by Leonardo Albuquerque de Abreu 
import os
from playsound import playsound
import pathlib
import keyboard as kb
import time
import sys
from datetime import date as dt

type_study = input("options: reading, programing: ").lower().strip(" ")

if type_study != ("reading" or "programing"):
    type_study = "programing"


print(dt.today())

sq = 0       #Conta as repeticoes do ciclo estudo & descanco

t0 = time.time()

cancel_timer = "shift+home"

print(f"To cancel the clock press '{cancel_timer}' key")

while not kb.is_pressed(cancel_timer):

    t30 = 1500
    t5 = 300

    while (t30 > 0 and not kb.is_pressed(cancel_timer)):
        t30 -= 1

        t2 = time.time()

        tf = int(t2-t0)

        thr, tmin, tsec = tf//3600 , (tf%3600)//60, (tf%3600)%60

        print("timer: {:02d}:{:02d}:{:02d}".format(thr,tmin,tsec),end="",flush=True)
        sys.stdout.flush()
        print("\r",end="",flush=True)
        time.sleep(1)

    if t30 == 0:
        playsound(str(os.path.dirname(__file__))+r"\Beep\short.wav")
        
        
    while (t5 > 0 and not kb.is_pressed(cancel_timer)):
        t5 -= 1
        
        t2 = time.time()

        tf = int(t2-t0)

        thr, tmin, tsec = tf//3600 , (tf%3600)//60, (tf%3600)%60

        print("timer: {:02d}:{:02d}:{:02d}".format(thr,tmin,tsec),end="",flush=True)
        sys.stdout.flush()
        print("\r",end="",flush=True)
        time.sleep(1)

    if t30 == 0 and t5 == 0:    
        playsound(str(os.path.dirname(__file__))+r"\Beep\short.wav")



t2 = time.time()

tf = int(t2-t0)

thr, tmin, tsec = tf//3600 , (tf%3600)//60, (tf%3600)%60
if type_study == "programing":

    with open("Tempo_de_estudo_programacao.txt","a") as time_archive:
        time_archive.write("{} : {:02d}:{:02d}:{:02d}\n".format(dt.today(),thr,tmin,tsec))

elif type_study == "reading":

    with open("Tempo_de_estudo_reading.txt","a") as time_archive1:
        time_archive1.write("{} : {:02d}:{:02d}:{:02d}\n".format(dt.today(),thr,tmin,tsec))

print("programa desativado. \n             Hr Mi Sec\ntempo total: {:02d}:{:02d}:{:02d}".format(thr,tmin,tsec))
