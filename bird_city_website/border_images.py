from PIL import Image, ImageOps
import os

DIR = "Community Logos/Community Profile Images - square"
SAVE_DIR = "images/logos/"
REPLACE = True

if not os.path.exists(DIR):
    print(f"No such directory {DIR}")
    exit(0)

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def expand_background(image_name, dir = DIR, savedir = SAVE_DIR, color="#b9bbba"):
    image = Image.open(file_path)
                
    # Add border to the image
    bordered_image = ImageOps.expand(image, border=400, fill=color)
    
    # Save the bordered image to the output directory
    output_path = os.path.join(SAVE_DIR, filename)

    if (not os.path.exists(output_path)):
        bordered_image.save(output_path)
    else:
        if REPLACE:
            bordered_image.save(output_path)
        else:
            print("File already exists.")

if __name__ == "__main__":
    f = open("error_log_logos.txt", "w")
    for filename in os.listdir(DIR):
        file_path = os.path.join(DIR, filename)

        # print(file_path)

        if os.path.isfile(file_path):
            try:
                expand_background(filename)
            except:
                print(f"{filename} is invalid.")
                f.write(f"{filename}\n")
    f.close()
    print(f"Files stored in {SAVE_DIR}")
   