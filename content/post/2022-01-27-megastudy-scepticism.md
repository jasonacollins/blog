---
title: 'Megastudy scepticism'
author: jasonacollins
date: 2022-03-24 09:00:00+00:00
draft: true
comments: true
image: []
slug: megastudy-scepticism
---

With much fanfare, in December a new "megastudy" was announced, a test of 54 different interventions to encourage exercise. But more that just testing these interventions, a very long list of authors stated:

>Policy-makers are increasingly turning to behavioural science for insights about how to improve citizens’ decisions and outcomes. Typically, different scientists test different intervention ideas in different samples using different outcomes over different time intervals. The lack of comparability of such individual investigations limits their potential to inform policy. Here, to address this limitation and accelerate the pace of discovery, we introduce the megastudy—a massive field experiment in which the effects of many different interventions are compared in the same population on the same objectively measured outcome for the same duration.

I suppose the introduction is for those who missed May's paper by most of the same authors, [A megastudy of text-based nudges encouraging patients to get vaccinated at an upcoming doctor’s appointment](https://doi.org/10.1073/pnas.2101165118). (To be fair, the exercise megastudy was submitted to a journal first.)

In this post I am going to pull apart what I don't like about this study. At its heart it is the same thing that bothers me about behavioural science more generally. There are some great things about this study - I'll discuss them too - but I'll focus on the criticism first.

### Comparability and generalisability

As stated in the abstract, the fundamental problem that the megastudy is trying to solve is the lack of comparability of interventions across experiments. The context of two different experiments may be sufficiently different that it is not reasonable to compare the interventions used in each. How can you determine which is better?

On one level, the megastudy solves this problem. The interventions are in the same context. Comparison is easy - in fact, that is what the experiment is designed to allow.

But this belief that we cannot easily compare across different contexts limits the benefit of the comparison within the mega-study. What confidence can you have that the ordering or magnitude of intervention effect sizes will hold up inthe different context? 

We end up in a situation where the bigger the size of the problem about a lack of comparability that the mega-study is seeking to solve, the less useful the mega-study results are for application in other contexts.

Ultimately, this is why the better policy advice should typically be to run an experiment. The mega-study and other literature could provide some guidance. 

### Theory

The idea that you can run this one big, theory free study to answer a question.

What if we had got some marketers to develop the messaging. 

Some of the non-incentive interventions seem rather half-hearted.



### Power

On its face, the megastudy has the benefit of getting a large sample with which to analyse the effect of interest. A sample of 61,293 sounds solid.

But it doesn't take much consideration to realise that across 54 interventions (including the control), we have not much more than 1000 participants for each. Doing a quick power calculation, if people averaged 1.5 trips to the gym a week with a variance of XX, 1000 participants enables the detection of an effect size of XX with 80% power.

As can be seen by the fact that the biggest effect was an increase of 0.4 gym visits, or an increase of 27%. Sure, the sample size enables differentiation from the control, but when you have 53 interventions jammed into that range of 0.4 you aren't going to be able to distinguish many of them from each other. Only 13 of the 53 were able to be distinguished from anything but the control, and even the best performing could be distinguished from less than half of the interventions.

The cost of this low power becomes most apparent when you examine the pre-registered analysis plans

Here's [one considering the effect of social norms](ADD_LINK), with the communicated norms including variations in level of exercise and the trend. They 

Exercise social norms (included 6 text message reminders):

| Intervention           | Description | Effect        | Predicted |
| :---                   |    :----:   |          ---: |      ---: |
| 3. High and increasing | Title       | Here's this   |           |
| 20. Low                | Text        | And more      |           |
| 47. Low but increasing |             |               |           |
| 53. High               |             |               |           |

The "3. High and increasing" intervention was significantly different from the "53. High" interventions, but otherwise they could not be statistically distinguished. And how confident would you be that this isn't an outlier result, given the High condition involved a social norm which typically has a positive effect. Here it was the only condition with a negative effect size (although not statistically distinguishable from the control). And if you tried to draw a conclusion that the trend is what is important, 

You suddenly find yourself referring to other literature and comparisons, which was part of what the mega-study is designed to enable you to avoid.

Further, most of the treatments . On top of that, given it's the winner and likely an overestimated effect size, 

### The predictions do not make any sense

One interesting thread behind this megastudy is that the researchers obtained estimates of the effect sizes of each intervention.

