from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            encrypted_pixel = (b, g, r)
            pixels[i, j] = encrypted_pixel

    img.save(output_path)
print("Image is encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            decrypted_pixel = (b, g, r)
            pixels[i, j] = decrypted_pixel

    img.save(output_path)
print("Image is decrypted successfully!")

input_path = r"C:\Users\DELL\Desktop\skill craft\TASK 2\input.jpg"
encrypted = r"C:\Users\DELL\Desktop\skill craft\TASK 2\encrypted.jpg"
decrypted = r"C:\Users\DELL\Desktop\skill craft\TASK 2\decrypted.jpg"

encrypt_image(input_path, encrypted, key=None)
decrypt_image(encrypted, decrypted, key=None)