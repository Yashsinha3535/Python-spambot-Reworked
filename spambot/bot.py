import pyautogui,time

time.sleep(10)



Script = open("file",'r')

for word in Script:
    pyautogui.typewrite(word)
    pyautogui.press("enter")