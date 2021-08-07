import tensorflow as tf
import numpy as np


class PredictDiabetes:
    def __init__(self,l):
        self.l = l
    
    def predict_diab(self):
        list_features = [[float(x) for x in self.l]]
        x = np.array(list_features).reshape(-1,16)
        model = tf.keras.models.load_model('model.h5')
        prediction = model.predict(x)
        return float(prediction[0][0])



        
        