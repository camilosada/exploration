## Learning curves
One case of **overfitting** training loss decreases and validation loss flattens out in some level

> training = model.fit(train_data,train_labels, epochs=`3`,validation_split=`0.2`)
> import matplotlib.pyplot as plt
> plt.plot(training.history[`'loss`])
> plt.plot(training.history[`'val_loss'`])
> plt.show()

## Store optimal parameters

The callback monitors the validation loss, and will only overwrite the weights whenever the validation loss shows improvement (the validation loss decreases) -> `The weights will be stored for the epoch at which the validation loss was the smallest, before it started rising back up.`

> from keras.callbacks import ModelCheckpoint
>
> checkpoint = ModelCheckpoint(`'weights.hdf5`,monitor=`'val_loss'`,save_best_only=`'True'`)
> callbacks_list = [checkpoint]
> model.fit(train_data,train_labels,validation_split=`0.2`,epochs=`3`,callbacks=`callbacks_list`)

After all epochs of fitting are done, the file contains the best weights. To use this weights, it will be necessary to initialize the model again with the same architecture, the same layers, with the same number of units each.

> model.load_weights(`'weights.hdf5`)
> model.predict_classes(test_data)

## Regularization of CNN (strategies to prevent overfitting)
** *Dropout*: ** 
- choose a random subset of the units in a layer and ignore them. This units will be ignored on the forward pass trhought the network, as well in the back propagation of error.
- Prevent different units in the network from becoming overly correlated in their activity
- Compensate if some part of the network becomes too sensitive to some noise in the data 

> from keras.models import Sequential
> from keras.layers import Dense, Conv2D, Flatten, Dropout
> 
> model= Sequential()
> model.add(Conv2D(`5`, kernel_size=`3`, activation=`'relu'`, input_shape=`(img_rows, img_cols, 1)`))
> model.add(Dropout(`0.25`))
> model.add(Conv2D(`15`, kernel_size=`3`, activation=`'relu'`)
> model.add(Flatten())
> model.add(Dense(3,activation=`'softmax'`))

- 0.25 is the proportion of the units in the layer to ignore in each learning step
- Dropout layer is added after the layer for wich the units will be ignored

** *Batch normalization*: ** 
- Takes the output of a particular layer and rescales it so that it always has 0 mean and standard deviation of 1 in every batch of training

> from keras.models import Sequential
> from keras.layers import Dense, Conv2D, Flatten, Dropout
> 
> model= Sequential()
> model.add(Conv2D(`5`, kernel_size=`3`, activation=`'relu'`, input_shape=`(img_rows, img_cols, 1)`))
> model.add(BatchNormalization())
> model.add(Conv2D(`15`, kernel_size=`3`, activation=`'relu'`)
> model.add(Flatten())
> model.add(Dense(3,activation=`'softmax'`))

- Is implemented as another type of layer that can be added after one of the layers whose output should be normalized

**!!!**
Sometimes dropout and batch normalization do not work well together.

Dropout slows down learning, making it more incremental and careful, batch normalization tends to make learning go faster -> "The disharmony of batch normalization"