import time
import Image
import ImageDraw
import ImageEnhance
import subprocess

from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(32,1)

data = subprocess.check_output("githubchart -u blerchin -t svg_square -- | convert - -resize 32x32 bmp:-", shell=True)

image = Image.fromstring("RGBA", (32, 32), data)
image.load()
brightness = ImageEnhance.Brightness(image)
dim_image = brightness.enhance(0.9)
matrix.Fill(0x000000)
matrix.SetPWMBits(1)
matrix.SetImage(image.im.id, 0, 0)
time.sleep(1000)
matrix.Clear()

