---
layout:     post
title:      "Project Story Two"
subtitle:   "Neural Networks and Time Series Data"
date:       2016-04-21
author:     "David, Patrick, and Philip"
header-img: "img/post-bg-01.jpg"
---

## What is a Recurrent Neural Network (RNN)?

From the rocky start of this project, we progressed into knowing that we wanted to instead study neural networks and time series data. As such, we’re interested in time series and language modeling, and the most applicable type of neural network for this type of work is the recurrent neural network. It adds the concept of ‘memory’ to neural networks, which allows present inputs to influence future inputs through a stored ‘state’. A common application of RNNs is in language modeling. We’ll be exploring it with this, along with other types of time-organized data.

Assuming you have a basic understanding of what a neural network is and how it works, if all you want is to know what steps to follow and what resources to use to begin implementing RNNs, here’s what we did:

Started with surface reading about RNNs. We liked [this](http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/) article, as well as [this one](http://karpathy.github.io/2015/05/21/rnn-effectiveness/).
The continued to implement our first RNN! We followed along with [this](https://iamtrask.github.io/2015/11/15/anyone-can-code-lstm/) tutorial.
Next, reading about [LSTMs](http://colah.github.io/posts/2015-08-Understanding-LSTMs/).
Finally we looked into Theano and Lasagne! We really liked [this](https://github.com/craffel/Lasagne-tutorial/blob/master/examples/tutorial.ipynb) tutorial for Lasagne. As for Theano, it’s self-explanatory for the most part, and any part you don’t understand you can google.

## So how can we write our own RNN in Python?
Going from a regular Neural Network to an RNN is not difficult. You can create a very simple Recurrent Neural Network by having the state of the hidden layer feed into the hidden layer at the next timestep, and so on. This type of RNN is commonly referred to as an Elman Network -- where the hidden layer is “copied” into a context layer at each timestep, and the context layer feeds into the hidden layer in the next timestep.

Along with that, generating predictions using an RNN is easy. At each timestep you simply feed your input and the previous hidden layer values into the neural network. Math happens (i.e. propagate values through the network using weights), and you get a prediction.

Backpropagation is a bit trickier, because the hidden layer propagates through timesteps. Changing the hidden layer at one time step then affects the value of the hidden layer at every subsequent timestep. You’re still just taking the derivative of the cost with respect to the neural network’s parameters, and then gradient descending the parameters until your neural network is optimally accurate. The process of applying backpropagation to RNNs is often called backpropagation through time, and in many implementations, hyperparameters are set dictating how many steps backward in time to propagate error.

From all this, we get the next question we need to ask to actually implement, that of...

## What tools can we leverage to make our lives easier when implementing a RNN?

### Theano

From day one of implementing our basic vanilla NN, we found that there’s a lot of derivatives involved in backpropagation, the process by which error travels backward through a NN, allowing for efficient training. Actually doing the calculus out and evaluating the chain rule over and over again until you have a programmable expression for the derivative is quite tedious, and often difficult, since none of us are very good at math. Thankfully, some smart people implemented a library to make this sort of mathematical modeling much easier, and it’s called Theano! Here’s a quick blurb from the official documentation (**tl;dr: Theano lets you define mathematical expressions symbolically, and then evaluate those expressions (and their derivatives!) with incredible accuracy, and with respect to any variable.**)

So ultimately, how can we use this to our advantage when implementing a NN? We can define relevant functions to the different components of our NN, like the cost function, and then easily compute gradients, letting Theano do all the heavy lifting. See our notebook for a quick example of how easy it is to implement a basic NN using Theano. We’ve come a long way since our first iteration when we were computing derivatives by hand, and then implementing them manually in Python. Phew! What could possibly be next?

#### Side note!

Super useful resources for Theano [here](http://deeplearning.net/software/theano/), [here](https://github.com/Lasagne/Recipes/tree/master/tutorials), and [here](https://github.com/craffel/theano-tutorial).

### Lasagne to the rescue!

As if Theano wasn’t powerful enough, a group of researchers from around the world have made implementing NNs even (even) easier (that’s like, 2 times easier)! The magical tool? Lasagne. Taken from the official Lasagne documentation - “Lasagne is a lightweight library to build and train neural networks in Theano.” What more could you possibly want? We get the combined unbiased intelligence of a bunch of researchers from around the world to make easy-to-use abstractions on top of an already highly optimized and fast mathematical modeling library, Theano. With Lasagne, creating a NN is as simple as compiling an input layer, middle (hidden layers) - of which there are many options, and the output. What’s great here is that Lasagne already has built in implementations for many different kinds of neural-net layers, from our barebones layer to a convolutional or LSTM layer.  From there, you define your cost function, optimizer (e.g. stochastic gradient descent), and train it up! Here are some good resources to get started with Lasagne, [here](http://lasagne.readthedocs.org/en/latest/index.html), [here](https://github.com/Lasagne/Recipes/tree/master/tutorials), and finally [here](https://github.com/craffel/Lasagne-tutorial/blob/master/examples/tutorial.ipynb).

An alternative to Lasagne is another library called Keras. The general consensus around the ML community is that Keras, while easier in a lot of cases to actually implement, falls short in customization. Lasagne exposes a lot of the Theano-like conventions, which allows you to customize a lot of the training processes involved. Keras, on the other hand, abstracts out much of the Theano insides, which makes it more difficult to customize to your needs. For the purpose of learning about the inner workings of neural networks, we would like to submit an official stamp of approval to some combination of Lasagne and Theano. **#patrickapproved**

## What’s next?

Following along with what we said in our earlier blog post, we wanted to explore the math/implementations behind RNNs. Now that we have done some of that exploration, we want to explore in the context of a dataset. Time series is a must, but we are still looking into different options. One interesting area to check for datasets is [here](https://datamarket.com/data/list/?q=provider%3Atsdl), which has a lot of (random) datasets that could be interesting. Then, we plan on implementing something with Lasagne+Theano. Finally, **profit!**