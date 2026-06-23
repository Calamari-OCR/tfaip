import tensorflow as tf


class PredictInputLayer(tf.keras.layers.Layer):
    def call(self, inputs):
        return {"predict": inputs}

class TrainingInputLayer(tf.keras.layers.Layer):
    def call(self, inputs):
        return {"training": inputs}

