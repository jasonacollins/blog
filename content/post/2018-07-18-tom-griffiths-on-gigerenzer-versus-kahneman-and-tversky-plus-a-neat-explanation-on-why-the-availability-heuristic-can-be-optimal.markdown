---
author: jasonacollins
comments: true
date: 2018-07-18 09:00:46+00:00
draft: no
link: https://jasoncollins.blog/2018/07/18/tom-griffiths-on-gigerenzer-versus-kahneman-and-tversky-plus-a-neat-explanation-on-why-the-availability-heuristic-can-be-optimal/
slug: tom-griffiths-on-gigerenzer-versus-kahneman-and-tversky-plus-a-neat-explanation-on-why-the-availability-heuristic-can-be-optimal
title: Tom Griffiths on Gigerenzer versus Kahneman and Tversky. Plus a neat explanation
  on why the availability heuristic can be optimal
wordpress_id: 22961
---

From an [interview of Tom Griffiths](http://rationallyspeakingpodcast.org/show/rs-154-tom-griffiths-on-why-your-brain-might-be-rational-aft.html) by Julia Galef on the generally excellent [Rationally Speaking](http://rationallyspeakingpodcast.org) podcast (transcript [here](http://static1.1.sqspcdn.com/static/f/468275/26898144/1457285505177/rs154transcript.pdf?token=kF%2FNCx3kE%2Bi67Itjd753Ac%2BRwIU%3D)):


<blockquote>**Julia:** There's this ongoing debate in the heuristics and biases field and related fields. I’ll simplify here, but between, on the one hand, the traditional Kahneman and Tversky model of biases as the ways that human reasoning deviates from ideal reasoning, systematic mistakes that we make, and then on the other side of the debate are people, like for example Gigerenzer, who argue, "No, no, no, the human brain isn't really biased. We're not really irrational. These are actually optimal solutions to the problems that the brain evolved to face and to problems that we have limited time and processing power to deal with, so it's not really appropriate to call the brain irrational, it's just optimized for particular problems and under particular constraints."

It sounds like your research is pointing towards the second of those positions, but I guess it's not clear to me what the tension actually is with Kahneman and Tversky in what you've said so far.

**Tom:** Importantly, I think, we were using pieces of both of those ideas. I don't think there's necessarily a significant tension with the Kahneman and Tversky perspective.

Here's one way of characterizing this. Gigerenzer's argument has focused on one particular idea which comes from statistics, which is called the bias‐variance trade off. The basic idea of this principle is that you don't necessarily want to use the most complex model when you're trying to solve a problem. You don't necessarily want to use the most complex algorithm.

If you're trying to build a predictive model, including more predictors into the model can be something which makes the model actually worse, provided you are doing something like trying to minimize the errors that you're making in accounting for the data that you've seen so far. The problem is that, as your model gets more complicated, it can overfit the data. It can end up producing predictions which are driven by noise that appears in the data that you're seeing, because it's got such a greater expressive capacity.

The idea is, by having a simpler model, you're not going to get into that problem of ending up doing a good job of modeling the noise, and as a consequence you're going to end up making better predictions and potentially doing a better job of solving those problems.

Gigerenzer's argument is that some of these heuristics, which you can think about as strategies that end up being perhaps simpler than other kinds of cognitive strategies you can engage in, they're going to work better than a more complex strategy ‐‐ precisely because of the bias‐variance trade off, precisely because they take us in that direction of minimizing the amount that we're going to be overfitting the data.

The reason why it's called the bias‐variance trade off is that, as you go in that direction, you add bias to your model. You're going to be able to do a less good job of fitting data sets in general, but you're reducing variance ‐‐ you're reducing the amount which the answers you're going to get are going to vary around depending on the particular data that you see. Those two things are things that are both bad for making predictions, and so the idea is you want to find the point which is the right trade off between those two kinds of errors.

**...**

What's interesting about that is that you basically get this one explanatory dimension where it says making things simpler is going to be good, but it doesn't necessarily explain why you get all the way to the very, very simple kinds of strategies that Gigerenzer tends to advocate. Because basically what the bias‐ variance trade off tells you is that you don't want to use the most complex thing, but you probably also don't want to use the simplest thing. You actually want to use something which is somewhere in between, and that might end up being more complex than perhaps the simpler sorts of strategies that Gigerenzer has identified, things that, say, rely on just using a single predictor when you're trying to make a decision.

Kahneman and Tversky, on the other hand, emphasized heuristics as basically a means of dealing with cognitive effort, or the way that I think about it is computational effort. Doing probabilistic reasoning is something which, as a computational problem, is really hard. It's Bayesian inference... It falls into the categories of problems which are things that we don't have efficient algorithms to get computers to do, so it's no surprise that they'd be things that would be challenging for people as well. The idea is, maybe people can follow some simpler strategies that are reducing the cognitive effort they need to use to solve problems.

Gigerenzer argued against that. He argued against people being, I think the way he characterized it was being “lazy,” and said instead, "No, we're doing a good job with solving these problems."

I think the position that I have is that I think both of those perspectives are important and they're going to be important for explaining different aspects of the heuristics that we end up using. If you add in this third factor of cognitive effort, that's something which does maybe push you a little bit further in terms of going in the direction of simplicity, but it's also something that we can use to explain other kinds of heuristics.</blockquote>


Griffiths later provides a great explanation of why the availability heuristic can be a good decision-making tool:


<blockquote>**Tom: **The basic idea behind availability is that if I ask you to judge the probability of something, to make a decision which depends on probabilities of outcomes, and then you do that by basically using those outcomes which come to mind most easily.

An example of this is, say, if you're going to make a decision as to whether you should go snorkeling on holiday. You might end up thinking not just about the colorful fish you're going to see, but also about the possibility of shark attacks. Or, if you're going to go on a plane flight, you'll probably end up thinking about terrorists more than you should. These are things which are very salient to us and jump out at us, and so as a consequence we end up overestimating their probabilities when we're trying to make decisions.

What Falk did was look at this question from the perspective of trying to think about a computational solution to the problem of calculating an expected utility. If you're acting rationally, what you should be doing when you're trying to make a decision as to whether you want to do something or not, is to work out what's the probabilities of all of the different outcomes that could happen? What's the utility that you assign to those outcomes? And then average together those utilities weighted by their probabilities. Then that gives you the value of that particular option.

That's obviously a really computationally demanding thing, particularly for the kinds of problems that we face as human beings where there could be many possible outcomes, and so on and so on.

A reasonable way that you could try and solve that problem instead is by sampling, by generating some sample of outcomes and then evaluating utilities of those outcomes and then adding those up.

Then you have this question, which is, well, what distribution should you be sampling those outcomes from? I think the immediate intuitive response is to say, "Well, you should just generate those outcomes with the probability that they occur in the world. You should just generate an unbiased sample." Indeed, if you do that, you'll get an unbiased estimate of the expected utility.

The problem with that is that if you are in a situation where there are some outcomes that are extreme outcomes ‐‐ that, say, occur with relatively lower probability, which is I think the sort of context that we often face in the sorts of decisions that we make as humans ‐‐ then that strategy is going to not work very well. Because there's a chance that you don't generate those extreme outcomes, because you're sampling from this distribution, and those things might have relatively low chance of happening.

...

The answer is, in order to deal with that problem, you probably want to generate from a different distribution. And we can ask, what's the best distribution to generate from, from the perspective of minimizing the variance in the estimates? Because in this case it's the variance which really kills you, it's the variability across those different samples. The answer is: Add a little bit of bias. It's the bias‐variance trade off again. You generate from a biased distribution, that results in a biased estimate.

The optimal distribution to generate from, from the perspective of minimizing variance, is the distribution where the probability of generating an outcome is proportional to the probability of that outcome occurring in the world, multiplied by the absolute value of its utility.

Basically, the idea is that you want to generate from a distribution where those extreme events that are either extremely good or extremely bad are given greater weight ‐‐ and that's exactly what we end up doing when we're answering questions using those available examples. Because the things that we tend to focus on, and the things that we tend to store in our memory, are those things which really have extreme utilities.</blockquote>


Can we make the availability heuristic work better for us?


<blockquote>I think the other idea is that, to the extent that we've already adopted these algorithms and these end up being strategies that we end up using, you can also ask the question of how we might structure our environments in ways that we end up doing a better job of solving the problems we want to solve, because we've changed the nature of the inputs to those algorithms. If intervening on the algorithms themselves is difficult, intervening on our environments might be easier, and might be the kind of thing that makes us able to do a better job of making these sorts of inferences.

To return to your example of shark attacks and so on, I think you could expect that there's even more bias than the optimal amount of bias in availability‐based decisions because what's available to us has changed. One of the things that's happened is you can hear about shark attacks on the news, and you can see plane crashes and you can see all of these different kinds of things. The statistics of the environment that we operate in are also just completely messed up with respect to what's relevant for making our own decisions.

So a basic recommendation that would come out of that is, if this is the way that your mind tends to work, try and put yourself in an environment where you get exposed to the right kind of statistics. I think the way you were characterizing that was in terms of you find out what the facts are on shark attacks and so on.</blockquote>


Listen to the [full](http://rationallyspeakingpodcast.org/show/rs-154-tom-griffiths-on-why-your-brain-might-be-rational-aft.html)[ episode](http://rationallyspeakingpodcast.org/show/rs-154-tom-griffiths-on-why-your-brain-might-be-rational-aft.html) - or in fact, much of the [Rationally Speaking](http://rationallyspeakingpodcast.org) back catalogue. I'm still only partway through, but recommend the interviews with [Daniel Lakens](http://rationallyspeakingpodcast.org/show/rs123-daniel-lakens-on-p-hacking-and-other-problems-in-psych.html) on p-hacking, [Paul Bloom](http://rationallyspeakingpodcast.org/show/rs142-paul-bloom-on-the-case-against-empathy.html) on empathy, [Bryan Caplan](http://rationallyspeakingpodcast.org/show/rs144-bryan-caplan-on-does-parenting-matter.html) on parenting, [Phil Tetlock](http://rationallyspeakingpodcast.org/show/rs145-phil-tetlock-on-superforecasting-the-art-and-science-o.html) on forecasting, [Tom Griffiths's reappearance](http://rationallyspeakingpodcast.org/show/rs-161-tom-griffiths-and-brian-christian-on-algorithms-to-li.html) with his Algorithms to Live By co-author, Brian Christian, and [Don Moore](http://rationallyspeakingpodcast.org/show/rs-168-don-moore-on-overconfidence.html) on overconfidence. Julia Galef is a great interviewer - I like the sceptical manner in which she probes her guests and digs into the points she wants to understand.
