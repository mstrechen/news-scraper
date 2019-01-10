import random
import os
import string
import requests
from PIL import Image
from resizeimage import resizeimage

def _generate_name(length = 20):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def _get_ext(url):
    if url.find('?') != -1:
        url = url[: url.rfind('?')]
    if url.find('.') != -1:
        url = url[url.rfind('.') : ]
    return url

def img_resize(path, width: int = None, height: int = None):
    with open(path, 'r+b') as f:
        with Image.open(f) as img:
            if height and width:
                cover = resizeimage.resize_cover(img, (height, width))
            elif height:
                cover = resizeimage.resize_height(img, height)
            else:
                cover = resizeimage.resize_width(img, width)
            img.save(path + '.tmp', img.format)
    os.rename(path + '.tmp', path)

def download_and_name_img(url, width: int = None, height: int = None):
    name = _generate_name() + _get_ext(url)
    r = requests.get(url)
    path = os.path.join(os.getcwd(), 'static', 'storage', name)
    open(path, 'wb').write(r.content)

    if width or height:
        img_resize(path, width=width, height=height)

    return name