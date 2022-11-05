from main import encode_text
import argparse

def main():
    print('[INFO] Encoding...')

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
        help="path to original image")
    ap.add_argument("-n", "--name", required=True,
        help="path to create the encoded image (with extension)")
    ap.add_argument("-m", "--message",
        help="string or a file with the message to encode"),
    ap.add_argument("-f", "--file",
        help="path to file with the message to encode"),
    args = vars(ap.parse_args())

    path_to_original_image = args.get('image')
    path_to_encoded_image = args.get('name')

    message_file = args.get('file')
    message = args.get('message')

    if message_file is not None:
        with open(message_file, 'r') as f:
            message = f.read()
            encode_text(message, path_to_original_image, path_to_encoded_image)
    elif message is not None:
        encode_text(message, path_to_original_image, path_to_encoded_image)
    
main()