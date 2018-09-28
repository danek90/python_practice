import pandas as pd
import qrcode
import qrcode.image.svg
from PIL import Image
import random
import os
from os import listdir
from os.path import isfile, join

#Generate barcode_images directory
if not os.path.exists("./images/barcodes_tubes"):
    os.makedirs("./images/barcodes_tubes")

#Create list of numbers to make barcodes from
bar_list = []
for i in range(0, 250):
    i += 1
    i = str(i).zfill(4)
    i = "BWB" + i
    bar_list.append(i)

#All items for each patient barcodes
label_list = []
for tag in bar_list:
    streck = tag + "-streck"
    buffy = tag + "-buffy"
    spin1 = tag + "-spin_1"
    spin2 = tag + "-spin_2"
    spin3 = tag + "-spin_3"
    spin4 = tag + "-spin_4"
    plasma1 = tag + "-plasma_1"
    plasma2 = tag + "-plasma_2"
    plasma3 = tag + "-plasma_3"
    plasma4 = tag + "-plasma_4"
    plasma5 = tag + "-plasma_5"
    label_list.append([streck, buffy, spin1, spin2, spin3, spin4, plasma1,
    plasma2, plasma3, plasma4, plasma5])


#create qr code for each item - png
for label in label_list:
    for name in label:
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 4,
            border = 1,
        )
        qr.add_data("{}".format(name))
        qr.make(fit=True)
        img = qr.make_image()
        img.save(os.path.join("images/barcodes_tubes/","{}.png".format(name)))
