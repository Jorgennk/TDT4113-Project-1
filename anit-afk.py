from pynput.keyboard import Key, Controller
import time

k = Controller()


while True:
    time.sleep(10)
    k.press("a")