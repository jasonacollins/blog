---
title: "Is following AI advice \"anchoring bias\"?"
author: "Jason Collins"
date: 2025-10-24 11:00:00+11:00
draft: false
sync_source: "posts/is-following-ai-advice-anchoring-bias.qmd"
sync_route: "quarto"
sync_hash: "4d2819371754"
---

{{< html >}}
<p>Want to demonstrate human “irrationality”? Ask half of your audience the following question:</p>
<blockquote class="blockquote">
<p>Was Elvis older or younger than age 45 when he died?</p>
</blockquote>
<p>Ask the other half:</p>
<blockquote class="blockquote">
<p>Was Elvis older or younger than age 75 when he died?</p>
</blockquote>
<p>Then ask both groups:</p>
<blockquote class="blockquote">
<p>How old was Elvis when he died?</p>
</blockquote>
<p>Those asked if Elvis was older or younger than age 45 tend to estimate a lower age of death than those asked about age 75.</p>
<p>This is an illustration of the “anchoring and adjustment” heuristic. When people estimate a quantity, they often start from an initial value (the anchor) and adjust from that anchor to get a final answer. The heuristic can be biased where we use weak anchors or insufficiently adjust from the anchor.</p>
<p>One famous experiment on anchors was by <span class="citation" data-cites="tversky1974">Tversky and Kahneman (<a href="#ref-tversky1974" role="doc-biblioref">1974</a>)</span>. They spun a wheel with numbers between 0 and 100 on it, but it was rigged to stop at either 10 or 65. They then asked experimental participants who had seen the spin whether the proportion of African countries who were members of the United Nations was above or below that number (this experiment was in the 1970s). The participants were also asked for a numerical estimate. Those who saw 10 on the wheel estimated 25 percent. Those who saw 65 estimated 45 percent. The (assumed) randomness of the anchor was a nice experimental feature. In my Elvis example above, the respondent might assume I chose the number (45 or 75) for a reason. There might be information in that number. There is no such information in the spinning of the wheel.</p>
<p>Insufficient adjustment from the anchor is the flipside of using an irrelevant anchor. If there is any trace of an irrelevant anchor in your answer, you haven’t adjusted enough. However, many anchors we use are sensible starting points - we just don’t adjust enough for our particular case.</p>
<p>Although anchoring is often called a “bias”, it is better to think of anchoring as a heuristic that can backfire in some task environments. If you’re considering making an offer for a four-bedroom house, it’s not a bad strategy to start with the sale price of the neighbouring three-bedroom house. Adjust for the extra bedroom and any other differences between the two. <span class="citation" data-cites="griffiths2015">Griffiths et al. (<a href="#ref-griffiths2015" role="doc-biblioref">2015</a>)</span> argued that anchoring and adjustment can be “resource-rational”, as accounting for the computational cost makes anchoring and adjustment an optimal estimation strategy.</p>
<p>Which brings me to the question of anchoring to artificial intelligence (AI) advice.</p>
<p>A challenge in human-AI interaction is calibrating the user’s trust in the AI system. When should a user trust the AI? When should they deviate from the AI recommendation? Most experimental evidence suggests we don’t calibrate well. Achieving complementary performance - where the human-AI team outperforms either alone - is difficult. Typically, AI assistance improves human performance but the combination still underperforms the AI working alone.</p>
<p><span class="citation" data-cites="rastogi2022">Rastogi et al. (<a href="#ref-rastogi2022" role="doc-biblioref">2022</a>)</span> proposed that one obstacle to complementary performance is “anchoring bias”. People do not explore the alternative hypotheses once the AI decision has provided an anchor.</p>
<p>To examine this question, <span class="citation" data-cites="rastogi2022">Rastogi et al. (<a href="#ref-rastogi2022" role="doc-biblioref">2022</a>)</span> conducted two experiments, which I walk through below.</p>
<section id="experiment-1" class="level2">
<h2 class="anchored" data-anchor-id="experiment-1">Experiment 1</h2>
<p>The authors asked a group of <a href="https://www.mturk.com/">Amazon Mechanical Turk</a> workers to use student data to predict whether a student would pass or fail a class. The data, drawn from a <a href="https://archive.ics.uci.edu/dataset/320/student+performance">student performance dataset</a>, included student characteristics, past performance and demographics. The workers were also provided with an AI model recommendation (logistic regression) based on the 10 most important student features (e.g.&nbsp;mother’s and father’s education, hours spent studying weekly).</p>
<p>Participants completed 15 training examples, during which the authors deliberately misled them about AI performance:</p>
<blockquote class="blockquote">
<p>To induce anchoring bias, the participant was informed at the start of the training section that the AI model was 85% accurate (we carefully chose the training trials to ensure that the AI was indeed 85% accurate over these trials), while the model’s actual accuracy is 70.8% over the entire training set and 66.5% over the test set. Since our goal is to induce anchoring bias and the training time is short, we stated a high AI accuracy.</p>
</blockquote>
<p>After each training estimate, the workers were shown the correct answer and the estimate made by the AI.</p>
<p>Effectively, participants are told the AI is 85% accurate and then see performance through the training set that aligns with that accuracy. The exact wording isn’t provided, but the intent is clear. I’m reluctant to call behaviour “biased” when it’s based on information designed to deceive. (Deception is common in human-AI experiments. I have another post on this coming.)</p>
<p>The test section had 36 trials. The AI accuracy was even lower than 66% because the experimenters deliberately “flipped” eight AI predictions, reducing task accuracy to 58%. Workers who followed these flipped predictions (called “probe trials” by the authors) would perform worse than those receiving unmanipulated AI advice.</p>
<p>The primary hypothesis the authors tested in Experiment 1 is whether anchoring is reduced if the workers were given more time to make their prediction. Workers were given 10, 15, 20 or 25 seconds to make their prediction. If they were less likely to follow the erroneous prediction in those flipped trials, that would be evidence of reduced anchoring.</p>
<p>The results at first glance, as presented in the following figure, support the hypothesis. Workers with 25 seconds were more likely to deviate from the incorrect recommendation. This might be thought of as being in line with <span class="citation" data-cites="griffiths2015">Griffiths et al. (<a href="#ref-griffiths2015" role="doc-biblioref">2015</a>)</span>, in that more resources enable more calculation and adjustment.</p>
<p><a href="img/is-following-ai-advice-anchoring/rastogi-et-al-2022-fig-2a.png" class="lightbox" data-gallery="quarto-lightbox-gallery-1">{{< img src="img/is-following-ai-advice-anchoring/rastogi-et-al-2022-fig-2a.png" class="img-fluid" >}}</a></p>
<p>(I also suspect there is an error in this chart. The average disagreement for the non-probe trials is unbelievably low.)</p>
<p>Only one statistical test is reported for the pattern in the figure. No p-value is given, but the confidence intervals suggest it barely reaches significance. The authors also don’t report broader accuracy data.</p>
<p>The lack of pre-registration is a concern. There are many ways to test the effect of time on anchoring. The authors used a linear regression on 5,000 bootstrapped resamples - a choice that isn’t explained. Other approaches might yield different results.</p>
<p>Further, like much human-computer interaction literature, the paper provides limited results without public data, making it impossible to test robustness or explore alternative analyses.</p>
<p>Finally, “adjustment” itself is hard to measure here. The only observable signal is disagreement with the AI. That leaves open whether participants are truly adjusting from an anchor or simply deferring to the AI unless they see clear reasons not to. These are two distinct processes.</p>
</section>
<section id="experiment-2" class="level2">
<h2 class="anchored" data-anchor-id="experiment-2">Experiment 2</h2>
<p>In experiment 2, the authors test a broader set of interventions to reduce “anchoring bias”. They also report richer data (in the form of a more detailed chart), so we’re able to see a little more of the dynamic.</p>
<p>Experiment 2 used the same task but the experimenters degraded the AI by training it without three important features: study hours, social hours, and educational support enrolment. Workers could see these features, creating an information asymmetry where human input could potentially improve AI predictions.</p>
<p>The authors don’t state the degraded AI’s accuracy. Workers were again told it had 85% accuracy during training, but its actual accuracy on the main task was around 60%.</p>
<p>Workers were then placed in the following conditions.</p>
<ul>
<li><strong>Human only</strong>: Workers provide their prediction without an AI prediction. They are given 25 seconds for each prediction</li>
<li><strong>Constant time</strong>: Workers provide their prediction with the help of the AI prediction, with 18 seconds per prediction.<br>
</li>
<li><strong>Random time</strong>: AI assistance with the time allocation randomly set to either 10 seconds or 25 seconds each trial.<br>
</li>
<li><strong>Confidence-based time</strong>: AI assistance with 10 or 25 seconds depending on AI confidence (low confidence = more time).<br>
</li>
<li><strong>Confidence-based time with explanation</strong>: As for confidence-based time but the AI confidence is explicitly provided (“low” or “high”).</li>
</ul>
<p>Each of these conditions aligns with a hypothesis that they might reduce anchoring. The one I will focus on is H2: Anchoring bias has a negative effect on human-AI collaborative decision-making accuracy when AI is incorrect.</p>
<p>The results are summarised in the following figures.</p>
<p><a href="img/is-following-ai-advice-anchoring/rastogi-et-al-2022-fig-4.png" class="lightbox" data-gallery="quarto-lightbox-gallery-2">{{< img src="img/is-following-ai-advice-anchoring/rastogi-et-al-2022-fig-4.png" class="img-fluid" >}}</a></p>
<p>The human only group has higher accuracy than all of the AI groups on instances where the AI is incorrect. The authors take this as evidence in support of H2.</p>
<p>This raises the question of whether “anchoring bias” is the right frame. To avoid lower accuracy when the AI errs, workers would need to ignore the AI completely on those trials, removing the anchor entirely. But that’s unreasonable. The workers were told the AI has 85% accuracy, and their training experience confirmed it.</p>
<p>“Anchoring” is the wrong label here and “anchoring bias” even more so. If using information degrades a decision, that doesn’t make the use of that information a bias.</p>
<p>To determine whether behaviour is biased, we need a model that accounts for the information the experimenters provided. The authors call the AI estimate an anchor. It’s better understood as a prior, shaped by the experimenters’ claim of 85% accuracy. In Bayesian terms, participants start with a belief about the AI’s accuracy and update it as they see evidence.</p>
<p>In experimental economics, where deception is forbidden, participants would rationally place high confidence in such a claim. The prior is strong. Even in this human-computer interaction experiment, treating the stated accuracy as credible information (or at least having some signal) is reasonable behaviour, not bias.</p>
<p>If one of my kids tells me they’ve got a normal coin and flip two heads, I update only marginally from my strong prior that the coin is fair. What is the level of trust of experimental participants in experimenters? What is the appropriate level of trust? (One reason deception is frowned upon in economics is because it degrades trust in experimenters, leading to an additional variable you need to account for in your analysis.)</p>
<p>Turning back to the figure, the results also point to a complementary hypothesis not identified by the authors:</p>
<blockquote class="blockquote">
<p>Anchoring bias has a positive effect on human-AI collaborative decision-making accuracy when AI is correct.</p>
</blockquote>
<p>Again, for this not to be true, we would need the person to completely ignore the AI. And unsurprisingly, eyeballing the figure, my hypothesis is true. The AI conditions all markedly outperform the human-only group on estimates where the AI recommendation is correct.</p>
<p>There’s an interesting pattern across all the conditions. Whenever you decrease the probability of following an incorrect AI recommendation, you also decrease the probability of following a correct recommendation. The result is that performance across all conditions is largely the same. Because the AI in this experiment is degraded to a quality similar to that of humans alone, reliance on the AI is largely a wash.</p>
<p>Finally, the authors provide another interesting interpretation when they state that they achieve complementary knowledge. Due to the three excluded variables, the human has more information than the AI. There are a lot of real-world applications where the human will have information the AI doesn’t - an AI-financial adviser for example - so finding ways to enhance the use of unshared information is vital to achieving complementary performance. In this case, we get complementary knowledge in that the humans do as well as the AI alone despite the fact they don’t always follow the AI. Unfortunately, we don’t get complementary performance - that is, outperformance by the human-AI team of both the human and AI alone. But examining how to get people to use unshared information seems a prospective path.</p>
</section>
<section id="the-problem-is-more-often-insufficient-anchoring" class="level2">
<h2 class="anchored" data-anchor-id="the-problem-is-more-often-insufficient-anchoring">The problem is more often insufficient anchoring</h2>
<p>This experiment involved an AI with capability on par with unassisted humans. But in most statistical tasks such as the one in this experiment, the AI outperforms the human. Further, human-AI teams tend to underperform the AI alone.</p>
<p>In other words, experiments typically find that people adjust too much! Here’s some data from <span class="citation" data-cites="dietvorst2018">Dietvorst et al. (<a href="#ref-dietvorst2018" role="doc-biblioref">2018</a>)</span>. People were more likely to use an algorithm if they could adjust it. That led to higher performance, largely because of this greater likelihood of selecting the model.</p>
<div class="quarto-figure quarto-figure-center">
<figure class="figure">
<figcaption><span class="citation" data-cites="dietvorst2018">Dietvorst et al. (<a href="#ref-dietvorst2018" role="doc-biblioref">2018</a>)</span> Figure 2b</figcaption>
<p><a href="img/is-following-ai-advice-anchoring/dietvorst-et-al-2018-fig-2b.png" class="lightbox" data-gallery="quarto-lightbox-gallery-3" title="@dietvorst2018 Figure 2b"><img src="img/is-following-ai-advice-anchoring/dietvorst-et-al-2018-fig-2b.png" class="img-fluid figure-img" width="400" alt="Dietvorst et al. (2018) Figure 2b"></a></p>
</figure>
</div>
<p>But how does the performance of those who selected the model compare to the model itself? Here is a chart I have generated from the experimental data provided in the <a href="https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.2016.2643/suppl_file/mnsc.2016.2643-sm-data.zip">supplementary materials</a>. (Again noting that business schools <a href="../posts/why-i-dont-trust-most-human-ai-interaction-experimental-research.html">more often share data</a>.) In the “Adjust by 10” group, the participant’s adjustments were a wash, with their performance on par with the unadjusted model. But for those in the “Change 10” group, their changes increased the error. The AI alone was a stronger performer.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb1"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">library</span>(tidyverse)</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="fu">library</span>(scales)</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="co"># Read the data - specify na values to handle periods as missing</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a>data <span class="ot">&lt;-</span> <span class="fu">read_csv</span>(<span class="st">"data/Overcoming_Algorithm_Aversion_Data-study-1-data.csv"</span>,</span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>                 <span class="at">na =</span> <span class="fu">c</span>(<span class="st">""</span>, <span class="st">"NA"</span>, <span class="st">"."</span>))</span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="co"># Convert necessary columns to numeric (many are stored as strings due to periods)</span></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>data <span class="ot">&lt;-</span> data <span class="sc">%&gt;%</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  <span class="fu">mutate</span>(<span class="fu">across</span>(<span class="fu">c</span>(ModelBonus, ModelAAEEstimate, HumanAAEEstimate,</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a>                  ModelConfidence, HumanConfidence, Age, Gender, Education,</span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>                  AAE, ModelAAE, HumanAAE, Bonus, BonusFromModel, BonusFromHuman,</span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>                  CorrelationWithModel, AvDiffFromModel, AvAdjustmentSize,</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>                  AdjustmentDividedByPotential, HumModelCorrelation, HumModelAvDiff,</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>                  AvgLargest10Changes, AnyBonus), </span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>                as.numeric))</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a><span class="co"># Define condition labels</span></span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>condition_labels <span class="ot">&lt;-</span> <span class="fu">c</span>(<span class="st">"1"</span> <span class="ot">=</span> <span class="st">"Can't change"</span>, </span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>                     <span class="st">"2"</span> <span class="ot">=</span> <span class="st">"Adjust by 10"</span>, </span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>                     <span class="st">"3"</span> <span class="ot">=</span> <span class="st">"Change 10"</span>, </span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>                     <span class="st">"4"</span> <span class="ot">=</span> <span class="st">"Use freely"</span>)</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a><span class="co"># Filter for participants who chose the model (ModelBonus == 1)</span></span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>model_choosers <span class="ot">&lt;-</span> data <span class="sc">%&gt;%</span></span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>  <span class="fu">filter</span>(ModelBonus <span class="sc">==</span> <span class="dv">1</span>)</span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a><span class="co"># Calculate summary statistics by condition</span></span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>summary_stats <span class="ot">&lt;-</span> model_choosers <span class="sc">%&gt;%</span></span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>  <span class="fu">group_by</span>(Condition) <span class="sc">%&gt;%</span></span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>  <span class="fu">summarise</span>(</span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>    <span class="at">n =</span> <span class="fu">n</span>(),</span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>    <span class="at">ModelAAE_mean =</span> <span class="fu">mean</span>(ModelAAE, <span class="at">na.rm =</span> <span class="cn">TRUE</span>),</span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a>    <span class="at">AAE_mean =</span> <span class="fu">mean</span>(AAE, <span class="at">na.rm =</span> <span class="cn">TRUE</span>),</span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a>    <span class="at">ModelAAE_sd =</span> <span class="fu">sd</span>(ModelAAE, <span class="at">na.rm =</span> <span class="cn">TRUE</span>),</span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>    <span class="at">AAE_sd =</span> <span class="fu">sd</span>(AAE, <span class="at">na.rm =</span> <span class="cn">TRUE</span>),</span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a>    <span class="at">Difference =</span> AAE_mean <span class="sc">-</span> ModelAAE_mean,</span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a>    <span class="at">PercentChange =</span> (Difference <span class="sc">/</span> ModelAAE_mean) <span class="sc">*</span> <span class="dv">100</span>,</span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a>    <span class="at">AvgAdjustmentSize =</span> <span class="fu">mean</span>(AvAdjustmentSize, <span class="at">na.rm =</span> <span class="cn">TRUE</span>)</span>
<span id="cb1-40"><a href="#cb1-40" aria-hidden="true" tabindex="-1"></a>  ) <span class="sc">%&gt;%</span></span>
<span id="cb1-41"><a href="#cb1-41" aria-hidden="true" tabindex="-1"></a>  <span class="fu">mutate</span>(<span class="at">ConditionLabel =</span> condition_labels[<span class="fu">as.character</span>(Condition)])</span>
<span id="cb1-42"><a href="#cb1-42" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-43"><a href="#cb1-43" aria-hidden="true" tabindex="-1"></a><span class="co"># Add info about total participants per condition</span></span>
<span id="cb1-44"><a href="#cb1-44" aria-hidden="true" tabindex="-1"></a>total_by_condition <span class="ot">&lt;-</span> data <span class="sc">%&gt;%</span></span>
<span id="cb1-45"><a href="#cb1-45" aria-hidden="true" tabindex="-1"></a>  <span class="fu">group_by</span>(Condition) <span class="sc">%&gt;%</span></span>
<span id="cb1-46"><a href="#cb1-46" aria-hidden="true" tabindex="-1"></a>  <span class="fu">summarise</span>(<span class="at">total_n =</span> <span class="fu">n</span>())</span>
<span id="cb1-47"><a href="#cb1-47" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-48"><a href="#cb1-48" aria-hidden="true" tabindex="-1"></a>summary_stats <span class="ot">&lt;-</span> summary_stats <span class="sc">%&gt;%</span></span>
<span id="cb1-49"><a href="#cb1-49" aria-hidden="true" tabindex="-1"></a>  <span class="fu">left_join</span>(total_by_condition, <span class="at">by =</span> <span class="st">"Condition"</span>) <span class="sc">%&gt;%</span></span>
<span id="cb1-50"><a href="#cb1-50" aria-hidden="true" tabindex="-1"></a>  <span class="fu">mutate</span>(<span class="at">PropChoseModel =</span> n <span class="sc">/</span> total_n)</span>
<span id="cb1-51"><a href="#cb1-51" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-52"><a href="#cb1-52" aria-hidden="true" tabindex="-1"></a><span class="co"># Prepare data for plotting</span></span>
<span id="cb1-53"><a href="#cb1-53" aria-hidden="true" tabindex="-1"></a>plot_data <span class="ot">&lt;-</span> summary_stats <span class="sc">%&gt;%</span></span>
<span id="cb1-54"><a href="#cb1-54" aria-hidden="true" tabindex="-1"></a>  <span class="fu">filter</span>(<span class="sc">!</span><span class="fu">is.na</span>(AAE_mean) <span class="sc">&amp;</span> Condition <span class="sc">!=</span> <span class="dv">1</span>) <span class="sc">%&gt;%</span>  <span class="co"># Remove can't change condition and any conditions with no data</span></span>
<span id="cb1-55"><a href="#cb1-55" aria-hidden="true" tabindex="-1"></a>  <span class="fu">select</span>(Condition, ConditionLabel, ModelAAE_mean, AAE_mean) <span class="sc">%&gt;%</span></span>
<span id="cb1-56"><a href="#cb1-56" aria-hidden="true" tabindex="-1"></a>  <span class="fu">pivot_longer</span>(<span class="at">cols =</span> <span class="fu">c</span>(ModelAAE_mean, AAE_mean),</span>
<span id="cb1-57"><a href="#cb1-57" aria-hidden="true" tabindex="-1"></a>               <span class="at">names_to =</span> <span class="st">"ErrorType"</span>,</span>
<span id="cb1-58"><a href="#cb1-58" aria-hidden="true" tabindex="-1"></a>               <span class="at">values_to =</span> <span class="st">"AAE"</span>) <span class="sc">%&gt;%</span></span>
<span id="cb1-59"><a href="#cb1-59" aria-hidden="true" tabindex="-1"></a>  <span class="fu">mutate</span>(</span>
<span id="cb1-60"><a href="#cb1-60" aria-hidden="true" tabindex="-1"></a>    <span class="at">ErrorType =</span> <span class="fu">case_when</span>(</span>
<span id="cb1-61"><a href="#cb1-61" aria-hidden="true" tabindex="-1"></a>      ErrorType <span class="sc">==</span> <span class="st">"ModelAAE_mean"</span> <span class="sc">~</span> <span class="st">"Model (no adjustment)"</span>,</span>
<span id="cb1-62"><a href="#cb1-62" aria-hidden="true" tabindex="-1"></a>      ErrorType <span class="sc">==</span> <span class="st">"AAE_mean"</span> <span class="sc">~</span> <span class="st">"Actual (with adjustment)"</span></span>
<span id="cb1-63"><a href="#cb1-63" aria-hidden="true" tabindex="-1"></a>    ),</span>
<span id="cb1-64"><a href="#cb1-64" aria-hidden="true" tabindex="-1"></a>    <span class="at">ErrorType =</span> <span class="fu">factor</span>(ErrorType, <span class="at">levels =</span> <span class="fu">c</span>(<span class="st">"Model (no adjustment)"</span>, <span class="st">"Actual (with adjustment)"</span>))</span>
<span id="cb1-65"><a href="#cb1-65" aria-hidden="true" tabindex="-1"></a>  )</span>
<span id="cb1-66"><a href="#cb1-66" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-67"><a href="#cb1-67" aria-hidden="true" tabindex="-1"></a><span class="co"># Create the plot</span></span>
<span id="cb1-68"><a href="#cb1-68" aria-hidden="true" tabindex="-1"></a>p <span class="ot">&lt;-</span> <span class="fu">ggplot</span>(plot_data, <span class="fu">aes</span>(<span class="at">x =</span> ConditionLabel, <span class="at">y =</span> AAE, <span class="at">fill =</span> ErrorType)) <span class="sc">+</span></span>
<span id="cb1-69"><a href="#cb1-69" aria-hidden="true" tabindex="-1"></a>  <span class="fu">geom_bar</span>(<span class="at">stat =</span> <span class="st">"identity"</span>, <span class="at">position =</span> <span class="st">"dodge"</span>, <span class="at">width =</span> <span class="fl">0.7</span>) <span class="sc">+</span></span>
<span id="cb1-70"><a href="#cb1-70" aria-hidden="true" tabindex="-1"></a>  <span class="fu">scale_fill_manual</span>(<span class="at">values =</span> <span class="fu">c</span>(<span class="st">"Model (no adjustment)"</span> <span class="ot">=</span> <span class="st">"#3498db"</span>, </span>
<span id="cb1-71"><a href="#cb1-71" aria-hidden="true" tabindex="-1"></a>                              <span class="st">"Actual (with adjustment)"</span> <span class="ot">=</span> <span class="st">"#e74c3c"</span>)) <span class="sc">+</span></span>
<span id="cb1-72"><a href="#cb1-72" aria-hidden="true" tabindex="-1"></a>  <span class="fu">labs</span>(</span>
<span id="cb1-73"><a href="#cb1-73" aria-hidden="true" tabindex="-1"></a>    <span class="at">title =</span> <span class="st">"Error Rates for Model Choosers by Adjustment Condition"</span>,</span>
<span id="cb1-74"><a href="#cb1-74" aria-hidden="true" tabindex="-1"></a>    <span class="at">subtitle =</span> <span class="st">"Comparing model performance with and without adjustments"</span>,</span>
<span id="cb1-75"><a href="#cb1-75" aria-hidden="true" tabindex="-1"></a>    <span class="at">x =</span> <span class="st">"Condition"</span>,</span>
<span id="cb1-76"><a href="#cb1-76" aria-hidden="true" tabindex="-1"></a>    <span class="at">y =</span> <span class="st">"Average Absolute Error (AAE)"</span>,</span>
<span id="cb1-77"><a href="#cb1-77" aria-hidden="true" tabindex="-1"></a>    <span class="at">fill =</span> <span class="st">"Error Type"</span></span>
<span id="cb1-78"><a href="#cb1-78" aria-hidden="true" tabindex="-1"></a>  ) <span class="sc">+</span></span>
<span id="cb1-79"><a href="#cb1-79" aria-hidden="true" tabindex="-1"></a>  <span class="fu">theme_minimal</span>() <span class="sc">+</span></span>
<span id="cb1-80"><a href="#cb1-80" aria-hidden="true" tabindex="-1"></a>  <span class="fu">theme</span>(</span>
<span id="cb1-81"><a href="#cb1-81" aria-hidden="true" tabindex="-1"></a>    <span class="at">plot.title =</span> <span class="fu">element_text</span>(<span class="at">size =</span> <span class="dv">16</span>, <span class="at">face =</span> <span class="st">"bold"</span>, <span class="at">hjust =</span> <span class="fl">0.5</span>),</span>
<span id="cb1-82"><a href="#cb1-82" aria-hidden="true" tabindex="-1"></a>    <span class="at">plot.subtitle =</span> <span class="fu">element_text</span>(<span class="at">size =</span> <span class="dv">12</span>, <span class="at">hjust =</span> <span class="fl">0.5</span>),</span>
<span id="cb1-83"><a href="#cb1-83" aria-hidden="true" tabindex="-1"></a>    <span class="at">axis.text.x =</span> <span class="fu">element_text</span>(<span class="at">angle =</span> <span class="dv">45</span>, <span class="at">hjust =</span> <span class="dv">1</span>),</span>
<span id="cb1-84"><a href="#cb1-84" aria-hidden="true" tabindex="-1"></a>    <span class="at">legend.position =</span> <span class="st">"top"</span>,</span>
<span id="cb1-85"><a href="#cb1-85" aria-hidden="true" tabindex="-1"></a>    <span class="at">legend.title =</span> <span class="fu">element_text</span>(<span class="at">face =</span> <span class="st">"bold"</span>),</span>
<span id="cb1-86"><a href="#cb1-86" aria-hidden="true" tabindex="-1"></a>    <span class="at">panel.grid.minor =</span> <span class="fu">element_blank</span>()</span>
<span id="cb1-87"><a href="#cb1-87" aria-hidden="true" tabindex="-1"></a>  ) <span class="sc">+</span></span>
<span id="cb1-88"><a href="#cb1-88" aria-hidden="true" tabindex="-1"></a>  <span class="fu">scale_y_continuous</span>(<span class="at">limits =</span> <span class="fu">c</span>(<span class="dv">0</span>, <span class="fu">max</span>(plot_data<span class="sc">$</span>AAE, <span class="at">na.rm =</span> <span class="cn">TRUE</span>) <span class="sc">*</span> <span class="fl">1.1</span>), </span>
<span id="cb1-89"><a href="#cb1-89" aria-hidden="true" tabindex="-1"></a>                     <span class="at">breaks =</span> <span class="fu">pretty_breaks</span>(<span class="at">n =</span> <span class="dv">5</span>)) <span class="sc">+</span></span>
<span id="cb1-90"><a href="#cb1-90" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Add percentage change labels on top of bars</span></span>
<span id="cb1-91"><a href="#cb1-91" aria-hidden="true" tabindex="-1"></a>  <span class="fu">geom_text</span>(<span class="at">data =</span> summary_stats <span class="sc">%&gt;%</span> <span class="fu">filter</span>(<span class="sc">!</span><span class="fu">is.na</span>(AAE_mean) <span class="sc">&amp;</span> Condition <span class="sc">!=</span> <span class="dv">1</span>),</span>
<span id="cb1-92"><a href="#cb1-92" aria-hidden="true" tabindex="-1"></a>            <span class="fu">aes</span>(<span class="at">x =</span> ConditionLabel, <span class="at">y =</span> AAE_mean <span class="sc">+</span> <span class="fl">0.5</span>, </span>
<span id="cb1-93"><a href="#cb1-93" aria-hidden="true" tabindex="-1"></a>                <span class="at">label =</span> <span class="fu">paste0</span>(<span class="fu">ifelse</span>(Difference <span class="sc">&gt;=</span> <span class="dv">0</span>, <span class="st">"+"</span>, <span class="st">""</span>), </span>
<span id="cb1-94"><a href="#cb1-94" aria-hidden="true" tabindex="-1"></a>                               <span class="fu">round</span>(PercentChange, <span class="dv">1</span>), <span class="st">"%"</span>)),</span>
<span id="cb1-95"><a href="#cb1-95" aria-hidden="true" tabindex="-1"></a>            <span class="at">inherit.aes =</span> <span class="cn">FALSE</span>,</span>
<span id="cb1-96"><a href="#cb1-96" aria-hidden="true" tabindex="-1"></a>            <span class="at">size =</span> <span class="fl">3.5</span>,</span>
<span id="cb1-97"><a href="#cb1-97" aria-hidden="true" tabindex="-1"></a>            <span class="at">fontface =</span> <span class="st">"bold"</span>)</span>
<span id="cb1-98"><a href="#cb1-98" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-99"><a href="#cb1-99" aria-hidden="true" tabindex="-1"></a><span class="co"># Display the plot</span></span>
<span id="cb1-100"><a href="#cb1-100" aria-hidden="true" tabindex="-1"></a><span class="fu">print</span>(p)</span></code></pre></div></div>
</details>
<div class="cell-output-display">
<div>
<figure class="figure">
<p><a href="is-following-ai-advice-anchoring-bias_files/figure-html/dietvorst-error-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-4"><img src="is-following-ai-advice-anchoring-bias_files/figure-html/dietvorst-error-1.png" class="img-fluid figure-img" width="672"></a></p>
</figure>
</div>
</div>
</div>
<p>A meta-analysis by <span class="citation" data-cites="vaccaro2024">Vaccaro et al. (<a href="#ref-vaccaro2024" role="doc-biblioref">2024</a>)</span> examined 370 effect sizes from 106 studies. Human-AI combinations usually underperformed the better of the two working alone, with the exception of creative tasks where teams more often outperformed individuals.</p>
<p><a href="img/is-following-ai-advice-anchoring/vaccaro-et-al-2024-fig-1a.png" class="lightbox" data-gallery="quarto-lightbox-gallery-5"><img src="img/is-following-ai-advice-anchoring/vaccaro-et-al-2024-fig-1a.png" class="img-fluid" width="600"></a></p>
<p>Bringing this back to the anchoring experiment, if the AI actually had accuracy of 85% as the experimental participants were informed, I suspect we would be talking about a different problem: insufficient anchoring. Anchoring and overadjustment. That’s a very different problem to solve.</p>
<p>The challenge, therefore, is not reducing “anchoring bias” but recognising when the anchor contains useful information and calibrating how much to adjust. It’s typically a problem of anchors being too weak, not too strong.</p>



