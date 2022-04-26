---
title: 'Megastudy scepticism'
author: jasonacollins
date: 2022-03-24 09:00:00+00:00
draft: true
comments: true
toc: true
image: ["/img/milkman_et_al_2021_figure_1.png"]
slug: megastudy-scepticism
---

## 0. Introduction
   
In December last year Katherine Milkman and friends published a ["megastudy"](https://doi.org/10.1038/s41586-021-04128-4) testing 54 interventions to encourage over 61,000 experimental participants to exercise. But more than just testing these interventions, the very long list of authors stated:

>Policy-makers are increasingly turning to behavioural science for insights about how to improve citizens’ decisions and outcomes. Typically, different scientists test different intervention ideas in different samples using different outcomes over different time intervals. The lack of comparability of such individual investigations limits their potential to inform policy. Here, to address this limitation and accelerate the pace of discovery, we introduce the megastudy—a massive field experiment in which the effects of many different interventions are compared in the same population on the same objectively measured outcome for the same duration.

In this post I am going to pull apart this experiment and the concept of the megastudy. At its heart, the biggest weakness of the megastudy (at least relative to the mildly oversold claims in the above paragraph) is that the problem it seeks to address also constrains its value. It's also not big enough! There are some great things about this study - I'll discuss them too - but I'll focus on the criticism first.

## 1. The experiment

Members of a national gym chain were asked if they wished to enrol in a "habit-building science-based workout program". Those who signed up formed the subject pool and were randomly assigned to the experimental conditions, including a control under which they received no further contact.

Over the following 28-days participants were subject to interventions involving varying mixes of incentives and messages. For example, those in the "Social norm (high and increasing)" treatment group received six text message reminders, with content such as:

>"Trivia time! What percent of Americans exercised at least 3 times per week in 2016? Reply 1 for 61%, 2 for 64%, 3 for 70% or 4 for 73%".

If they respond 1, 2 or 3, they receive a message back stating:

>It’s actually 73%. And this is up from 71% in 2015.

They also receive emails with similar facts.

Those in the "Social norm (low and decreasing)" received messages with a less rosy situation and trend:

>Trivia time! What percent of Americans exercised at least 3 times per week in 2016? Reply 1 for 35%, 2 for 38%, 3 for 41% or 4 for 44%

As an aside, there don't seem be any qualms about using deception here.

Regardless, the headline results of the interventions are in Figure 1 below.

*Figure 1: Measured versus predicted changes in weekly gym visits induced by interventions*

![Figure 1: Measured versus predicted changes in weekly gym visits induced by interventions](/img/milkman_et_al_2021_figure_1.png)

Twenty-four of the 53 interventions were found to have a statistically significant effect over the control, increasing visits by between 9% and 27% (or by between 0.14 to 0.40 extra weekly gym visits from the control average of 1.48 visits per week).

This figure also contains predictions made by behavioural practitioners, public health academics and lay people. More on those predictions below.

## 2. Comparability

As stated in the abstract, the fundamental problem that the megastudy is designed to address is the lack of comparability of interventions across experiments. The context of two different experiments may be sufficiently different that it is not reasonable to compare the interventions used in each. How can you determine which intervention is more effective?

On one level, the megastudy solves this problem. The interventions are in the same context. Comparison is easy.

But this belief that we cannot easily compare across experiments in different contexts implies a limit of what you learn from the megastudy. What confidence can you have that the ordering or magnitude of intervention effect sizes in the megastudy will be reflected in a different context? 

We are in a Catch-22 situation. The bigger the comparability problem that the megastudy is seeking to solve, the less useful the megastudy results are for application in other contexts.

Ultimately, this is why good policy or business advice should typically be to run an experiment. A megastudy and other literature could provide some guidance as to what interventions might be more successful. But I am not convinced a megastudy provides more insight than an equivalent set of experiments across a few different contexts (although I agree it might provide different insight, as will be noted below). If there is large variation in contexts, seeing a few effective interventions that aren't all in the same domain might give more confidence in the robustness of the phenomena.

So what should we take from this particular megastudy? 

The context is gym attendance. But more than that, it is gym attendance among a group of gym members at a particular gym who self-selected into a digital program to build better gym habits. Incentives weren't simply dollars. They were Amazon points - and those Amazon points had different values depending on the intervention (we'll touch on this again later).

