from pyvirtualdisplay import Display
from ghost import Ghost
from PIL import Image

display = Display(visible=0, size=(320,240))
display.start()

ghost = Ghost()
ghost.open('http://bbc.uk.com')

# picture name must end with file type
picture = 'imgname.jpg'


ghost.capture_to(picture, selector='body')

img = Image.open(picture)

display.stop()
