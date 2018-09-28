from PIL import Image, ImageFont, ImageDraw, ImageOps
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import csv
import random

#Set names into list
names = []
with open("./patient_stickers/names_test.txt", "r") as file:
    for line in file:
        names.append(line)

stickers = [x[:-2] for x in names]

stickers_list = []
for name in stickers:
    for x in range(4):
        stickers_list.append(name)

print(stickers_list)

index_list = []
for i in range(0, 49):
    i += 1
    index_list.append(i)


###For loop to create full stickers

#Generate name sticker directories
if not os.path.exists("./images/name_stickers"):
    os.makedirs("./images/name_stickers")


#create font for sticker
fnt = ImageFont.truetype('System/Library/Fonts/Arial.ttf', 50)

for name in stickers_list:
    for x in range(1,5):
        from PIL import Image, ImageFont, ImageDraw, ImageOps
        import os
        from os import listdir
        from os.path import isfile, join
        #make sticker background
        sticker_width, sticker_height = int(1.77*300), int(0.5118*300)
        txt_width, txt_height = int(500), int(150)
        sticker = Image.new('RGB', (sticker_width, sticker_height), 'white')
        txt_data = Image.new('RGB', (txt_width, txt_height), 'white')
        #make text fit to sticker
        txt_name = Image.new('RGB', txt_data.size, (255,255,255))
        #create write text to txt
        d_name = ImageDraw.Draw(txt_name)
        d_name.text((0,0), str(name), font = fnt, fill = (0,0,0))
        #paste text and qr on sticker
        sticker.paste(txt_name, (10, 50))
        sticker_with_border = ImageOps.expand(sticker,border=2,fill='black')
        sticker_with_border.save("./images/name_stickers/" + str(name) + str(x) + ".png")
