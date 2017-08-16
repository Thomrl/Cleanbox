# I just started learning Python, so the code could probably be a lot better :)
import os, shutil, glob
os.chdir("c:\\files\\settings\\Thomas\\Desktop\\Inbox")#Chosen directory.

#Functions for the sorting code to eliminate DRY code.
def sortByWord(word, location):    #I want it to look for "word" in the folder and move it to the "location".
    for file in glob.glob(word):                     #Goes through each file in the directory looking for "word".
        if not os.path.exists(location):             #If "word" is found check for "location".
            os.mkdir(location)                       #If "location" is not there, make it.
        print(file + " --->> \""+location+"\"")      #Let the user know what goes where.
        shutil.move(file, location)                  #Move file to folder.

def sortByFile(fileType, location):#Same as the other, this is just for filetype.
    for file in os.listdir():                        #Check every file in the folder
        if file.endswith(fileType):                  #and search for "fileType".
            if not os.path.exists(location):         #If "fileType" is found check for "location".
                os.mkdir(location)                   #If "location" is not there, make it.
            print(file + " --->> \""+location+"\"")  #Let the user know what goes where.
            shutil.move(file, location)              #Move file to folder.

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
