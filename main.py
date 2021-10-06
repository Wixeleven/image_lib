from PIL import Image, ImageFilter
im = Image.open("bilde.jpg")
print(im.format, im.size, im.mode)
#im.show()
izmers = (132, 84 )
im.thumbnail(izmers)
im.save("bilde-maza.jpg", im.format)
#im.show()
im = im.rotate(132)
#im.show()
r, g, b = im.split()

im = Image.merge("RGB", (g,r,b))
#im.show()
im = im.filter(ImageFilter.CONTOUR)
im.show()

cropped = im.crop((1,2,100,60))
cropped.show()




