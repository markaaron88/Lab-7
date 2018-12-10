# Team 10 - Tech Life Balance Best Engineers
# Lab 7 Module 3


# This warmup function draws a snowman on the supplied desert image
def drawSnowman():

  # Retrieve desert image
  pic = getPic()
  
  # Make the snowman body
  addOvalFilled(pic, 100, 260, 100, 100, white)
  addOvalFilled(pic, 115, 200, 75, 75, white)
  addOvalFilled(pic, 125, 147, 60, 60, white)
  
  # Add buttons
  addOvalFilled(pic, 150, 330, 5, 5, black)
  addOvalFilled(pic, 150, 295, 5, 5, black)
  addOvalFilled(pic, 150, 250, 5, 5, black)
  
  
  # Make hat
  addRectFilled(pic, 130, 142, 50, 10, black)
  addRectFilled(pic, 138, 112, 35, 30, black)
  
  # Make eyes and pipe
  brown = makeColor(120, 100, 85)
  addOvalFilled(pic, 145, 170, 10, 10, black)
  addOvalFilled(pic, 165, 170, 10, 10, black)
  addLine(pic,160, 190, 180, 200, brown)
  addRectFilled(pic, 178, 196, 5, 5, brown)
  
  # Make right arm
  addLine(pic, 185, 234, 215, 240, brown)
  addLine(pic, 215, 240, 217, 234, brown)
  addLine(pic, 217, 234, 240, 228, brown)
  
  # Make left arm
  addLine(pic, 120, 240, 80, 210, brown)
  addLine(pic, 90, 217, 71, 223, brown)
  addLine(pic, 71, 223, 60, 219, brown)
  
  explore(pic)
  return pic

# This function returns opens a file browser and returns the file
def getPic():
 return makePicture(pickAFile())

# This function receives a source and target image, then
def pyCopy(source, target, targetX, targetY):

  sourceWidth = getWidth( source )
  sourceHeight = getHeight( source )
  targetWidth = getWidth( target )
  targetHeight = getHeight( target )
  
  for x in range( 0, sourceWidth ):
    for y in range( 0, sourceHeight ):
      pixel = getPixel( source, x, y )
      color = getColor( pixel )
      
      if x + targetX < targetWidth - 1 and y + targetY < targetHeight - 1:      
        setColor( getPixel( target, x + targetX, y + targetY ), color )
        
  return target

# This function adds text to the supplied image
def addingText(pic):
  message = "HAPPY THANKSGIVING"
  # setting the font name, style and size
  font = makeStyle(sansSerif, bold, 30)
  # here we have to use the explore(pic) to get the pixel range we want for our wording
  addTextWithStyle(pic, 280, 630, message, font, orange)
  return pic

# This function assembles a collage
def makeCard():
  target = makeEmptyPicture( 950, 1300, white)
  
  #background_Pic "fall_leaves.jpg
  print 'Select Background Image: '
  backgroundPic = getPic()
  
  #group pic: group_photo(1).jpg
  print 'Select Center Image: '
  picture1 = getPic()
  
  #turkey.png
  print 'Select Corner Image: '
  picture2 = getPic()

  #assemble Thanksgiving card
  target = pyCopy(backgroundPic, target, 0,0)
  target=pyCopy(picture1,target, 200, 350)
  target=pyCopy(picture2,target, 500, 200)
  target=pyCopy(picture2,target, 175, 900)
  target=pyCopy(picture2,target, 175, 200)
  target=pyCopy(picture2,target, 500, 900)
  target = addingText(target)
  
  return target