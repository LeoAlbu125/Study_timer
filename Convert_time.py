import numpy as np
import os
import sys
import glob

#Depois juntar tudo em uma class chamada studtime_d

def get_options():
    print(glob.glob("*.txt"))

def convert_time(arq:str = "Tempo_de_estudo_programacao.txt") -> "return list [year,month,day,time(seconds)]":

    with open(arq) as txt:
        t = []
        d_amdts = []

        for x in txt.readlines():
            x = x.replace("\n","").split(" : ")
            t = x[1].split(':')
            ts = int(t[0])*3600 + int(t[1])*60 + int(t[2])
            d = x[0].split("-")
            d_amdts.append([int(d[0]),int(d[1]),int(d[2]),ts])
            
        
        return d_amdts



if __name__ == "__main__":
    print(get_options())
    print(convert_time())
    
