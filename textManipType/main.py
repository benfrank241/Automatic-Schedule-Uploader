import string
import pyautogui
import time


# college = open("colleges.txt", "r")

# college_list = []
# for line in college:
#   stripped_line = line.strip()
#   college_list.append(stripped_line)


# def location(h):
#     islocation = any(college_location in h for college_location in college_list)
#     print(islocation)

def month(x):
    y = x.split()
    # print(y[0])
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
        case 'June':
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


time.sleep(5)

print ("start")

# final = []

for line in open("typing-data.txt", "r"):

    # location(line)
    month(line)
    pyautogui.press("tab")
    day(line)
    pyautogui.press("tab")

    
    # if final in college_list:
    #     print("yes")


    for word in line.split():
        if len(word) == 3 or len(word) == 1:
            pass
        elif word in ["(Mon)", "(Tue)", "(Wed)", "(Thu)", "(Fri)", "(Sat)", "(Sun)", "Home", "Away"]:
            pass
        elif ":" in word:
            pass
        elif "pm" in word:
            pass
        elif "am" in word:
            pass
        elif word.isdigit():
            pass

            # this gets to the college

        else:
            pyautogui.typewrite(word  + " ")

    pyautogui.press("enter", presses=2)

    

           
print ("done")

