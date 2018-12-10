def getluminance(pixel):
  return((getRed(pixel) + getGreen(pixel) + getBlue(pixel)) / 3)

def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = r*0.299 + g*0.587 + b*0.114
    setRed(p,luminance)
    setGreen(p,luminance)
    setBlue(p,luminance)
  return(pic)

def lineDrawing():
  pic = makePicture(pickAFile())
  pic = betterBnW(pic)
  for x in range(0, getWidth(pic) - 1):
    for y in range(0, getHeight(pic) - 1):
      pixel = getPixel(pic, x, y)
      rightPixel = getPixel(pic, x + 1, y)
      bottomPixel = getPixel(pic, x, y + 1)
      basePix = getluminance(pixel)
      rightPix = getluminance(rightPixel)
      bottomPix = getluminance(bottomPixel)
      if ab(basePix - rightPix) > 1 and abs(basePix - bottomPix) > 1:
        setColor(pixel, black)
      else:
        setColor(pixel, white)
  show(pic)