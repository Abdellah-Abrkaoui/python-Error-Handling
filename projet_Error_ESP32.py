from machine import Pin
import time

# Initialize LEDs
green_led = Pin(4, Pin.OUT)
red_led = Pin(2, Pin.OUT)

def control_led(command):
    """
    Controls the LEDs based on user input.
    Raises exceptions for invalid input.
    """
    if command.upper() == "ON":
        green_led.on()  # Turn on Green LED
        red_led.off()   # Turn off Red LED
        print("Green LED is ON")
    elif command.upper() == "OFF":
        green_led.off()  # Turn off Green LED
        print("green LED is off")
    elif command.upper() == "EXIT":
        print("Exiting program...")
        return False  # Signal to exit the program
    else :
        green_led.off()
        for i in range(10):
          red_led.on()
          time.sleep(0.2)  # 200ms on
          red_led.off()
          time.sleep(0.2)  # 200ms off
        raise ValueError(f"Invalid command: {command}. Please use 'ON', 'OFF', or 'EXIT'.")


    return True  # Continue the program

def main():
    """
    Main program loop to control the LEDs.
    """
    print("Enter 'ON' to turn on Green LED, 'OFF' to turn on Red LED, or 'EXIT' to quit.")
    try:
        while True:
            # Wait for a command via the serial input
            command = input_serial("Enter command: ")
            if not control_led(command):  # Exit if command is 'EXIT'
                break
    except Exception as e:
        print(f"Error : {e}")  # Handle exceptions
        
        
    

def input_serial(prompt=""):
    """
    Reads a line of input from the serial interface.
    """
    print(prompt, end="")
    while True:
        line = input()  # Use `sys.stdin.read` if `input()` is unavailable in your setup
        if line:
            return line.strip()

# Run the main program
main()
