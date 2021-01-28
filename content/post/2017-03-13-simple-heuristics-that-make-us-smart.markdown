---
author: jasonacollins
comments: true
date: 2017-03-13 08:00:47+00:00
draft: no
link: https://jasoncollins.blog/2017/03/13/simple-heuristics-that-make-us-smart/
slug: simple-heuristics-that-make-us-smart
title: Gerd Gigerenzer, Peter Todd and the ABC Research Group's Simple Heuristics
  That Make Us Smart
wordpress_id: 21855
---

I have recommended Gerd Gigerenzer, Peter Todd and the ABC Research Group's  [Simple Heuristics That Make Us Smart](http://amzn.to/2mpR4EY) enough times on this blog that I figured it was time to post a synopsis or review.

After re-reading it for the first time in five or so years, this book will still be high on my recommended reading list. It provides a nice contrast to the increasing use of complex machine learning algorithms for decision making, although it is that same increasing use that makes some parts of the book are seem a touch dated.

The crux of the book is that much human (or other animal) decision making is based on fast and frugal heuristics. These heuristics are fast in that they do not rely on heavy computation, and frugal in that they only search for or use some of the available information.

Importantly, fast and frugal heuristics do not simply trade-off speed for accuracy. They can be both fast and accurate as the tradeoff is between generality versus specificity. The simplicity of fast and frugal heuristics allows them to be robust in the face of environmental change and generalise well to new situations, leading to more accurate predictions for new data than a complex, information-guzzling strategy. The heuristics avoid the problem of overfitting as they don't assume every detail to be of utmost relevance, and tend to ignore the noise in many cues by looking for the cues that swamp all others.

These fast and frugal heuristics often fail the test of logical coherence, a point often made in the heuristics and biases program kicked off by Kahneman and Tversky. But as Gigerenzer and Todd argue in the opening chapter, pursuing rationality of this nature as an ideal is misguided, as many of our forms of reasoning are powerful and accurate despite not being logically coherent. The function of heuristics is not to be coherent. Their function is to make reasonable adaptive inference with limited time and knowledge.

As a result, Gigerenzer and Todd argue that we should replace the coherence criteria with an assessment of real-world functionality. Heuristics are the way the mind takes advantage of the structure of the environment. They are not unreliable aids used by humans despite their inferior performance.

This assessment of the real-world functionality is also not a general assessment. Heuristics will tend to be domain specific solutions, which means that "ecological rationality" is not simply a feature of the heuristic, but a result of the interaction between the heuristic and the environment.

**Bounded rationality**

If you have read much Gigerenzer you will have seen his desire to make clear what bounded rationality actually is.

Bounded rationality is often equated with decision making under constraints (particularly in economics). Instead of having perfect foresight, information must be obtained through search. Search is conducted until the costs of search balance the benefits of the additional information.

One of the themes of the first chapter is mocking the idea that decision making under constraints brings us closer to a model of human decision making. Gigerenzer and Todd draw on the example of Charles Darwin, who created a list of the pros and cons of marriage to assist his decision. This unconstrained optimisation problem is difficult. How do you balance children and the charms of female chit chat against the conversation of clever men at clubs?

But suppose a constrained Darwin is starting this list from scratch. He already has two reasons for marriage. Should he try to find another? To understand whether he should continue his search he effectively needs to know the costs and benefits of all the possible third options and understand how each would affect his final decision. He effectively needs to know and consider more than the unconstrained man. You could even go the next order of consideration and look at the costs and benefits of all the cost and benefit calculations, and so on. Infinite regress.

So rather than bounded rationality being decision making under constraints, Gigerenzer argues for something closer to Herbert Simon's conception, where bounded rationality is effectively adaptive decision making. The mind is computationally constrained, and uses approximations to achieve most tasks as optimal solutions often do not exist or are not tractable (think the relatively simple world of chess). The effectiveness of this approximation is then assessed in the environment in which the mind makes the decisions, resulting in what Gigerenzer terms the "ecological rationality" of the decision.

**The recognition heuristic**

The first fast and frugal heuristic to be examined in detail in the book is the recognition heuristic. Goldstein and Gigerenzer (the authors of that chapter) define the  recognition heuristic as "If one of two objects is recognized and the other is not, then infer that the recognized object has the higher value."

