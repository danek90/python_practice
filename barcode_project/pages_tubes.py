from PIL import Image, ImageFont, ImageDraw, ImageOps
import os
from os import listdir
from os.path import isfile, join

#run page across multiple subdirectories

outputDir = "/Users/dkania/Documents/bloodDrive_20180827/images/output/"

dir_list = []
for i in range(0, 43):
    i += 1
    i = str(i).zfill(3)
    dir_list.append(i)

print(dir_list)

for page_number in dir_list:
    if not page_number.startswith('.'):
        rootDir = "/Users/dkania/Documents/bloodDrive_20180827/images/tubes_stickers/{}".format(page_number)
        from PIL import Image, ImageFont, ImageDraw, ImageOps
        import os
        from os import listdir
        from os.path import isfile, join
        #make page for stickers
        outer_page_width, outer_page_height = int(8.5 * 300), int(11 * 300)
        outer_page = Image.new('RGB', (outer_page_width, outer_page_height), 'white')
        page_width, page_height = int(2150), int(3050)
        page = Image.new('RGB', (page_width, page_height), 'white')
        p_w, p_h = page.size

        #path
        path = "{}".format(rootDir)
        listing = sorted(os.listdir(path))

        #generate path+filename in a list
        npath = []
        im = []
        for infile in listing:
            im.append(infile)
            npath.append(os.path.join(path, infile))
        from PIL import Image, ImageFont, ImageDraw, ImageOps
        import os
        from os import listdir
        from os.path import isfile, join

        #Loop trhough a given directory and add them to page
        #the range is thus: range(intital location, entire sheet, spacing)
        for i in range(0, p_w, 553):
            for j in range(0, p_h, 191):
                try:
                    filepath = npath.pop(0)
                except IndexError:
                    break
                im = Image.open(filepath)
                page.paste(im, (i,j))
            else:
                continue
            break

        page.save("{}/{}_tube_temp.png".format(rootDir, page_number))


        #paste text and qr on sticker


        final = Image.open("{}/{}_tube_temp.png".format(rootDir, page_number))

        #Draw sequential number on page
        number_font = ImageFont.truetype('System/Library/Fonts/Arial.ttf', 40)
        number_page = Image.new('RGB', outer_page.size, (255,255,255))
        d = ImageDraw.Draw(number_page)
        d.text((0,0), str(page_number), font = number_font, fill = (0,0,0))
        outer_page.paste(number_page, (10, 10))
        outer_page.paste(final, (220, 177))

        outer_page.save("{}/{}_output_tube.png".format(outputDir, page_number))