</section>

<div id="quarto-appendix" class="default"><section class="quarto-appendix-contents" role="doc-bibliography" id="quarto-bibliography"><h2 class="anchored quarto-appendix-heading">References</h2><div id="refs" class="references csl-bib-body hanging-indent" data-entry-spacing="0" data-line-spacing="2" role="list">
<div id="ref-dietvorst2018" class="csl-entry" role="listitem">
Dietvorst, B. J., Simmons, J. P., and Massey, C. (2018). Overcoming algorithm aversion: People will use imperfect algorithms if they can (even slightly) modify them. <em>Management Science</em>, <em>64</em>(3), 1155–1170. <a href="https://doi.org/10.1287/mnsc.2016.2643">https://doi.org/10.1287/mnsc.2016.2643</a>
</div>
<div id="ref-griffiths2015" class="csl-entry" role="listitem">
Griffiths, T. L., Lieder, F., and Goodman, N. D. (2015). Rational use of cognitive resources: Levels of analysis between the computational and the algorithmic. <em>Topics in Cognitive Science</em>, <em>7</em>(2), 217–229. <a href="https://doi.org/10.1111/tops.12142">https://doi.org/10.1111/tops.12142</a>
</div>
<div id="ref-rastogi2022" class="csl-entry" role="listitem">
Rastogi, C., Zhang, Y., Wei, D., Varshney, K. R., Dhurandhar, A., …. (2022). Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making. <em>Proc. ACM Hum.-Comput. Interact.</em>, <em>6</em>(CSCW1), 83:183:22. <a href="https://doi.org/10.1145/3512930">https://doi.org/10.1145/3512930</a>
</div>
<div id="ref-tversky1974" class="csl-entry" role="listitem">
Tversky, A., and Kahneman, D. (1974). Judgment under Uncertainty: Heuristics and Biases. <em>Science</em>, <em>185</em>(4157), 1124–1131. <a href="https://doi.org/10.1126/science.185.4157.1124">https://doi.org/10.1126/science.185.4157.1124</a>
</div>
<div id="ref-vaccaro2024" class="csl-entry" role="listitem">
Vaccaro, M., Almaatouq, A., and Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. <em>Nature Human Behaviour</em>, 1–11. <a href="https://doi.org/10.1038/s41562-024-02024-1">https://doi.org/10.1038/s41562-024-02024-1</a>
</div>
</div></section></div>
{{< /html >}}
