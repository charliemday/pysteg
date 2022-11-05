import cv2
import numpy as np

def message_to_binary(message):
    """
    Takes a string and converts it binary
    """
    if type(message) == str:
        return ''.join([ format(ord(i), "08b") for i in message ])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [ format(i, "08b") for i in message ]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")


def hide_data(image, secret_message):
    """
    Hides the secret
    """    
    # Calculate the maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8

    # If the message is too big compared to the image you
    # want to hide it in, throw an error
    if len(secret_message) > n_bytes:
        raise ValueError("Error encountered insufficient bytes, need bigger image or less data !!")
    
    # We use a delimiter to know when the message ends
    secret_message += "#####"

    data_index = 0

    binary_secret_msg = message_to_binary(secret_message)

    data_len = len(binary_secret_msg)

    for values in image:
        for pixel in values:
            r, g, b = message_to_binary(pixel)
            if data_index < data_len:
                pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index >= data_len:
                break

    return image


def show_data(image):
    """
    Take an image and show the data 
    """
    binary_data = ""
    for values in image:
        for pixel in values:
            r, g, b = message_to_binary(pixel)
            # This extracts the data from the least significant bit
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]

    all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]

    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####":
            break

    return decoded_data[:-5]


def encode_text(data, img, filename):
    """
    Encode into a large image
    """
    if data is None or len(data) == 0:
        raise ValueError('Data is empty')

    if img is None:
        raise ValueError('Image is empty')

    if filename is None or len(filename) == 0:
        raise ValueError('Filename is empty')

    image = cv2.imread(img)

    # Details of the image
    resized_image = cv2.resize(image, (500, 500))
    cv2.imshow("Stego Image", resized_image)

    encoded_image = hide_data(image, data)
    cv2.imwrite(filename, encoded_image)


def decode_image(img):
    """
    Decode the image to the original message
    """
    image = cv2.imread(img)

    resized_image = cv2.resize(image, (500, 500))
    cv2.imshow("Stego Image", resized_image)

    text = show_data(image)
    return text


