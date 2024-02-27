# Import the required libraries 
# sudo apt install python3 python3-pil python3-torch python3-torchvision

import glob, os
from PIL import Image
from PIL import ImageEnhance
import torchvision.transforms.functional as Filter

def hue(color=0.5, power=range(0,10), path='checked.png'):
    if color > 0.5 or color < -0.5:
        color = 0.15        
    img = Image.open(path)
    img = Filter.adjust_hue(img, color)
    img = ImageEnhance.Color(img)
    img = img.enhance(power)

    return img

if __name__=="__main__":
    # Single file
    img = hue(0.15, 3, 'image.png')
    img.save('image_hue.png')
    img.show()

    # Multiple files from dir
    for infile in glob.glob("images/*.png"):
        print("Image", infile)
        # Image
        file, ext = os.path.splitext(infile)
        filename = os.path.basename(file)
        # Dir
        dir = 'output'
        if not os.path.exists(dir):
            os.makedirs(dir)        
        # Image         
        im = hue(-0.2, 3, infile)
        im.save(dir + '/' + filename + ext)