from PIL import Image, ImageFont, ImageDraw, ImageOps
import os
from os import listdir
from os.path import isfile, join

###For loop to create full stickers

#Generate 39 tube sticker directories
if not os.path.exists("./images/boxes_stickers"):
    os.makedirs("./images/boxes_stickers")

if not os.path.exists("./images/output"):
    os.makedirs("./images/output")

qr_images = [f for f in listdir("./images/barcodes_boxes") if isfile(join("./images/barcodes_boxes", f))]
#create font for sticker
fnt = ImageFont.truetype('System/Library/Fonts/Arial.ttf', 40)

for image in qr_images:
    if not image.startswith('.'):
        image_name = image.replace(".png", "")
        image_ID = image_name[0:4]
        image_name = image_name[4:]
        #make sticker background
        sticker_width, sticker_height = int(1.77*300), int(0.5118*300)
        txt_width, txt_height = int(500), int(150)
        sticker = Image.new('RGB', (sticker_width, sticker_height), 'white')
        txt_data = Image.new('RGB', (txt_width, txt_height), 'white')
        #make text fit to sticker
        txt_ID = Image.new('RGB', txt_data.size, (255,255,255))
        txt_name = Image.new('RGB', txt_data.size, (255,255,255))
        #import qr code images
        im = Image.open(os.path.join("./images/barcodes_boxes","{}".format(image)))
        #create write text to txt
        d_ID = ImageDraw.Draw(txt_ID)
        d_ID.text((0,0), str(image_ID), font = fnt, fill = (0,0,0))
        d_name = ImageDraw.Draw(txt_name)
        d_name.text((0,0), str(image_name), font = fnt, fill = (0,0,0))
        #paste text and qr on sticker
        sticker.paste(txt_ID, (150, 20))
        sticker.paste(txt_name, (150, 80))
        #sticker.paste(txt_name, (250, 75))
        sticker.paste(im, (15, 20))

        sticker_with_border = ImageOps.expand(sticker,border=2,fill='black')
        sticker_with_border.save(os.path.join("./images/boxes_stickers", "out_{}".format(image)))
