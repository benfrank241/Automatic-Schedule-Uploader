import string
import pyautogui
import time


# f = open("typing-data.txt")
# line_list = f.readlines

# for x in line_list:

def f(x):
    y = x.split()
    # print(y[0])
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
        case 'June':
            return pyautogui.press('down', presses = 10)
        case 'Jul':
            return pyautogui.press('down', presses = 11)
        case _:
            return 0 

def func(x):
    y = x.split()
    print(y[1])
    count = y[1]
    done = pyautogui.press('down', presses = count)
    print (done)
    return done


time.sleep(5)

print ("start")

for line in open("typing-data.txt", "r"):

    f(line)
    pyautogui.press("tab")

    func(line)

    # pyautogui.typewrite(line)
     
    pyautogui.press("enter")

print ("done")

