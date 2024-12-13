import pyautogui
from PIL import ImageGrab
import time

# Configurable Variables
TARGET_COLOR = (75, 219, 106)  # RGB color to detect
CLICK_DELAY_MS = 30  # Delay before the first click in milliseconds

def get_mouse_color():
    # Get the current position of the mouse
    x, y = pyautogui.position()
    # Take a screenshot of the screen
    screen = ImageGrab.grab()
    screen_width, screen_height = screen.size

    # Ensure the mouse position is within screen bounds
    if 0 <= x < screen_width and 0 <= y < screen_height:
        # Get the color of the pixel under the mouse
        return screen.getpixel((x, y)), (x, y)
    else:
        return None, (x, y)

def main():
    click_delay_seconds = CLICK_DELAY_MS / 1000.0  # Convert delay to seconds
    print(f"Move your mouse. Program will wait {CLICK_DELAY_MS} ms before clicking when color {TARGET_COLOR} is detected.")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            color, position = get_mouse_color()
            if color is not None:
                if color == TARGET_COLOR:
                    print(f"Detected color {TARGET_COLOR} at {position}. Waiting {CLICK_DELAY_MS} ms before clicking...")
                    time.sleep(click_delay_seconds)  # Wait before clicking
                    pyautogui.click(position)
                    print(f"Clicked at {position}.")
                    # To avoid continuous detection, you can add additional logic here if needed
            else:
                print(f"Mouse out of bounds at position {position}.")
    except KeyboardInterrupt:
        print("\nProgram terminated.")

if __name__ == "__main__":
    main()
