def translating_utf8(s):
    return ''.join(format(byte, '08b') for byte in s.encode('utf-8'))

def expanding_key(binary_message, key):
    binary_key = translating_utf8(key)
    return (binary_key * (len(binary_message) // len(binary_key) + 1))[:len(binary_message)]

def XOR(message, key):
    return ''.join('1' if a != b else '0' for a, b in zip(message, key))

def convert_to_bytes(transform):
    return bytes(int(transform[i:i + 8], 2) for i in range(0, len(transform), 8))

def encoder_message(message, key):
    binary_message = translating_utf8(message)
    expanded_key = expanding_key(binary_message, key)
    encoder = XOR(binary_message, expanded_key)
    encoded_bytes = convert_to_bytes(encoder)
    hex_encoded_message = encoded_bytes.hex()
    print("Encoded message: ", hex_encoded_message)

def decoder_message(encoded_message, key):
    encoded_bytes = bytes.fromhex(encoded_message)
    encoded_binary = ''.join(format(byte, '08b') for byte in encoded_bytes)
    expanded_key = expanding_key(encoded_binary, key)
    decoder = XOR(encoded_binary, expanded_key)
    decoded_bytes = convert_to_bytes(decoder)
    decoded_message = decoded_bytes.decode('utf-8')
    print("Decoded message: ", decoded_message)

key = "1"

print("Available options:")
print("1. Set the key")
print("2. Encode the message")
print("3. Decode the message")
print("4. Finish the work")

while True:
    choice = input("\nСhoose an option (1,2,3,4) ")
    if choice == "1":
        key = input("Enter a key: ")

    elif choice == "2":
        message = input("Enter a message: ")
        encoder_message(message, key)

    elif choice == "3":
        message = input("Enter a message: ")
        decoder_message(message, key)

    elif choice == "4":
        break

    else:
        print("The option is missing")
