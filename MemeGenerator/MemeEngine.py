from PIL import Image, ImageDraw
import random


class MemeEngine():
    def __init__(self, out_path):
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=500) -> str:
        img = Image.open(img_path)

        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        x = random.randint(10, 200)
        y = random.randint(10, 200)
        draw.multiline_text((x, y), f'{text}\n{author}', fill='white')

        img.save(f'{self.out_path}\out.jpg')
        return self.out_path