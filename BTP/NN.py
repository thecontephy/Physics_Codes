import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from time import time
from tensorflow.python.keras.callbacks import TensorBoard
from keras.models import Sequential
from keras.layers.core import Dense, Dropout


df = pd.read_csv('material__data.csv')

x_array1 = df[["effective hole mass"]].to_numpy()
x_array2 = df[["min of e.n. diff"]].to_numpy()

x_array1 = x_array1/np.max(np.absolute(x_array1))
x_array2 = x_array2/np.max(np.absolute(x_array2))
x_array_II = np.array(list(zip(x_array1, x_array2)))
y_array = df[["PBE bandgap"]].to_numpy()
y_array = y_array/np.max(np.absolute(y_array))


X_train, X_test, Y_train, Y_test = train_test_split(
    x_array_II, y_array, test_size=0.3, random_state=42, shuffle=True)


tensorboard = TensorBoard(log_dir='logs/{}'.format(time()))



model= Sequential([
    Dense(16, activation='sigmoid'),
    Dense(32, activation='sigmoid'),
    Dense(64, activation='sigmoid'),
    Dense(128, activation='sigmoid'),
    Dropout(0.2),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(128, activation='sigmoid'),
    Dropout(0.2),
    Dense(64, activation='sigmoid'),
    Dense(32, activation='sigmoid'),
    Dense(16, activation='sigmoid'),
    Dense(1, activation='sigmoid')
])

model.compile(loss='mean_absolute_percentage_error',
                 optimizer='Adam',
                 metrics=['mean_squared_error'])


EPOCHS = 500

model.fit(X_train, Y_train, epochs=EPOCHS, callbacks=[tensorboard])
model.summary()

test_loss, test_accu = model.evaluate(X_test, Y_test)
