from transformers import pipeline
from PIL import Image
import logging
import torch

SCORE = 0.965 # 0.965 and less - is safety content

logging.getLogger('transformers').setLevel(logging.ERROR)

def nsfw_image(img_path: str, model_path: str):
    # Function modified to always return False (no NSFW classification)
    return False
