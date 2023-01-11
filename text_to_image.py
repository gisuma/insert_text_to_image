from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pathlib import Path
import glob
import re

file_Directory = Path().absolute()
path=str(file_Directory)
all_files = glob.glob(path+'\input\*.jpg')
print(all_files)
for file in all_files:
    img = Image.open(file)
    I1 = ImageDraw.Draw(img)
    text = re.search(r'(\w+)(.jpg)',file)
    I1.text((0, 0),text.group(1), fill=(255, 0, 0))
    img.show()
    new_path = "{}\{}{}".format('ouput',text.group(1),'.jpg')
    print(new_path)
    img.save(new_path)
