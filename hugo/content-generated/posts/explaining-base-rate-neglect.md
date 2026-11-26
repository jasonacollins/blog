---
title: 'Explaining base rate neglect'
author: "Jason Collins"
date: 2022-04-11 20:00:00+00:00
draft: false
sync_source: "posts/explaining-base-rate-neglect.qmd"
sync_route: "quarto"
sync_hash: "42a91a9d009a"
---

{{< html >}}
<p>In a seminar for a team from an investment manager I described how base rates are often neglected when people are grappling with conditional probabilities. My description was somewhat confusing, so the below is a short write-up for the participants.</p>
<p>–</p>
<p>Consider the following question scenario.</p>
<blockquote class="blockquote">
<p>You test yourself with a rapid antigen test for COVID-19. The following information is known:</p>
<ul>
<li>The probability that a person has COVID-19 is 1% (the prevalence).</li>
<li>If a person has COVID-19, the probability that they test&nbsp;positive using this brand of rapid antigen test is 90% (the sensitivity).</li>
<li>If a person does not have COVID-19, the probability that they&nbsp;nevertheless test&nbsp;positive is 9% (the false positive rate).</li>
</ul>
<p>You test positive. What is the chance that you have COVID-19?</p>
</blockquote>
<p>When students, doctors and other experimental subjects answer variants of this question, a common response is around 80% to 90%.</p>
<p>Yet, the answer is approximately 9%. There are far more false positives than true positives. For those that are mathematically inclined, this is a fairly simple application of Bayes’ rule (shown in the Appendix below).</p>
<p>The correct answer becomes more apparent if I show an alternative representation, such as the following:</p>
<blockquote class="blockquote">
<p>You test yourself with a rapid antigen test for COVID-19. The following information is known:</p>
<ul>
<li>Ten in every 1000 people have COVID-19&nbsp;(the prevalence)</li>
<li>Of these 10 people with COVID-19, nine will test positive (the sensitivity)</li>
<li>Of the 990 people without COVID-19, about 89 nevertheless test positive (the false positive rate).</li>
</ul>
<p>You test positive. What is the chance that you have COVID-19?</p>
</blockquote>
<p>This use of natural frequencies was first proposed by <a href="https://doi.org/10.1016/0010-0277(95)00664-8">Cosmides and Tooby (1996)</a> (<a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.131.8290&amp;rep=rep1&amp;type=pdf">pdf</a>). Natural frequencies are derived from observing cases that have been representatively sampled from a population.</p>
<p>In a <a href="https://journals.lww.com/academicmedicine/Abstract/1998/05000/Using_natural_frequencies_to_improve_diagnostic.24.aspx">paper by Gigerenzer and Ulrich Hoffrage</a>, they report that this change in representation increased the proportion of correct answers among physicians from 10% to 46%.</p>
<p>There is some evidence (<a href="https://doi.org/10.54870/1551-3440.1329">e.g.</a>) that you can get further gains through a frequency tree representation. Here’s one such tree from <a href="https://doi.org/10.1136/bmj.d6386">Gigerenzer (2011)</a>, which also has the benefit of further highlighting the benefits of the natural frequency approach.</p>
<p><a href="img/gigerenzer_2011.png" class="lightbox" data-gallery="quarto-lightbox-gallery-1">{{< img src="img/gigerenzer_2011.png" class="img-fluid" >}}</a></p>
<p>The numbers at the bottom of the conditional probability tree do not contain the base rate information. You can’t simply compare across them in calculating conditional probabilities. You also need to refer back to the middle layer. Conversely, the natural frequency tree contains all you need in the bottom row.</p>
<p>Note that we could convert the numbers in the bottom of the conditional probability tree into frequencies: 900 in 1000, 10 in 1000, 90 in 1000 and 910 in 1000. Gigerenzer calls these simple frequencies.</p>
<p>There are many scenarios where simple frequencies can make a problem more tractable, but they do not solve the computational complexity here. Simple frequencies are just a restatement of the probabilities. In contrast, natural frequencies are joint frequencies, such as the number of people who test positive and who have COVID-19.</p>
<p>So why do people make errors of the type described above in the first place?</p>
<p>One explanation is that people confuse the conditional probability of having COVID-19 given a positive test with the conditional probability of receiving a positive result given they have COVID. That is, they confuse <em>P</em>(COVID-19 | positive) with <em>P</em>(positive | COVID-19).</p>
<p>This mistake leads to the largest errors when the base rate of the event you are attempting to predict - in this case having COVID-19 - is low. Confusing the two conditional probabilities effectively results in the base rate being neglected.</p>
<p>Another explanation is that there are two types of information here: general information in the form of a base rate and specific information in the form of a positive test. The positive test is <em>representative</em> of a person who has COVID-19, so is given greater weight than the more general information.</p>
<p>Let’s now put this classic problem into a domain relevant to you.</p>
<blockquote class="blockquote">
<p>You want to know if management of a company or managed fund is skilled. You want to know this as you believe skilled management can lead to outperformance. The following (completely made up) information is known:</p>
<ul>
<li>10% of managers or management teams are skilled.</li>
<li>If a management team is skilled, the probability that they outperform the market is 90%.</li>
<li>If a management team is unskilled, the probability that they outperform the market is 40%.</li>
</ul>
<p>You observe an outperforming firm or fund. What is the probability that they are skilled?</p>
</blockquote>
<p>It’s not 90%. We are not asking the probability of outperformance if they are skilled.</p>
<p>For this example we have a higher base rate than for the COVID-19 example: 10% of teams are skilled. But the evidence on performance has a weaker link to skill than a positive test does to COVID-19. 40% of unskilled teams outperform. There are many false positives.</p>
<p>The result: 20% of outperforming teams are skilled. There is some signal in the noise, but it is weak signal. You cannot neglect that low base rate of skilled teams.</p>
<section id="mathematical-appendix" class="level2">
<h2 class="anchored" data-anchor-id="mathematical-appendix">Mathematical appendix</h2>
<p>Applying Bayes’ rule to the COVID diagnosis:</p>
{{< math display >}}\begin{align*}
P(\text{COVID | positive}) &=\dfrac{P(\text{positive | COVID})P(\text{COVID})}{P(\text{positive})} \\[12pt]
&=\dfrac{P(\text{positive | COVID})P(\text{COVID})}{\Bigg(\begin{align*}
P&(\text{positive | COVID})P(\text{COVID}) \\ &+P(\text{positive | not COVID})P(\text{not COVID})
\end{align*}\Bigg)} \\[30pt]
&=\dfrac{0.9\times0.01}{0.01\times0.9+0.99\times0.09} \\[12pt]
&=0.092
\end{align*}{{< /math >}}
<p>Applying Bayes’ rule to the assessment of skill:</p>
{{< math display >}}\begin{align*}
P(\text{skill | outperform}) &=\dfrac{P(\text{outperform | skill})P(\text{skill})}{P(\text{outperform})} \\[12pt]
&=\dfrac{P(\text{outperform | skill})P(\text{skill})}{\Bigg(\begin{align*}
P(&\text{outperform | skill})P(\text{skill}) \\
&+P(\text{outperform | no skill})P(\text{no skill})
\end{align*}\Bigg)} \\[30pt]
&=\dfrac{0.9\times0.1}{0.9\times0.1+0.4\times0.9} \\[12pt]
&=0.2
\end{align*}{{< /math >}}


</section>
{{< /html >}}
