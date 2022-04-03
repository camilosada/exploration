# Convolution
Fundamental operation that convolutional neural networks use to process images

- [Convolution](#convolution)
  - [Correlation in images](#correlation-in-images)
  - [Build a network with convolution layers](#build-a-network-with-convolution-layers)
    - [Compile](#compile)
  - [Zero padding](#zero-padding)
  - [Size of the stride](#size-of-the-stride)
    - [Size of the output can be calculated as (I - K + 2*P)/(S + 1)](#size-of-the-output-can-be-calculated-as-i---k--2ps--1)
  - [Dilated convolutions](#dilated-convolutions)

* The **kernel** defines the feature that we are looking for. For
example: k=[-1,1], we look for a change from small values on the left 
to large values on the right.
* The resulting array after the convolution is called **Feature map**, it contains a map of the locations in the image that match the feature represented by the kernel.
    
## Correlation in images
* Pixels are not independent from their neighbors: natural images contain spatial correlations
* Neighboring pixels along an edge tend to have similar patterns

## Build a network with convolution layers

* It resembles the Dense layers, but instead of having every unit in the
layer connected to every unit in the previous layer, these connect to
the previous layer through a convolution kernel. 
* The output of each unit in this layer is a convolution of a kernel over
the image input
* Dense layers :one weight for each pixel, a **convolution layer** has
only one weight for each pixel in the kernel.

>from keras.models import Sequential<br>
>from keras.layers import Dense,Conv2D, Flatten<br>
We need Dense as well as the Conv2D layers. The Flatten layer serves as a conector between convolution and densely connected layers.
>model = Sequential()<br>
>model.add(Conv2D(`10`, kernel_size=`3`,activation=`'relu'`,input_shape=`(img_rows, img_cols,1)`)) -> We define the input shape not to lose the >spatial relationship between pixels<br>
>model.add(Flatten())-> Flattens the feature map into a one dimensional >array (expected input of the Dense layer)<br>
>model.add(Dense(`3`,activation =`'softmax'`))

### Compile
>model.compile(optimizer=`'adam'`,loss=`'categorical_crossentropy'`,metrics=[`'accuracy'`])<br>
>model.fit(train_data, train_labels, validation_split=`0.2`,epochs=`3`)<br>
>model.evaluate(test_data,test_labels,epochs=`3`)<br>

## Zero padding
* Useful when building a network with many layers
* Not to lose a pixel from the edge of the image in each subsequent layer
>model.add(Conv2D(`10`, kernel_size=`3`,activation=`'relu'`,input_shape=`(img_rows, img_cols,1)`),padding=`'same'`) we add the keyword argument *padding*
* padding='valid' -> no zero padding is added (default)
* padding='same' -> zero padding will be applied, so the output of the convolution has the same size as the input 

## Size of the stride
* Affects the size of the output of a convolution
* Size of the step that we take with the kernel between input pixels
* Implemented as a keyword argument to the Conv2D layers (Default=1)
>model.add(Conv2D(`10`, kernel_size=`3`, activation=`'relu'`, input_shape=`(img_rows, img_cols,1)`)strides=`1`)

### Size of the output can be calculated as (I - K + 2*P)/(S + 1)
I= size of the input, K= size of the kernel, P= size of the zero padding, S= strides

## Dilated convolutions
* Twek the spacing between the pixels affected by the kernel
* Useful in cases where you need to aggregate information across multiple scales
* Controled by the keyword argument *dilation_rate*: sets the distance between subsequent pixels