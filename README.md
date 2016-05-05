# DataScience16FinalProject
This is the repo for Patrick, David, and Philip's work on the final Data Science project, Spring 2016.

## Navigating this Repository
This repository contains a series of python scripts, iPython notebooks, and project documentation tracking our progress through learning about neural networks. See below for an overview of the different stages (organized into separate directories):

1. [01_Implementing_a_NN](01_Implementing_a_NN) - Basic implementation of a feed-forward NN

2. [02_Conversion_to_RNN](02_Conversion_to_RNN) - Conversion of our basic NN into a recurrent network

3. [03_NN_in_Theano](03_NN_in_Theano) - Exploring Theano and leveraging it to create a basic NN

4. [04_NN_in_Lasagne](04_NN_in_Lasagne) - Exploring Lasagne and using it to create a basic NN

5. [06_LSTM_Lasagne_Text_gen](06_LSTM_Lasagne_Text_gen) - Implementation of an LSTM for NLP and text generation in Lasagne

6. [05_LSTM_Keras_Weather](05_LSTM_Keras_Weather) - Implementation of an LSTM to predict weather patterns using Keras

7. [07_LSTM_Keras_NFL](07_LSTM_Keras_NFL) - Implementation of an LSTM to predict NFL football game outcomes using Keras

## Our Final Poster

[This](final_poster.pdf) is the final poster we demoed. We also created a [PDF writeup](poster_writeup.pdf) of the core content from the poster, with some edits and improvements to be more readable!

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

##### [05_LSTM_Keras_Weather](05_LSTM_Keras_Weather)

* http://danielhnyk.cz/predicting-sequences-vectors-keras-using-rnn-lstm/

	Here's a walk-through of how to use Keras to build and train a RNN that can predict sequences of data (ie, weather, stock prices, etc.). One downside to this article is that it is based on a previous version of Keras, and some of the syntax used won't work on the newest distributions of Keras. However, our notebook has the new syntax, so you can use our code as an example!

	What we really liked about this article was that it explains exactly how to convert a time-series (with time on your x-axis, something else on your y) into something a Neural Network can learn and predict. In fact, the procedure used in this article to preprocess weather data is nearly identical to how you preprocess any sequential data for RNNs. Check out the article and our repo for an explanation of the process!

##### [06_LSTM_Lasagne_Text_gen](06_LSTM_Lasagne_Text_gen)

* http://karpathy.github.io/2015/05/21/rnn-effectiveness/
* https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py

	The first resource here is a blog post by a very knowledgable guy named Andrew Karpathy, and wow, is he engaging. It offers a fun, interesting, and very helpful introduction into how RNNs work with a great-in depth look at what goes on inside during the training process. This was a great resource as we developed a character-level recurrent network, as Karpathy offers a lot of great advice on architecture and data representation.

	The second resource is an implementation of what we built, but in Keras! We used this and borrowed a lot to inform decisions about the network hyperparameters (e.g. shape, size, etc.).

##### [07_LSTM_Keras_NFL](07_LSTM_Keras_NFL)

We were planning on trying to run an LSTM on historical NFL data so that our NN could learn which teams are "good" and "bad" based on previous performance, and predict a winner and margin of victory. Alas, we ran out of time. This will be completed in the future.

## Supplemental Resources

If all of the above resources weren't enough for you, have no fear. We've prowled the internet and came up with even more things you can (and we did) read. These definitely helped us out with understanding Neural Networks from a more technical perspective. Here they are, sorted into which phase of our project they help most with:

##### [01_Implementing_a_NN](01_Implementing_a_NN)

* ftp://ftp.sas.com/pub/neural/FAQ2.html#A_std

Holy cow was this useful. It's basically a Neural Network FAQ. Almost every question we had about NNs was clarified in this. It contains answers to questions like, "Should I normalize/standardize/rescale the data?" and "What is a softmax activation function?" and "What is the curse of dimensionality?"

* http://iamtrask.github.io/2015/07/12/basic-python-network/

This is a good precursor to the "i am trask" RNN implementation.

* https://moalquraishi.wordpress.com/2014/05/25/what-does-a-neural-network-actually-do/

A blog post on what a NN actually does, and some exploration of the underlying relationships/math.

* https://medium.com/learning-new-stuff/how-to-learn-neural-networks-758b78f2736e#.90xgkk6wi

Another basic NN implementation. Probably don't need to read this if you've gone through all the other things, since its basically just another framing.

* http://karpathy.github.io/neuralnets/

"Hacker's guide to Neural Networks." It's just that, with an in-depth exploration of NN from the perspective of circuits and the code. Very code heavy.

* http://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw

A discussion on how many hidden layers and nodes to use.

##### [02_Conversion_to_RNN](02_Conversion_to_RNN)

* http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/

A tutorial about recurrent NNs and where they can be implemented, and some visualizations to help show the architecture.

##### [03_NN_in_Theano](03_NN_in_Theano)

* http://deeplearning.net/tutorial/

A set of Theano tutorials.

##### [04_NN_in_Lasagne](04_NN_in_Lasagne)

* http://lasagne.readthedocs.io/en/latest/user/layers.html#creating-a-layer

Just the Lasagne docs.

##### [05_LSTM_Keras_Weather](05_LSTM_Keras_Weather)

* http://keras.io/

And the Keras ones.

* http://colah.github.io/posts/2015-08-Understanding-LSTMs/

This was a really, really informative read. It contains a step-by-step walkthrough about how a LSTM has "memory." If we were to recommend one article when it comes to understanding the underlying math of LSTMs, this would be it.

* https://www.youtube.com/watch?v=56TYLaQN4N8

A great lecture from the CS department at Oxford about RNNs and LSTMs. This gets pretty crazy with math and once he starts talking about Hessians we got lost. Up until then though, very informative. If you're good at or enjoy attempting to learn math, you'll enjoy this.

* https://datamarket.com/data/list/?q=provider%3Atsdl

A huge databank of time series data sets. It's where we got the weather data from. Great for just diving into RNNs.

##### [06_LSTM_Lasagne_Text_gen](06_LSTM_Lasagne_Text_gen)

* https://github.com/Lasagne/Recipes/blob/master/examples/lstm_text_generation.py

A Lasagne LSTM recipe.
