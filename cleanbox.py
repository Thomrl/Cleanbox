# I just started learning Python, so the code could probably be a lot better :)
import glob, os, shutil

# Change directory to the inbox folder
os.chdir("c:\\files\\settings\Thomas\\Desktop\\inbox")

    
# Check every file in inbox for "PUBG" in the filename. If there is, proceed to next if statement.
for file in glob.glob("*PUBG*"):
    # Check if there is a folder called Youtube if not make one.
    if not os.path.exists("c:\\files\\settings\Thomas\\Desktop\\inbox\\Youtube"):
        os.mkdir("c:\\files\\settings\Thomas\\Desktop\\inbox\\Youtube")
    #
    # prints status text and moves file to its destination
    print(file + " - has been moved to the folder: Youtube")
    shutil.move(file, ".\\Youtube")


# Check every file in inbox, if a file ends with ".py" proceed to next if statement.
for file in os.listdir("c:\\files\\settings\Thomas\\Desktop\\inbox"):
    if file.endswith((".py")):
        # Check if there is a folder called scripts if not make one.
        if not os.path.exists("c:\\files\\settings\Thomas\\Desktop\\inbox\\scripts"):
            os.mkdir("c:\\files\\settings\Thomas\\Desktop\\inbox\\scripts")
        #
        # prints status text and moves file to its destination
        print(file + " - has been moved to the folder: scripts")
        shutil.move(file, ".\\scripts")


# Check every file in inbox, if a file ends with ".jpg | .JPG | .jpeg | .png proceed to next if statement.
for file in os.listdir("c:\\files\\settings\Thomas\\Desktop\\inbox"):
    if file.endswith((".jpg", ".JPG", ".jpeg", ".png")):
        # Check if there is a folder called images if not make one.
        if not os.path.exists("c:\\files\\settings\Thomas\\Desktop\\inbox\\images"):
            os.mkdir("c:\\files\\settings\Thomas\\Desktop\\inbox\\images")
        #
        # prints status text and moves file to its destination
        print(file + " - has been moved to the folder: images")
        shutil.move(file, ".\\images")


# Check every file in inbox, if a file ends with ".exe" or ".msi" proceed to next if statement.
for file in os.listdir("c:\\files\\settings\Thomas\\Desktop\\inbox"):
    if file.endswith((".exe", ".msi")):
        # Check if there is a folder called installers if not make one.
        if not os.path.exists("c:\\files\\settings\Thomas\\Desktop\\inbox\\installers"):
            os.mkdir("c:\\files\\settings\Thomas\\Desktop\\inbox\\installers")
        #
        # prints status text and moves file to its destination
        print(file + " - has been moved to the folder: installers")
        shutil.move(file, ".\\installers")
        
