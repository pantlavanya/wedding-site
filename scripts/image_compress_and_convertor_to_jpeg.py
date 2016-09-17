#! /usr/bin/env python
# scripts/image_compress_and_convertor_to_jpeg.py

from PIL import Image
from django.conf import settings
from images.models import Images
from config.models import Config

__author__ = "lavanya_pant"

SLIDER_IMAGE = Config.objects.get(key='SLIDER_IMAGE')
PROFILE_IMAGE = Config.objects.get(key='PROFILE_IMAGE')
ADVERTISEMENT_IMAGE = Config.objects.get(key='ADVERTISEMENT_IMAGE')
OTHER_IMAGE = Config.objects.get(key='ADVERTISEMENT_IMAGE')

def main():
    for img in Images.objects.filter(cron_checked=False):
        image_object = Images.objects.get(id=img.id)
        image_object.cron_comment = convert_and_compress_image(img.path)
        image_object.cron_checked = 1
        image_object.save()

def convert_and_compress_image(filename):
    d = {}
    try:
        imagez = Image.open(filename)
        d.update({'size': imagez.size})
        d.update({'format': imagez.format})
    except:
        return
    return str(d)


def run():
    print "Start Image Compress and Convert To JPEG"
    main()
    print "Stop Image Compress and Convert To JPEG"

if __name__ == "__main__":
    run()