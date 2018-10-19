import os
import sys
import io
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


client = vision.ImageAnnotatorClient()
# The name of the image file to annotate

for i in range(1,36):
    name = str(i)+'.jpg'
    file_name = os.path.join(os.path.dirname(__file__),name)

# Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('labels:')
    label_text = []
    for label in labels: 
        label_text.append(label.description)
        print(label.description)

    label_text_str=str(label_text)    
    img = Image.open(file_name)
    draw =  ImageDraw.Draw(img)
    newfont=ImageFont.truetype('ubuntu.ttf',12)  #you can change the ".ttf' to change the type of the labels
    draw.text((0,20),label_text_str,font=newfont)
    img.save(file_name)
