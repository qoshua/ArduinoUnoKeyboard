import serial
from pynput.keyboard import Controller, Key
#import time

print("To Exit, press CTRL-C")

# Let the user input the COM port
com_port = input("Enter the COM port (e.g., COM3): ")

# Set up the serial port with user-provided COM port
ser = serial.Serial(com_port, 9600)

print("Running...")


# Set up the keyboard controller
keyboard = Controller()

# Track button state to avoid holding down the key
button_pressed = False

def process_joystick(x, y, button):
    global button_pressed
    
    # Define thresholds for movement
    threshold = 100  # Adjust based on the joystick's sensitivity

    if x < 512 - threshold:
        # Move left
        keyboard.press(Key.left)
        keyboard.release(Key.right)  # Ensure the opposite key is released
        print("Left")
    elif x > 512 + threshold:
        # Move right
        keyboard.press(Key.right)
        keyboard.release(Key.left)  # Ensure the opposite key is released
        print("Right")
    else:
        keyboard.release(Key.left)
        keyboard.release(Key.right)

    if y < 512 - threshold:
        # Move up
        keyboard.press(Key.up)
        keyboard.release(Key.down)  # Ensure the opposite key is released
        print("Up")
    elif y > 512 + threshold:
        # Move down
        keyboard.press(Key.down)
        keyboard.release(Key.up)  # Ensure the opposite key is released
        print("Down")
    else:
        keyboard.release(Key.up)
        keyboard.release(Key.down)

    # Handle button press
    if button == 0 and not button_pressed:
        keyboard.press(Key.space)  # Example action: press the spacebar
        button_pressed = True
        print("Space")
    elif button == 1 and button_pressed:
        keyboard.release(Key.space)
        button_pressed = False

try:
    while True:
        # Read the serial input
        if ser.in_waiting > 0:
            serial_input = ser.readline().decode('utf-8').strip()
            x, y, button = map(int, serial_input.split(','))

            # Process joystick input
            process_joystick(x, y, button)

        # Sleep to prevent overloading the CPU
        #time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    ser.close()
