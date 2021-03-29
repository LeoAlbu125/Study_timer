#UTF-8
#Made by Leonardo Albuquerque de Abreu 

from playsound import playsound
import pathlib
import keyboard as kb
import time

sq = 0       #Conta as repeticoes do ciclo estudo & descanco

t0 = time.time()




while not kb.is_pressed("ctrl"):

    t30 = 1800
    t5 = 300

    while (t30 > 0 and not kb.is_pressed("ctrl")):
        t30 -= 1
        time.sleep(1)
    

    playsound(str(pathlib.Path().absolute())+r"\Beep\violin_jingle.wav")
    print("teste")

    while (t5 > 0 and not kb.is_pressed("ctrl")):
        t5 -= 1
        time.sleep(1)
        
    playsound(str(pathlib.Path().absolute())+r"\Beep\short.wav")



t2 = time.time()

tf = int(t2-t0)

thr, tmin, tsec = tf//3600 , (tf%3600)//60, (tf%3600)%60

print("programa desativado. \n             Hr Mi Sec\ntempo total: {:02d}:{:02d}:{:02d}".format(thr,tmin,tsec))
