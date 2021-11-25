---
title: 'Gerd Gigerenzer’s Gut Feelings: Short Cuts to Better Decision Making'
author: jasonacollins
date: 2018-08-22 09:00:56+00:00
draft: no
slug: gerd-gigerenzers-gut-feelings-short-cuts-to-better-decision-making
---

For many years I have been influenced by Gerd Gigerenzer's arguments about the power of simple heuristics and the underlying rationality to many human decisions. But I have contrasting reactions to different parts of Gerd Gigerenzer's body of work.

His published collections of essays - [Simple Heuristics That Make Us Smart](https://www.jasoncollins.blog/simple-heuristics-that-make-us-smart/) (with Peter Todd and the ABC research group), *Adaptive Thinking* and [Rationality for Mortals](https://www.jasoncollins.blog/gerd-gigerenzers-rationality-for-mortals-how-people-cope-with-uncertainty/) - are fantastic, although some people might find them a touch academic.

Gigerenzer's popular books are more accessible, but the loss of some of the nuance, plus his greater stridency of argument, push them to a point where I find a fair bit to disagree with.

In his most recent book, [Risk Savvy](https://www.jasoncollins.blog/nudging-citizens-to-be-risk-savvy/), I struggled with how far Gigerenzer extended his arguments about the power of human decision-making. I agree that the heuristics and biases approach can lead us to be overeager in labelling decisions as "irrational" or sub-optimal. "Biased" heuristics can find a better point on the bias-variance trade-off. They are designed to operate in an uncertain world, not in a lab. But there is little doubt that humans err in some cases - particularly in environments with no resemblance to those in which we evolved. Gigerenzer can be somewhat quick to disparage use of data and praise gut instinct in environments where there is little evidence that these instincts work.

Gigerenzer's earlier *Gut Feelings: Short Cuts to Better Decision Making* strikes perhaps the best balance between nuance and accessibility. While it still leaves an impression about the accuracy of our instincts that I'm not completely in agreement with, it provides a good overview of how our gut feelings can lead to good decisions.

Gigerenzer defines a gut feeling - which you might also call an intuition or hunch - as a feeling that appears quickly in consciousness, with us unaware of the underlying reasons, but strong enough for us to act on. Gut feelings work through simple rules of thumb that take advantage of the evolved capacities of the brain. The skill of the unconscious is knowing what rule to apply at what time.

Let's break this down.

**The power of simple rules**

Gut feelings can be powerful tools despite (and because of) their reliance rules of thumb. Often in decision-making, "less is more", in that there is a beneficial degree of ignorance, or benefits to excluding information from consideration. The recognition heuristic is an example of this: if you recognise one option but not the other, infer that the recognised option has the higher value. The recognition heuristic only works if recognise one but not the other option.

In contrast, complex strategies can explain too much in hindsight. In an uncertain world where only part of the information is useful for the future, a simple rule that focuses on only the best or a limited subset of information has a good chance of hitting that useful information. Gigerenzer provides plenty of examples of the superiority or utility of simple rules of thumb, a point that many advocates of complex statistical methods and machine learning should hear.

But sometimes Gigerenzer's examples drift toward becoming straw man competitions. For instance, he describes a competition between two models - multinomial regression and a heuristic called "Take the best" - in predicting school drop-out rates. Take the best operates by looking only at the cue which has the strongest relationship with drop-out rates (such as the attendance rate), and if one is higher than the other, you make a decision at that point. If the cues have the same value, move to the next cue and repeat.

The two models were trained on half the data, and tested against the other half of the data. Take the best achieved 65% accuracy in the training data, and 60% on the test data. In contrast, multinomial regression achieved 72% on training data, but this plunged to 54% on test data. (Gigerenzer only shows a chart in the book - I got the numbers from the related chapter of [Simple Heuristics That Make Us Smart](https://www.jasoncollins.blog/simple-heuristics-that-make-us-smart/).) Multinomial regression overfit the training data.

This victory for Take the best sounds impressive, but there were observations for only 57 schools, with half the data used in training. Of course basing a prediction on a regression with 18 variables and twenty-odd observations is rubbish. I wouldn't expect anything else. Gigerenzer often frames the victory of simple rules such as Take the Best as surprising to others (and originally to him), which it might be at a general level. But when you look at many of the specific examples and the numbers involved, the surprise doesn't last long.

There is some more subtlety in the reporting of these results in [Simple Heuristics That Make Us Smart](https://www.jasoncollins.blog/simple-heuristics-that-make-us-smart/), where the prediction of drop out rates was one of 20 "competitions" between Take the Best and multiple regression. The overall gap between Take the Best and multiple regression on the test data was 71% versus 68%, an impressive but narrow victory for Take the Best despite its reliance on far fewer cues.

That said, most of the competitions involved small samples - an area where the simple heuristics excel. Only three of the 20 had more than 30 examples available for training the model. The models also had access to dichotomised, not numerical, values, further decreasing the utility of regression. There is a tie at 76% apiece when numerical values were used. The tie is still an impressive result for the simple Take the Best heuristic, but this is now some way from the headline story we get in Gut Feelings. (Conversely, I should also note that the territory of these competitions was fairly stable, which might give more complex techniques an edge. Move to an uncertain dynamic environment, and the simple heuristics may gain an advantage even if the datasets are much larger.)

**How humans use these heuristics**

An important part of Gigerenzer's argument is that these simple heuristics are used by humans. An example he provides is a picture of a boy's head surrounded by four chocolate bars. Which bar does Charlie want? The one he is looking at. The simple heuristic is that "If a person looks at one alternative (longer than at others), it is likely the one the person desires."

The gaze heuristic is another example. Someone seeking to catch a ball will run so as to maintain the angle of the ball in their gaze. The gaze heuristic will eventually lead them to where the ball will land. They don't simply compute where the ball will land and then run there.

The question of whether humans use these heuristics has been tested in the lab. People have been demonstrated to rely heavily on the recognition heuristic when picking winners of tennis matches and football games, particularly where they are unfamiliar with the teams, or in determining which of two cities is larger. Less is more, as if you know all the teams or cities, you can't use the recognition heuristic. This gives the people using these heuristics surprising predictive power, close (or superior) to more knowledgeable experts.

An interesting question about these heuristics is how someone knows when they should apply a particular heuristic. Gigerenzer notes that the skill of the unconscious is knowing, without thinking, what rule to apply at what time. This is the least satisfactory piece of the book, with little discussion as to how this process might work or be effective. It is fair to say the selection is unconscious - people are particularly poor at explaining what rule they applied - but are they skilful at this selection?

The other question mark relates to the inconsistency of our decisions. As Daniel Kahneman and friends have [written about recently](https://www.jasoncollins.blog/noise/), human decisions are often noisy, with decisions varying across occasions. If we are applying heuristics, why do our decisions appear so haphazard in some environments? Does our selection of heuristics only work where we have had the right experience with feedback? More on that below.

**Applied gut feelings**

A point that Gigerenzer highlights - one of his important contributions to how we should think about the heuristics and biases approach - is that the structure of the environment is central to how well a rule of thumb works. A rule of thumb is not good or bad in itself, but depends on the environment in which it is used.

This point was earlier made by Herbert Simon, with his description of the capabilities of the decision maker, and the environment in which they are used, as blades on a pair of scissors. You cannot assess one without the other.

Where I find the discussion of rules of thumb becomes most interesting is in complex environments where we need to learn the rules of thumb to be applied. The heuristic of following someone else's gaze to determine what they are talking about is something that one-year olds do. But consider a hospital, where a doctor is trying to determine whether someone is having a heart attack. Or a CEO deciding whether to support a merger.

Gigerenzer points out - as you can also see in work by others such as Gary Klein - that you need feedback to develop expertise. Absent feedback you are likely to fall back on rules that don't work or that achieve other purposes. Gigerenzer gives the example of judges who are not given feedback on their parole decisions. They then fall back on the heuristic of protecting themselves from criticism by simply following the police and prosecution recommendation.

Gigerenzer offered a few examples where I was not clear on how that expertise could develop. One involves discussion of the benefits of strategies that involve incremental change toward a solution, rather than first computing the ideal solution and acting on it. The gaze heuristic is a good example of this, whereby someone seeking to catch a ball maintains the angle of the ball in their gaze, with this heuristic eventually leading them to where it will land. They don't simply compute where the ball will land and then run there.

Gigerenzer extends this argument to the setting of company budgets:


<blockquote>Strategies relying on incremental changes also characterize how organizations decide on their yearly budgets. At the Max Planck Institute where I work, my colleagues and I make slight adjustments to last year’s budget, rather than calculating a new budget from scratch. Neither athletes nor business administrators need to know how to calculate the trajectory of the ball or the business. An intuitive “shortcut” will typically get them where they would like to be, and with a smaller chance of making grave errors.</blockquote>


The idea of lower probability of "grave error" might be right. But how does someone learn this skill? And here is [Dan Lovallo and Olivier Sibony writing](https://hbr.org/2012/03/can-you-re-anchor-your-next-bu) on the same concept:


<blockquote>It has been another long, exhausting budget meeting. As the presenters showed you their plans, you challenged every number, explored every assumption. In the end you raised their targets a little, but, if you’re honest, you have to admit it: the budget this unit will have to deliver next year is not very different from the one they proposed at the beginning of the budget process, which in turn is not very different from the latest forecast for this year.</blockquote>




<blockquote>What happened? The short answer is, you’ve been anchored. Anchoring is the psychological phenomenon that makes a number stick in your mind and influence you — even though you think you’re disregarding it.</blockquote>


I have some sympathy to the Lovallo and Sibony assessment, having sat in numerous organisations where it was near unanimously agreed that the budget needed to be reallocated, but the status quo prevailed. But I'm not overly convinced it was due to anchoring, rather than trenchant self-interest of those who might be affected, and a timidity and desire to avoid conflict on the behalf of the decision makers. It would be interesting to see a study on this. (Maybe it's out there - I briefly searched, but not particularly hard).

An interesting story in the chapter about medical environments concerned doctors who were required to judge whether someone was having a heart attack. The doctors were doing a generally poor job, defensively sending 90% of people with chest pain to the coronary care unit.

Some researchers developed a process whereby doctors would use a complicated chart with 50-odd probabilities, a long formula and a pocket calculator to determine whether a patient should be admitted to the coronary care unit. The doctors didn't like it and didn't understand it, but its use improved their decision-making and reduced overcrowding in the coronary care unit.

The researchers then took the chart and calculator away from the doctors, with the expectation that the decision-making quality would decline back to what it was previously. But the decision quality did not drop. Exposure to the calculator had improved their intuition permanently. What the doctors needed was the cues that they could not learn from experience, but when provided with them, they applied them in a fast and frugal way that matched the accuracy of the more complicated procedure.

As an aside, the above is how the story is told in Gut Feelings, which might have been coloured by some discussion between Gigerenzer and the researchers. My reading of the [related article](http://psycnet.apa.org/record/1997-30170-001) ([pdf minus charts](http://web.missouri.edu/~segerti/capstone/CCUdecisions.pdf)) has a different chain of events. The researchers first developed the tool using patient data, and presented their results to the doctors. Seven months later, the tool was trialed. They found that admissions to the coronary care unit had declined following the presentation, but not on introduction of the tool, suggesting the doctors started using the cues after the presentation and could achieve equal superiority through their own decision processes. The paper notes that "Take the Best" and tallying - simply adding up the number of cues - would be good strategies. Gigerenzer takes the analysis further [here](http://library.mpib-berlin.mpg.de/ft/gg/GG_Fast_2005.pdf).

As a second aside, this story is similar to one by Daniel Kahneman tells in [Thinking Fast and Slow](https://www.jasoncollins.blog/re-reading-kahnemans-thinking-fast-and-slow/) where military recruiters were asked to use a mechanical process to select candidates. After protesting that they were not robots, Kahneman suggested that after collecting the required data, the recruiters close their eyes, imagine the recruit as a soldier and assign a score of one to five. It turned out the "close your eyes" score was as accurate as the sum of the six factors that were collected, both being much better than the useless interviewing technique they had replaced. Intuition worked, but only after disciplined collection of data (cues).

And as a third aside and contrast, here's a story from [another study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1633627/https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1633627/) (quoted text from [here](https://doi.org/10.1016/0749-5978(86)90046-4)):


<blockquote>During an 18 month period the authors used a computer-based diagnosis system which surpassed physicians in diagnostic accuracy. During the course of this research after each physician made a diagnosis, he or she was informed of the computer’s diagnosis. The diagnostic accuracy of the physicians gradually rose toward that of the computer during the 18 month period. The authors attributed this improvement in part to the “discipline” forced upon the physicians, the constraint of carefully collecting patient information, the “constant emphasis on reliability of clinical data collected, and the rapid ‘feedback’ from the computer,” which may have promoted learning. When the computer system was terminated, the physicians very quickly reverted to their previous lower level of diagnostic accuracy. Apparently discipline and reliability fell victim to creativity and inconsistency.</blockquote>


**The rest of the book**

Gigerenzer provides plenty of other thought-provoking material about the role of heuristics and gut feeling in various domains. Sometimes it feels a bit shallow Advertising is put down to the recognition heuristic. What about signalling, discussed shortly after in another context? The final couple of chapters relating to moral behaviour and social instincts seemed somewhat out-of-date when looked at next to the burgeoning literature on cultural transmission and learning. But there are enough interesting ideas in those chapters to make them worthwhile. And you can't expect someone to pin every point down in-depth in a popular book.

So, if you want a dose of Gigerenzer, Gut Feelings is interesting and worth reading. But if you have the patience, I recommend starting with [Simple Heuristics That Make Us Smart](https://www.jasoncollins.blog/simple-heuristics-that-make-us-smart/), *Adaptive Thinking* and [Rationality for Mortals](https://www.jasoncollins.blog/gerd-gigerenzers-rationality-for-mortals-how-people-cope-with-uncertainty/). Then if you want a slightly less "academic" Gigerenzer, move on to Gut Feelings.
