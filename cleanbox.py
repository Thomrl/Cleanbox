# I just started learning Python, so the code could probably be a lot better :)
import os, shutil, glob
os.chdir("c:\\files\\settings\\Thomas\\Desktop\\Inbox\\")#Chosen directory.

#Functions for the sorting code to eliminate DRY code.
def sortByWord(word, location):
    for file in glob.glob(word):                     #Goes through each file in the directory looking for word.
        if not os.path.exists(location):             #If "word" is found check for "location".
            os.mkdir(location)                       #If "location" folder is not found, make it.
        print(file + " --->> \""+location+"\"")      #Letting the user know which file is being moved to which folder.
        shutil.move(file, location)                  #Move file to the folder.

def sortByFile(fileType, location):
    for file in os.listdir():                        #Goes through each file in the directory.
        if file.endswith(fileType):                  #Search for these files.
            if not os.path.exists(location):         #If the files are found check for "Images" folder.
                os.mkdir(location)                   #If folder is not found make it.
            print(file + " --->> \""+location+"\"")  #Letting the user know what goes where.
            shutil.move(file, location)              #Move file to the folder.

#Files to look for.
imgFiles = (".jpg", ".JPG", ".jpeg", ".png", ".gif") #Images.
installFiles = (".exe", ".msi")                      #files thats typically used to install software.
rarFiles = (".rar", ".zip")

#Calling the functions.
sortByWord("*PUBG*", "Youtube")          #Call sorting function in this case for the word PUBG.
sortByWord("*Rocket League*", "Youtube")
sortByFile(imgFiles, "Images")           #Call sorting function in this case for image files.
sortByFile(installFiles, "Installers")
sortByFile(rarFiles, "Archives")
