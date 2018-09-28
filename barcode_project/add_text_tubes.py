from PIL import Image, ImageFont, ImageDraw, ImageOps
import os
from os import listdir
from os.path import isfile, join

###For loop to create full stickers

#Generate 39 tube sticker directories
if not os.path.exists("./images/tubes_stickers"):
    os.makedirs("./images/tubes_stickers")

if not os.path.exists("./images/output"):
    os.makedirs("./images/output")



qr_images = [f for f in listdir("./images/barcodes_tubes") if isfile(join("./images/barcodes_tubes", f))]
#create font for sticker
fnt = ImageFont.truetype('System/Library/Fonts/Arial.ttf', 25)

for image in qr_images:
    if not image.startswith('.'):
        image_name = image.replace(".png", "")
        #make sticker background
        sticker_width, sticker_height = int(486), int(177)
        sticker = Image.new('RGB', (sticker_width, sticker_height), 'white')
        #make text fit to sticker
        txt = Image.new('RGB', sticker.size, (255,255,255))
        #import qr code images
        im = Image.open(os.path.join("./images/barcodes_tubes","{}".format(image)))
        #create write text to txt
        d = ImageDraw.Draw(txt)
        d.text((0,0), str(image_name), font = fnt, fill = (0,0,0))
        #paste text and qr on sticker
        sticker.paste(txt, (30,20))
        sticker.paste(im, (70, 50))
        #sticker_with_border = ImageOps.expand(sticker,border=2,fill='black')
        sticker.save(os.path.join("./images/tubes_stickers", "out_{}".format(image)))
