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

* https://github.com/Newmu/Theano-Tutorials
* http://outlace.com/Beginner-Tutorial-Theano/

	These two resources are great places to start out when getting a grasp for the somewhat esoteric conventions Theano imposes. Alec Radford (Olin shoutout!) does a great job in introducing concepts central to Theano that give a great background to start from. Starting from a 12 line implemention of a multiplication function in Theano, Alec goes through all the way to inplementing a modern convolutional image processing network over the course of 5 examples. Some of the more well-written, clever, and clean Theano code we've come across during this project.

	The second resource here is a good walkthrough to get up to speed in Theano syntax, going from start to finish in implementing a super simple feedforward NN that acts as an XOR gate. To see a full, working example that's easy to understand, check this one out.

##### [04_NN_in_Lasagne](04_NN_in_Lasagne)

* https://github.com/craffel/Lasagne-tutorial/blob/master/examples/tutorial.ipynb

This is an awesome tutorial on a variety of NN Lasagne applications, from simple feed-forward NNs to LSTM and Convolutional layers.

##### [05_LSTM_Lasagne_Text_gen](05_LSTM_Lasagne_Text_gen)

##### [06_LSTM_Keras_Weather](06_LSTM_Keras_Weather)

* http://danielhnyk.cz/predicting-sequences-vectors-keras-using-rnn-lstm/

Here's a walk-through of how to use Keras to build and train a RNN that can predict sequences of data (ie, weather, stock prices, etc.). One downside to this article is that it is based on a previous version of Keras, and some of the syntax used  What we really liked about this article was that it explains exactly how to convert a time-series (with time on your x-axis, something else on your y) into something a Neural Network can learn and predict. In fact, the procedure used in this article to preprocess weather data is nearly identical to how you preprocess any sequential data for RNNs. Check out the article and our repo for an explanation of the process!

##### [07_LSTM_Keras_NFL](07_LSTM_Keras_NFL)
