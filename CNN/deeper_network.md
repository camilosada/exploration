## Why depeer networks?
Multiple layers of convolutions in the network allows the network to gradually build up representations of objects in the images from simple features to more complex features and up to sensitivity to distinct categories of objects

## How deep??
Depth comes at a computational cost and deeper the network, more data is required for training

## How many parameters?
> model.summary() Tells the number of parameters in the model

Convolutions have more expressive power, so they require less parameters,
but reading out these more expenssive representations then requires many
more parameters on the output side

## Pooling operations
*max pooling*: summarize a group of pixels based on its maximal value and replace these pixels with one large pixel that stores the maximal value<br>

> from keras.models import Sequential
> from keras.layers import Dense, Conv2D, Flatten, MaxPool2D
>
>model= Sequential()
>model.add(Conv2D(`5`, kernel_size=`3`,activation=`'relu'`,input_shape=`(img_rows, img_cols,1)`))
>model.add(MaxPool2D(`2`)) 
>model.add(Conv2D(`15`,kernel_size=`3`,activation=`'relu'`,input_shape=`(ing_rows,img_cols,1)`))
>model.add(MaxPool2D(`2`)) 
>model.add(Flatten())
>model.add(Dense(`3`,activation=`'softmax'`))

The input to the MaxPool2D object is the size of the pooling window