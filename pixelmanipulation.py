from PIL import Image
import numpy as np

def load_image(image_path):
    return Image.open(image_path)

def save_image(image, path):
    image.save(path)

def encrypt_image(image):
    # Convert image to numpy array
    image_data = np.array(image)
    
    # Simple encryption by swapping pixels and adding a value
    encrypted_data = image_data.copy()
    height, width, channels = encrypted_data.shape
    for i in range(height):
        for j in range(0, width, 2):
            if j+1 < width:
                # Swap adjacent pixels
                encrypted_data[i, j], encrypted_data[i, j+1] = encrypted_data[i, j+1], encrypted_data[i, j]
    
    # Apply a basic mathematical operation (adding a value to each pixel)
    encrypted_data = (encrypted_data + 50) % 256
    
    # Convert back to image
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    return encrypted_image

def decrypt_image(image):
    # Convert image to numpy array
    image_data = np.array(image)
    
    # Reverse the mathematical operation (subtracting the added value)
    decrypted_data = (image_data - 50) % 256
    
    # Reverse the pixel swapping
    height, width, channels = decrypted_data.shape
    for i in range(height):
        for j in range(0, width, 2):
            if j+1 < width:
                # Swap adjacent pixels back
                decrypted_data[i, j], decrypted_data[i, j+1] = decrypted_data[i, j+1], decrypted_data[i, j]
    
    # Convert back to image
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    return decrypted_image

def main():
    # Ask the user if they want to encrypt or decrypt
    operation = input("Enter 'encrypt' to encrypt an image or 'decrypt' to decrypt an image: ").strip().lower()
    
    if operation not in ['encrypt', 'decrypt']:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
        return
    
    image_path = input("Enter the path of the image: ").strip()

    try:
        image = load_image(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    if operation == 'encrypt':
        result_image = encrypt_image(image)
        result_image_path = 'encrypted_image.png '
    else:
        result_image = decrypt_image(image)
        result_image_path = 'decrypted_image.png'

    save_image(result_image, result_image_path)
    print(f"{operation.capitalize()}ed image saved as {result_image_path}")
    result_image.show(title=f"{operation.capitalize()}ed Image")

if __name__ == "__main__":
    main()