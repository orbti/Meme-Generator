"""Web App."""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    if not request.form['image_url']:
        return render_template('meme_form.html')

    img_url = request.form['image_url']
    res = requests.get(img_url)
    filename = f'./static/tmp_img.png'
    with open(filename, 'wb') as img:
        img.write(res.content)
    
    img_path = './static/tmp_img.png'

    body = request.form['body']
    author = request.form['author']
    path = meme.make_meme(img_path, body, author)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
