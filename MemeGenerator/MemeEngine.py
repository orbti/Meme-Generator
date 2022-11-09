from PIL import Image, ImageDraw, ImageFont
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

            fnt = ImageFont.truetype('arial.ttf', size=20, encoding='unic')

            draw = ImageDraw.Draw(img)

            x = random.randint(5, img.width/4)
            y = random.randint(5, img.height/4)

            draw.text((x, y), text, font=fnt, fill='white')
            draw.text((x, y+20), author, font=fnt, fill='white')
            img.save(out_path)
        return out_path
