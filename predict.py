import sys, os,glob
from PIL import Image
import numpy as np
from PIL import Image
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import numpy as np



def build_model(in_shape):
    categories = ["business", "love"]
    nb_classes = len(categories)

    model = Sequential()
    model.add(Convolution2D(32, 3, 3, 
    border_mode='same',
    input_shape=in_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Convolution2D(64, 3, 3, border_mode='same'))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten()) 
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='binary_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy'])
    return model


def start_predict():
    categories = ["business", "love"]

    # 検査対象のファイルを指定
    lst=[]
    for file in os.listdir("static/"):
        if file != ".DS_Store":
            if file != "test.txt":
                filepath = "static/" + file
                lst.append(filepath)
            
                
    image_size = 64


    # 入力画像をNumpyに変換
    X = []
    files = []
    for fname in lst:
        img = Image.open(fname)
        img = img.convert("RGB")
        img = img.resize((image_size, image_size))
        in_data = np.asarray(img)
        X.append(in_data)
        files.append(fname)
    X = np.array(X)

    # CNNのモデルを構築
    model = build_model(X.shape[1:])
    model.load_weights("./Data/hotel.hdf5")

    # データを予測
    pre = model.predict(X)
    for file in glob.glob('./static/*.jpg'):
        os.remove(file)

    for i, p in enumerate(pre):
        y = p.argmax()
        result = "これは..."+categories[y]+"!!"
        print(result)
        return(result)


if __name__ == '__main__':
    start_predict()

