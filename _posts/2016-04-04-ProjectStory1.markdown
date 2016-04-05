---
layout:     post
title:      "Project Story One"
subtitle:   "A Bird in the Hand may not be Worth Two in the Bush"
date:       2016-04-04
author:     "David, Patrick, Philip"
header-img: "img/post-bg-01.jpg"
---

<h2>A Tale of Twitter</h2>

<p>Working with huge datasets is a hallmark of Data Science. Up until now, that sounded like an amazing idea. However, as we discovered, there is a big difference between working with large datasets and working with bad datasets. Our initial idea of a project revolved around working with Twitter as our dataset, which turns out to be a remarkably bad dataset. But first, our mentality!</p>

<p>For our project idea, we were interested in exploring a time-series based dataset and the influence or correlation of some external factors with this dataset. We initially came from the angle of looking into the stock market as the time series, as there is a lot of publicly available data on it. Along with that, it seemed like an easy dataset in that it contained mainly doubles values and would require little cleaning. For our external factor, we wanted to look into Twitter and the general sentiment that a body of Tweets for a day can show. What we found out was that Twitter utterly sucks. For one, there is no (free) publicly available historical data. The only way to get Twitter data is to use their stream api, which gathers 1% of Twitter in realtime. Yep, that bad. We did not instantly give up however. We started data collection, and up until recently collected about 15 million Tweets. What we realized sadly is that this data meant very little. We could not analyze trends over time, because we were only able to gather data for days at a time, meaning that if something happened in the stock market a week or two ago, we would not have any information linking to it. So we scrapped that idea. Along with that, we realized that if we were going to be collecting Twitter data, this project would quickly turn into more of a data collection project, instead of our goal of an algorithmic/ML and data science influenced project. So, we decided pivoting made the most sense.</p>

<h2>Finding our Wings</h2>

<p>So you may be thinking, what are we even doing. Good question. We are pivoting, and the next move we are looking into is doing something that this team is interested in and can be applied to the course of data science. What we eventually decided was why not start with an algorithm we know we’re interested in, and then apply it from there. This algorithm (and concept as a whole) is neural networks. Very high level, we came up with the plan as follows:</p>

<ul>
  <li>Learn as much as we can about neural networks</li>
  <li>Along the way, create some implementations of neural networks and validate their outputs through some simple tests on datasets</li>
  <li>Use existing implementation(s) of neural networks and apply this to an interesting dataset - perhaps something sports or time-series or gambling/betting related</li>
</ul>