# DataScience16FinalProject
This is the repo for Patrick, David, and Philip's work on the final Data Science project, Spring 2016.

## Navigating this Repository
This repository contains a series of python scripts, iPython notebooks, and project documentation tracking our progress through learning about neural networks. See below for an overview of the different stages (organized into separate directories):

1. [01_Implementing_a_NN](01_Implementing_a_NN) - Basic implementation of a feed-forward NN

2. [02_Conversion_to_RNN](02_Conversion_to_RNN) - Conversion of our basic NN into a recurrent network

3. [03_NN_in_Theano](03_NN_in_Theano) - Exploring Theano and leveraging it to create a basic NN

4. [04_NN_in_Lasagne](04_NN_in_Lasagne) - Exploring Lasagne and using it to create a basic NN

5. [05_LSTM_Lasagne_Text_gen](05_LSTM_Lasagne_Text_gen) - Implementation of an LSTM for NLP and text generation in Lasagne

6. [06_LSTM_Keras_Weather](06_LSTM_Keras_Weather) - Implementation of an LSTM to predict weather patterns using Keras

7. [07_LSTM_Keras_NFL](07_LSTM_Keras_NFL) - Implementation of an LSTM to predict NFL football game outcomes using Keras

## Our Website

We also have a [website](http://neuralolin.github.io/DataScience16FinalProject/) where we wrote blog posts documenting all the stuff we've done throughout this project in long-form. We also linked to many of the resources we used throughout our blog posts. However, if sifting through all our gibberish sounds like too much of a chore, and you really just want to learn about Neural Networks from smarter people than us...

## Resources, you say

Here's a succinct list of resources we used, in the (rough) order we used them. If all you want to learn about Neural Networks from smart people on the internet, reading through these should do the trick.

##### [01_Implementing_a_NN](01_Implementing_a_NN)

* https://www.youtube.com/playlist?list=PLiaHhY2iBX9hdHaRr6b7XevZtgZRa1PoU
* https://github.com/stephencwelch/Neural-Networks-Demystified

This is a fantastic starting place, and assumes only a basic understanding of linear algebra and python. You will walk through implementing your very own neural network in python, complete with forward and back propagation. You will also walk through the math involved in back-prop, like gradients, gradient descent, and cost functions.

##### [02_Conversion_to_RNN](02_Conversion_to_RNN)

* https://iamtrask.github.io/2015/11/15/anyone-can-code-lstm/

Despite the misleading url, here "i am trask" has a created a great writeup on how RNNs work, and how you can implement one in python. He walks you through creating an RNN that learns how to do binary addition. Because we wanted to make sure we were building on what we learned in the previous section, rather than starting from scratch using this walk-through's architecture, we used this walk-through to convert the NN from section 1 into an RNN that learns binary addition!

##### [03_NN_in_Theano](03_NN_in_Theano)

##### [04_NN_in_Lasagne](04_NN_in_Lasagne)

##### [05_LSTM_Lasagne_Text_gen](05_LSTM_Lasagne_Text_gen)

##### [06_LSTM_Keras_Weather](06_LSTM_Keras_Weather)

##### [07_LSTM_Keras_NFL](07_LSTM_Keras_NFL)
