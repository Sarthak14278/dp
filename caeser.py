def encode(text, key):
    """Encodes the given text using a shift cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char  # Keep spaces and special characters unchanged
    return result

def decode(text, key):
    """Decodes the given text using a shift cipher."""
    return encode(text, -key)  # Decoding is the inverse of encoding

# Input from the user
text = input("Enter any string: ")
key = int(input("Enter any key: "))

# Encoding the text
encoded_text = encode(text, key)
print("\nEncoded Text: ", encoded_text)

# Decoding the text
decoded_text = decode(encoded_text, key)
print("Decoded Text: ", decoded_text)
