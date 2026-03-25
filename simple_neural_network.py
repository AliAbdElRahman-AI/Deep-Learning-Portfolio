import tensorflow as tf
import numpy as np

# Simple Neural Network to predict: y = 2x - 1
# Input data
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
model.fit(xs, ys, epochs=500)

# Test the model
print("Prediction for 10 is: ", model.predict(np.array([10.0])))
