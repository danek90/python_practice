import pandas as pd
import qrcode
import qrcode.image.svg
from PIL import Image
import random
import os
from os import listdir
from os.path import isfile, join

#Generate barcode_images directory
if not os.path.exists("./images/barcodes_paperwork"):
    os.makedirs("./images/barcodes_paperwork")

#Create list of numbers to make barcodes from
bar_list = []
for i in range(0, 250):
    i += 1
    i = str(i).zfill(4)
    i = "BWB" + i
    bar_list.append(i)
with open('barcode_list.txt', 'w') as file:
    for item in bar_list:
        file.write("{}\n".format(item))

#All items for each patient barcodes
label_list = []
for tag in bar_list:
    patient = tag + "-patient"
    media = tag + "-media_release"
    hipaa = tag + "-HIPAA"
    consent = tag + "-consent"
    medical = tag + "-questionaire"
    kit = tag + "-patient_kit"
    label_list.append([patient, media, hipaa, consent, medical, kit])


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
        img.save(os.path.join("images/barcodes_paperwork/","{}.png".format(name)))


'''
### ??? Figure out how to add text to these qr images ???


#tile images on single page
width, height = int(11 * 300), int(8.5 * 300)
page = Image.new('RGB', (width, height), 'white')
p_w, p_h = page.size

#path
path = "/Users/dkania/Documents/bloodDrive_20180827/barcode_images_test/"
listing = sorted(os.listdir(path))

#generate path+filename in a list
npath = []
im = []
for infile in listing:
    im.append(infile)
    npath.append(os.path.join(path, infile))

#Loop trhough a given directory and add them to page
#the range is thus: range(intital location, entire sheet, spacing)
for i in range(100, p_w, 170):
    for j in range(100, p_h, 170):
        try:
            filepath = npath.pop(0)
        except IndexError:
            break
        im = Image.open(filepath)
        page.paste(im, (i,j))
    else:
        continue
    break

page.save("qr_output.png")


scraps
################################################
image_files = [f for f in listdir("./barcode_images/") if isfile(join("./barcode_images", f))]

with open('label_list.txt', 'w') as file:
    for item in label_list:
        file.write("{}\n".format(item))

#MAKE a real barcode
for bar in bar_list:
    cod = barcode.codex.Code39("{}".format(bar),
    writer = ImageWriter(), add_checksum = False)
    filename = cod.save(os.path.join("barcode_images/","cod_{}".format(bar)))

#Add qr code - svg
for label in label_list:
    for name in label:
        print(name)
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 1,
            border = 2,
        )
        qr.add_data("{}".format(name))
        qr.make(fit=True)
        img = qrcode.make("{}".format(name),
        image_factory=qrcode.image.svg.SvgPathImage
        )
        img.save(os.path.join("./barcode_images/","{}.svg".format(name)))

############################################
'''
