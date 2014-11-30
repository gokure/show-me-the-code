#!/bin/env python

# pip install Pillow

from PIL import Image, ImageDraw, ImageFont

img = Image.open("avatar.jpg")

font = ImageFont.truetype("simsun.ttc", 30)

draw = ImageDraw.Draw(img)

draw.text((img.size[1]-20, 10), "4", font=font, fill=(255,0,0,255))

del draw, font

img.save("copy.jpg", quality=80)

img.close()