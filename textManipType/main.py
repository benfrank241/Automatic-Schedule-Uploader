import string
import pyautogui
import time


def month(x):
    y = x.split()
    if len(y) == 0:
        return
    match y[0]:
        case 'Sep':
            return pyautogui.press('down')
        case 'Oct':
            return pyautogui.press('down', presses = 2)
        case 'Nov':
            return pyautogui.press('down', presses = 3)
        case 'Dec':
            return pyautogui.press('down', presses = 4)
        case 'Jan':
            return pyautogui.press('down', presses = 5)
        case 'Feb':
            return pyautogui.press('down', presses = 6)
        case 'Mar':
            return pyautogui.press('down', presses = 7)
        case 'Apr':
            return pyautogui.press('down', presses = 8)
        case 'May':
            return pyautogui.press('down', presses = 9)
        case 'Jun':
            return pyautogui.press('down', presses = 10)
        case 'Jul':
            return pyautogui.press('down', presses = 11)
        case _:
            return 0 

def day(x):
    if len(x) == 0:
        return
    y = x.split()
    if len(y) == 0:
        return
    y[1] = int(y[1])
    for _ in range(y[1]-1):
        pyautogui.press('down')
    return 

def hour(x):
    if len(x) == 0:
        return
    y = x.split()
    if len(y) == 0:
        return
    if y[3] == 'TBD': #TBD CASE, might need to hit tab
        return
    # print (y[3])
    time = y[3].split(":")
    time[0] = int(time[0])
    # print (time[0])
    for _ in range(time[0]-1):
        pyautogui.press('down')
        # print ("#")
    # print (time[1])
    pyautogui.press("tab")
    time[1] = int(time[1])
    div = int(time[1]/5)
    for _ in range(div):
        pyautogui.press('down')
        # print ("#")
    pyautogui.press("tab")
    twelve = y[4]
    # print(twelve)
    if twelve == "PM":
        pyautogui.press('down')
        # print ("down")
    if twelve == "pm":
        pyautogui.press('down')
        # print ("down")
    return 

print ("Five seconds to click correct entry point")

time.sleep(5)

print ("start")

check = 0

for line in open("typing-data.txt", "r"):

    print("begining inputs")

    if line == "\n":
        # print("skip")
        continue
        
    month(line)
    pyautogui.press("tab")
    day(line)
    pyautogui.press("tab")

    
    for word in line.split():
        
        if len(word) == 1:
            pass
        elif word in ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]:
            pass
        elif word in ["Home", "Away", "Neutral"]:
            pass
        elif word in ["am", "pm", "Am","Pm", "AM", "PM", "Prats"]:
            pass
        elif word.isdigit():
            pass
        elif "(" in word:
            pass
        elif ")" in word:
            pass
        elif "TBD" in word:
            pyautogui.press("tab")
            pyautogui.typewrite(word)
        elif ":" in word:
            pass
        elif word in ["St.", "Mt.", "River", "Cedar", "Rock", "Mt."]:
            pyautogui.press("tab")
            pyautogui.typewrite(word  + " ")
            check = 1
        elif "," in word and check == 0:
            pyautogui.press("tab")
            pyautogui.typewrite(word  + " ")
        elif "," in word and check == 1:
            pyautogui.typewrite(word  + " ")
            check = 0

            # this gets to the college

        else:
            pyautogui.typewrite(word  + " ")
            # print("pause")
            # time.sleep(1)
            pass

    pyautogui.press("tab")
    hour(line)


    pyautogui.press("tab")
    pyautogui.press("enter")
    print("Line done, click on correct entrypoint")
    time.sleep(8)
    

           
print ("Schedule Complete")

