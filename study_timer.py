#UTF-8
#Made by Leonardo Albuquerque de Abreu 
import os
from playsound import playsound
import pathlib
import keyboard as kb
import time

sq = 0       #Conta as repeticoes do ciclo estudo & descanco

t0 = time.time()

cancel_timer = "shift+home"

print(f"To cancel the clock press '{cancel_timer}' key")

while not kb.is_pressed(cancel_timer):

    t30 = 10
    t5 = 10

    while (t30 > 0 and not kb.is_pressed(cancel_timer)):
        t30 -= 1
        time.sleep(1)
    
    if t30 == 0:
        playsound(str(os.path.dirname(__file__))+r"\Beep\violin_jingle.wav")
        print("teste")

    while (t5 > 0 and not kb.is_pressed(cancel_timer)):
        t5 -= 1
        time.sleep(1)

    if t30 == 0 and t5 == 0:    
        playsound(str(os.path.dirname(__file__))+r"\Beep\short.wav")



t2 = time.time()

tf = int(t2-t0)

thr, tmin, tsec = tf//3600 , (tf%3600)//60, (tf%3600)%60

print("programa desativado. \n             Hr Mi Sec\ntempo total: {:02d}:{:02d}:{:02d}".format(thr,tmin,tsec))
