from PIL import Image

def encode_text_in_image(image_path, output_image_path, text):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0
    
    # Convert text to binary
    binary_text = ''.join([format(ord(i), "08b") for i in text])
    binary_text += '1111111111111110'  # Delimiter to indicate end of text

    for row in range(height):
        for col in range(width):
            if index < len(binary_text):
                r, g, b = img.getpixel((col, row))
                r = int(format(r, '08b')[:-1] + binary_text[index], 2)
                encoded.putpixel((col, row), (r, g, b))
                index += 1

    # Save the encoded image
    encoded.save(output_image_path)
    print(f"Text encoded and saved in {output_image_path}")

def decode_text_from_image(image_path):
    img = Image.open(image_path)
    binary_text = ""
    width, height = img.size

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            binary_text += format(r, '08b')[-1]

    text = ''.join([chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8)])
    delimiter = '1111111111111110'
    text = text.split(chr(int(delimiter[:8], 2)))[0]
    print(f"Decoded Text: {text}")

def main():
    print("Welcome to the Steganography Tool")
    choice = input("Do you want to (e)ncode or (d)ecode a message? ")

    if choice.lower() == 'e':
        image_path = input("Enter the path of the image to encode: ")
        output_image_path = input("Enter the output image path: ")
        text_to_hide = input("Enter the text to hide: ")
        encode_text_in_image(image_path, output_image_path, text_to_hide)

    elif choice.lower() == 'd':
        image_path = input("Enter the path of the image to decode: ")
        decode_text_from_image(image_path)

    else:
        print("Invalid choice. Please enter 'e' to encode or 'd' to decode.")

if __name__ == "__main__":
    main()
