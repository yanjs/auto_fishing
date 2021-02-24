from PIL import Image, ImageGrab
import pytesseract
from pynput.mouse import Button, Controller
from time import sleep

def main(left, up, right, down):
    mouse = Controller()
    while True:
        sleep(.5)
        screenshot = ImageGrab.grab()
        screenwidth = screenshot.size[0]
        screenheight = screenshot.size[1]
        text_box = (screenwidth * left, screenheight * up, screenwidth * right, screenheight * down)
        text_img = screenshot.crop(text_box)
        text = pytesseract.image_to_string(text_img)
        if 'Splashing' not in text:
            mouse.click(Button.right, 1)
            sleep(4)
            continue
        if 'splashes' in text:
            mouse.click(Button.right, 1)
            sleep(.5)
            mouse.click(Button.right, 1)
            sleep(4)

if __name__ == "__main__":
    main(.8, .7, 1, .95)
