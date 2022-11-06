from pynput import keyboard
from pynput.keyboard import Key


def on_key_release(key):
    if key == Key.right:
        print("West")
    elif key == Key.left:
        print("East")
    elif key == Key.up:
        print("North")
    elif key == Key.down:
        print("South")


with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
