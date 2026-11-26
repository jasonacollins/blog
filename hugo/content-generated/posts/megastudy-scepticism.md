---
title: 'Megastudy scepticism'
author: "Jason Collins"
date: 2022-05-27 07:00:00+10:00
draft: false
toc: true
image: "img/milkman_et_al_2021_figure_1.jpeg"

sync_source: "posts/megastudy-scepticism.qmd"
sync_route: "pandoc"
sync_hash: "3c77ebc78121"
---

{{< html >}}
<div class="toc" data-pagefind-ignore><ul>
<li><a href="#introduction">0. Introduction</a></li>
<li><a href="#the-experiment">1. The experiment</a></li>
<li><a href="#comparability">2. Comparability</a></li>
<li><a href="#power">3. Power</a></li>
<li><a href="#the-predictions">4. The predictions</a></li>
<li><a href="#intervention-design">5. Intervention design</a></li>
<li><a href="#theory">6. Theory</a></li>
<li><a href="#the-false-discovery-rate">7. The false discovery rate</a></li>
<li><a href="#return-on-investment">8. Return on investment</a></li>
<li><a href="#the-common-task-approach">9. The common task approach</a></li>
<li><a href="#other-things-i-like">10. Other things I like</a></li>
<li><a href="#conclusion">11. Conclusion</a></li>
<li><a href="#random-thoughts-that-didnt-fit-above">12. Random thoughts that didn’t fit above</a></li>
</ul></div>
<h2 id="introduction">0. Introduction</h2>
<p>In December last year Katherine Milkman and friends published a <a href="https://doi.org/10.1038/s41586-021-04128-4">“megastudy”</a> testing 54 interventions to increase the gym visits of 61,000 experimental participants. But more than just testing these interventions, the long list of authors stated:</p>
<blockquote>
<p>Policy-makers are increasingly turning to behavioural science for insights about how to improve citizens’ decisions and outcomes. Typically, different scientists test different intervention ideas in different samples using different outcomes over different time intervals. The lack of comparability of such individual investigations limits their potential to inform policy. Here, to address this limitation and accelerate the pace of discovery, we introduce the megastudy - a massive field experiment in which the effects of many different interventions are compared in the same population on the same objectively measured outcome for the same duration.</p>
</blockquote>
<p>In this post I am going to pull apart this experiment and the concept of the megastudy. At its heart, the problem the megastudy seeks to address also constrains its value. It’s also not big enough! There are some great things about this study - I’ll discuss them too - but I’ll describe the experiment and focus on the criticism first.</p>
<h2 id="the-experiment">1. The experiment</h2>
<p>Members of a national gym chain were asked if they wished to enrol in a “habit-building science-based workout program”. Those who signed up formed the subject pool and were randomly assigned to the experimental conditions, including a control under which they received no further contact.</p>
<p>Over the following 28-days participants were subject to interventions involving varying mixes of incentives and messages. For example, those in the “3. Social norm (high and increasing)” treatment group received six text message reminders, with content such as:</p>
<blockquote>
<p>“Trivia time! What percent of Americans exercised at least 3 times per week in 2016? Reply 1 for 61%, 2 for 64%, 3 for 70% or 4 for 73%”.</p>
</blockquote>
<p>If they respond 1, 2 or 3, they receive a message back stating:</p>
<blockquote>
<p>It’s actually 73%. And this is up from 71% in 2015.</p>
</blockquote>
<p>They also receive emails with similar facts.</p>
<p>Those in the “47. Social norm (low and decreasing)” group received messages with a less rosy situation and trend:</p>
<blockquote>
<p>Trivia time! What percent of Americans exercised at least 3 times per week in 2016? Reply 1 for 35%, 2 for 38%, 3 for 41% or 4 for 44%</p>
</blockquote>
<p>As an aside, there don’t seem to be any qualms about using deception here.</p>
<p>Some interventions involved incentives. For example, the “14. Rigidity Rewarded” intervention paid 500 Amazon points worth $1.79 each time they attended a planned gym visit, and 250 Amazon points worth $0.90 if they attended the gym at another time.</p>
<p>The headline results of all the interventions tested in the megastudy are in Figure 1 below. The intervention with the largest effect size involved incentives for returning to the gym after a missed workout.</p>
<figure>
{{< img src="img/milkman_et_al_2021_figure_1.jpeg" alt="Figure 1: Measured versus predicted changes in weekly gym visits induced by interventions" >}}
<figcaption aria-hidden="true">Figure 1: Measured versus predicted changes in weekly gym visits induced by interventions</figcaption>
</figure>
<p>Twenty-four of the 53 interventions were found to have a statistically significant effect over the control, increasing visits by between 9% and 27%. That equates to 0.14 to 0.40 extra weekly gym visits over the control average of 1.48 visits per week.</p>
<p>This figure also contains predictions made by behavioural practitioners, public health academics and lay people. More on those predictions below.</p>
<h2 id="comparability">2. Comparability</h2>
<p>As stated in the abstract, the fundamental problem that the megastudy is designed to address is the lack of comparability of interventions across experiments. The context of two different experiments may be sufficiently different that it is not reasonable to ask which intervention is more effective.</p>
<p>On one level, the megastudy solves this problem. The interventions are in the same context. Comparison is easy.</p>
<p>But this belief that we cannot easily compare across experiments in different contexts implies a limit to what you learn from the megastudy. What confidence can you have that the ordering or magnitude of intervention effect sizes in the megastudy will be reflected in a different context?</p>
<p>We are in a Catch-22 situation. The bigger the comparability problem that the megastudy is seeking to solve, the less useful the megastudy results are for application in other contexts.</p>
<p>Ultimately, this is why good policy or business advice should typically be to run an experiment. A megastudy could provide guidance as to what interventions might be more successful. But I am not convinced a megastudy provides more insight than an equivalent set of experiments across a few different contexts (although it might provide different insight, as will be noted below). If there is large variation in contexts, seeing a few effective interventions tested across different domains might give more confidence in the robustness of the phenomena than one megastudy.</p>
<p>So what should we take from this particular megastudy?</p>
<p>The context is gym attendance. But more than that, it is gym attendance among a group of gym members at a particular gym who self-selected into a digital program to build better gym habits. Incentives weren’t simply dollars. They were Amazon points. And those Amazon points had different values depending on the intervention.</p>
<p>To what other contexts might you be willing to take the results? Further interventions at this same gym? What of another similar gym? A gym with less similar demographics, business model or mode of operation? Gym members who haven’t signed up to a habit building program? A program with physical sign up? Cash incentives instead of Amazon points? People who don’t yet exercise or have gym memberships? Exercise more generally? Other positive habits?</p>
<p>Beyond similar gyms I wouldn’t take those results too far.</p>
<h2 id="power">3. Power</h2>
<p>We then come to the question of what we can actually learn.</p>
<p>On its face, the megastudy has the benefit of getting a large sample. A total of 61,293 participants sounds solid.</p>
<p>But it doesn’t take much thought to realise that across 54 interventions (including the control) there is an average of not much more than 1000 participants per intervention, with most interventions having less than a thousand participants in execution. This number of participants enables the detection of a mean difference in effect size of around 0.32 gym visits with 90% power.</p>
<p>The largest effect of any intervention was an increase of 0.4 gym visits. The sample size enables differentiation from the control for 24 of the interventions, but when you have 53 interventions jammed into that range of 0.4 you aren’t going to be able to distinguish many of them from each other. As a result, only 13 of the 53 interventions were statistically distinguished from any interventions beyond the control. Even the best performing intervention could be distinguished from less than half of the other interventions.</p>
<p>You can see one cost of this low power when you examine the pre-registered analysis plans. One plan <a href="https://osf.io/cthm5/?view_only=ea1b0ba75fc84d4b838614ed9feebb2a">considered the effect of social norms</a>. The communicated norms included variations in the level of exercise and the trend. I gave a couple of examples of the social norm interventions in the description of the experiment above. Table 1 shows the four social norm interventions and the average effect size (in additional gym visits) of each.</p>
<p><em>Table 1: Exercise social norms (included 6 text message reminders)</em></p>
<table>
<thead>
<tr>
<th style="text-align: left;">Intervention</th>
<th style="text-align: right;">Effect size</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">3. High and increasing</td>
<td style="text-align: right;">0.345</td>
</tr>
<tr>
<td style="text-align: left;">20. Low</td>
<td style="text-align: right;">0.193</td>
</tr>
<tr>
<td style="text-align: left;">47. Low but increasing</td>
<td style="text-align: right;">0.052</td>
</tr>
<tr>
<td style="text-align: left;">53. High</td>
<td style="text-align: right;">-0.030</td>
</tr>
</tbody>
</table>
<p>The “3. High and increasing” intervention was significantly different from the “53. High” intervention, but otherwise the four intervention effect sizes could not be statistically distinguished. And how confident would you be that this isn’t an outlier result, given the “53. High” intervention involved a social norm which typically (if you believe the literature) has a positive effect? It was the only intervention with a negative effect size relative to the control (although not a statistically significant difference). And if you tried to draw a conclusion about whether the trend in exercise is what is important, we have statistically insignificant opposite effects depending on whether the trend is paired with a high or low baseline.</p>
<p>Absent the requisite power, to make sense of these results you find yourself referring to other literature. But this was part of what the megastudy is designed to enable you to avoid.</p>
<p>The power issue isn’t restricted to this particular megastudy. A <a href="https://doi.org/10.1073/pnas.2101165118">megastudy on vaccinations</a> published in May 2021 by most of the same authors has the same problem. The 19 interventions boosted vaccinations by an average of 2.1 percentage points, but the authors noted that “we cannot reject the null hypothesis that all 19 effects have the same true value”. They use some post-hoc analysis to propose some statistically significant differences, but pulling those differences out after the fact is less than convincing.</p>
<p><a href="https://doi.org/10.1073/pnas.2115126119">A third megastudy</a> (also by many of the same authors) released earlier this year gets closer to the mark. All 22 messages to increase vaccination had an effect size that was a statistically significant difference from the control. (Reminders work!) They were also able to reject the hypothesis that all effects have the same true value.</p>
<h2 id="the-predictions">4. The predictions</h2>
<p>One interesting concept in this megastudy is that the researchers obtained predictions of the effect sizes of each intervention from third party observers: applied behavioural practitioners, public health academics and lay people.</p>
<p>The authors draw two conclusions from the predictions they received.</p>
<p>The first is that all three types of third-party observers overestimate the effect size of the interventions by around an order of magnitude. That is a fair conclusion for this particular study, although there is ambiguous evidence as to whether this is a more general trend. For example, <a href="https://doi.org/10.3982/ECTA18709">Stefano DellaVigna and Elizabeth Linos</a> found that academics overestimated effect sizes in applied trials, whereas applied practitioners did not. Earlier work by <a href="https://doi.org/10.1093/restud/rdx033">DellaVigna and Devin Pope</a> found roughly accurate calibration for “nudges” but underestimation for incentives. In the <a href="https://doi.org/10.1073/pnas.2115126119">third megastudy</a> noted above lay people had the effect size roughly right while the behavioural scientists underestimated it.</p>
<p>I can only assume that the authors of the megastudy themselves also underestimated the expected effect sizes, given the lack of power to distinguish most of the hypotheses proposed. If we turn to the pre-analysis plan I linked above relating to social norms, they stated that they needed a sample size of 3,000 people per condition to detect a change of around ~15-20%. That’s within the realm of the effect size required to differentiate from the controls, but not likely to be enough to separate four separate interventions from each other, which of course was the point of the experiment. (And to top it off they didn’t get the number of participants they sought.)</p>
<p>The second conclusion the authors make about the predictions is that the observers were not able to predict the ordering of the effect sizes of the interventions.</p>
<p>I am going to argue that, at least for this experiment, it is premature to draw this conclusion.</p>
<p>One reason is that the prediction exercise lacked power (this is in addition to the power issue discussed above). You can see this in the massive error bars around the predictions in Figure 1. These error bars are, of course, a function of both the range and number of predictions. But each participant was asked to estimate the effect size of only 3 interventions. Each intervention has only 17, 9 and 5 predictions from the lay people, public health experts and behavioural practitioners respectively. None of the predicted effect sizes are statistically significant from any other.</p>
<p>I don’t have the statistical nous to work out what number of predictions would be appropriate, but I can see that we have a small number of noisy predictions of some underpowered noisy experimental results. I wouldn’t expect anything to be found.</p>
<p>But outside of power, a larger challenge with the predictions is that the experimental design did not enable useful comparisons by observers making predictions. The result is that many predictions are nonsense.</p>
<p>To tease this out, let’s look at a couple of sets of predictions. Table 2 lists the social norm interventions described above with additional columns for the predictions by practitioners, professors, lay people and the pooled group.</p>
<p><em>Table 2: Exercise social norm effect sizes and predictions</em></p>
<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Intervention</th>
<th style="text-align: right;">Effect size</th>
<th style="text-align: right;">Practitioner</th>
<th style="text-align: right;">Professor</th>
<th style="text-align: right;">Lay people</th>
<th style="text-align: right;">Average Prediction</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">3. High and increasing</td>
<td style="text-align: right;">0.345</td>
<td style="text-align: right;">2.18</td>
<td style="text-align: right;">3.10</td>
<td style="text-align: right;">3.94</td>
<td style="text-align: right;">3.48</td>
</tr>
<tr>
<td style="text-align: left;">20. Low</td>
<td style="text-align: right;">0.193</td>
<td style="text-align: right;">2.68</td>
<td style="text-align: right;">3.29</td>
<td style="text-align: right;">3.72</td>
<td style="text-align: right;">3.42</td>
</tr>
<tr>
<td style="text-align: left;">47. Low but increasing</td>
<td style="text-align: right;">0.052</td>
<td style="text-align: right;">2.72</td>
<td style="text-align: right;">2.72</td>
<td style="text-align: right;">3.27</td>
<td style="text-align: right;">2.99</td>
</tr>
<tr>
<td style="text-align: left;">53. High</td>
<td style="text-align: right;">-0.030</td>
<td style="text-align: right;">2.34</td>
<td style="text-align: right;">3.15</td>
<td style="text-align: right;">3.41</td>
<td style="text-align: right;">3.19</td>
</tr>
</tbody>
</table>
<p>There is a reasonably-sized literature that social norms can affect behaviour. People tend to follow the masses. If you used this as a basis for your predictions, you would predict the high social norm would be more effective than the low social norm. (The effect of trends is less well established so I’ll ignore them for the moment.)</p>
<p>But if we look at Table 2, the low social norm is consistently predicted to have larger effect. On what basis would you have expected them to make this prediction? (I realise there is a certain irony in asking this question given the high social norm actually ended up as the worst performing….)</p>
<p>The reason is that none of the participants were asked to compare intervention “20. Low” with intervention “53. High”. No participant was asked to compare more than two of the four social norm interventions (a total of 9 observers had that opportunity). The consequence is that there was little opportunity for observers to calibrate their responses based on their knowledge of empirical phenomena.</p>
<p>We see a similar pattern in collection of five interventions in Table 3 below in which incentives were offered (all interventions named “Rigidity Rewarded” in Figure 1). In these interventions, incentives of Amazon points were paid for either attending a planned or unplanned gym session. The interventions are in order of effect size from largest to smallest (the numbers being where they rank in the 54 interventions).</p>
<p><em>Table 3: Rigidity rewarded incentives</em></p>
<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Ranking</th>
<th style="text-align: right;">Points planned</th>
<th style="text-align: right;">$ planned</th>
<th style="text-align: right;">Points other</th>
<th style="text-align: right;">$ other</th>
<th style="text-align: right;">Text messages</th>
<th style="text-align: right;">Predicted</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">14.</td>
<td style="text-align: right;">500</td>
<td style="text-align: right;">$1.79</td>
<td style="text-align: right;">250</td>
<td style="text-align: right;">$0.90</td>
<td style="text-align: right;">9</td>
<td style="text-align: right;">3.70</td>
</tr>
<tr>
<td style="text-align: left;">24.</td>
<td style="text-align: right;">300</td>
<td style="text-align: right;">$0.22</td>
<td style="text-align: right;">150</td>
<td style="text-align: right;">$0.11</td>
<td style="text-align: right;">2</td>
<td style="text-align: right;">3.08</td>
</tr>
<tr>
<td style="text-align: left;">28.</td>
<td style="text-align: right;">725</td>
<td style="text-align: right;">$0.52</td>
<td style="text-align: right;">250</td>
<td style="text-align: right;">$0.18</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">3.54</td>
</tr>
<tr>
<td style="text-align: left;">48.</td>
<td style="text-align: right;">425</td>
<td style="text-align: right;">$0.31</td>
<td style="text-align: right;">150</td>
<td style="text-align: right;">$0.11</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">2.77</td>
</tr>
<tr>
<td style="text-align: left;">51.</td>
<td style="text-align: right;">300</td>
<td style="text-align: right;">$1.08</td>
<td style="text-align: right;">150</td>
<td style="text-align: right;">$0.54</td>
<td style="text-align: right;">9</td>
<td style="text-align: right;">3.04</td>
</tr>
</tbody>
</table>
<p>The experimental results kinda make sense. The largest incentive had the largest effect. Intervention 14 can be statistically differentiated from 51. But that’s it. The others are not significantly different from each other.</p>
<p>Then we look at the prediction column. The largest incentive was predicted to have the largest effect. All fine there. But intervention 28 with incentives of $0.52 and $0.18 was predicted to have greater effect than the $1.08 and $0.54 associated with intervention 51. What’s a plausible basis for that prediction ordering?</p>
<p>I can see one argument that people were ranking according to the Amazon points available rather than the value of those points. But accepting that argument further confuses the comparability of these interventions with each other and limits their generalisability if we want to take them to other domains.</p>
<p>I think the claim that the observers are poor predictors is likely right. Practitioners, professors and the average punter don’t have a great feel for the relative effectiveness of a bunch of weak interventions. But putting the critiques of these predictions together, I’d like to see a replication with more power on both sides: more power to differentiate interventions and a larger number of predictions in which the third-party observers get to see the full set of interventions and make direct comparisons between them.</p>
<p>In the <a href="https://doi.org/10.1073/pnas.2115126119">newest megastudy on vaccinations</a>, those criteria were largely met. Another prediction competition was run, with lay people and the scientists who designed the interventions among the “competitors”. They were asked to predict the vaccination rates for the people in all 22 treatment groups and the control.</p>
<p>Here we have a more promising result, for the lay people at least. The predictions of the scientists who contributed an intervention did not correlate with observed vaccination rates. Conversely, lay people did well. The correlation between observed and predicted vaccination rates was 0.6. And beyond that, their estimate of the average lift in vaccinations was close to that observed. (The scientists underestimated the increase by around 25%.)</p>
<p>Despite that success by the lay people, it was not without flaws. They did not anticipate the top-performing intervention. If you’re in the mindset that you simply want to maximise vaccinations, that’s an important miss. That, of course, leads us to the usual conclusion:</p>
<blockquote>
<p>Regardless, the inability of either scientists or laypeople to anticipate the top-performing intervention underscores the value of empirical testing when seeking the best policy.</p>
</blockquote>
<p>Finally, the success of the laypeople relative to the scientists hints at some of the following points I plan to make. Why are we just using behavioural scientists to design these interventions? Do they have any special skill in developing interventions? Why not give marketers a go at designing them! And if only we had some theory to guide our understanding. More on those points below.</p>
<h2 id="intervention-design">5. Intervention design</h2>
<p>Going from concept to intervention design is tough. I’ve been there.</p>
<p>But almost every time I see an applied behavioural experiment, this challenge strikes me anew. You see all the degrees of freedom in developing the intervention, such as the design (why do academics pretend to have design skills?), precise copy (please, start using decent copywriters!), the choice of medium (e.g. text message or email) and the method of execution (e.g. when is it sent).</p>
<p>The result is that it is typically not hard to come up with reasons why (or why not) the intervention will be effective for reasons that don’t relate to the empirical phenomena that is being explicitly tested. “The copy doesn’t convey the concept.” “The wording is confusing.” And so on.</p>
<p>Some of these problems appear magnified in this megastudy via the involvement of 30 people from 15 universities working in independent teams. Many interventions are only weakly comparable.</p>
<p>Here’s two examples from this megastudy.</p>
<p>First, some interventions have 2 text messages sent to participants, others nine. Is the difference in effect size due to the number of text messages or the stated form of the intervention?</p>
<p>Second, the social norm experiments described above rely on people responding to a quiz to get the full force of the intervention. Are we testing the effect of quizzes or norms?</p>
<p>And here’s an example from the first megastudy on vaccinations.</p>
<p>The worst performing message related to health, with the line “It’s flu season &amp; getting a flu shot at your appt is an easy thing you can do to be healthy!” Who are their copywriters?! Would anyone normally spruik the health benefits of a flu shot in this way? I would argue that the poor performance of this message gives little information about the effectiveness of health messaging.</p>
<p>These implementation problems again point to that number one piece of advice: test in your own domain. It’s hard to pick up a concept and simply transplant to your own space. Wording and delivery almost always have to change. You need to test which degrees of freedom matter.</p>
<h2 id="theory">6. Theory</h2>
<p>My final gripe isn’t completely fair, but it’s my hobby-horse, so I’ll voice it anyway.</p>
<p>At first glance, the list of 54 interventions suggests the megastudy has an underlying philosophy of “throw enough things at a wall and surely something will stick”. If you can’t predict which interventions are most effective, maybe that is what you have to do:</p>
<blockquote>
<p>One could argue that the harder it is to predict the results of experiments, the more valuable the megastudy approach. The more difficult it is to forecast ex ante which interventions will work, the harder it is to decide in advance which interventions to prioritize for testing, and the more useful it is to instead test a large number of treatment approaches.</p>
</blockquote>
<p>Fair enough. But this concession implicitly means the authors have given up on developing an understanding of human decision making that might allow us to make predictions. Each hypothesis or set of hypotheses they tested concern discrete empirical regularities. They are not derived from or designed to test a core model of human decision making. We have behavioural scientists working as technicians, seeking to optimise a particular objective with the tools at hand.</p>
<p>It’s the way the wind is blowing. Instead of taking on the challenge of giving the mass of empirical evidence some theoretical backbone, the best minds have turned to taking an empirical body of work and applying it to real-world problems. As a policy maker or business owner, you might reap the benefits. The academics taking this path are reaping the publication benefits. (This megastudy landed in <em>Nature</em> of all places.) But progress as a science? It feels stagnant.</p>
<p>I admit I’m asking too much of this study. I want to see behavioural science build theoretical understanding as to what is going on. This study is designed to test how to increase gym attendance. This big, theory free study isn’t going to provide the answer to my question, but nor is it designed to.</p>
<p>But this lack of theory is not without costs. For instance, as already noted, when asked to predict the ordering of effect sizes, the practitioners had no idea. In the newer vaccination study they were outperformed by laypeople. We don’t have a theoretical framework that can outperform common sense (and by making us focus on a menu of effects and biases, possibly have a body of knowledge that leads us to underperform common sense.)</p>
<p>If we’re simply technicians working on public policy issues, this further builds the case to open the door to other technicians. Why are we just asking behavioural scientists? What if we got some marketers to develop interventions? Here’s one megastudy I would like to see. Get half the interventions from behavioural scientists. Get the other half from random non-academic marketers (plus Rory Sutherland). See which are more successful. I don’t have much confidence that the behavioural scientists would outperform.</p>
<p>On that point, the first vaccination megastudy contains the following line:</p>
<blockquote>
<p>[O]ur findings show nudges sent via text messages to patients prior to a primary care visit and developed by behavioral scientists to encourage vaccine adoption can substantially boost vaccination rates at close to zero marginal cost.</p>
</blockquote>
<p>It’s true in a sense, but whether you actually need the “behavioral scientists” to develop the interventions hasn’t been tested yet. And again, given their poor performance at predicting what would be successful relative to lay people in the second vaccination megastudy, I’m not convinced.</p>
<h2 id="the-false-discovery-rate">7. The false discovery rate</h2>
<p>Now to a couple of things I like about this study. The first is that the study enables calculation of a false discovery rate.</p>
<p>When you run multiple comparisons in an experiment, you will typically adjust the threshold for significance to reduce the number of false positives. If you set a statistical significance threshold ({{< math >}}\alpha{{< /math >}}) of 0.05, you would expect 1 in 20 interventions to reach this threshold by chance even if they have no effect. Run 54 interventions and you would expect a couple.</p>
<p>To eliminate those false positives, there are corrections you can make such as a Bonferroni correction, by which you divide {{< math >}}\alpha{{< /math >}} by the number of interventions you are testing. These types of adjustments, however, are conservative. Make a Bonferroni adjustment to the megastudy results and (from eyeballing the p-values) you are left with around half a dozen statistically significant effect sizes.</p>
<p>To deal with this problem <a href="https://doi.org/10.1073/pnas.1530509100">John Storey and Robert Tibshirani developed</a> a test to determine the false discovery rate. The false discovery rate is the rate that interventions with statistically significant effect sizes are truly null. This contrasts with the false positive rate, which is the rate that null interventions are called significant.</p>
<p>Storey and Tibshirani’s test capitalises on the fact that with multiple comparisons you have multiple p-values that themselves have a distribution. This distribution of p-values can be used to calculate the number of false positives you would expect across the multiple tests that you have constructed.</p>
<p>Using this test, the authors of the megastudy argue that there is only a 5.07% chance that any of the statistically significant interventions are false positives. I’m willing to believe that. The experimental participants have signed up to a program to go to the gym more. They are then delivered a range of reminders, messages and incentives to stick to it. I’d be surprised if any of the incentives truly had zero effect. They are just small effects with a lot of noise, so you need a decent sample to detect them.</p>
<p>But what does this mean for interpreting the megastudy results? It tells us that this basic concept works. Yes you can get people going to the gym more. But does the test help us differentiate these interventions? No.</p>
<p>As a final note for myself, I’m interested in whether the Storey and Tibshirani test is robust with the small number of interventions in the megastudy. Storey and Tibshirani developed the test for genomic analysis, where you might be conducting millions of comparisons, so would have a distribution of millions of p-values. The distribution of p-values in the megastudy comes from far fewer observations. I’ll come back to this another time.</p>
<h2 id="return-on-investment">8. Return on investment</h2>
<p>Another strong feature of this study is that (buried in the supplementary material) the authors examine the fiscal costs and benefits of these interventions. A common refrain for much applied behavioural science is that the effects are small but the costs are also small. Thus, the return on investment pays off.</p>
<p>On face value, this argument holds for the megastudy. Drawing on a couple of other studies, the authors estimated the benefit of a gym visit to society due to reduced health care expenditures as being between $1.66 and $3.71 per visit. Given the size of these benefits and the low cost of many of the megastudy interventions, they argue that four of the top five interventions have a positive cost-benefit and would be worth scaling.</p>
<p>The gap in this analysis is that it is better described as a <em>fiscal</em> analysis rather than a true cost-benefit analysis. It’s ignoring many of the costs and benefits that a good public policy cost-benefit analysis would typically include.</p>
<p>On the cost ledger, the largest missing cost is the time-cost to participants. The benefits side would consider health benefits to the individual themselves: probably some change in quality-adjusted life-years. I suspect this would be substantial: I don’t think there’s much better life advice than to go to the gym.</p>
<p>Alternatively, you could attempt to capture those personal costs and benefits through some measure of customer willingness to pay.</p>
<p>An interesting additional question would be whether the gym chain gets a return that makes it worthwhile from a business perspective. Do more people retain their gym membership? To the extent they do, this builds the business case but also creates another cost to individuals we should consider in our cost-benefit analysis.</p>
<h2 id="the-common-task-approach">9. The common task approach</h2>
<p>One interesting suggestion in the paper is that the megastudy drew inspiration from the common task framework.</p>
<blockquote>
<p>We propose an experimental paradigm for evaluating many behavioural interventions at once: the megastudy is a massive field experiment in which many different treatments are tested synchronously in one large sample using a common, objectively measured outcome. This approach takes inspiration from the common task framework, which has substantially accelerated progress in the field of machine learning. In a common task framework, researchers compete to solve the same problem (such as image recognition), subject to the same constraints (for example, the same validation method) and using the same dataset, with complete transparency in terms of hypotheses tested and results.</p>
</blockquote>
<p>I like that point of inspiration. Common task datasets have enabled new machine learning approaches to establish their credentials, often resulting in a new paradigm sweeping the field (such as the sudden improvements in performance from a convolutional neural network on Imagenet in 2012).</p>
<p>But it is not hard to see differences between the megastudy and the common task framework. For a start, common task tournaments typically create an open playing field by making the dataset generally available. Anyone can enter. Contrast that with the submissions from a relatively narrow set of behavioural science teams.</p>
<p>Most common task frameworks also allow iterative exploration and progress. Teams can access the data outside of tournaments (although sometimes there is a holdout dataset for testing). Each year people get to return to the problem. Here we’ve got a one-shot tournament.</p>
<p>Maybe the megastudy study teams should take the inspiration from the common task framework more seriously.</p>
<ul>
<li><p>Why don’t they run this experiment with the gym chain every year? Solicit open entries, with a process to whittle them down to the required number of interventions. Include a range of the best interventions from previous years. (And do it with more power.)</p></li>
<li><p>Introduce a version of out-of-sample testing through replication. Take the top interventions from an initial run of four weeks, and run them with a new group of gym members over another four weeks. This will allow testing of the robustness of the ordering and another check on the magnitude of the winner effect.</p></li>
<li><p>Here’s one half-baked idea: treat the prediction process as a tournament. Maybe one element could involve people submitting models (likely with some combination of Natural Language Processing and an underlying model of the decision maker) to predict which interventions will outperform. Use that to get an insight into theory.</p></li>
</ul>
<p>If we took these extra steps, however, a limitation to the common task framework will become of increasing importance to the megastudy: overfitting. If you run a contest to increase gym attendance again and again there’s a higher probability that one of the interventions will capitalise on an idiosyncratic feature of that gym and its members. Great results, poor generalisation. Maybe we need a different gym each year, or another parallel context, but then you get into questions of comparability.</p>
<h2 id="other-things-i-like">10. Other things I like</h2>
<p>Here’s a list of other things I like about the megastudy but don’t plan to discuss in depth:</p>
<ul>
<li><p>I appreciate the economies of scale that can come with the megastudy approach. The more studies that seek to expand interventions and sample size the better. While I’ve implied above a megastudy may not be better than multiple small studies as multiple studies could give us more generalisable insight, multiple megastudies would provide even greater benefit as comparison both within and across domains is possible.</p></li>
<li><p>The megastudy builds in the publication of null findings. I don’t find the null findings of this gym megastudy interesting as I expect nearly every intervention has a positive effect. But if this megastudy approach is used in other domains, those null findings will be published and start to pile up. And if the power was increased, the constant underperformance of some interventions (even if superior to a null) will become more apparent. (The constant underperformer from my practical experience: loss framing.)</p></li>
<li><p>The authors note that the intervention with the highest effect size is likely to be suffering from a winner effect. As a result, we have an overestimate of the effect size. Thus, the authors note that “Replicating the effects of outlier interventions identified in megastudies will therefore be important for establishing their true impact.” In the two flu megastudies, the winner effect is explicitly examined and adjusted for in reporting the expected effect size of the most effective intervention.</p></li>
</ul>
<h2 id="conclusion">11. Conclusion</h2>
<p>I’ve dedicated most of this post to examining limitations to the megastudy. I don’t want to appear harsh - there are good features - but I feel this study highlights a limitation of behavioural science as it is practised. Even in a world of megastudies, we are still in a world of poor theory, questionable generalisability and inadequate statistical power. I am sure there is a souped-up version of the mega-study that could cover the latter of these, but the other two require something else.</p>
<h2 id="random-thoughts-that-didnt-fit-above">12. Random thoughts that didn’t fit above</h2>
<ul>
<li><p>I suppose the “introduction” in the Nature paper is for those who missed the May 2021 paper by most of the same authors, <a href="https://doi.org/10.1073/pnas.2101165118">A megastudy of text-based nudges encouraging patients to get vaccinated at an upcoming doctor’s appointment</a> … although to be fair, the exercise megastudy was submitted to a journal first.</p></li>
<li><p>The “winning” message for that first vaccination study appears, to me at least, a bit deceptive: “…this is a reminder that a flu vaccine has been reserved for your appt…”</p></li>
<li><p>What is the threshold for a megastudy? The vaccination megastudy involved 19 nudges. Does the Behavioural Insights team <a href="https://doi.org/10.1186/s13063-018-2855-5">trial of 7 different messages on organ donation</a> make the cut? It had 1,085,322 participants. And it enabled the testing of multiple hypotheses in a single context while maintaining adequate power. I’ve seen industry trials in the digital realm with more treatments. Is the concept of the megastudy that new? What seems new to me is the emergence of star academic researchers with access to enough resources to run these projects.</p></li>
</ul>
{{< /html >}}