The recognition heuristic is frugal as it requires a lack of knowledge to work - a failure to recognise one of the alternatives. The lack of computation required to apply it points to its speed. Goldstein and Gigerenzer argue that the recognition heuristic is a good model for how people actually choose, and present evidence that it is often applied despite conflicting or additional information being available.

Recognition is different from the concept of "[availability](https://en.m.wikipedia.org/wiki/Availability_heuristic)" developed by Tversky and Kahneman. The availability heuristic works by drawing on the most immediate or recent examples when making an evaluation.  Availability refers to the availability of terms or concepts in memory, whereas recognition relies on the differences between things _in and out_ of memory.

As an example application (and success) of the recognition heuristic, American and German students were asked to compare pairs of German or American cities and select the larger. American students comparing pairs of American cities did worse than Germans on those same American cities - the Americans knew too much to apply the recognition heuristic. The Americans do as well comparing less familiar German cities as they do American cities.

The success of the recognition heuristic results in what could be described as a "less is more" effect. There are situations where decisions based on missing information can be more accurate than those made with more knowledge. There is information implicit in the failure to recognise something.

A second chapter on the recognition heuristic by Borges and friends involves the authors using the recognition heuristic to guide their stock market purchases. They surveyed US and German experts and laypeople about US and German shares and invested based on those that were recognised.

Overall, the authors' returns beat the aggregate market indices. A German share portfolio based on the recognition of any of the US and German experts or US and German laypeople outperformed the market indices, as did the US stock portfolio based on recognition by Germans. The only group for which recognition delivered lower returns was the US portfolio based on US expert or layperson recognition.

Borges and friends did note that this was a one-off experiment in a bull market, so there is a question of whether it would generalise to other market conditions (or even if it was more than a stroke of luck). But the next chapter took the question of the robustness of simple heuristics somewhat more seriously.

**The competition**

One of the more interesting chapters in the book is a contest across a terrain of 20 datasets between a fast and frugal heuristic, "take-the-best", and a couple of other approaches, including the more computationally intensive multiple linear regression. In each of these 20 contests, the competitors were tasked with selecting for all pairs of options which has the highest value. This includes predicting which of two schools had the highest drop out rates, which stretches of highway had the highest accident rates, or which people had the highest body fat percentage.

The take-the-best heuristic works as follows: Choose the cue most likely to distinguish correctly between the two. If the two choices differ on that cue, select the one with the highest value, and end the search. If they are the same, move to the cue with the next highest validity and repeat.

For example, suppose you are comparing the size of two German cities and the best predictor (cue) of size is whether they are a capital city. If neither is a capital city, you then move to the next best cue of whether they have a soccer team. If one does and the other doesn't, select the city with the soccer team as being the larger.

The general story is that in terms of fitting the full dataset, take-the-best performs well but is narrowly beaten by multiple regression (75% to 77% - although multiple regression was only fed cue direction, not quantitative variables). The closeness across the range of datasets suggests that the power of take the best is not just restricted to one environment.

The story changes more in favour of take-the-best when the assessment shifts to prediction out-of-sample, with multiple regression suffering a severe penalty. Regression accuracy dropped to 68%, whereas take-the-best dropped less to 71%.

There was a model in the competition - the minimalist - which only considered a randomly chosen cue and seeing if it points in one direction or the other. If so, select that choice, otherwise select another cue. The performance of the minimalist suggested frugality can be pushed too far, although it did perform only 3 percentage points below regression in out-of-sample prediction.

The results of the challenge suggests that take-the-best tends not to sacrifice accuracy for its frugality. The relative performance of take-the-best is particularly strong when there is a low number of training examples, with regression having less chance of overfitting in larger environments. Regression tended to perform relatively worse when there were less examples per cue. One point that favoured take-the-best is that the trial didn't have many large environments. Only two had more than 100 examples, and many had between 10 and 30.

The restriction of regression to use cue direction rather than the quantitative variable also dampened its effectiveness. If able to use quantitative predictors, regression tied take the best on 76% out of sample, even though take-the-best doesn't use these quantitative values. There was effectively no penalty for the frugality.

