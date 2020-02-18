from PIL import Image, ImageFilter

# Open file we want to work with
img_pika = Image.open('./pokedex/pikachu.jpg')
img_squirtle = Image.open('./pokedex/squirtle.jpg')

# Do some actions -- apply some methods
filtered_img = img_pika.convert('L')
rotate_pika = img_pika.rotate(180)
resize_squirtle = img_squirtle.resize((300, 300))
pika_box = (100, 100, 400, 400)
region = filtered_img.crop(pika_box)

# save new files output to see results
filtered_img.save('pikconvert.png', 'png')
rotate_pika.save('rotatepika.png', 'png')
resize_squirtle.save('squirtleresize.png', 'png')
region.save('charmanderBox.png', 'png')
