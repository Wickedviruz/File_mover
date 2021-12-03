#Import av nödvändiga moduler
import os
import shutil
import glob
import time


#Sätter sökvägen för körfilen
Korfil = "/Users/path/to/file/folder/"

while True: 

    #Kollar om platsen "korfil" finns.
    #Finns plasen körs scriptet och sedan väntar 10 sekunder.
    if os.path.exists(Korfil):

        #Input för vart XML filen skapas
        #Output för vart XML filen skall läggas
        XMLinput = "/Users/path/to/file/folder/"
        XMLoutput = "/Users/path/to/file/folder/"

        #Bestämmer vilken fil-typ som skall flyttas
        os.chdir(XMLinput)
        for file in glob.glob("*.XML"):
            shutil.move(XMLinput+'/'+file,XMLoutput)

        #Mappinput för vart mappen skapas
        #Mappoutput för vart mappen skall läggas
        Mappinput = "/Users/path/to/file/folder/"
        Mappoutput = "/Users/path/to/file/folder/"
        
        Mapp = os.listdir(Mappinput)  
        for m in Mapp:
            os.rename(Mappinput + m, Mappoutput + m)

        time.sleep(10)

    #Finns inte platsen så avbryts skriptet
    else:
        break