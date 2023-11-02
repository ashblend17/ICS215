def encrypt_transposition_cipher(message, key):
    message = message.replace(" ", "").upper()

    num_columns = len(key)

    num_rows = (len(message) + num_columns - 1) // num_columns

    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    message_index = 0
    for row in range(num_rows):
        for col in range(num_columns):
            if message_index < len(message):
                grid[row][col] = message[message_index]
                message_index += 1

    key_order = sorted(range(num_columns), key=lambda x: key[x])
    encrypted_message = ""
    for col in key_order:
        for row in range(num_rows):
            encrypted_message += grid[row][col]

    return encrypted_message

message = "This is a secret message"
key = "GERMAN"

encrypted_message = encrypt_transposition_cipher(message, key)
print( encrypted_message)