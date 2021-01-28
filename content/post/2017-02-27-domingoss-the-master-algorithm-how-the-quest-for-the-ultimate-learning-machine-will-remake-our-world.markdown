---
author: jasonacollins
comments: true
date: 2017-02-27 08:00:33+00:00
draft: no
link: https://jasoncollins.blog/2017/02/27/domingoss-the-master-algorithm-how-the-quest-for-the-ultimate-learning-machine-will-remake-our-world/
slug: domingoss-the-master-algorithm-how-the-quest-for-the-ultimate-learning-machine-will-remake-our-world
title: 'Pedro Domingos''s The Master Algorithm: How the Quest for the Ultimate Learning
  Machine Will Remake Our World'
wordpress_id: 21757
---

My view of Pedro Domingos's [The Master Algorithm: How the Quest for the Ultimate Learning Machine Will Remake Our World](http://amzn.to/2gwanIv) depends on which part of the book I am thinking about.

The opening and the close of the book verge on techno-Panglossianism. The five chapters on the various "tribes" of machine learning, plus the chapter on learning without supervision, are excellent. And I simply don't have the knowledge to judge the value of Domingos's reports on his own progress to the master algorithm.

Before getting to the details, The Master Algorithm is a book on machine learning. Machine learning involves the development of algorithms that can learn from data. Domingos describes it as computers programming themselves, but I would prefer to describe it as humans engaging in a higher level of programming. Give the computer some data and the objective, provide a framework for developing the solution (each of Domingos's tribes has a different approach to this), and let the computer develop it.

Machine learning's value is becoming more apparent with increasing numbers of problems involving "big data" and mountains of variables that cannot be feasibly be incorporated into explicitly designed programs. Tasks such as predicting the tastes of Amazon's customers or deciding which updates to show each Facebook user are effectively intractable given the millions of choices available. In response, the Facebooks and Amazons of the world are designing learning algorithms that can use the massive amounts of data available to attempt to determine what their customers or users want.

Similarly, explicitly programming a self-driving car for every possible scenario is not feasible. But train it on massive amounts of data and it can learn to drive itself.

The master algorithm of the book's title is a learning algorithm that can be used across all domains. Today there are five tribes (as categorised by Domingos), each with their own master algorithm. The ultimate master algorithm combines them into a general purpose learning machine.

The first tribe, the **symbolists**, believe in the power of logic. Their algorithms build sets of rules that can classify the examples in front of it. Induction, or as Domingos notes, inverse deduction, can be used to generate further rules to fill in the gaps.

To give the flavour of this approach, suppose you are trying to find the conditions under which certain genes are expressed. You run a series of experiments and your algorithm generates an initial set of rules from the results.



<blockquote>_If the temperature is high, gene A is expressed._

_If the temperature is high, genes B and D are not expressed._

_If gene C is expressed, gene D is not._</blockquote>



Gaps in these rules can then be filled in by inverse deduction. From the above, the algorithm might induce _If gene A is expressed and gene B is not, gene C is expressed_. This could then be tested in experiments and possibly form the basis for further inductions. These rules are then applied to new examples to predict whether the gene will be expressed or not.

One tool in the symbolist toolbox is the decision tree. Start at the first rule, and go down the branch pointed to by the answer. Keep going until you reach the end of a branch. Considering massive bodies of rules together is computationally intensive, but the decision tree saves on this by ordering the rules and going through them one-by-one until you get the class. (This also solves the problem of conflicting rules.)

The second tribe are the **connectionists**. The connectionists take their inspiration from the workings of the brain. Similar to the way that connections between neurons in our brain are shaped by experience, the connectionists build a model of neurons and connect them in a network. The strength of the connections between the neurons is then determined by training on the data.

Of the tribes, the connectionists could be considered to be in the ascendency at the moment. Increases in computational power and data have laid the foundations for the success of their deep learning algorithms - effectively stacks or chains of connectionist networks - in applications such as image recognition, natural language processing and driving cars.

The third tribe are the **evolutionaries**, who use the greatest algorithm on earth as their inspiration. The evolutionaries test learning algorithms by their "fitness", a scoring function as to how well the algorithm meets its purpose. The fitter algorithms are more likely to live. The successful algorithms are then mutated and recombined (sex) to produce new algorithms that can continue the competition for survival. Eventually an algorithm will find a fitness peak where further mutations or recombination do not increase the algorithm's success.

A major contrast with the connectionists is the nature of evolutionary progress. Neural networks start with a predetermined structure. Genetic algorithms can learn their structure (although a general form would be specified). Backpropogation, the staple process by which neural networks are trained, starts from an initial random point for a single hypothesis but then proceeds deterministically in steps to the solution. A genetic algorithm has a sea of hypotheses competing at any one moment, with the randomness of mutation and sex potentially producing big jumps at any point, but also generating many useless algorithm children.

The fourth tribe are the **Bayesians**. The Bayesian's start with a set of hypotheses that could be used to explain the data, each of which has a probability of being true (their 'priors'). Those hypotheses are then tested against the data, with those hypotheses that better explain the data increasing in their probability of being true, and those that can't decreasing in their probability. This updating of the probability is done through Bayes' Rule. The effective result of this approach is that there is always a degree of uncertainty - although often the uncertainty relating to improbable hypotheses is negligible.

This Bayesian approach is typically implemented through Bayesian networks, which are arrangements of events that each have specified probabilities and conditional probabilities (the probability that an event will occur conditional on another event or set of events occurring). To prevent explosions in the number of probability combinations required to specify a network, assumptions about the degree of independence between events are typically made. Despite these possibly unrealistic assumptions, Bayesian networks can still be quite powerful.

The fifth and final tribe are the **analogisers**, who, as the name suggests, reason by analogy. Domingos suggests this is perhaps the loosest tribe, and some members might object to being grouped together, but he suggests their common reliance on similarity justifies their common banner.

The two dominant approaches in this tribe are nearest neighbour and support vector machines. Domingos describes nearest neighbour as a lazy learner, in that there is no learning process. The work occurs when a new test example arrives and it needs to be compared across all existing examples for similarity. Each data point (or group of data points for _k_-nearest neighbour) is its own classifier, in that the new example is classified into the same class as that nearest neighbour. Nearest neighbour is particularly useful in recommender systems such as those run by the Netflixes and Amazons of the world.

Support vector machines are a demonstration of the effectiveness of gratuitously complex models. Support vector machines classify examples by developing boundaries between the positive and negative examples, with a specified "margin" of safety between the examples. They do this by mapping the points into a hyper-dimensional space and developing boundaries that are straight lines. The examples along the margin are the "support vectors".

Of Domingos's tribes, I feel a degree of connection to them all. Simple decision trees can be powerful decision tools, despite their simplicity (or possibly because of it). It is hard not to admire the progress of the connectionists in recent years in not just technical improvement but also practical applications in areas such as medical imaging and driverless cars. Everyone seems to be a Bayesian nowadays (or wants to be), including me. And having played around with support vector machines a bit, I'm both impressed and perplexed by their potential.

From a machine learning perspective, it is the evolutionaries I feel possibly the least connection with. Despite my interest and background in evolutionary biology, it's the one group I haven't seen practically applied in any of the domains I operate. I've read a few John Holland books and articles (Holland being one of the main protagonists in the evolutionary chapter) and always appreciate the ideas, but have never felt close to the applications.

Outside of the chapters on the five tribes, Domingos's Panglossianism grates, but it is relatively contained to the opening and closing of the book. In Domingos's view, the master algorithm will make stock market crashes fewer and smaller, and the play of our personal algorithms with everyone else's will make our lives happier, longer and more productive. Every job will be better than it is today. Democracy will work better because of higher bandwidth communication between voters and politicians.

But Domingos's gives little thoughts to what occurs where people have different algorithms, different objectives, different data they have trained their algorithm on and, in effect, different beliefs. Little thought is given to the complex high-speed interaction of these algorithms.

There are a few other interesting threads in the books worth highlighting. One is the idea that you need bias to learn. If you don't have preconceived notions of the world, you could conceive of a world where everything you haven't seen is the opposite of what you predict (known as the 'No free lunch theorem').

Another is the idea that once computers get to a certain level of advancement, the work of scientists will largely be trying to understand the outputs of computers rather than generate the outputs themselves.

So all up, a pretty good read. For a snapshot of the book, the [Econtalk episode](http://www.econtalk.org/archives/2016/05/pedro_domingos.html) featuring Domingos is (as usual) excellent.
