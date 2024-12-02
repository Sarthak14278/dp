def encrypt(plain_text, depth):
    """Encrypt the text using the Rail Fence Cipher."""
    plain_text = plain_text.replace(" ", "")
    rows = [''] * depth
    row = 0
    direction = 1  # 1 for down, -1 for up

    for char in plain_text:
        rows[row] += char
        if row == 0:
            direction = 1
        elif row == depth - 1:
            direction = -1
        row += direction

    return ''.join(rows)

def decrypt(cipher_text, depth):
    # Create a list of empty strings to represent the rails
    rows = [''] * depth
    row, direction = 0, 1  # Start at row 0, direction is down
    
    # Step 1: Determine the number of characters in each rail
    rail_lengths = [0] * depth
    for _ in cipher_text:
        rail_lengths[row] += 1
        if row == 0:
            direction = 1
        elif row == depth - 1:
            direction = -1
        row += direction
    
    # Step 2: Fill the rails with cipher_text
    index = 0
    for r in range(depth):
        rows[r] = cipher_text[index:index + rail_lengths[r]]
        index += rail_lengths[r]
    
    # Step 3: Reconstruct the message from the rails
    decrypted_text = []
    row, direction = 0, 1
    for _ in cipher_text:
        decrypted_text.append(rows[row][0])  # Take the first character from the rail
        rows[row] = rows[row][1:]  # Remove the used character from the rail
        if row == 0:
            direction = 1
        elif row == depth - 1:
            direction = -1
        row += direction
    
    return ''.join(decrypted_text)  # Join and return the final decrypted text

# Code execution starts here
plain_text = "thank you very much"
depth = 3

print("Encryption")
cipher_text = encrypt(plain_text, depth)
print("Encrypted text:", cipher_text)

print("Decryption")
decrypted_text = decrypt(cipher_text, depth)
print("Decrypted text:", decrypted_text)
