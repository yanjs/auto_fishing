from PIL import Image, ImageGrab
import pytesseract
from pynput.mouse import Button, Controller
from time import sleep

def main(left, up, right, down):
    mouse = Controller()
    while True:
        sleep(.5)
        screenshot = ImageGrab.grab()
        screenw = screenshot.size[0]
        screenh = screenshot.size[1]
        text_box = (screenw * left, screenh * up, screenw * right, screenh * down)
        text_img = screenshot.crop(text_box)
        text = pytesseract.image_to_string(text_img)
        if 'splashes' in text:
            mouse.click(Button.right, 1)
            sleep(.5)
            mouse.click(Button.right, 1)
            sleep(4)

if __name__ == "__main__":
    main(.9, .75, 1, .95)
