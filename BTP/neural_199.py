import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from time import time
from tensorflow.python.keras.callbacks import TensorBoard
from keras.models import Sequential
from keras.layers.core import Dense, Dropout


df = pd.read_csv('199data_points.csv')

x_array1 = df[["effective hole mass"]].to_numpy()
x_array2 = df[["min of e.n. diff"]].to_numpy()
#x_array3 = df[["electronegativity diff bw anion and cation"]].to_numpy()

x_array1 = x_array1/np.max(np.absolute(x_array1))
x_array2 = x_array2/np.max(np.absolute(x_array2))
#x_array3 = x_array3/np.max(np.absolute(x_array3))
x_array_II = np.array(list(zip(x_array1, x_array2)))
y_array = df[["PBE bandgap"]].to_numpy()
y_array = y_array/np.max(np.absolute(y_array))

#y_array = df[["ind. PBE"]].to_numpy()

X_train2, X_test2, Y_train2, Y_test2 = train_test_split(
    x_array_II, y_array, test_size=0.3, random_state=42, shuffle=True)


tensorboard = TensorBoard(log_dir='logs/{}'.format(time()))
# MODEL I



model_II = Sequential([
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

model_II.compile(loss='mean_absolute_percentage_error',
                 optimizer='Adam',
                 metrics=['mean_squared_error'])


EPOCHS = 500

model_II.fit(X_train2, Y_train2, epochs=EPOCHS, callbacks=[tensorboard])
model_II.summary()

test_loss2, test_accu2 = model_II.evaluate(X_test2, Y_test2)