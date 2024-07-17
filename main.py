from PIL import Image

hash_map = {
    (1, 10): '_',
    (10, 20): '.',
    (20, 30): ',',
    (30, 40): '-',
    (40, 50): '=',
    (50, 60): '+',
    (60, 70): ':',
    (70, 80): ';',
    (80, 90): 'c',
    (90, 100): 'b',
    (100, 110): 'a',
    (110, 120): '!',
    (120, 130): '?',
    (130, 140): '0',
    (140, 150): '1',
    (160, 170): '2',
    (170, 180): '3',
    (190, 200): '4',
    (200, 210): '5',
    (210, 220): '6',
    (220, 230): '7',
    (230, 240): '8',
    (240, 250): '9',
    (250, 255): '$'
}

invert_hash_map = {
    (1, 10): '$',
    (10, 20): '9',
    (20, 30): '8',
    (30, 40): '7',
    (40, 50): '6',
    (50, 60): '5',
    (60, 70): '4',
    (70, 80): '3',
    (80, 90): '2',
    (90, 100): '1',
    (100, 110): '0',
    (110, 120): '?',
    (120, 130): '!',
    (130, 140): 'a',
    (140, 150): 'b',
    (160, 170): 'c',
    (170, 180): ';',
    (190, 200): ':',
    (200, 210): '+',
    (210, 220): '=',
    (220, 230): '-',
    (230, 240): ',',
    (240, 250): '.',
    (250, 255): '_'
}


def get_invert_range_value(value):
    for key_range, mapped_value in invert_hash_map.items():
        if key_range[0] <= value <= key_range[1]:
            return mapped_value
        return ' '


def get_range_value(value):
    for key_range, mapped_value in hash_map.items():
        if key_range[0] <= value <= key_range[1]:
            return mapped_value
        return ' '


im = Image.open("reference.png")

rgb_im = im.convert('RGB')
width, height = im.size

grayscale_array = [[0] * width for _ in range(height)]
character_array = [[0] * width for _ in range(height)]
invert_character_array = [[0] * width for _ in range(height)]

for y in range(height):
    for x in range(width):
        red, green, blue = rgb_im.getpixel((x, y))
        grayscale = (red + green + blue) / 3
        print(int(grayscale))

        grayscale_array[y][x] = grayscale
        invert_character_array[y][x] = get_invert_range_value(grayscale)
        character_array[y][x] = get_range_value(grayscale)

image = Image.new("L", (width, height))

for y in range(height):
    for x in range(width):
        pixel_value = grayscale_array[y][x]
        image.putpixel((x, y), int(pixel_value))

image.save("grayscale_image1.jpg")
image.show()

for y in range(height):
    for x in range(width):
        print(character_array[y][x], end="")
    print(end='\n')

for y in range(height):
    for x in range(width):
        print(invert_character_array[y][x], end="")
    print(end='\n')
