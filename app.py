import random
import os
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from meme import generate_meme

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """
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
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    print(quote)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)

@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    if not request.form['imgage_url']:
        return render_template('meme_form.html')

    imgage_url = request.form['image_url']
    try:
        r = requests.get(imgage_url, verify=False)
        tmp = f'./static/tmp_img.png'
        img = open(tmp, 'wb').write(r.content)
    except:
        print("Bad Image Url")
        return render_template('meme_form.html')

    body = request.form['body']
    author = request.form['author']
    path = meme.make_meme(img, body, author)

    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True)
