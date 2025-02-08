import numpy as np
from PIL import Image
import os


def create_random_image(width=100, height=100, output_filename="random_image.jpg"):
    """
    Creates a random image using NumPy and saves it as a JPEG file.

    Args:
        width (int): Width of the image.
        height (int): Height of the image.
        output_filename (str): Name of the output image file.

    Returns:
        str: Path of the saved image.
    """
    try:
        # Generate random pixel data
        array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
        image = Image.fromarray(array)

        # Save the image
        image.save(output_filename)
        print(f"Image saved as {output_filename}")

        return output_filename
    except Exception as e:
        print(f"Error creating image: {e}")
        return None


def display_image(image_path):
    """
    Opens and displays an image.

    Args:
        image_path (str): Path to the image file.
    """
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return

    try:
        image = Image.open(image_path)
        image.show()
    except Exception as e:
        print(f"Error displaying image: {e}")


if __name__ == "__main__":
    # Generate and save a random image
    image_path = create_random_image()

    # Display the saved image
    if image_path:
        display_image(image_path)
