
#stop snooping, you know who you are.
from PIL import Image
from PIL import ImageDraw
from random import randint
import os

print("YO YO YO! Welcome to the Pretty (un)Intuitive Sketching Software!")
print("When it asks you to erase or draw, type in QUIT instead if you want your drawing to be exported!")
print("By the way, you aren't `drawing` in a normal sense, rather you're screwing around with plotting dots on a board.")
print("Have fun!")
print("")

screen = []

print("Select your picture settings:")
screen_length = int(input("Enter the height of your image: "))
screen_width = int(input("Enter the width of your image: "))
pixel_size = int(input("!MAKE THIS A MULTIPLIE OF YOUR HEIGHT AND WIDTH! Enter the size of each pixel: "))
print("")

print("Now you can choose your pretty colours!\n")
print("You have options here as it supports common colours like `red` and `purple` and hex codes.\n By the way, don't misspell or it will die.\n")
print("If you're too lazy leaving it blank makes it default to black pixels white background")

background_colour = input("Background colour: ")
pixel_colour = input("Pixel colour: ")

if background_colour == "":
    background_colour = "white"
if pixel_colour == "":
    pixel_colour = "black"

im = Image.new("RGB", (screen_width, screen_length), background_colour)

for i in range(screen_length//pixel_size):
    screen.append([])
    for j in range(screen_width//pixel_size):
        screen[i].append("□")

print(len(screen))
def display():
    for i in screen:
        string = ""
        for j in i:
            string += j + " "
        print(string)

select = ""
while select != "QUIT":
    display()
    mode = "■"
    colour = pixel_colour
    select = input("Erase? Y/Enter/QUIT: ").upper()
    if select == "Y":
        mode = "□"
        colour = background_colour
    elif select == "QUIT":
        continue
        
    x = int(input("Enter X Coordinate: ")) - 1
    y = screen_length//pixel_size - int(input("Enter Y Coordinate: "))
    
    screen[y][x] = mode
    
    shape_x = (pixel_size * x,  screen_length - (pixel_size * abs(y-(screen_length//pixel_size))))
    shape_y = (pixel_size * (x+1),  screen_length - (pixel_size * abs(y+1-(screen_length//pixel_size))))
    shape = [shape_x, shape_y]
    rect = ImageDraw.Draw(im)
    rect.rectangle(shape, fill = colour, outline = colour)
    os.system("cls")

im.save("output/"+str(randint(1,1000000000))+".bmp")
im.show()