import webbrowser
import pyautogui
import time
import sys
import cv2
from pynput.mouse import Button, Controller

def goClickLeft(x):
    mouse = Controller()
    pyautogui.moveTo(x.left/2 +x.width/4 , x.top/2 + x.height/4)
    mouse.click(Button.left)

def goClickMiddle(x):
    mouse = Controller()
    pyautogui.moveTo(x.left/2 +x.width/4 , x.top/2 + x.height/4)
    mouse.click(Button.middle)

def checkPriceLocations(x):
    count = 0
    locations = {}
    for i in x:
        locations[count] = i.left
        count = count + 1
    deletethese=[]
    for i in range(len(x)):
        try:
            if (abs(locations[i] - locations[i+1]) < 4):
                del locations[i+1]
                deletethese.append(i+1)
        except KeyError:
            pass
    for i in deletethese:
        del x[i]
    return x
    
def hauntedQuest():
    webbrowser.open("https://www.marapets.com/elger.php")
    time.sleep(2)
    count = 0
    while (pyautogui.locateOnScreen("questagain.png", confidence = 0.70) != None) or (pyautogui.locateOnScreen("acceptquest.png") != None):
        count = count + 1
        startquest = pyautogui.locateOnScreen("questagain.png") if (pyautogui.locateOnScreen("questagain.png") != None) else pyautogui.locateOnScreen("acceptquest.png")
        goClickLeft(startquest)
        time.sleep(2)
        x=checkPriceLocations(list(pyautogui.locateAllOnScreen('checkprice.png', confidence=0.90)))
        for i in x:
            goClickLeft(i)
            time.sleep(1)
            buy = pyautogui.locateOnScreen("buyfor.png", confidence = 0.80)
            time.sleep(1)
            goClickMiddle(buy)
            time.sleep(1)
        if pyautogui.locateOnScreen("securitycode.png") != None:
            
            break
        finish = pyautogui.locateOnScreen("completequest.png")
        goClickLeft(finish)
        time.sleep(2)
        print(count)
        if (count % 5 == 0):
            pyautogui.hotkey('option', 'command', 'w')
            webbrowser.open("https://www.marapets.com/elger.php")
            
        
def simerianQuest():
    webbrowser.open("https://www.marapets.com/excavator.php")
    time.sleep(2)
    count = 0
    tabs = 0
    while (pyautogui.locateOnScreen("questagainsim.png", confidence = 0.70) != None) or (pyautogui.locateOnScreen("acceptquest.png", confidence = 0.60) != None):
        count = count + 1
        startquest = pyautogui.locateOnScreen("questagainsim.png", confidence = 0.70) if (pyautogui.locateOnScreen("questagainsim.png") != None) else pyautogui.locateOnScreen("acceptquest.png")
        goClickLeft(startquest)
        time.sleep(2)
        x=checkPriceLocations(list(pyautogui.locateAllOnScreen('checkprice.png', confidence=0.90)))
        for i in x:
            goClickLeft(i)
            time.sleep(1)
            buy = pyautogui.locateOnScreen("buyfor.png", confidence = 0.80)
            time.sleep(1)
            goClickMiddle(buy)
            tabs = tabs + 1
            time.sleep(1)
        if pyautogui.locateOnScreen("securitycode.png") != None:
            print("security code")
            break
        finish = pyautogui.locateOnScreen("completequest.png")
        goClickLeft(finish)
        time.sleep(2)
        if (count % 2 == 0):
            pyautogui.hotkey('command', '9')
            time.sleep(1)
            for i in range(tabs):
                pyautogui.hotkey('command', 'w')
            time.sleep(2)
            tabs = 0
    print("A total of",count," simerian quests were completed")

