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
                "url": "http://www.google.com",
                "sites": {
                    "model": "sites.Site",
                    "fields": { 
                        "name": "example.com"
                    }
                },
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
                "code": "<strong>strong tag</strong>",
                "sites": {
                    "model": "sites.Site",
                    "fields": { 
                        "name": "example.com"
                    }
                },
            },
        })

    load_json(objects)
