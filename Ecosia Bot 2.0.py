# Author Thor
import pyautogui
from time import sleep
import random
from pyscreeze import ImageNotFoundException


def start():
    class Keyboard:
        # The list where a word gets chosen for later.
        list = ["Lars and Henrik", "Are monkeys cool?", "Who is Kaj Andersen?", "It's always nice help our climate!",
                "Yeet", "United States America", "So ehmm Denmark? Great..", "GuEsS thEy nEvEr miSS hUh?"]
        # Picks a random word from the list.
        write = random.choice(list)

    try:
        # Try and click the 'Searchbar.PNG if found, with grayscale on to make it faster, and a confidence at 0.6 because that's a good
        # value that works very well. Confidence is just how confident the bot is that it's 100% that image it's looking for.
        pyautogui.click(pyautogui.locateCenterOnScreen('Searchbar.PNG', grayscale=True, confidence=0.6))
        # Writes the random word
        pyautogui.write(Keyboard.write)
        sleep(0.1)
        pyautogui.press('enter')
        sleep(0.1)
        pyautogui.click(pyautogui.locateCenterOnScreen('Ecosia2.png', confidence=0.3))
        sleep(0.1)
        # Moves the cursor 20 pixels down the Y-axis, so the Ecosia picture can be used again without confusing the bot.
        pyautogui.move(None, 20)
        sleep(0.2)
        # Jumps to the old tab and closes it.
        pyautogui.hotkey('ctrl', '1'), sleep(0.5), pyautogui.hotkey('ctrl', 'w')
        # And finally prints success if it succeeded.
        print("Success")
        sleep(10)
    # And if it did not, it tries this:
    except ImageNotFoundException:
        print("Image not found, trying another one..")
        try:
            # Tries with another picture from the library, but still the same confidence.
            pyautogui.click(pyautogui.locateCenterOnScreen('Searchbar2.PNG', grayscale=True, confidence=0.6))
            pyautogui.write(Keyboard.write)
            sleep(0.1)
            pyautogui.press('enter')
            sleep(0.1)
            pyautogui.click(pyautogui.locateCenterOnScreen('Ecosia2.png', confidence=0.3))
            sleep(0.1)
            pyautogui.move(None, 20)
            sleep(0.2)
            pyautogui.hotkey('ctrl', '1'), sleep(0.5), pyautogui.hotkey('ctrl', 'w')
            print("Success")
            sleep(10)
        except ImageNotFoundException:
            sleep(1)
            print("Image not found, most likely caused by a server error or timeout.")
            pyautogui.click(pyautogui.locateCenterOnScreen('Ecosia2.png', confidence=0.3))
            pyautogui.moveTo(None, 20)
            sleep(3)
            pyautogui.hotkey('ctrl', '1'), sleep(0.5), pyautogui.hotkey('ctrl', 'w')


while True:
    # Gives you one second from when opening the terminal, to the bot starts doing its magic, and also gives it a little cooldown.
    sleep(1)
    start()