def carpQuest():
    webbrowser.open("https://www.marapets.com/carpenter.php")
    time.sleep(2)
    count = 0
    tabs = 0
    while (pyautogui.locateOnScreen("carper.png", confidence = 0.60) != None) or (pyautogui.locateOnScreen("acceptquest.png", confidence = 0.60) != None):
        count = count + 1
        startquest = pyautogui.locateOnScreen("carper.png", confidence = 0.60) if (pyautogui.locateOnScreen("carper.png") != None) else pyautogui.locateOnScreen("acceptquest.png")
        goClickLeft(startquest)
        time.sleep(2)
        x=checkPriceLocations(list(pyautogui.locateAllOnScreen('checkprice.png', confidence=0.90)))
        for i in x:
            goClickLeft(i)
            time.sleep(1)
            buy = pyautogui.locateOnScreen("buyfor.png", confidence = 0.80)
            time.sleep(1)
            goClickMiddle(buy)
            tabs = tabs + 1
            time.sleep(1)
        if pyautogui.locateOnScreen("securitycode.png") != None:
            print("security code")
            break
        finish = pyautogui.locateOnScreen("completequest.png")
        goClickLeft(finish)
        time.sleep(2)


        if (count % 2 == 0):
            pyautogui.hotkey('command', '9')
            time.sleep(1)
            for i in range(tabs):
                pyautogui.hotkey('command', 'w')
            time.sleep(2)
            tabs = 0
    print("A total of",count," carp quests were completed")

def travQuest():
    webbrowser.open("https://www.marapets.com/traveller.php")
    time.sleep(2)
    count = 0
    tabs = 0
    while (pyautogui.locateOnScreen("again.png", confidence = 0.60) != None) or (pyautogui.locateOnScreen("acceptquest.png", confidence = 0.60) != None):
        count = count + 1
        startquest = pyautogui.locateOnScreen("again.png", confidence = 0.60) if (pyautogui.locateOnScreen("again.png") != None) else pyautogui.locateOnScreen("acceptquest.png")
        goClickLeft(startquest)
        time.sleep(2)
        x=checkPriceLocations(list(pyautogui.locateAllOnScreen('checkprice.png', confidence=0.90)))
        for i in x:
            goClickLeft(i)
            time.sleep(1)
            buy = pyautogui.locateOnScreen("buyfor.png", confidence = 0.80)
            time.sleep(1)
            goClickMiddle(buy)
            tabs = tabs + 1
            time.sleep(1)
        if pyautogui.locateOnScreen("securitycode.png") != None:
            print("security code")
            break
        finish = pyautogui.locateOnScreen("completequest.png")
        goClickLeft(finish)
        time.sleep(2)


        if (count % 2 == 0):
            pyautogui.hotkey('command', '9')
            time.sleep(1)
            for i in range(tabs):
                pyautogui.hotkey('command', 'w')
            time.sleep(2)
            tabs = 0
    print("A total of",count," trav quests were completed")

def microwaveQuest():
    webbrowser.open("https://www.marapets.com/microwave.php")
    time.sleep(2)
    count = 0
    tabs = 0
    while (pyautogui.locateOnScreen("microwave.png", confidence = 0.60) != None) or (pyautogui.locateOnScreen("acceptquest.png", confidence = 0.60) != None):
        count = count + 1
        startquest = pyautogui.locateOnScreen("microwave.png", confidence = 0.60) if (pyautogui.locateOnScreen("microwave.png") != None) else pyautogui.locateOnScreen("acceptquest.png")
        goClickLeft(startquest)
        time.sleep(2)
        x=checkPriceLocations(list(pyautogui.locateAllOnScreen('checkprice.png', confidence=0.90)))
        for i in x:
            goClickLeft(i)
            time.sleep(1)
            buy = pyautogui.locateOnScreen("buyfor.png", confidence = 0.80)
            time.sleep(1)
            goClickMiddle(buy)
            tabs = tabs + 1
            time.sleep(1)
        if pyautogui.locateOnScreen("securitycode.png") != None:
            print("security code")
            break
        finish = pyautogui.locateOnScreen("completequest.png")
        goClickLeft(finish)
        time.sleep(2)


        if (count % 2 == 0):
            pyautogui.hotkey('command', '9')
            time.sleep(1)
            for i in range(tabs):
                pyautogui.hotkey('command', 'w')
            time.sleep(2)
            tabs = 0
    print("A total of",count," microwave quests were completed")

#microwaveQuest()
travQuest()
simerianQuest()
pyautogui.hotkey('command', 'w')
carpQuest()
pyautogui.hotkey('command', 'w')
#pyautogui.hotkey('command', 'w')