The authors draw two conclusions from the estimates. The first is that they grossly overestimate the effect size of the interventions. That is a fair conclusion, although weaker than it might appear. Effectively we have a prediction about the effect size in a single context, with those effect size errors all highly correlated. (I think there is support for this point, but again you need to look at other studies.)

That brings us to the second conclusion, which is that the predictors were not able to predict the ordering of the effect sizes. 

I am going to argue here that, at least for this experiment, that it is premature to draw this conclusion. This is for two reasons: the exercise lacked power and then experimental design did not enable useful comparisons, leading to some nonsensical predictions.

One indication of the lack of power is the chart in the paper showing the predictions. The error bars 

This, of course, is a function of both the range and number of predictions. But with each intervention having around only X predictions each and those making predictions being poorly callibrated as to the likely size of effect sizes, this setup was never going to elicit a set of predictions that could be statistically differentiated so as to determien an order.


I can only assume that the researchers also underestimated the expected effect sizes, given the lack of power to distinguish most of the hypotheses proposed. If we turn to the pre-analysis plan I linked above relating to social norms, they stated that they needed a sample size of XX to detect an XX effect size. That's within the realm of the effect size required to differentiate from the controls, but not going to be anywhere near enough to separate four separate interventions from each other - which was the point of the experiment.

But outside of power, I also think there is a larger problem with the predictions. And to tease this out, let's look at a collection of five interventions in which incentives were (I know these interventions came from a couple of different teams, and weren't designed to be compared in any particular analysis plan, but the point of the mega-study is supposed to be cross-comparison.)

In the table below are five interventions in which incentives were paid for either attending a planned or unplanned gym session. They are in order of effect size (the numbers being where they rank in the 54 interventions.)

The experimental results kinda make sense. The largest incentive intervention had the largest effect. 14. can be statistically differentiated from 51., but that's it. The others are not significantly different from each other.

But look at the prediction column.

Rigidity rewarded - only 14 sig higher than 51

| Ranking     | Points planned | $ planned | Points other   | $ other | Text messages | Predicted |
| :---        |:---        |:---        |:---        |:---        |:---        |:---        |
| 14.         |     500     |     $1.79     |     250     |     $0.90    |    9     |
| 24.         |     300     |     $0.22     |     150     |     $0.11    |    2     |
| 28.         |     725     |     $0.52     |     250     |     $0.18    |    8     |
| 48.         |     425     |     $0.31     |     150     |     $0.11    |    8     |
| 51.         |     300     |     $1.08     |     150     |     $0.54    |    9     |

A more useful exercise given the uncertainty as to effect size would have been to get the respondents to rank the proposed interventions in order of effectiveness. Since each intervention is only getting around three predictions, its a very noisy measure given the likely variation between respondents.


I do wonder what the threshold is for a megastudy. Does the Behavioural Insights team [trial of 8 different messages on organ donation](https://www.bi.team/publications/applying-behavioural-insights-to-organ-donation/) make the cut?

Rankings by third parties incoherent

Replicate - run again with more power

Competition against marketers

Where is the theory?!

Sallis and friends as a model of getting the mega-study right.

Parking lot:
- another vaccination study: https://doi.org/10.1073/pnas.2115126119

## The X test

Now to one thing I do like about this study. When you run multiple comparisons in an experiment like this, you will typically adjust the threshold for significance to reduce the number of false positives. For instance, you might do a Bonferroni correction, by which you divide the typical $\alpha$ threshold by the number of interventions you are testing. These types of adjustments, however, are very conservative.

To deal with this, XX and XX developed an alternative test that they call the X-test. The X-test gives you the number of false positives you would expect given the structure of the p-values across the multiple tests that you have constructed.

From this, the authors of the mega-study argue that there is only a 2% chance that any of . This is relative to a control, and I'm willing to believe that. The experimetnal participants have signed up to a program to go to the gym more. They are then delivered a range of reminders, messages and incentives to stick to it. I'd be surprised if any of them truly had zero effect. They are just small effects with a lot of noise, so you need a decent sample to detect them using the traditional tests.

But what does this test actually tell us. It tells us that this basic concept works. Does it help us rank these different interventions? No.

## Conclusion

I've dedicated most of this post to examining some weaknesses and limitations to this mega-study. I don't want to appear too harsh - it's better than most of the rubbish out there - but at the same time, I feel this study is papering over some of the fundamental limitations of behavioural science. Even in a world of mega-studies, we are still in a world of poor theory, limited generalisability and inadequate statistical power. I am sure there is a souped up version that could cover the latter of these, but the other two require something else.