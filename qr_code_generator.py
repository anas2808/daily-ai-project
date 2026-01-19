import qrcode
from qrcode.exceptions import DataOverflowError
import sys

def generate_qr_code(data, file_path='qrcode.png'):
    """
    Generates a QR code from the provided data and saves it to the specified file path.
    
    :param data: The data to encode in the QR code.
    :param file_path: The file path to save the QR code image.
    :raises ValueError: If the data is too large to be encoded.
    """
    try:
        # Initialize the QR code object with configuration
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code: 1 is the smallest
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in pixels
            border=4,  # Width of the border (minimum is 4)
        )
        
        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)  # Optimize the QR code size
        
        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image to the specified file path
        img.save(file_path)
        print(f"QR code generated and saved to {file_path}")
        
    except DataOverflowError as e:
        raise ValueError("Data is too large to be encoded in a QR code.") from e

def main():
    """
    Main function to execute the QR code generation.
    """
    if len(sys.argv) != 3:
        print("Usage: python qrcode_generator.py '<data>' <output_file_path>")
        sys.exit(1)
    
    data = sys.argv[1]
    file_path = sys.argv[2]
    
    try:
        generate_qr_code(data, file_path)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()