# Author Thor
import pyautogui
from time import sleep
import random
from pyscreeze import ImageNotFoundException


def start():
    class Keyboard:
        list = ["Lars og Henrik", "Er aber seje?", "Hvem er Kaj Andersen?", "Jeg elsker at hjælpe til med miljøet :)",
                "Vom", "Overlund Skole"]
        write = random.choice(list)

    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('Searchbar.PNG', grayscale=True, confidence=0.6))
        pyautogui.write(Keyboard.write)
        sleep(0.1)
        pyautogui.press('enter')
        sleep(0.1)
        pyautogui.click(pyautogui.locateCenterOnScreen('Ecosia2.png', confidence=0.3))
        sleep(0.1)
        pyautogui.move(20, None)
        sleep(0.2)
        pyautogui.hotkey('ctrl', '1'), sleep(0.5), pyautogui.hotkey('ctrl', 'w')
        print("Success")
        sleep(10)
    except ImageNotFoundException:
        try:
            pyautogui.click(pyautogui.locateCenterOnScreen('Searchbar2.PNG', grayscale=True, confidence=0.6))
            pyautogui.write(Keyboard.write)
            sleep(0.1)
            pyautogui.press('enter')
            sleep(0.1)
            pyautogui.click(pyautogui.locateCenterOnScreen('Ecosia2.png', confidence=0.3))
            sleep(0.1)
            pyautogui.move(20, None)
            sleep(0.2)
            pyautogui.hotkey('ctrl', '1'), sleep(0.5), pyautogui.hotkey('ctrl', 'w')
            print("Success")
            sleep(10)
        except ImageNotFoundException:
            sleep(1)
            print("Image not found")
            pyautogui.click(pyautogui.locateCenterOnScreen('Ecosia2.png', confidence=0.3))
            pyautogui.moveTo(20, None)
            sleep(3)
            pyautogui.hotkey('ctrl', '1'), sleep(0.1), pyautogui.hotkey('ctrl', 'w')


while True:
    sleep(1)
    start()
