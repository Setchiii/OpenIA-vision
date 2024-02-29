from PIL import Image as PIL

# Function to change the format of an image. Input : image_path, Output : new_image_path. Use the PIL library to convert most common image extentions to .jpeg


def change_format(image_path):
    image = PIL.open(image_path)
    new_image_path = image_path.split(".")[0] + ".jpeg"
    image.save(new_image_path)
    return new_image_path


# Example
if __name__ == "__main__":
    print(change_format("test.bmp"))
