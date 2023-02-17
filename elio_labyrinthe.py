#control la carte
import board

#control des LED sur le robot
import neopixel

#pour faire des pauses entre les mouvements du robot
import time

#utilisation des ports d'entrées-sorties
from digitalio import DigitalInOut, Direction
import pwmio



#Déclaration des fonctions
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = 0.2, auto_write = False, pixel_order = neopixel.GRB)

#moteurs
PWMfrequency = 50
MoteurDroiteMoins = pwmio.PWMOut(board.IO36, frequency = PWMfrequency)
MoteurDroitePlus = pwmio.PWMOut(board.IO38, frequency = PWMfrequency)
MoteurGaucheMoins = pwmio.PWMOut(board.IO35, frequency = PWMfrequency)
MoteurGauchePlus = pwmio.PWMOut(board.IO37, frequency = PWMfrequency)
# MoteurDroiteMoins.direction = Direction.OUTPUT
# MoteurDroitePlus.direction = Direction.OUTPUT
# MoteurGaucheMoins.direction = Direction.OUTPUT
# MoteurGauchePlus.direction = Direction.OUTPUT

#on a renomme les noms des capteurs
CptG  = DigitalInOut(board.IO4)
CptF  = DigitalInOut(board.IO5)
CptD  = DigitalInOut(board.IO6)
CptAR = DigitalInOut(board.IO7)

#Le robot est équipé de quatre capteurs (CptG, CptF, CptD et CptAR) qui détectent les obstacles autour de lui
#G = gauche, D= Droite, F= Front et AR pour arriere

#La fonction "Detect" lit les capteurs et prend une décision sur la direction à prendre
def Detect():

    #GFD  
    if (CptG.value == False and CptF.value == False and CptD.value == False):
        DemiTour()
    #FD
    elif (CptG.value == True and CptF.value == False and CptD.value == False):
        Gauche45()
    #GF
    elif (CptG.value == False and CptF.value == False and CptD.value == True):
        Gauche45()
    
    #GD
    elif (CptG.value == False and CptF.value == True and CptD.value == False):
        DemiTour()
        #Si CptF est False depuis plus de 2 secondes
   
        
    #D
    elif (CptG.value == True and CptF.value == True and CptD.value == False):
        GoGauche()
    #G
    elif (CptG.value == False and CptF.value == True and CptD.value == True):
        GoDroite()
    #F   
    elif (CptG.value == True and CptF.value == False and CptD.value == True):
        Droite45()
        Droite45()
    else:
        GoDroite()


#note: nos moteurs ne sont pas à la même puissance#le robot recule
def Recule():
    #65535 correspond à la valeur maximale des moteurs, 54500 correspond à la différence avec l'autre moteur pour reculer droit
    MoteurDroiteMoins.duty_cycle = 54500
    MoteurDroitePlus.duty_cycle = 0
    MoteurGaucheMoins.duty_cycle = 65535
    MoteurGauchePlus.duty_cycle = 0
    #jaune
    pixels.fill((255, 255, 0))
    pixels.show()
    time.sleep(0.1)
    print ("Recule")


#le robot recule avant de faire un demi tour à gauche
def DemiTour():
    Recule()
    MoteurDroiteMoins.duty_cycle = 0
    MoteurDroitePlus.duty_cycle = 54500
    MoteurGaucheMoins.duty_cycle = 65535
    MoteurGauchePlus.duty_cycle = 0
    #rouge
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(0.6)
    print ("DemiTour")

#le robot avance en suivant une courbe à droite
def GoDroite():
    MoteurDroiteMoins.duty_cycle = 0
    MoteurDroitePlus.duty_cycle = 0
    MoteurGaucheMoins.duty_cycle = 0
    MoteurGauchePlus.duty_cycle = 65535
    #vert 
    pixels.fill((50,200,50))
    pixels.show()
    #time.sleep(0.8)
    print ("GoDroite")

#le robot avance en suivant une courbe à gauche
def GoGauche():
    MoteurDroiteMoins.duty_cycle = 0
    MoteurDroitePlus.duty_cycle = 54500
    MoteurGaucheMoins.duty_cycle = 0
    MoteurGauchePlus.duty_cycle = 35000
    #cian
    pixels.fill((0, 255, 255))
    pixels.show()
    time.sleep(0.1)
    print ("GoGauche")

#le robot tourne d'environ 45 degres à droite
def Droite45():
    MoteurDroiteMoins.duty_cycle = 54500
    MoteurDroitePlus.duty_cycle = 0
    MoteurGaucheMoins.duty_cycle = 0
    MoteurGauchePlus.duty_cycle = 65535
    #vert clair
    pixels.fill((100,255,50))
    pixels.show()
    time.sleep(0.2)
    print ("Droite45")
    
#le robot tourne d'environ 45 degres à droite
def Gauche45():
    MoteurDroiteMoins.duty_cycle = 0
    MoteurDroitePlus.duty_cycle = 54500
    MoteurGaucheMoins.duty_cycle = 65535
    MoteurGauchePlus.duty_cycle = 0
    #bleu gris 
    pixels.fill((0, 150, 150))
    pixels.show()
    time.sleep(0.2)
    print ("Gauche45")
    
#le robot fait un demi tour sur la droite    
def Droite180():
    MoteurDroiteMoins.duty_cycle = 54500
    MoteurDroitePlus.duty_cycle = 0
    MoteurGaucheMoins.duty_cycle = 0
    MoteurGauchePlus.duty_cycle = 65535
    #vert fonce
    pixels.fill((120,180,50))
    pixels.show()
    time.sleep(0.6)
    print ("Droite180")
    
#le robot fait un demi tour sur la gauche 
def Gauche180():
    MoteurDroiteMoins.duty_cycle = 0
    MoteurDroitePlus.duty_cycle = 65535
    MoteurGaucheMoins.duty_cycle = 65535
    MoteurGauchePlus.duty_cycle = 0
    #bleu
    pixels.fill((0, 255, 255))
    pixels.show()
    time.sleep(0.6)
    print ("Gauche180")
    
#fonction permettant de faire avancer le robot en ligne droite
#comme nos moteurs n'ont pas la même puissance, on a cherché à trouver les bons réglages, constaté environ 17 pourcents d'écart entre nos 2 moteurs
def Avancer():
    MoteurDroiteMoins.duty_cycle = 0
    MoteurDroitePlus.duty_cycle = 54500
    MoteurGaucheMoins.duty_cycle = 0
    MoteurGauchePlus.duty_cycle = 65535
    #jaune
    pixels.fill((255, 255, 0))
    pixels.show()
    time.sleep(0.85)
    print ("Avancer")
