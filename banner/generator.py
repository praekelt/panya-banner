import random

from generate import IMAGES
from generate.json_loader import load_json

BANNER_COUNT = 10

def generate():
    objects = []
    
    # gen imagebanner objects
    for i in range(1, BANNER_COUNT + 1):
        objects.append({
            "model": "banner.ImageBanner",
            "fields": {
                "title": "Image Banner %s Title" % i,
                "state": "published",
                "image": random.sample(IMAGES, 1)[0],
                "url": "/",
            },
        })
    
    # gen codebanner objects
    for i in range(1, BANNER_COUNT + 1):
        objects.append({
            "model": "banner.CodeBanner",
            "fields": {
                "title": "Code Banner %s Title" % i,
                "state": "published",
                "image": random.sample(IMAGES, 1)[0],
                "code": "<< code embed >>",
            },
        })
    
    # gen post photo sizes
    objects.append({
        "model": "photologue.PhotoSize",
        "fields": {
            "name": "banner_large",
            "width": "728",
            "height": "90",
            "crop": True,
        },
    })
    objects.append({
        "model": "photologue.PhotoSize",
        "fields": {
            "name": "banner_medium",
            "width": "300",
            "height": "250",
            "crop": True,
        },
    })
    
    load_json(objects)
