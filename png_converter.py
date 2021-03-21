from PIL import Image
import sys
import os

img_folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for file in os.listdir(img_folder):
    img = Image.open(f'{img_folder}/{file}')
    img.save(f'{new_folder}/{file.rsplit(".", 1)[0]}.png', 'png')

print('All images converted.')
