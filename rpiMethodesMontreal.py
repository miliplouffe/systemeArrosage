# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Simple demo of reading and writing the digital I/O of the MCP2300xx as if
# they were native CircuitPython digital inputs/outputs.
# Author: Tony DiCola
import time

# import board
# import busio
# import digitalio
from dataclasses import dataclass
from datetime import datetime, timedelta
from gpiozero import LED
from time import sleep

led = LED(17)
led.on()


class const:
    pinGicleur1 = 23
    pinGicleur2 = 24
    pinGicleur3 = 25
    pinGicleur4 = 26


gicleur1 = LED(const.pinGicleur1)
gicleur2 = LED(const.pinGicleur2)
gicleur3 = LED(const.pinGicleur3)
gicleur4 = LED(const.pinGicleur4)


def initialiseRelaisGicleur(gicleurs):
    global gicleur1, gicleur2, gicleur3,gicleur4
    if gicleurs["1"].ZoneActive==True:
        print ("gicleur 1 initialise")
        gicleur1.on()
    if gicleurs["2"].ZoneActive==True:
        print ("gicleur 2 initialise")
        gicleur2.on()
    if gicleurs["3"].ZoneActive==True:
        print ("gicleur 3 initialise")
        gicleur3.on()
    if gicleurs["4"].ZoneActive==True:
        print ("gicleur 4 initialise")
        gicleur4.on()


def set_relais(nomRelais, statut):
    global relais1, relais2, relais3, relais4

    if statut==True:
        print ("statut True")
        if nomRelais =="1":
            print(" ouverture gicleur 1")
            gicleur1.off()
        if nomRelais =="2":
            gicleur2.off()        
        if nomRelais =="3":
            gicleur3.off()
        if nomRelais =="4":
            gicleur4.off()            
    else:
        gicleur1.on()
        gicleur2.on()
        gicleur3.on()
        gicleur4.on()


def getValeursGicleurs(gicleurs):
    equipementsGicleurs=[]
    if gicleurs["1"].ZoneActive==True:
        if gicleur1.value == 1:
            equipementsGicleurs.append(0)
        else:
            equipementsGicleurs.append(1)
    else:
         equipementsGicleurs.append(-1)
    if gicleurs["2"].ZoneActive==True:
        if gicleur2.value == 1:
            equipementsGicleurs.append(0)
        else:
            equipementsGicleurs.append(1)
    else:
         equipementsGicleurs.append(-1)
    if gicleurs["3"].ZoneActive==True:
        if gicleur3.value == 1:
            equipementsGicleurs.append(0)
        else:
            equipementsGicleurs.append(1)
    else:
         equipementsGicleurs.append(-1)
    if gicleurs["4"].ZoneActive==True:
        if gicleur4.value == 1:
            equipementsGicleurs.append(0)
        else:
            equipementsGicleurs.append(1)
    else:
         equipementsGicleurs.append(-1)
                  
   

    return equipementsGicleurs