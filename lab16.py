import os
import random

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from PIL import Image

from lab16_data import acronyms

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Directory where our static images live.
IMAGE_DIR = os.path.join(app.static_folder, 'images')

# Task 4 — load at least three images into a list of Pillow Image objects.
image_files = ['fire.png', 'flower.png', 'collage.png']
images = [Image.open(os.path.join(IMAGE_DIR, name)) for name in image_files]


def negative(img):
    """Return the negative (inverted colors) of a Pillow Image."""
    img = img.convert('RGB')
    result = Image.new('RGB', img.size)
    src = img.load()
    dst = result.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = src[x, y]
            dst[x, y] = (255 - r, 255 - g, 255 - b)
    return result


@app.route('/')
def index():
    # Tasks 1 & 2 — show a static image, styled with Bootstrap.
    return render_template('lab16_index.html')


@app.route('/dictionary')
def dictionary():
    # Task 3 — pass the imported dictionary to the template for a Jinja loop.
    return render_template('lab16_dict.html', acronyms=acronyms)


@app.route('/random')
def random_negative():
    # Task 4 — randomly pick an image, make its negative, save it, display it.
    chosen = random.choice(images)
    result = negative(chosen)
    output_name = 'negative.png'
    result.save(os.path.join(IMAGE_DIR, output_name))
    return render_template('lab16_random.html', filename='images/' + output_name)


if __name__ == '__main__':
    app.run(debug=True)
