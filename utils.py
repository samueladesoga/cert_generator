# utils.py
from PIL import Image, ImageDraw, ImageFont
import random


def write_name(name: str) -> str:
    # Open the Base certificate image
    img = Image.open("SDN_Certificate.png")  # Replace with your base certificate image name
    # Make the image drawable
    d = ImageDraw.Draw(img)
    # Save all the information we are going to use
    text_color = (18, 48, 134)  # Replace with the color you want the text to be
    font = ImageFont.truetype(
        "Amsterdam.ttf", 190
    )  # Replace with a font of your chosing (or remove this if you dont want to use a font). Change the number to change font size
    # Insert the text to the location, with the person's name as text and fill the text in the color of our choice (and use the selected font)
    text_width, text_height = d.textbbox((0, 0), name, font=font)[2:4]
    image_width, image_height = img.size
    location = ((image_width - text_width)/2, 570)  # Replace with the coordinates you noted. (X, Y)
    d.text(location, name, fill=text_color, font=font)
    # Create a unique name for the file. Feel free to edit the format, this is an example
    file_name = "generated/" + name + str(random.randint(0, 255)) + ".png"
    # Save the image
    img.save(file_name)
    # Return the name we generated
    return file_name