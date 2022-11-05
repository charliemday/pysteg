## PySteg: A Simple Steganography Tool written in Python

### How does it work?

PyStegasaurus uses the LSB (Least Significant Bit) method to hide data in images. It works by taking the least significant bit of each pixel in the image and replacing it with a bit from the data. This is done for each pixel in the image, and the data is hidden in the image. The image is then saved as a PNG/JPG file.

Code *heavily* inspired by blog article [this](https://towardsdatascience.com/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372)

### How do I use it?

Git clone this repo and then install the (very small and simple) requirements:

    pip install -r requirements.txt

Then, get an image you want to encode. We've added a simple image but you can use any image you want. Then, run the following command:

    python encode.py -i images/image.png -n images/image2.png -f text/message.txt

Alternatively you can you a string to encode:

    python encode.py -i images/image.png -n images/image2.png -m "I love Steganography!"

This will encode the message in the image and save it as image2.png. You can then decode the message by running:

    python decode.py -i images/image2.png
