import PIL.Image
import time

asciiChar = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize(image, newWidth = 100):
    width, height = image.size
    ratio = height/width
    newHeight = int(newWidth * ratio * 0.6)
    resizeImg = image.resize((newWidth,newHeight))
    return(resizeImg)

def grayAss(image):
    grayImg = image.convert('L')
    return(grayImg)

def assination(image):
    pixels = image.getdata()
    chars = "".join([asciiChar[pixel//25] for pixel in pixels])
    return(chars)

def main(newWidth=100):
    path = input("Enter location to image: ")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "not found")
    newImg = assination(grayAss(resize(image)))
    pixel_count = len(newImg)
    assciImg = '\n'.join(newImg[i:(i+newWidth)] for i in range(0, pixel_count, newWidth))
    print(assciImg)


def assify(newWidth=100):
    i=0
    while i<6570:
        path = "data/frame" + str(i) + ".jpg"
        image = PIL.Image.open(path)
        newImg = assination(grayAss(resize(image)))
        pixel_count = len(newImg)
        assciImg = '\n'.join(newImg[i:(i+newWidth)] for i in range(0, pixel_count, newWidth))
        print(assciImg)
        i+=1
        time.sleep(0.04166)
    print(i)
    

assify()