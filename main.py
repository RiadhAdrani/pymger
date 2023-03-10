from PIL import Image
import os
import sys


def checkScales(n):
    return float(n)


args = sys.argv[1:]

path = args[0]
scales = list(map(checkScales, args[1:]))


def collect_imgs_in_directory(path):
    imgs = []
    valid_images = [".jpg", ".gif", ".png", ".tga"]

    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue

        imgs.append({
            'image': Image.open(os.path.join(path, f)),
            'fileName': f,
        })

    return imgs


def set_scale(imgs, scale):
    scaled_imgs = []

    for img in imgs:
        scaled_img = {}

        scaled_img['image'] = img['image'].copy()
        scaled_img['scale'] = scale
        scaled_img['fileName'] = img['fileName']

        img['scale'] = scale

        scaled_img['image'] = scaled_img['image'].resize(
            (int(scaled_img['image'].size[0] * scale), int(scaled_img['image'].size[1] * scale)))

        scaled_imgs.append(scaled_img)

    return scaled_imgs


def save(imgs, scale):
    try:
        os.mkdir('output_x' + str(scale))
    except:
        print('Output folder already exist !')

    for img in imgs:
        data = os.path.splitext(img['fileName'])

        new_name = 'output_x' + str(scale) + '/' + \
            data[0] + data[1]

        img['image'].save(new_name)


def run():
    if len(scales) == 0:
        print('No scales provided.')
        return

    items = collect_imgs_in_directory(path)

    for scale in scales:
        save(set_scale(items, scale), scale)


run()
