# Project Proposal
## Team Twitter Science Data Squad (WIP)

#### *Who is on the team?*
David Abrahams, Patrick Huston, Philip Seger

#### *In a couple of paragraphs, describe the key ideas of your proposed project?  What is your MVP?  What are your stretch goals?*

The main idea behind our project is looking into the giant complex system that is the stock market. There are huge amounts of available data on individual companies, with very specific granularity, for long periods of time, so the idea of looking into the stock market and utilizing it as our dataset was quite interesting. However, the stock market as a whole is too complex to evaluate, along with the fact that it is near impossible to build predictions on a specific company without also looking to external sources. For that reason, we are planning on looking into the stock market with relation to popular opinion from Twitter. Our main question we plan on figuring out is how good of an indicator public opinion is in relation to stock data, and how the public’s feelings for a given day (calm, angry, happy, etc.) relate back to how well the market may be doing. For this question, we want to build visualizations that correlate the data and show trends from historical Twitter data and historical stock market data.

It is worth mentioning that single Tweets can provide very little information to us. For one, there is a lot of randomness Tweeted about. Along with that, a Tweet is 140 characters, which would be difficult to properly clean for a dataset. As such, we plan on using sentiment analysis for Tweets to be able to gather whether they are positive or negative. From this, we can assign a value for each Tweet and build a usable dataset. Then, we will compare this information to gathered data for the stock market around the similar timeframe. As such, the MVP for this project would be a system to compared Twitter data to data from the stock market, which we could then build visualizations from. A possible stretch goal we have thought about is looking into building a model that could use real-time Twitter data and market data to predict whether a specific stock (or the market as a whole) will be positive or negative for the day.

#### *To the best of your current knowledge, what datasets will you use for your project?  Are there any obstacles you foresee in terms of getting access to the data?*

We plan on utilizing two main sources of data during the course of this project:

1. Historical Twitter Data. This may end up being more difficult than initially conceived, however we have backup plans to implement a utility to start amassing our own dataset autonomously. 
2. Historical stock market data. This is easily accessible to the public and exposed by convenient APIs provided by CNN money and Yahoo! Finance, to name a few. We foresee few troubles in this area. 

#### *What are the most important new skills / techniques you will have to learn to be successful in this project?  If you think some of these skills would be useful for us to cover in class, please indicate which ones.*

In the course of this project, we will have to learn several key skills:

1. Working with a potentially huge dataset. We haven’t done this before, and will have to navigate our way through some expected troubles we may encounter. Along with just being able to store a huge amount of data, we also need to figure out clever ways to clean it so that it can be used effectively. 
2. Being creative with accessing difficult-to-retrieve data from sources like Twitter. Our worst case scenario, where we are unable to get historical Twitter data, will involve gathering our own Twitter dataset, which will be done as soon as possible if needed.
3. Working more with the statistical side of the datasets. The papers we have read point out that there is a correlation between Twitter and stock data, however we want to jump in and see if we can make our own conclusions.

#### *Outline a rough timeline for the major milestones of your project.  This will mainly be useful to refer back to as we move through the project.*

3/25 - Project proposal due

3/27 - If unable to get historical Twitter data, start collecting our own data from Twitter

3/29 - Have an example dataset, begin cleaning (continue collecting data if needed)

4/1 - Cleaned, usable stock dataset, along with Twitter dataset to playtest with, if possible

4/5 - Have started exploring visualizations surrounding stock and Twitter relation

4/8 - Show one example visualization

4/12 - Begin model development

4/15 - CODE REVIEW

4/19 - Continue model development, continue visualization development

4/22 - Begin development of medium to show data to others

4/26 - Continue everything

4/29 - Final code review, along with cleaning up bugs and making sure everything is set

5/3 - Expo presentation of what we worked on

5/4 - Final documentation added to the repo

#### *What do you view as the biggest risks to you being successful on this project?*

The biggest obstacle would likely be the fact that we may be scraping our own data, continuously. Getting a workable dataset that is both useful to what we are looking into and contains enough information is going to be tough, so we need to figure out the best course of action that will get us the most useful information.

#### *Given each of your YOGAs (see here), in what ways is this project well-aligned with these goals, and in what ways is it misaligned?  If there are ways in which it is not well-aligned, please provide a potential strategy for bringing the project and your learning goals into better alignment.*
##### Patrick

This project seems to align very well with my goals. My primary goal is to spend more time looking at outside research papers and contributions made from the community, which is well-aligned with this project in particular. There’s a lot of prior research that has been done in this space, and I’ve already found some great papers that have been just challenging enough such that I can gain a lot from them with some investment of time. Additionally, there seems to be a good amount of room for me to get better at documentation over the course of the project. There’s a lot to learn, a lot to do, which should indicate that there will be a lot to document. 

##### David

This project aligns well with my goals, specifically my last two. My second goal is to do something impactful in the professional sense. My goal was to create something that has concrete value that is applicable in industry, and doing stock market analysis is extremely valuable. This project will also definitely provide me the opportunity to expand my skillset. There’s a ton of complex math that can be done with the stock market, and definitely an opportunity to utilize a breadth of different models. There is also room to learn about sentiment analysis. I’m not entirely sure what the final product would be for this project yet, but whether we create a website or notebook or something else, I’m sure we’ll create something professional.

##### Philip

This project will follow along with what my goals state quite closely. Given the amount of time, and our proposed schedule, we should have enough time to create a proper codebase that is largely bug free and accurately conveys the information we are looking into. On top of that, the project is jumping into fairly new territory for the whole team, which means we are going to have to learn new methods for visualization and building models. The only challenge I foresee in relation to my goals is how much we are able to accomplish. Our general plan as of right now is manually collecting Twitter data, running sentiment analysis on individual tweets to build a general idea of what is being said, build a dataset from that, create a dataset from stock data, then begin working on the two. Right out of the gate, this is complex, but it should be really interesting and challenging, which I am also excited about. 
