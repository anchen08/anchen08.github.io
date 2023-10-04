from PIL import Image
import os

DIR = "Community Maps/"
# DIR = "images/"
SAVE_DIR = "images/maps/"
# ENDING = " (grey background).png"
ENDING = " (white background).png"
REPLACE = True

if not os.path.exists(DIR):
    print(f"No such directory {DIR}")
    exit(0)

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def expand_background(image_name, ending = ENDING, dir = DIR, savedir = SAVE_DIR, color="#b9bbba"):

    new_image = image_name.split(".png")[0]

    img = Image.open(dir + image_name)
    width, height = img.size
    new_width = width + 2000
    new_height = height + 100
    new_img = Image.new('RGB', (new_width, new_height), color=color)
    new_img.paste(img, (1000, 50), img)


    if (not os.path.exists(savedir + new_image + ending)):
        new_img.save(savedir + new_image + ending)
    else:
        if REPLACE:
            new_img.save(savedir + new_image + ending)
        else:
            print("File already exists.")
            
expand_background("Kenosha County.png", ENDING, DIR, SAVE_DIR, color="white" )


# if __name__ == "__main__":
#     f = open("image_error_log.txt", "w")
#     for filename in os.listdir(DIR):
#         file_path = os.path.join(DIR, filename)

#         if os.path.isfile(file_path):
#             try:
#                 expand_background(filename)
#             except:
#                 print(f"{filename} is invalid.")
#                 f.write(f"{filename}\n")
#     f.close()
#     print(f"Files stored in {SAVE_DIR}")
   