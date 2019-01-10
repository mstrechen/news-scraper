import random
import os
import string
import requests


def _generate_name(length = 20):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def _get_ext(url):
    if url.find('?') != -1:
        url = url[: url.rfind('?')]
    if url.find('.') != -1:
        url = url[url.rfind('.') : ]
    return url

def download_and_name_img(url):
    name = _generate_name() + _get_ext(url)
    r = requests.get(url)
    path = os.path.join(os.getcwd(), 'static', 'storage', name)
    open(path, 'wb').write(r.content)
    return name