import pathlib
import PIL.Image
import time
import os



asciiChar = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize(image, newWidth = 150):
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

def main(newWidth=150):
    path = input("Enter location to image:   ")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "not found")
    newImg = assination(grayAss(resize(image)))
    pixel_count = len(newImg)
    assciImg = '\n'.join(newImg[i:(i+newWidth)] for i in range(0, pixel_count, newWidth))
    print(assciImg)

def countFrames():
    count=0
    for path in pathlib.Path("./data").iterdir():
        if path.isFile():
            count+=1
    return count

fps = int(input("fps: "))
frames = float(1/fps)



def assify(newWidth=150):
    i=0
    while i<4000:
        path = "data/frame" + str(i) + ".jpg"
        image = PIL.Image.open(path)
        newImg = assination(grayAss(resize(image)))
        pixel_count = len(newImg)
        assciImg = '\n'.join(newImg[i:(i+newWidth)] for i in range(0, pixel_count, newWidth))
        print(assciImg)
        i+=1
        time.sleep(frames)
        os.system("clear")

    
os.system('resize -s 100 46')
assify()