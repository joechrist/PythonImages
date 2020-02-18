from PIL import Image, ImageFilter

# Open file we want to work with
img_pika = Image.open('./pokedex/pikachu.jpg')
img_squirtle = Image.open('./pokedex/squirtle.jpg')

# Do some actions -- apply some methods
filtered_img = img_pika.convert('L')
rotate_pika = img_pika.rotate(180)
resize_squirtle = img_squirtle.resize((300, 300))

# save new files output to see results
filtered_img.save('pikconvert.png', 'png')
rotate_pika.save('rotatepika.png', 'png')
resize_squirtle.save('squirtleresize.png', 'png')
