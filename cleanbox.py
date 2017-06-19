# I just started learning Python, so the code could probably be a lot better :)
import os, shutil, glob

#Make sure the inbox folder is chosen.
os.chdir("c:\\files\\settings\\Thomas\\Desktop\\Inbox2\\")#Chosen directory

#Look for "PUBG" in filenames.
for file in glob.glob("*PUBG*"):         #Goes through each file in the directory looking for "PUBG"
    if not os.path.exists(".\\Youtube"): #If "PUBG" is found check for "Youtube" folder
        os.mkdir(".\\Youtube")           #If folder is not found make it.
    print(file + " --->> \"Youtube\"")   #Letting the user know which file is being moved to Youtube
    shutil.move(file, ".\\Youtube")      #Move file to the folder

#Files to look for.
imgFiles = (".jpg", ".JPG", ".jpeg", ".png", ".gif") #Images
pyFile = (".py")                                     #python files
installFiles = (".exe", ".msi")                      #files thats typically used to install software.

#Function for the sorting code to eliminate DRY code.
def sorting(fileType, location):
    for file in os.listdir():                        #Goes through each file in the directory
        if file.endswith(fileType):                  #Search for these files
            if not os.path.exists(location):         #If the files are found check for "Images" folder
                os.mkdir(location)                   #If folder is not found make it.
            print(file + " --->> \""+location+"\"")  #Letting the user know what goes where.
            shutil.move(file, location)              #Move file to the folder

sorting(imgFiles, "Images")           #Call sorting function in this case for the images
sorting(pyFile, "Scripts")            #Call sorting function in this case for the python scripts
sorting(installFiles, "Installers")   #Call sorting function in this case for the install files
