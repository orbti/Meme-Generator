from PIL import Image, ImageDraw
import random


class MemeEngine():
    def __init__(self, tmp_dir):
        self.tmp_dir = tmp_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        out_path = f'{self.tmp_dir}/tmp_img.png'

        with Image.open(img_path) as img:
            ratio = img.height / img.width
            height = width * ratio
            img = img.resize((int(width), int(height)))

            draw = ImageDraw.Draw(img)

            x = random.randint(10, 200)
            y = random.randint(10, 200)

            draw.multiline_text((x, y), f'{text}\n{author}', fill='white')
            img.save(out_path)
        return out_path