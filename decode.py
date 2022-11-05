from main import decode_image
import argparse 

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
        help="path to image to decode (with extension)")
    args = vars(ap.parse_args())

    path_to_stego_image = args.get('image')

    print('Message:', decode_image(path_to_stego_image))


main()