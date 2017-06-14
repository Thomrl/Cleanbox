# I just started learning Python, so the code could probably be a lot better :)
import os, shutil, glob

#Make sure the inbox folder is chosen.
os.chdir("c:\\files\\settings\\Thomas\\Desktop\\Inbox\\")#Chosen directory

#Look for "PUBG" in filenames.

for file in glob.glob("*PUBG*"):
    if not os.path.exists(".\\Youtube"): #If "PUBG" is found check for "Youtube" folder
        os.mkdir(".\\Youtube")           #If folder is not found make it.
    print(file + " --->> \"Youtube\"")
    shutil.move(file, ".\\Youtube")      #Move file to the folder
    
#Look for image files like .jpg.

for file in os.listdir():                #Goes through each file in the directory
    if file.endswith((".jpg", ".JPG", ".jpeg", ".png", ".gif")): #Search for these files
        if not os.path.exists(".\\Images"):#If the files are found check for "Images" folder
            os.mkdir(".\\Images")        #If folder is not found make it.
        print(file + " --->> \"Images\"")
        shutil.move(file, ".\\Images")   #Move file to the folder

#Look for ".py" files

for file in os.listdir():
    if file.endswith((".py")):
        if not os.path.exists(".\\Scripts"):
            os.mkdir(".\\Scripts")
        print(file + " --->> \"Scripts\"")
        shutil.move(file, ".\\Scripts")
        
#Look for ".exe" and ".msi" files

for file in os.listdir():
    if file.endswith((".exe", ".msi")):
        if not os.path.exists(".\\Installers"):
            os.mkdir(".\\Installers")
        print(file + " --->> \"Installers\"")
        shutil.move(file, ".\\Installers")
