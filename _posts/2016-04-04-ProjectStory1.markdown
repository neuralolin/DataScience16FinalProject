---
layout:     post
title:      "Project Story One"
subtitle:   "A Bird in the Hand may not be Worth Two in the Bush"
date:       2016-04-04
author:     "David, Patrick, and Philip"
header-img: "img/post-bg-01.jpg"
---

<h2>A Tale of Twitter</h2>

<p>Working with huge datasets is a hallmark of Data Science. Up until now, that sounded like an amazing idea. However, as we discovered, there is a big difference between working with large datasets and working with bad datasets. Our initial idea of a project revolved around working with Twitter as our dataset, which turns out to be a remarkably bad dataset. But first, our mentality!</p>

<p>For our project idea, we were interested in exploring a time-series based dataset and the influence or correlation of some external factors with this dataset. We initially came from the angle of looking into the stock market as the time series, as there is a lot of publicly available data on it. Along with that, it seemed like an easy dataset in that it contained mainly doubles values and would require little cleaning. For our external factor, we wanted to look into Twitter and the general sentiment that a body of Tweets for a day can show. What we found out was that Twitter utterly sucks. For one, there is no (free) publicly available historical data. The only way to get Twitter data is to use their stream api, which gathers 1% of Twitter in realtime. The only historical data available are from people who have been running servers and querying the stream (or some other) api, and then storing the tweets and selling them for money. We have no money. We did not instantly give up however. We started data collection, and up until recently collected about 15 million Tweets. What we realized sadly is that this data meant very little. We could not analyze trends over time, because we were only able to gather data for days at a time, meaning that if something happened in the stock market a week or two ago, we would not have any information linking to it. So we scrapped that idea. Along with that, we realized that if we were going to be collecting Twitter data, this project would quickly turn into more of a data collection project, instead of our goal of an algorithmic/ML and data science influenced project. So, we decided pivoting made the most sense.</p>

<h2>Finding our Wings</h2>

<p>So you may be thinking, what are we even doing. Good question. What we’ve eventually decided is to start with an algorithm we know we’re interested in, and then apply it from there. This algorithm (and concept as a whole) is neural networks. Very high level, we came up with the plan as follows:</p>

<ul>
  <li>Learn as much as we can about neural networks</li>
  <li>Along the way, create some implementations of neural networks and validate their outputs through some simple tests on datasets</li>
  <li>Use existing implementations of neural networks and apply them to an interesting dataset - perhaps something sports or time-series or gambling/betting related</li>
</ul>

<h2>#progress</h2>

<p>We’ve dedicated the last two weeks to developing a strong understanding of the math behind neural networks. At this point we’ve focused largely on the following key components:</p>

<ol>
  <li>The basic structure of neural networks from a conceptual perspective. NN’s are comprised of several layers, each filled with “neurons”. The neurons pass data from layer to layer through synapses, which basically just take scalar multiples of the previous layer, sum them up, and assign the output to a neuron’s “activity” in the next layer.</li>
  <li>How inputs propagate forward through the network in order to make predictions. The original features each get their own neuron in the base layer. For each example, the next layer’s neurons are populated with linear combinations (using the synapses’ weights) of the current layer’s neurons. The final layer of the network has a single-node, whose activity is the network’s prediction.</li>
  <li>Defining a cost function to optimize, and the process by which backpropagation penalizes high levels activity backwards through the network. To maximize each synapse’s weight, you take partial derivatives of the error function with respect to the weights. This results in the chain rule being applied over and over, as the cost is a function of an activity, which is a function of weights and activities, which are a function of other weights and activities, which are..., okay you get the point. Chain rule 5ever.</li>
  <li>The process by which gradient descent is applied to training a neural network, and different optimization algorithms that attempt to avoid pitfalls like local minima.</li>
</ol>

<p>We focused on all of the above components of NNs with a focus on leveraging matrix operations from the beginning to set the context for a focus on computational efficiency in addition to a deep mathematical comprehension.</p>

<p>In terms of an actual implementation, we’ve created a basic neural network that can predict outputs based on given weights and perform back propagation to calculate the gradient of the cost function and optimize the weights. For gradient descent, we used an existing implementation of the BFGS algorithm provided by the scipy optimize package.</p>

<p>Moving forward, we plan to apply or simple implementation to a simple dataset to more fully verify its functionality. At that point, we intend on gaining more insight about the application of neural networks to real-world problems and when their use is appropriate or inappropriate. Watch out for coverage soon on that subject.</p>

<h3>Note:</h3>

<p>This was the Twitter-themed project story. If the fluff was too much, our repo (found <a href="https://github.com/neuralolin/DataScience16FinalProject">here</a>) has more of the nitty-gritty code, along with documentation of our mentality and work along the way. </p>