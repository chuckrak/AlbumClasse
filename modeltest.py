from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Load the model
model = load_model('keras_modelv4.h5')
# 0 - RAP
# 1 - ROCK
# 2 - ALTERNATIVE

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


# Replace this with the path to your image
def test_model(fileRange, genre, directory, expectedClass):
    total = len(fileRange)
    correct = 0
    for i in fileRange:
        i = str(i)
        image = Image.open(f'{directory}/album{i}.png')
        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        #turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        try:
            data[0] = normalized_image_array
        except:
            total -= 1
            print(f"Error with file {i}")
            continue

        # run the inference
        prediction = model.predict(data)
        if np.argmax(prediction[0]) == expectedClass:
            correct += 1
    print(f"{genre} Classification accuracy rate " + str(correct / total))

rockFileRange = list(range(138,222)) + list(range(324, 396))
rapFileRange = list(range(276, 348))
jazzFileRange = list(range(222, 284))
test_model(rockFileRange, "Rock", "RockTest", 1)
test_model(rapFileRange, "Rap", "RapTest", 0)
test_model(jazzFileRange, "Jazz", "JazzTest", 2)
