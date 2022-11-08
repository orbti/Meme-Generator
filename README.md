# Meme-Generator

The goal of this project is to build a "meme generator" - a 
multimedia application to dynamically generate memes, 
including an image with an overlaid quote.

# Installation
Clone this github repo using the below code.

```
git clone https://github.com/orbti/Meme-Generator.git
```
Install the required modules using PIP.
```
pip install -r requirements.txt
```
# CLI
```
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

Genearate a meme

options:
  -h, --help       show this help message and exit
  --path PATH      Path to an image file
  --body BODY      Quote body to add to the image
  --author AUTHOR  Quote author to add to the image
  ```
# Web App
Use this code in your CLI to run the server.
```
python app.py
```
Open this address in a web browser. http://127.0.0.1:5000
# Dependencies
* pandas
* flask
* requests
* python-docx
* Pillow
* numpy