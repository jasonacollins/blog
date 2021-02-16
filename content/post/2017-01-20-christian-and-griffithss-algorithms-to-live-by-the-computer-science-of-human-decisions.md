---
author: jasonacollins
date: 2017-01-20 08:00:26+00:00
draft: no
slug: christian-and-griffithss-algorithms-to-live-by-the-computer-science-of-human-decisions
title: 'Brian Christian and Tom Griffiths''s Algorithms to Live By: The Computer Science
  of Human Decisions'
---

In a sea of books describing a competition between perfectly rational decision makers and biased humans who make systematic errors in the way they decide, Brian Christian and Tom Griffiths's *Algorithms to Live By: The Computer Science of Human Decisions* provides a nice contrast.

Christian and Griffiths's decision-making benchmarks are the algorithms developed by mathematicians, computer scientists and their friends. In that world, decision making under uncertainty involves major trade-offs between efficiency, accuracy and the types of errors you are willing to accept. As they write:

<blockquote>The solutions to everyday problems that come from computer science tell a different story about the human mind. Life is full of problems that are, quite simply, hard. And the mistakes made by people often say more about the intrinsic difficulties of the problem than about the fallibility of human brains. Thinking algorithmically about the world, learning about the fundamental structures of the problems we face and about the properties of their solutions, can help us see how good we actually are, and better understand the errors that we make.

...

Even where perfect algorithms haven’t been found, however, the battle between generations of computer scientists and the most intractable real-world problems has yielded a series of insights. These hard-won precepts are at odds with our intuitions about rationality, and they don’t sound anything like the narrow prescriptions of a mathematician trying to force the world into clean, formal lines. They say: Don’t always consider all your options. Don’t necessarily go for the outcome that seems best every time. Make a mess on occasion. Travel light. Let things wait. Trust your instincts and don’t think too long. Relax. Toss a coin. Forgive, but don’t forget. To thine own self be true.</blockquote>



And as they close:



<blockquote>The intuitive standard for rational decision-making is carefully considering all available options and taking the best one. At first glance, computers look like the paragons of this approach, grinding their way through complex computations for as long as it takes to get perfect answers. But as we’ve seen, that is an outdated picture of what computers do: it’s a luxury afforded by an easy problem. In the hard cases, the best algorithms are all about doing what makes the most sense in the least amount of time, which by no means involves giving careful consideration to every factor and pursuing every computation to the end. Life is just too complicated for that.</blockquote>



Here's a few examples.

Suppose you face a choice between two uncertain options. Those options have an expected value - the most likely result. If your objective is to maximise your outcome, you pick the option with the highest expected value.

But what if you objective is to minimise regret - the feeling of pain when you look back at what you did compared to what you could have done? In that case it may be worth looking at the confidence intervals around that expected value - the plausible ranges in which the actual value could lie. Picking the option which has the highest upper confidence interval - the highest plausible value - is the rational approach, even if it has the lower expected value. It is "optimism" in the way a behavioural scientist might frame it, but for an objective of minimising regret, it is rational.

Or consider memory. From a computer science perspective, memory is often not a question of storage but of organisation - particularly in today's world of cheap storage. How does a computer predict which items it will want from its memory in the future such that they are accessible within a reasonable time? Faced with that problem, it makes sense to forget things. In particular, it is often useful to forget things with time - those items least recently used. The human mind mimics this strategy, as more recently used items are more likely to be used in the future. It is too expensive to maintain access to an unbounded number of items.

One chapter of the book covers the idea of "less is more", which you may be familiar if you know the work of Gerd Gigerenzer and friends. The idea behind "less is more" it that it is often rational to ignore information in making decisions to prevent "overfitting". Overfitting is an over-sensitivity to the observed data in developing a model. The inclusion of every detail helps the model match the observed data, but prevents generalisation to new situations and predictions based on new data lack reliability.

To avoid overfitting you might deliberately exclude certain factors, impose penalties for including factors in analysis, or stop the analysis early. These strategies are often used in both computer science or machine learning applications, and by humans, and can result in better decisions.

Christian and Griffiths suggest that evolution tends not to overfit as it is constrained by existing infrastructure and time - features of the environment need some degree of persistence before adaptations to that environment spread, preventing major changes in response to short-term phenomena. Preventing overfitting is also a benefit of a conservative bias in society – preventing us getting caught up in the boom and bust of fads.

There are times in the book where Christian and Griffiths jump too far from experiment or algorithm to real world application. As an example, they suggest that [analysis of a routing](http://theory.stanford.edu/~tim/papers/routing.pdf) tells us not to try to control traffic congestion using a top down coordinator, as the selfish solution is only 33% worse than best case top down coordination. They give little thought to whether congestion has more dimensions of control than just routing. The prisoner's dilemma chapter also seemed shallow at points - possibly reflecting that it is the area for which I already had the most understanding.

But those are small niggles about an otherwise excellent book.
