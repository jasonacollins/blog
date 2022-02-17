---
title: 'Megastudy scepticism'
author: jasonacollins
date: 2022-02-28 09:00:00+00:00
lastmod: 2022-02-28 09:00:00+00:00
draft: true
comments: true
slug: megastudy-scepticism
---

With much fanfare, in December a new "megastudy" was announced, a test of 54 different interventions to encourage exercise. But more that just testing these interventions, the authors (a very long list) stated:

>Policy-makers are increasingly turning to behavioural science for insights about how to improve citizens’ decisions and outcomes. Typically, different scientists test different intervention ideas in different samples using different outcomes over different time intervals. The lack of comparability of such individual investigations limits their potential to inform policy. Here, to address this limitation and accelerate the pace of discovery, we introduce the megastudy—a massive field experiment in which the effects of many different interventions are compared in the same population on the same objectively measured outcome for the same duration.

I suppose the introduction is for those who missed May's paper by most of the same authors, [A megastudy of text-based nudges encouraging patients to get vaccinated at an upcoming doctor’s appointment](https://doi.org/10.1073/pnas.2101165118). (To be fair, the exercise megastudy was submitted to a journal first.)

In this post I am going to pull apart what I don't like about this study, and at its heart it is the same thing that bothers me most about behavioural science more generally. There are some great things about this study - I'll discuss them too - but I'll focus on the criticism first.

### Comparability and generalisability

As stated in the abstract, the fundamental problem that the megastudy is trying to solve is the lack of comparability of interventions across experiments. This lack of comparability limits the potential to inform policy as advice as to the

- directly hints to why 

Ultimately, this is why the better policy advice should typically be to run an experiment - maybe with a bit better guidance from the mega-study as well as other literature - 

The idea that you can run this one big, theory free study to answer a question.

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

The '3. High and increasing' was significantly different from the '53. High' Interventions, but otherwise they could not be distinguished. And how confident would you be that this isn't an outlier result, given the High condition involved a social norm which typically has a positive effect. Here it was the only condition with a negative effect size (although not statistically distinguishable from the control). And if you tried to draw a conclusion that the trend is what is important, 

You suddenly find yourself referring to other literature and comparisons, which was part of what the mega-study is designed to allow you to avoid.

Further, most of the treatments . On top of that, given it's the winner and likely an overestimated effect size, 

### The predictions do not make any sense

One interesting thread behind this megastudy is that the researchers obtained estimates of the effect sizes of each intervention 

A more useful exercise given the uncertainty as to effect size would have been to get the respondents to rank the proposed interventions in order of effectiveness. Since each intervention is only getting around three predictions, its a very noisy measure given the likely variation between respondents.

I can only assume that the researchers also underestimated the expected effect sizes, given the lack of power to distinguish most of the hypotheses proposed 



Rigidity rewarded - only 14 sig higher than 51

| Ranking     | Points planned | $ planned | Points other   | $ other | Text messages | Predicted |
| :---        |:---        |:---        |:---        |:---        |:---        |:---        |
| 14.         |     500     |     $1.79     |     250     |     $0.90    |    9     |
| 24.         |     300     |     $0.22     |     150     |     $0.11    |    2     |
| 28.         |     725     |     $0.52     |     250     |     $0.18    |    8     |
| 48.         |     425     |     $0.31     |     150     |     $0.11    |    8     |
| 51.         |     300     |     $1.08     |     150     |     $0.54    |    9     |


I do wonder what the threshold is for a megastudy. Does the Behavioural Insights team [trial of 8 different messages on organ donation](https://www.bi.team/publications/applying-behavioural-insights-to-organ-donation/) make the cut?

Rankings by third parties incoherent

Replicate - run again with more power

Competition against marketers

Where is the theory?!

Sallis and friends as a model of getting the mega-study right.