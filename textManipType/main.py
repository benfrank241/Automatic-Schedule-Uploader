import string
import pyautogui
import time


def month(x):
    y = x.split()
    print(y[0])
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
    y = x.split()
    if len(y) == 0:
        return
    y[1] = int(y[1])
    for _ in range(y[1]-1):
        pyautogui.press('down')
    return 

def hour(x):
    y = x.split()
    if len(y) == 0:
        return
    if y == 'TBD': #TBD CASE, might need to hit tab
        return
    print (y[3])
    time = y[3].split(":")
    time[0] = int(time[0])
    print (time[0])
    for _ in range(time[0]-1):
        pyautogui.press('down')
        print ("#")
    print (time[1])
    pyautogui.press("tab")
    time[1] = int(time[1])
    div = int(time[1]/5)
    for _ in range(div):
        pyautogui.press('down')
        print ("#")
    pyautogui.press("tab")
    twelve = y[4]
    print(twelve)
    if twelve == 'pm' or 'PM':
        pyautogui.press('down')
        print ("down")
    return 

print ("Five seconds to click correct entry point")

time.sleep(5)

print ("start")


for line in open("typing-data.txt", "r"): #NEED TO SKIP EVERY SECOND LINE

    if line =="":
        pass
    
    month(line)
    pyautogui.press("tab")
    day(line)
    pyautogui.press("tab")

    
    for word in line.split():
        
        if len(word) == 1:
            pass
        elif word in ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]:
            pass
        elif word in ["Home", "Away"]:
            pass
        elif "pm" in word:
            pass
        elif "am" in word:
            pass
        elif "PM" in word:
            pass
        elif "AM" in word:
            pass
        elif word.isdigit():
            pass
        elif "(" in word:
            pass
        elif ")" in word:
            pass
        elif "TBD" in word:
            pass
        elif ":" in word:
            pass
        elif "," in word:
            pyautogui.press("tab")
            pyautogui.typewrite(word  + " ")

            # this gets to the college

        else:
            pyautogui.typewrite(word  + " ")
            print("pause")
            time.sleep(1)
            pass

    pyautogui.press("tab")
    hour(line)


    pyautogui.press("tab")
    pyautogui.press("enter")
    print("Line done, click on correct entrypoint")
    time.sleep(10)
    

           
print ("done")

