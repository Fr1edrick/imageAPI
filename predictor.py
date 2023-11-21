from fastapi import UploadFile
from responseSquema import ResponseSquema
import tensorflow as tf
from tensorflow import keras
import numpy as np

def ModelLoading():
        """Return trained model
        \nThis function return ``model`` trained.
        """
        model = tf.keras.models.load_model('./model_trained')
        # Check its architecture
        model.summary()
        return model

def ImageBinaryDecode( file: UploadFile ):
    """Params:
    \n``file`` => request body - UploadFile.
    \nReturn Binary image
    \nThis function return ``Binary Image``.
    """
    try:
        content = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(content)
        return file.filename
    except Exception:
        print( 'Error uploading the file' )
        return str('')
    finally:
        print( f"Successfully uploaded {file.filename}" )
        file.file.close()

class Predictor:
    def PredictImageLoaded( file: UploadFile ):
        """ Params:
        \n``file`` => request body (UploadFile).
        \nReturn: Image prediction response
        \nThis function return ``the image`` that model predicted.
        """
        img_height = 400
        img_width = 400
        class_names = ['llaveBristol', 'llaveCodo', 'llaveEstrella', 'llaveInglesa']

        try:
            filename = file.filename # Retrive filename from file parameter
            imageData = ImageBinaryDecode( file ) # Binary process
            print( f'Image to process: { filename }' )
             # Show the image which was just taken.
            img = keras.preprocessing.image.load_img(
                imageData, target_size=(img_height, img_width)
            )
            img_array= keras.preprocessing.image.img_to_array(img)
            img_array= tf.expand_dims(img_array, 0) # Create a batch

            # Loading model
            model = ModelLoading()
            predictions = model.predict(img_array)
            score = tf.nn.softmax(predictions[0])

            print(str(class_names))
            print(str(predictions))

            print(
                "El objeto capturado es {} con un {:.2f} de probabilidad."
                .format(class_names[np.argmax(score)], 100 * np.max(score))
            )
            return ResponseSquema(
                filename    =str( filename ),
                classes     =str( class_names ),
                predictions =str( predictions ),
                prediction  =str( class_names[ np.argmax( score ) ] ),
                score       =str( 100 * np.max( score ) )
            )

        except Exception as err:
            # Errors will be thrown if the user does not have a webcam or if they do not
            # grant the page permission to access it.
            print(str(err))