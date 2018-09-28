from PIL import Image, ImageFont, ImageDraw, ImageOps
import os
from os import listdir
from os.path import isfile, join

###For loop to create full stickers

#Generate 39 tube sticker directories
if not os.path.exists("./images/paperwork_stickers"):
    os.makedirs("./images/paperwork_stickers")

if not os.path.exists("./images/output"):
    os.makedirs("./images/output")

qr_images = [f for f in listdir("./images/barcodes_paperwork") if isfile(join("./images/barcodes_paperwork", f))]
#create font for sticker
fnt = ImageFont.truetype('System/Library/Fonts/Arial.ttf', 50)

for image in qr_images:
    if not image.startswith('.'):
        image_name = image.replace(".png", "")
        image_ID = image_name[0:8]
        image_name = image_name[8:]
        #make sticker background
        sticker_width, sticker_height = int(1.77*300), int(0.5118*300)
        txt_width, txt_height = int(500), int(150)
        sticker = Image.new('RGB', (sticker_width, sticker_height), 'white')
        txt_data = Image.new('RGB', (txt_width, txt_height), 'white')
        #make text fit to sticker
        txt_ID = Image.new('RGB', txt_data.size, (255,255,255))
        txt_name = Image.new('RGB', txt_data.size, (255,255,255))
        #import qr code images
        im = Image.open(os.path.join("./images/barcodes_paperwork","{}".format(image)))
        #create write text to txt
        d_ID = ImageDraw.Draw(txt_ID)
        d_ID.text((0,0), str(image_ID), font = fnt, fill = (0,0,0))
        d_name = ImageDraw.Draw(txt_name)
        d_name.text((0,0), str(image_name), font = fnt, fill = (0,0,0))
        #paste text and qr on sticker
        sticker.paste(txt_ID, (170, 20))
        sticker.paste(txt_name, (170, 80))
        #sticker.paste(txt_name, (250, 75))
        sticker.paste(im, (15, 20))

        sticker_with_border = ImageOps.expand(sticker,border=2,fill='black')
        sticker_with_border.save(os.path.join("./images/paperwork_stickers", "out_{}".format(image)))

'''
###Attach Full stickers to final page

#make page for stickers
outer_page_width, outer_page_height = int(8.5 * 300), int(11 * 300)
outer_page = Image.new('RGB', (outer_page_width, outer_page_height), 'white')
page_width, page_height = m
page = Image.new('RGB', (page_width, page_height), 'white')
p_w, p_h = page.size

#path
path = "/Users/dkania/Documents/bloodDrive_20180827/images/paperwork_stickers/"
listing = sorted(os.listdir(path))

#generate path+filename in a list
npath = []
im = []
for infile in listing:
    im.append(infile)
    npath.append(os.path.join(path, infile))

#Loop trhough a given directory and add them to page
#the range is thus: range(intital location, entire sheet, spacing)
for i in range(0, p_w, 304):
    for j in range(0, p_h, 304):
        try:
            filepath = npath.pop(0)
        except IndexError:
            break
        im = Image.open(filepath)
        page.paste(im, (i,j))
    else:
        continue
    break


outer_page.paste(page, (220, 182))
outer_page.save("./images/output/final_output_paperwork.png")

outer_page.show()
'''
