from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    print("Starting encryption...")
    img = Image.open(image_path)
    img_array = np.array(img)

    # Convert to a larger integer type to prevent overflow
    img_array = img_array.astype(np.int32)

    # Encrypting the image
    encrypted_array = (img_array + key) % 256

    # Creating and saving the encrypted image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save('encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'")

def decrypt_image(image_path, key):
    print("Starting decryption...")
    img = Image.open(image_path)
    img_array = np.array(img)

    # Convert to a larger integer type to prevent overflow
    img_array = img_array.astype(np.int32)

    # Decrypting the image
    decrypted_array = (img_array - key) % 256

    # Creating and saving the decrypted image
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save('decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'")

def compare_images(original_path, decrypted_path):
    print("Comparing original and decrypted images...")
    original = Image.open(original_path)
    decrypted = Image.open(decrypted_path)
    
    if np.array_equal(np.array(original), np.array(decrypted)):
        print("Decryption successful: The images match.")
    else:
        print("Decryption failed: The images do not match.")

if __name__ == "__main__":
    # Update the path to your image file
    image_path = r'C:\Users\Konda Reddy\Desktop\my projects\prodigy\wp5485212.jpg'
    key = 50
    
    # Encrypt the image
    encrypt_image(image_path, key)

    # Decrypt the encrypted image
    encrypted_image_path = 'encrypted_image.png'
    decrypt_image(encrypted_image_path, key)

    # Compare original and decrypted images
    compare_images(image_path, 'decrypted_image.png')

    print("Image manipulation completed successfully.")
