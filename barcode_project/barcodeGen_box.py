import pandas as pd
import qrcode
import qrcode.image.svg
from PIL import Image
import random
import os
from os import listdir
from os.path import isfile, join

#Generate barcode_images directory
if not os.path.exists("./images/barcodes_boxes"):
    os.makedirs("./images/barcodes_boxes")

#Create list of numbers to make barcodes from
bar_list = []
for i in range(0, 6):
    i += 1
    i = str(i).zfill(3)
    i = "BWB" + i
    bar_list.append(i)

#All items for each patient barcodes
label_list = ["BWB-Plasma_Box001", "BWB-Plasma_Box002", "BWB-Plasma_Box003",
                "BWB-Plasma_Box004", "BWB-Plasma_Box005", "BWB-Plasma_Box006", 
                "BWB-Plasma_Box007", "BWB-Plasma_Box008", "BWB-Plasma_Box009",
                "BWB-Plasma_Box010", "BWB-Buffy_Box001", "BWB-Buffy_Box002",
                "BWB-Buffy_Box003", "BWB-Buffy_Box004", "BWB-Buffy_Box005",
                "BWB-Buffy_Box006", "BWB-Buffy_Box007", "BWB-Buffy_Box008",
                "BWB-Buffy_Box009", "BWB-Buffy_Box010"]


#create qr code for each item - png
for name in label_list:
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 4,
        border = 1,
    )
    qr.add_data("{}".format(name))
    qr.make(fit=True)
    img = qr.make_image()
    img.save(os.path.join("images/barcodes_boxes/","{}.png".format(name)))
