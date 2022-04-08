from lib2to3.pytree import convert
from PIL import Image
from pip import main
from IPython.display import display
import random
import json
import os
from trait_classify import *
from trait_rarity import *
from input import *

## ======================Generate Traits: Define the images traits================================
all_images = []

# A recursive function to generate unique image combinations

def create_new_image():
    """
    Create new image with traits

    Returns:
        JSON string: image
    """
    new_image = {}

    # For each trait category, select a random trait based on the weightings
    new_image["Face"] = random.choices(face, face_weights)[0]
    new_image["Ears"] = random.choices(ears, ears_weights)[0]
    new_image["Eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image["Hair"] = random.choices(hair, hair_weights)[0]
    new_image["Mouth"] = random.choices(mouth, mouth_weights)[0]
    new_image["Nose"] = random.choices(nose, nose_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image

# ******************************************************
# Returns true if all images are unique
def all_images_unique(all_images):
    """Check if all the images generated are unique

    Args:
        all_images (JSON object): List of all images with each element as JSON object

    Returns:
        bool: true or false
    """
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)


# =============================MAIN===========================
def main():
    # ----------------------------------------------------------
    # Generate the unique combinations based on trait weightings
    for i in range(TOTAL_IMAGES):

        new_trait_image = create_new_image()

        all_images.append(new_trait_image)

    # print(all_images)
    """
    Output looks like this so far for a total of 2 images:
    ```json
    [
        {
            "Face": "Black",
            "Ears": "Right Earring",
            "Eyes": "Regular",
            "Hair": "Up Hair",
            "Mouth": "Big Smile",
            "Nose": "Nose"
        },
        {
            "Face": "White",
            "Ears": "No Earring",
            "Eyes": "Regular",
            "Hair": "Caret Hair",
            "Mouth": "Teeth Smile",
            "Nose": "Nose"
        }
    ]
    ```
    """
    # ===========================Validate uniqueness==========================
    print("Are all images unique?", all_images_unique(all_images))
    # Add token Id to each image
    i = 0
    for item in all_images:
        item["tokenId"] = i
        i = i + 1

    print(all_images)

    """
    Output looks like this so far for a total of 2 images
    ```json
    [
        {
            "Face": "Black",
            "Ears": "Right Earring",
            "Eyes": "Regular",
            "Hair": "Up Hair",
            "Mouth": "Big Smile",
            "Nose": "Nose"
            "tokenId": 0
        },
        {
            "Face": "White",
            "Ears": "No Earring",
            "Eyes": "Regular",
            "Hair": "Caret Hair",
            "Mouth": "Teeth Smile",
            "Nose": "Nose"
            "tokenId": 1
        }
    ]
    ```
    """

    # ===========================Trait Counting============================
    """
    You assigned traits based on the predefined weights and the random function. This means that it is unlikely you have exactly 60 white faces even if you have defined the weight of white faces to be 60. To know exactly how much each trait occurs, you have to You will want to keep track of how many traits are now present in your collection of images.

    To do this, you write the following code:
    1. Define a dictionary for each trait with their respective classifications and initiate at 0
    2. Loop over your created images and add them to your respective trait dictionary if you come across the trait.
    """

    face_count = {}
    for item in face:
        face_count[item] = 0

    # --------------------------
    ears_count = {}
    for item in ears:
        ears_count[item] = 0
    # --------------------------
    eyes_count = {}
    for item in eyes:
        eyes_count[item] = 0
    # --------------------------
    hair_count = {}
    for item in hair:
        hair_count[item] = 0

    # --------------------------
    mouth_count = {}
    for item in mouth:
        mouth_count[item] = 0

    # --------------------------
    nose_count = {}
    for item in nose:
        nose_count[item] = 0


    # --------------------------
    for image in all_images:
        face_count[image["Face"]] += 1
        ears_count[image["Ears"]] += 1
        eyes_count[image["Eyes"]] += 1
        hair_count[image["Hair"]] += 1
        mouth_count[image["Mouth"]] += 1
        nose_count[image["Nose"]] += 1

    print(face_count)
    print(ears_count)
    print(eyes_count)
    print(hair_count)
    print(mouth_count)
    print(nose_count)

    """
    {'White': 1, 'Black': 4}
    {'No Earring': 0, 'Left Earring': 1, 'Right Earring': 4, 'Two Earrings': 0}
    {'Regular': 3, 'Small': 1, 'Rayban': 0, 'Hipster': 0, 'Focused': 1}
    {'Up Hair': 0, 'Down Hair': 1, 'Mohawk': 0, 'Red Mohawk': 0, 'Orange Hair': 2, 'Bubble Hair': 0, 'Emo Hair': 0, 'Thin Hair': 1, 'Bald': 1, 'Blonde Hair': 0, 'Caret Hair': 0, 'Pony Tails': 0}
    {'Black Lipstick': 1, 'Red Lipstick': 0, 'Big Smile': 1, 'Smile': 0, 'Teeth Smile': 2, 'Purple Lipstick': 1}
    {'Nose': 4, 'Nose Ring': 1}
    """

    # ==================================Generating the images========================

    # create a directory only if the image output path doesn't exist
    img_output_path = '../img/output/'
    if not os.path.exists(img_output_path):
        os.mkdir(f'{img_output_path}')

    # read each generated image & convert its component into 'RGBA'
    for image in all_images:
        im1 = Image.open(
            f'../img/face_parts/face/{face_files[image["Face"]]}.png').convert('RGBA')
        im2 = Image.open(
            f'../img/face_parts/ears/{ears_files[image["Ears"]]}.png').convert('RGBA')
        im3 = Image.open(
            f'../img/face_parts/eyes/{eyes_files[image["Eyes"]]}.png').convert('RGBA')
        im4 = Image.open(
            f'../img/face_parts/hair/{hair_files[image["Hair"]]}.png').convert('RGBA')
        im5 = Image.open(
            f'../img/face_parts/mouth/{mouth_files[image["Mouth"]]}.png').convert('RGBA')
        im6 = Image.open(
            f'../img/face_parts/nose/{nose_files[image["Nose"]]}.png').convert('RGBA')
        
        
        # Create each composite
        com1 = Image.alpha_composite(im1, im2)
        com2 = Image.alpha_composite(com1, im3)
        com3 = Image.alpha_composite(com2, im4)
        com4 = Image.alpha_composite(com3, im5)
        com5 = Image.alpha_composite(com4, im6)
        
        
        # Convert to RGB
        rgb_im = com5.convert('RGB')
        file_name = str(image["tokenId"]) + ".png"
        rgb_im.save(img_output_path + file_name)


if __name__ == "__main__":
    main()