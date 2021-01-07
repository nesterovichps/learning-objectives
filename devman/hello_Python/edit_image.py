from PIL import Image


def resize(image, image_wigth, image_height):
    print(image.size)
    image.thumbnail((image_wigth, image_height))

    return image


shift = 100
image = Image.open('data/foto.jpg')
print('Format image', image.format)
print('Image color mod', image.mode, ' need RGB')
if image.mode != 'RGB':
    print('convert image')
    image = image.convert('RGB')
    print('Image color mod', image.mode, ' need RGB')
print('Image width', image.width)
print('Image height', image.height)
red_chanel, green_chanel, blue_chanel = image.split()
# red
crop_coord_1 = (shift, 0, red_chanel.width, red_chanel.height)
new_1_red_chanel = red_chanel.crop(crop_coord_1)
crop_coord_2 = (shift / 2, 0, red_chanel.width - shift / 2, red_chanel.height)
new_2_red_chanel = red_chanel.crop(crop_coord_2)
red_chanel = Image.blend(new_1_red_chanel, new_2_red_chanel, 0.5)
# blue
crop_coord_1 = (0, 0, blue_chanel.width - shift, blue_chanel.height)
new_1_blue_chanel = blue_chanel.crop(crop_coord_1)
crop_coord_2 = (shift / 2, 0, blue_chanel.width - shift / 2, blue_chanel.height)
new_2_blue_chanel = blue_chanel.crop(crop_coord_2)
blue_chanel = Image.blend(new_1_blue_chanel, new_2_blue_chanel, 0.5)
# green
green_chanel = green_chanel.crop((shift / 2, 0, green_chanel.width - shift / 2, green_chanel.height))
result_image = Image.merge('RGB', (red_chanel, green_chanel, blue_chanel))

# result_image=resize(result_image,80,80)
print(result_image.size)
result_image.save('data/result.jpg')
