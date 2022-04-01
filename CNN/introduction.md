# Clasification with Keras

[[_TOC_]]

## Densely connected layers 
**->** every unit of every layer is connected to all the units in the previous layer.

**->** the first layer is connected to all the pixels in the input image

## Import sequencial model

`from keras.models import Sequential` 

## Initialize sequential model
`model = Sequential()` 

`from keras.layers import Dense`

### First layer is a set of densely connected units

`model.add(Dense(10,activation='relu',input_shape=(784,)))` 

* 10 is the number of units
* *more units, more complex would be the network and it's capacity to represent complex inpus
* 784 is the number of pixels of the image (height * width)

### Second layer (hidden layer)
`model.add(Dense(10, activation='relu'))`

### The output of the network 
`model.add(Dense(3,activation='softmax'))`

* fully conected layer with a unit of each class of inputs (3 classes in this case)
* Activation = "Softmax" to decide which of the three classes was presented.

## Compilation of the model
`model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])`

* categorical_crossentropy is appropriate for the classification task

## Dimentions of the image
* (n,m,d)-> n it's the height, m it's the width (both in n of pixels), d represents red, green and blue of each pixel (channels)
* train image data (number of samples, height, width, channels)

## Model input
* The model expects samples to be rows in an array, and each column to represent a pixel in the image, so before fit the model, it is necessary to convert the images into a two dimensional table

`train_data = train_data.reshape((50,784))`

## Fit the model to training data
`model.fit(train_data,train_labels,validation_split=0.2,epochs=3)`
* During training, the network adjust its weights through backpropagation and gradient descent
* Epochs: number of times the model will go over all the training data
* validation_split: percentage of data that will be used for validation (avoid overfitting)

* In each epoch, the program tracks progress through the data set and at the end of the epoch prints the values of the loss function and accuracy

## Test set
`test_data = test_data.reshape((10,784))`

* Another evaluation of the model should be done on a separate test set that was not used during training. This gives a realistic evaluation of the model quality