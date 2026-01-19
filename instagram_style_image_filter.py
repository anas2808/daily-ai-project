import cv2
import numpy as np
from typing import Tuple


def apply_sepia(image: np.ndarray) -> np.ndarray:
    """
    Apply a sepia filter to the given image.

    :param image: The input image in BGR format.
    :return: The image with a sepia filter applied.
    """
    try:
        # Define sepia filter kernel
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        # Apply the filter
        sepia_img = cv2.transform(image, kernel)
        # Clip values to ensure they remain in valid range
        return np.clip(sepia_img, 0, 255).astype(np.uint8)
    except Exception as e:
        print(f"Error applying sepia filter: {e}")
        return image


def apply_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert the given image to grayscale.

    :param image: The input image in BGR format.
    :return: The grayscale image.
    """
    try:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception as e:
        print(f"Error converting image to grayscale: {e}")
        return image


def apply_vignette(image: np.ndarray, strength: float = 0.5) -> np.ndarray:
    """
    Apply a vignette filter to the given image.

    :param image: The input image in BGR format.
    :param strength: The strength of the vignette effect.
    :return: The image with a vignette filter applied.
    """
    try:
        rows, cols = image.shape[:2]
        # Create vignette mask
        kernel_x = cv2.getGaussianKernel(cols, cols * strength)
        kernel_y = cv2.getGaussianKernel(rows, rows * strength)
        kernel = kernel_y * kernel_x.T
        mask = 255 * kernel / np.linalg.norm(kernel)
        vignette_img = np.copy(image)

        for i in range(3):
            vignette_img[:, :, i] = vignette_img[:, :, i] * mask

        return np.clip(vignette_img, 0, 255).astype(np.uint8)
    except Exception as e:
        print(f"Error applying vignette filter: {e}")
        return image


def load_image(file_path: str) -> np.ndarray:
    """
    Load an image from a file path.

    :param file_path: Path to the image file.
    :return: The loaded image.
    """
    try:
        return cv2.imread(file_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


def save_image(image: np.ndarray, file_path: str) -> None:
    """
    Save an image to a specified file path.

    :param image: The image to save.
    :param file_path: The path where to save the image.
    """
    try:
        cv2.imwrite(file_path, image)
    except Exception as e:
        print(f"Error saving image: {e}")


def main():
    """
    Main function to apply filters to an image.
    """
    image_path = 'input.jpg'  # Path to the input image
    output_path_sepia = 'output_sepia.jpg'  # Output path for sepia filter
    output_path_grayscale = 'output_grayscale.jpg'  # Output path for grayscale filter
    output_path_vignette = 'output_vignette.jpg'  # Output path for vignette filter

    # Load the image
    image = load_image(image_path)

    if image is None:
        print("Failed to load image. Exiting.")
        return

    # Apply sepia filter
    sepia_image = apply_sepia(image)
    save_image(sepia_image, output_path_sepia)

    # Apply grayscale filter
    grayscale_image = apply_grayscale(image)
    save_image(grayscale_image, output_path_grayscale)

    # Apply vignette filter
    vignette_image = apply_vignette(image)
    save_image(vignette_image, output_path_vignette)


if __name__ == "__main__":
    main()