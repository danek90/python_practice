from PIL import Image, ImageFont, ImageDraw, ImageOps
import os
from os import listdir
from os.path import isfile, join
from os import walk

#run page across multiple subdirectories

rootDir = "/Users/dkania/Documents/bloodDrive_20180827/images/tubes_stickers/"

###Attach Full stickers to final page

def print_to_page(dir_path):
    for dirName, subdirList, fileList in os.walk(dir_path):
        print(int(dirName[-3:]))
'''
        print('Directory: {}'.format(dirName))
        for fname in sorted(fileList):
            print('{}'.format(fname))

        #make page for stickers
        outer_page_width, outer_page_height = int(8.5 * 300), int(11 * 300)
        outer_page = Image.new('RGB', (outer_page_width, outer_page_height), 'white')
        page_width, page_height = int(2150), int(3050)
        page = Image.new('RGB', (page_width, page_height), 'white')
        p_w, p_h = page.size

        #path
        path = "{}".format(dir_path)
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

        page.save("./images/output/tube_temp.png")

        final = Image.open("./images/output/tube_temp.png")

        outer_page.paste(final, (220, 182))
        outer_page.save("./images/output/{}_output_tube.png".format(subdirList))
        os.remove("./images/output/tube_temp.png")

        outer_page.show()
'''

def main():
    print_to_page(rootDir)


if __name__ == '__main__':
    main()