To what other contexts might you be willing to take the results? Further interventions at this same gym? What of another similar gym? A gym with less similar demographics, business model or mode of operation? Gym members who haven't signed up to a habit building program? A program with physical sign up? Straight cash incentives instead of Amazon points? People who don't yet exercise or have gym memberships? Exercise more generally? Other positive habits?

Beyond similar gyms I wouldn't take those results too far.

## 3. Power

We then come to the question of what we can actually learn.

On its face, the megastudy has the benefit of getting a large sample with which to analyse the effect of interest. A sample of 61,293 sounds solid.

But it doesn't take much thought to realise that across 54 interventions (including the control), we have an average of not much more than 1000 participants for each, with most actually having less than a thousand. This number of participants enables the detection of a mean difference in effect size of around 0.32 gym visits with 90% power.

The largest effect of any intervention was an increase of 0.4 gym visits. The sample size does enable differentiation from the control for 24 of the interventions, but when you have 53 interventions jammed into that range of 0.4 you aren't going to be able to distinguish many of them from each other. Only 13 of the 53 interventions were able to be distinguished from anything but the control. Even the best performing intervention could be distinguished from less than half of the others.

The cost of this low power becomes most apparent when you examine the pre-registered analysis plans. One that I mentioned above [considered the effect of social norms](https://osf.io/cthm5/?view_only=ea1b0ba75fc84d4b838614ed9feebb2a). The communicated norms including variations in the level of exercise and the trend. Table 1 shows the four social norm interventions and the average effect size of each.

*Table 1: Exercise social norms (included 6 text message reminders)*

| Intervention           | Effect size   |
| :---                   |          ---: |
| 3. High and increasing | 0.345         |
| 20. Low                | 0.193         |
| 47. Low but increasing | 0.052         |
| 53. High               | -0.030        |

The "3. High and increasing" intervention was significantly different from the "53. High" intervention, but otherwise the four intervention effect sizes could not be statistically distinguished. And how confident would you be that this isn't an outlier result, given the High condition involved a social norm which typically (if you believe the literature) has a positive effect. It was the only intervention in the whole experiment with a negative effect size (although not statistically distinguishable from the control). And if you tried to draw a conclusion that the trend is what is important, we have opposite (statistically insignificant) effects depending on whether the trend is paired with a high or low baseline.

Absent the requisite power, to make sense of these results, you find yourself referring to other literature. But this was part of what the megastudy is designed to enable you to avoid.

This power issue isn't just restricted to this particular megastudy. A [megastudy on vaccinations](https://doi.org/10.1073/pnas.2101165118) published in May 2021 by most of the same authors has the same problem. The 19 interventions boosted vaccinations by an average of 2.1 percentage points, but "we cannot reject the null hypothesis that all 19 effects have the same true value". They use some post-hoc analysis they proposed some statistically significant differences, but pulling them out after the fact is less than convincing.

[A third megastudy](https://doi.org/10.1073/pnas.2115126119) (also by many of the same authors) released earlier this year gets closer to the mark. All 22 messages to increase vaccination has an effect size that was a statistically significant difference from the control. (Reminders work!) They were also able to reject the hypothesis that all effects have the same true value.

## 4. The predictions

One interesting thread behind this megastudy is that the researchers obtained estimates of the effect sizes of each intervention from third party observers: applied behavioural practitioners, public health academics and lay people.

The authors draw two conclusions from the estimates they received.

The first is that all three types of third-party observers grossly overestimate the effect size of the interventions. That is a fair conclusion for this particular study, although there is ambiguous evidence as to whether is a more general trend. For example, [Stephano DellaVigna and Elizabeth Linos found](https://doi.org/10.3982/ECTA18709) that academics overestimated effect sizes in applied trials, whereas applied practitioners did not. Earlier work by [DellaVigna and Devin Pope](https://doi.org/10.1093/restud/rdx033) found roughly accurate calibration for "nudges" but underestimation for incentives.

The second conclusion is that those observers were not able to predict the ordering of the effect sizes of the interventions.

I am going to argue that, at least for this experiment, it is premature to draw this conclusion.

One reason is that the prediction exercise lacked power (this is in addition to the power issue discussed above). You can see this in the massive error bars around the predictions in Figure 1 above. These error bars are, of course, a function of both the range and number of predictions. But each participant was asked to estimate the effect size of only XX predictions. Each intervention having around only X predictions each and those making predictions being poorly calibrated as to the likely size of effect sizes, this setup was never going to elicit a set of predictions that could be statistically differentiated so as to determine an order.

I can only assume that the authors of the megastudy themselves also underestimated the expected effect sizes, given the lack of power to distinguish most of the hypotheses proposed. If we turn to the pre-analysis plan I linked above relating to social norms, they stated that they needed a sample size of 3,000 people per condition to detect a change of around ~15-20%. That's within the realm of the effect size required to differentiate from the controls, but not likely to be enough to separate four separate interventions from each other, which of course was the point of the experiment.

I don't have the statistical nous to work out what number of predictions would be appropriate, but I can see that we have a small number of noisy predictions of some underpowered noisy experimental results. I wouldn't expect anything to be found.

But outside of power, there is a larger problem with the predictions in that the experimental design did not enable useful comparisons by those making predictions. The result is that some nonsensical predictions

To tease this out, let's look at a couple of sets of predictions. Table 2 lists the social norm interventions described above with additional columns for the predictions by practitioners, professors and the pooled group also including lay people.

*Table 2: Exercise social norm effect sizes and predictions*

| Intervention           | Effect size   | Practitioner  | Professor | Average Prediction |
| :---                   |          ---: |      ---:     |     ---:  |   ---:             |
| 3. High and increasing | 0.345         |    2.18       |  3.10     |   3.48             |
| 20. Low                | 0.193         |    2.68       |  3.29     |   3.42             |
| 47. Low but increasing | 0.052         |    2.72       |  2.72     |   2.99             |
| 53. High               | -0.030        |    2.34       |  3.15     |   3.19             |

There is a huge literature that argues that social norms can affect behaviour. People tend to follow the masses. If you used this as a basis for your predictions, you would predict the high social norm would be more effective than the low social norm. (The effect of trends is less well established so I'll ignore them for the moment.)

But if we look at Table 2, the low social norm is consistently predicted to have larger effect. On what basis would you have expected them to make this prediction.

The reason is that none of the participants were actually asked to compare these two. They were only ever asked one or the other and never had a chance to calibrate at points where they had a theory that would guide their predictions. (I realise there is a certain irony in making this argument given the high social norm actually ended up as the worst performing....) They weren't typically asked to compare predictions with like features or that were related to a single hypothesis.

We see a similar pattern in collection of five interventions in Table 3 below in which incentives were offered (all interventions named "Rigidity Rewarded" in Figure 1). (These interventions came from a couple of different teams, and weren't designed to be compared in any particular analysis plan, but the point of the megastudy is supposed to be cross-comparison.)

In these interventions, incentives were paid for either attending a planned or unplanned gym session. The interventions are in order of effect size from largest to smallest (the numbers being where they rank in the 54 interventions).

The experimental results kinda make sense. The largest incentive intervention had the largest effect. 14. can be statistically differentiated from 51. But that's it. The others are not significantly different from each other.

But look at the prediction column. The largest incentive was predicted to have the largest effect. All OK there. But the $0.52 and $0.18 intervention was predicted to have greater effect than the $1.08 and $0.54 intervention.  What's a plausible basis for that prediction ordering?

I can see one argument that refers to the points rather than the value of those points. But that then further confuses the comparability of these interventions with each other and if we want to take them to other domains.

*Table 3: Rigidity rewarded incentives*

| Ranking     | Points planned | $ planned  | Points other | $ other    | Text messages | Predicted  |
| :---        |:---         |:---           |:---          |:---        |:---           |:---        |
| 14.         |     500     |     $1.79     |     250      |     $0.90  |    9          |     3.70       |
| 24.         |     300     |     $0.22     |     150      |     $0.11  |    2          |     3.08       |
| 28.         |     725     |     $0.52     |     250      |     $0.18  |    8          |     3.54       |
| 48.         |     425     |     $0.31     |     150      |     $0.11  |    8          |     2.77       |
| 51.         |     300     |     $1.08     |     150      |     $0.54  |    9          |     3.04       |

A more useful exercise given the uncertainty as to effect size would have been to get the respondents to rank the proposed interventions in order of effectiveness. Since each intervention is only getting around three predictions, its a very noisy measure given the likely variation between respondents.

I think the result is likely right - that practitioners, professors and the average punter don't have a great feel for the relative effectiveness of a whole bunch of weak interventions.

Putting these critiques of these predictions together, I'd like to see a replication with more power on both sides: more power to differentiate interventions and a larger number of predictions in which the third-party observers get to see a larger set and get to make direct comparisons between them.

In the newest megastudy on vaccinations [add link], those criteria were least partially met. Another prediction competition was run, with lay people and the scientists who designed the interventions among the "competitors".

Here's another piece of evidence that we should give the marketers a go at designing these!

And again we come to our conclusion:

>"Regardless, the inability of either scientists or laypeople to anticipate the top-performing intervention underscores the value of empirical testing when seeking the best policy."

## 5. Intervention design

Going from concept to intervention design is tough. I get it.

But almost every time I see an applied behavioural experiment, this challenge strikes me anew. You see all the degrees of freedom in developing the intervention: the precise copy (please, start using decent copywriters!), the choice of medium (e.g. text message or email) and the method of execution (e.g. when is it sent).

The result is that it is typically not hard to come up with reasons why (or why not) the intervention will be a effective outside of the empirical phenomena that is being explicitly tested. The copy doesn't actually convey the concept. The wording is confusing. And so on.

Some of these problem appear magnified in the megastudy by the involvement of 30 people from 15 universities working in independent teams. Many interventions are only weakly comparable.

Here's two megastudy examples.

First, some interventions have 2 text messages sent to participants, others nine. Is the difference in effect size due to the number of text messages or the stated form of the intervention?

Second, the social norm experiments above rely on people responding to a quiz to get the full force of the intervention. Are we testing the effect of quizzes or norms when we compare across interventions?

These implementation problems again point to that number one piece of advice: test in your own domain. It's hard to simply pick up a concept and transplant to your own space. Wording and delivery almost always have to change. Around that central concept you need to test which degrees of freedom matter.

## 6. Theory

My final gripe isn't a fair one, but it's my hobby-horse, so I'll voice it anyway.

At first glance, the list of 54 interventions suggests the megastudy has an underlying philosophy of "throw enough things at a wall and surely something will stick".

The method is not that loose. If you read through the series of pre-analysis plans (linked in the [supplementary material](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-04128-4/MediaObjects/41586_2021_4128_MOESM1_ESM.pdf)), you can see that there are subsets of interventions that are intended to tease out a point of interest. For example, one plan [involves testing social norms](https://osf.io/cthm5/?view_only=ea1b0ba75fc84d4b838614ed9feebb2a), and in particular how people respond to differences in level and trend (as per the text message examples above).

But despite this structure, this megastudy is not going to provide theoretical advance. Rather than 50 interventions on a common basis and frame to inform a model of human decision making, we have disparate sets of hypotheses that have few theoretical bridges between them. Each hypothesis or set of hypotheses concern specific empirical regularities rather than a core choice model. We have behavioural scientists working as technicians, seeking to optimise a particular objective with the tools at hand.

It's the way the wind is blowing. Instead of taking on the challenge of giving the mass of empirical evidence some theoretical backbone, the best minds have turned to taking bits and pieces of this empirical body of work and applying them to real-world problems. As a policy maker or business owner, you might reap the benefits. The academics taking this path a reaping the publication benefits. (This megastudy landed in *Nature* of all places.) But progress as a science? It feels stagnant.

I admit I'm asking too much of this study. I want to see behavioural science build strong foundations that lead to theoretical understanding as to what is going on. This study is designed to test how to increase gym attendance. This big, theory free study isn't going to provide the answer to my question, but nor is it designed to.

But if we're simply technicians working on (admittedly important) public policy issues, we also need to open the door to other technicians. If we're simply after finding ways to bump gym attendance, why are we just asking behavioural scientists? What if we had got some marketers to develop the messaging? Here's one megastudy I would like to see. Get half the interventions from behavioural scientists. Get the other half from random marketers (plus Rory Sutherland). See which are more successful. I don't have much confidence that the behavioural scientists would outperform.

## 7. The X test

Now to a couple of things I like about this study. The first is the X-test.

When you run multiple comparisons in an experiment like this, you will typically adjust the threshold for significance to reduce the number of false positives. If you set a statistical significance threshold ($\alpha$) of 0.05, you would expect 1 in 20 interventions to reach this by chance even if they have no effect. Run 54, you would expect a couple.

To eliminate those false positives, you might do a Bonferroni correction, by which you divide the typical $\alpha$ threshold by the number of interventions you are testing. These types of adjustments, however, are conservative. Make this adjustment to the megastudy results and [how many remain significant??]

To deal with this, XX and XX developed an alternative test that they call the X-test. The X-test was developed for genomic analysis, where you might be conducting millions of comparisons (a typical micro-array will have 5 million SNPs).

The X-test capitalises on the fact that with multiple comparisons you have multiple p-values that themselves have a distribution. This distribution of p-values can be used to calculate the number of false positives you would expect across the multiple tests that you have constructed.

Using the X-test, the authors of the megastudy argue that there is only a 2% chance that any of the statistically significant interventions () are false positives. This is relative to a control, and I'm willing to believe that. The experimental participants have signed up to a program to go to the gym more. They are then delivered a range of reminders, messages and incentives to stick to it. I'd be surprised if any of them truly had zero effect. They are just small effects with a lot of noise, so you need a decent sample to detect them using the traditional tests.

But what does this X-test actually tell us. It tells us that this basic concept works. Yes you can get people going to the gym (a tiny bit) more. But does the test help us rank these different interventions? No.

## 8. Return on investment

The second strong feature of this study is that (buried in the supplementary material) the authors examine the cost and benefits of these interventions. A common refrain for much applied behavioural science is that the effects are small but the costs are also small, so the return on investment pays off.

Here, that claim is questionable, at least from the perspective of public policy

An interesting alternative question here would be whether there is a greater return to the gym. Do more people remain members? Is there a pay-off there? But to the extent there is, is this then leading to a net negative loss to the participants who might be paying more in gym fees than the dollar gain to their fitness?

## 9. Other things I like

One big benefit of theEconomies of scale

Publishing null findings

Common task - tournament - create some discipline around comparison. So narrow - increase gym attendance, but it's got to be by using text messages and emails over a four week period....not much scope for serious advance.

Interventions overfitted to the particular context. Winner effect likely overestimating effect size.

Should be out of sample testing. Let's go really big - test one set of interventions, use to predict in out of sample.

## 10. Conclusion

I've dedicated most of this post to examining some weaknesses and limitations to this megastudy. I don't want to appear harsh - it's better than most of the rubbish out there - but at the same time, I feel this study is papering over some of the fundamental limitations of behavioural science as it is practised. Even in a world of mega-studies, we are still in a world of poor theory, limited generalisability and inadequate statistical power. I am sure there is a souped-up version that could cover the latter of these, but the other two require something else.

## 11. Other random thoughts

- I suppose the "introduction" in the Nature paper is for those who missed the May 2021 paper by most of the same authors, [A megastudy of text-based nudges encouraging patients to get vaccinated at an upcoming doctor’s appointment](https://doi.org/10.1073/pnas.2101165118). To be fair, the exercise megastudy was submitted to a journal first.

- The "winning" messages for this vaccination study appear, to me at least, a bit deceptive: "...this is a reminder that a flu vaccine has been reserved for your appt..."

- The worst performing message related to health, with the line "It’s flu season & getting a flu shot at your appt is an easy thing you can do to be healthy!" Who are their copywriters?! Would anyone normally spruik the health benefits of a flu shot in this way? I would say the poor performance of this line gives little information about the effectiveness of health messaging.

- That megastudy also has the line "Overall, our findings show nudges sent via text messages to patients prior to a primary care visit and developed by behavioral scientists to encourage vaccine adoption can substantially boost vaccination rates at close to zero marginal cost." It is true, but the "developed by behavioral scientists" part wasn't seriously tested against any control. As per above, would they beat marketers? Given their poor performance at predicting what would be more successful relative to lay people (in the second vaccine megastudy), I'm not convinced.

- What is the threshold is for a megastudy. The vaccination megastudy involved 19 nudges. Does the Behavioural Insights team [trial of 8 different messages on organ donation](https://www.bi.team/publications/applying-behavioural-insights-to-organ-donation/) make the cut? It has XXX,XXX participants. At least it enabled the testing of multiple hypotheses in a single context while maintaining adequate power.