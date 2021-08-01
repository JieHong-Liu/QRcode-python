import qrcode
from PIL import Image
import cv2
import tkinter as tk


def make_qrcode():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data('https://jiehong-liu.github.io/')
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    logo_display = Image.open('1.jpg')
    logo_display.thumbnail((100, 100))
    logo_pos = ((img.size[0] - logo_display.size[0]) // 2,
                (img.size[1] - logo_display.size[1]) // 2)
    img.paste(logo_display, logo_pos)

    img.save("sample2.png")


def qr_decode():
    im = cv2.imread('sample2.png')
    det = cv2.QRCodeDetector()
    retval, points, straight_qrcode = det.detectAndDecode(im)
    print("The website is", retval)


# make_qrcode() # uncomment this to make your own qrcode

# qr_decode() # uncomment this to decode your qrcode