A later chapter added to the competition computationally expensive Bayesian models. Bayesians networks won the competition on out-of-sample testing by three percentage points over take-the-best. Again, take-the-best did best relatively when there were small numbers of examples. The more frugal naive Bayes also did pretty well - falling somewhere between the two approaches.

The results suggest that each approach has its place. Use fast and frugal approaches when you need to be quick with low numbers of examples, and use Bayesian approaches when have time, computational power and knowledge. This is where some of the examples start to feel dated when the size of the datasets in many domains is rapidly growing in combination with cheaper computational power.

This dated feel is even more apparent in the competition between another heuristic, categorisation by elimination, and neural networks across 3 datasets.

Categorisation by elimination is a classification algorithm that walks through examples and cues, starting from the cue with the highest probability of success. If the example can be categorised, categorise it and move to the next example. If not, move to the next cue, with possible categories limited to those possible given earlier cues. Repeat until classified.

In measured performance, categorisation by elimination was only a few percentage points behind neural networks, although the datasets contained only 150, 178 and 8124 examples. The performance of neural networks also capped out at 100% on the largest mushroom dataset (not bad when picking what should eat and consequences) and 94 and 96% on the other two. There wasn't much room for a larger victory.

A couple of the chapters are also just a touch too keen to show the effectiveness of the simple heuristics. This was one such case. An additional competition was run giving neural networks only a limited number of cues, in which case its performance plunges. But these cues were chosen based on the number of cues used by categorisation by elimination, rather than a random selection.

**The 37% rule**

One interesting chapter is on the "secretary problem" and the resulting 37% rule. The basic idea is that you have a series of candidates you are interviewing for the role of secretary (this conception of the problem spread in the 1950s). You view each candidate one by one and must decide on the spot if you will stop your search there and hire the candidate in front of you. If you move to the next candidate, the past candidate is gone forever.

To maximise your probability of finding the best secretary, you should view 37% of the candidates without making any choice, and then accept the next candidate who is better than all you have seen to date. This rule gives (coincidentally) a 37% chance of ending up with the best mate.

But this rule is not without risks. If the best candidate was in that first 37%, you will end up with the last person you see, effectively a random person from the population. So there is effectively a 37% chance of a random choice. Because of that random choice, the 37% rule leaves you with a 9% chance you will end up with someone in the bottom quartile.

But what if, like most people, you have a degree of risk aversion - particularly if you are applying the rule to serious questions such as mate choice. Suppose there are 100 candidates and you want someone out of the top 10%. In that case you only want to look at the first 14% of candidates and choose the next candidate who is better than all previous candidates. That gives you an 83% chance of a top 10% candidate. If you will settle for the top 25%, you only need look at the first 7% for a 92% chance of getting someone in the top quartile.

In larger populations, you need to look at even less. With 1000 people, you need only look at only 3% of the candidates to maximise chance of top 10% at 97% probability. For a top 25% mate, you should only check out 1 to 2%.

The net result is that the 37% rule sets aspirations too high unless you will settle for nothing but the best. It is less robust than other rules.

This exploration points to the potential for a simple search heuristic. Try a dozen will generally outperform the 37% rule across most population sizes for getting a good but not perfect mate. Try a few dozen is a great rule for someone in New York who wants close to the best.

Then there is the issue that the success of the 37% rule depends on your own value. On finding the mate you will finally propose to, what is the probability that the two-sided choice will end up with them saying yes? In domains such as mate choice, only one or two people could get away with applying that rule - and that leads to a whole new range of considerations.

**Odds and ends**

The book is generally interesting throughout. Here are a few odds and ends:




    
  * One chapter argues that the hindsight bias is the product of fast and frugal approach to recalling decisions. We update knowledge when it is received. If we cannot recall the original decision, we can approximate it by going through the same process as used to generate the decision last time. But if we have updated our knowledge, we get a new answer.

    
  * As mentioned, some chapters are a bit out of date. One chapter is on using heuristics to predict intention from motion. I expect neural networks will likely be in another league on domains such as this compared to when the book was written.

    
  * Another chapter is on investment in offspring. Heuristics such as invest in the oldest do almost as well as the optimal investment rules developed by [Becker](https://en.m.wikipedia.org/wiki/Gary_Becker#Families), despite their lack of relative complexity. The best rule for a particular time will depend on the harshness of the environment.


