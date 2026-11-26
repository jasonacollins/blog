---
title: "The AI behind the curtain: deception in human-AI experiments"
author: "Jason Collins"
date: 2026-05-25 10:00:00+11:00
draft: false
image: "img/curtain.png"
sync_source: "posts/the-ai-behind-the-curtain-deception-in-human-ai-experiments.md"
sync_route: "quarto"
sync_hash: "b111144060ad"
---

{{< html >}}
<p>Experimental economists don’t deceive their subjects. It’s not legislated, but break the norm and don’t expect to be published. Here’s Andreas <span class="citation" data-cites="ortmann2019">Ortmann (<a href="#ref-ortmann2019" role="doc-biblioref">2019</a>)</span>:</p>
<blockquote class="blockquote">
<p>I open with a statement of fact: deception in the form of acts of commission, while still widespread in (social) psychology and business sciences such as marketing, is factually banned in laboratory experimental economics. This ban is not legislated but, until recently, was a social norm that the community of experimental economists had been able to reasonably enforce.</p>
</blockquote>
<p>There are a few reasons for this norm. One is that if participants suspect they are being deceived, they will alter their behaviour and undermine the experimental results. An example of this is the famous <a href="https://en.wikipedia.org/wiki/Asch_conformity_experiments">Solomon Asch conformity experiments</a>, in which those who believed they were being deceived were less likely to conform with the group.</p>
<p>Deception also creates an externality for other experiments. After being deceived in one experiment - as they discover when promises aren’t kept or in experimental debriefs - participants will be less trusting in future experiments, again changing their behaviour. In subject pools where people complete many experiments and surveys, regular deception could shift their expectations.</p>
<p>There is no norm against deception in psychology. Deception is common and often argued to be necessary for many experiments, albeit with explicit ethical frameworks and debriefing.</p>
<p>There is also no such norm in human-computer interaction research, as I have discovered over the last couple of years. This is not only deception by omission: not telling people everything about the experiment. Rather, there are many acts of commission, such as telling people things that are not true.</p>
<p>One common form of deception is that there is no actual AI. Rather, the participants are shown hand-crafted responses. I have seen this called “synthetic AI” or “simulated AI”, and in design circles it is often called the “Wizard of Oz” paradigm.</p>
<p>It also seems common for experimenters to tell the occasional lie to generate the desired response.</p>
<p>Below are examples of each, along with some questions they raise. I don’t have a firm view on some of this deception apart from a general desire to avoid it, so the below is more observation than a hardened view.</p>
<section id="synthetic-ai" class="level2">
<h2 class="anchored" data-anchor-id="synthetic-ai">Synthetic AI</h2>
<p>To run an experiment on human responses to an AI, you want an AI. But that’s a challenge. You need to procure or develop an AI to train on the task or data. Depending on the nature of the AI, you might also design an interface. There’s also no guarantee that your AI will have the features you desire, such as a certain error rate or error boundary.</p>
<p>In economics, this challenge typically leads to the use of statistical prediction tasks. Given a dataset about, say, student achievement, you develop a statistical model (which you then call an AI) to predict achievement based on other features of the student. With readily available datasets (such as those on <a href="https://www.kaggle.com/datasets">Kaggle</a> or in repositories such as the <a href="https://archive.ics.uci.edu/">UC Irvine Machine Learning Repository</a>), developing statistical models is bread-and-butter work for an economist. You can train a model on these well-structured datasets in a few lines of code.</p>
<p>These models typically outperform human judgement by a considerable margin. The optimal interaction is for the human to hand off the decision to the AI. These models are useful for algorithm aversion studies, but provide limited scope to examine collaborative decision making.</p>
<p>If you want a weaker model, you might withhold data from the model (as done in a recent paper <a href="../posts/is-following-ai-advice-anchoring-bias.html">I posted about</a> on anchoring). This gives the human information the model doesn’t have. Ultimately, however, statistical prediction is only a subset of the space in which you might want to study human-AI interaction. That moves us into more complex domains where it’s not so easy to develop a model.</p>
<p>In experiments coming from the human-computer interaction field, you do see statistical models, but often the experiments require a richer environment. And that’s where they turn to deception via synthetic AI.</p>
<p>One example of synthetic AI is in <span class="citation" data-cites="buçinca2021">Buçinca et al. (<a href="#ref-buçinca2021" role="doc-biblioref">2021</a>)</span>, who examined whether triggering slow thinking can increase engagement with explanations of AI recommendations. The authors created a task where participants were shown a picture of a meal and information on the main ingredients. Participants were then asked what ingredients to substitute to make it low-carb while maintaining the original flavour.</p>
<div id="fig-bucinca_et_al_2021_fig_1" class="quarto-float quarto-figure quarto-figure-center anchored">
<figure class="quarto-float quarto-float-fig figure">
<figcaption class="quarto-float-caption-top quarto-float-caption quarto-float-fig" id="fig-bucinca_et_al_2021_fig_1-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;1: <span class="citation" data-cites="buçinca2021">Buçinca et al. (<a href="#ref-buçinca2021" role="doc-biblioref">2021</a>)</span>, Figure 1
</figcaption>
<div aria-describedby="fig-bucinca_et_al_2021_fig_1-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<a href="img/the-ai-that-wasnt-deception-in-human-ai-experiments/bucinca-et-al-2021-fig-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-1" title="Figure&nbsp;1: @buçinca2021, Figure 1">{{< img src="img/the-ai-that-wasnt-deception-in-human-ai-experiments/bucinca-et-al-2021-fig-1.png" class="img-fluid figure-img" >}}</a>
</div>
</figure>
</div>
<p>And how was this AI developed? The authors write:</p>
<blockquote class="blockquote">
<p>We designed a simulated AI for the experiment, which had 75% accuracy of correctly recognizing the ingredient with the highest carbohydrate impact in the image of the meal. Note that we did not train an actual machine learning model for this task because we wanted to have control over the type and prevalence of error the AI would make.</p>
</blockquote>
<p>This is one of the more direct statements that the AI was simulated rather than built. But even where less explicitly stated, it is common practice.</p>
<p>The question then becomes what participants believe about this scenario. Do they believe an AI is actually delivering these suggestions and associated explanations? To the extent they don’t, does this affect their likelihood of following the AI recommendation? Are you losing a degree of control over the participant’s mental model?</p>
<p>Some researchers in human-computer interaction do go the extra mile of developing a more complex model - and full praise to them. As an example, <span class="citation" data-cites="lai2022">Lai et al. (<a href="#ref-lai2022" role="doc-biblioref">2022</a>)</span> developed a neural architecture to classify Wikipedia comments and Reddit hate speech. The architecture allowed identification of the rationale, communicated through highlights of the relevant words in the text. It looks like a lot of effort, but it avoids deceiving participants. It also looks like a more ecologically valid experimental setup. That would boost my confidence in the results.</p>
<div id="fig-lai_et_al_2022_table_1" class="quarto-float quarto-figure quarto-figure-center anchored">
<figure class="quarto-float quarto-float-fig figure">
<figcaption class="quarto-float-caption-top quarto-float-caption quarto-float-fig" id="fig-lai_et_al_2022_table_1-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;2: <span class="citation" data-cites="lai2022">Lai et al. (<a href="#ref-lai2022" role="doc-biblioref">2022</a>)</span>, Table 1
</figcaption>
<div aria-describedby="fig-lai_et_al_2022_table_1-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<a href="img/the-ai-that-wasnt-deception-in-human-ai-experiments/lai-et-al-2022-table-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-2" title="Figure&nbsp;2: @lai2022, Table 1">{{< img src="img/the-ai-that-wasnt-deception-in-human-ai-experiments/lai-et-al-2022-table-1.png" class="img-fluid figure-img" >}}</a>
</div>
</figure>
</div>
<p>To avoid deception, some researchers get creative. <span class="citation" data-cites="logg2019">Logg et al. (<a href="#ref-logg2019" role="doc-biblioref">2019</a>)</span> wanted to test whether algorithm aversion was due to aversion to algorithms or external advice. They needed to deliver identical predictions to experimental participants (to maintain experimental control) while describing the advice as coming from either an algorithm or a human.</p>
<p>In the first experiment in the paper, 202 participants were asked to estimate the weight of a person in a photo. Everyone received advice, described as coming from either an algorithm or a person. The precise wording was either:</p>
<blockquote class="blockquote">
<p>An algorithm ran calculations based on estimates of participants from a past study. The output that the algorithm computed as an estimate was: 163 pounds.</p>
</blockquote>
<blockquote class="blockquote">
<p>The average estimate of participants from a past experiment was: 163 pounds.</p>
</blockquote>
<p>Both statements are technically true, though calling averaging an algorithm likely creates a gap between technical accuracy and lay interpretation.</p>
<p>The word “algorithm” is stretched even more in Experiment 1C, a task to estimate a person’s attractiveness from another perspective based on a text description. The wording in each condition was:</p>
<blockquote class="blockquote">
<p>An algorithm estimated this (wo)man’s attractiveness (humor/ enjoyableness) from Mike’s (Julia’s) perspective. The algorithm’s estimate was: X</p>
</blockquote>
<blockquote class="blockquote">
<p>In another study, 48 people estimated this (wo)man’s attractiveness (humor/enjoyableness) from Mike’s (Julia’s) perspective. Their estimate was: X</p>
</blockquote>
<p>Again, averaging is the “algorithm”.</p>
<p><span class="citation" data-cites="logg2019">Logg et al. (<a href="#ref-logg2019" role="doc-biblioref">2019</a>)</span> described their choice of procedure as allowing them to avoid deception. I am not convinced, as the word “algorithm” triggers expectations that don’t match reality. If someone told me an algorithm was estimating attractiveness, I would assume something more sophisticated than averaging estimates from humans. I’d likely assume a text analysis model.</p>
<p>One mitigating factor is that this experiment ran pre-ChatGPT in 2019. Participants might not immediately imagine a text analysis algorithm. But in 2026 I’d assume exactly that and would respond based on that assumption. This raises the question: if participants couldn’t picture a text analysis algorithm in 2019, what were they assuming?</p>
<p>Much recent literature actually uses AI, in the form of ChatGPT and other LLMs. It’s finally easy to get an “AI” for almost any task. The deception is fading away, but that comes at the cost of control. I haven’t seen many ChatGPT experiments that tell me something useful about human-AI interaction or that aren’t already outdated on publication. But that’s a topic for a different post.</p>
</section>
<section id="misrepresented-ai" class="level2">
<h2 class="anchored" data-anchor-id="misrepresented-ai">Misrepresented AI</h2>
<p>Although I don’t like it, I understand the appeal of synthetic AI. It’s hard to create tasks where an actual AI does what you claim. For many specific questions, it’s beyond the technical capability of the experimenters.</p>
<p>But the deception isn’t limited to synthetic AI. The AI is often misrepresented.</p>
<p>Here’s an example from <span class="citation" data-cites="rastogi2022">Rastogi et al. (<a href="#ref-rastogi2022" role="doc-biblioref">2022</a>)</span>, who examined whether they could de-anchor experimental participants from AI advice. I <a href="../posts/is-following-ai-advice-anchoring-bias.html">posted about this paper previously</a>. (I should also note I didn’t select the papers in this post because they’re particularly problematic. Rather, they’re papers with interesting ideas that I am familiar with.)</p>
<p>The authors write:</p>
<blockquote class="blockquote">
<p>To induce anchoring bias, the participant was informed at the start of the training section that the AI model was 85% accurate (we carefully chose the training trials to ensure that the AI was indeed 85% accurate over these trials), while the model’s actual accuracy is 70.8% over the entire training set and 66.5% over the test set. Since our goal is to induce anchoring bias and the training time is short, we stated a high AI accuracy.</p>
</blockquote>
<p>The “training trials” shown to participants were not a representative sample of the model’s performance. They were selected so that the 85% claim was true within those training trials. But the model was not 85% accurate over the full training set, where its accuracy was 70.8%. Nor was it that accurate over the test set, where its accuracy was 66.5%.</p>
<p>The gap was even larger in the actual experimental task. The authors included probe trials where they flipped some AI predictions shown to participants. The AI predictions shown to participants in this phase were 58.3% accurate, far below the 85% figure participants had just been given.</p>
<p>So participants were not merely “anchored” by an arbitrary AI recommendation. They were first given a selectively favourable impression of the AI’s reliability, then exposed to a test phase where the AI advice was less reliable.</p>
<p>The authors defend this approach:</p>
<blockquote class="blockquote">
<p>[T]his disparity between stated accuracy (85%) and true accuracy (70.8%) is realistic if there is a distribution shift between the training and the test set, which would imply that the humans’ trust in AI is misplaced.</p>
</blockquote>
<p>But this makes the experiment harder to interpret. The “anchoring” is justified by what participants were told or shown. You can’t study anchoring bias when you’ve deliberately created the conditions for justified trust.</p>
<p>The engineering of deceptive scenarios is a recurring theme across the literature. Here are a few more examples. <span class="citation" data-cites="yin2024">Yin et al. (<a href="#ref-yin2024" role="doc-biblioref">2024</a>)</span> told participants that responses came from either a human or AI, irrespective of the actual source. <span class="citation" data-cites="longoni2023">Longoni et al. (<a href="#ref-longoni2023" role="doc-biblioref">2023</a>)</span> took real news articles on AI failures and substituted either a human or an AI as the cause of the problem. <span class="citation" data-cites="khadpe2020">Khadpe et al. (<a href="#ref-khadpe2020" role="doc-biblioref">2020</a>)</span> used human workers to simulate chatbots, telling participants that these “AI” workers they were interacting with were modelled on a toddler, middle schooler, young student, recent graduate or trained professional.</p>
<p>In each case you’re relying on there being no “smell” to the AI outputs. You’re relying on participants believing your statement even when the evidence in front of them might point elsewhere.</p>
<p>Then there is contamination of the subject pool. Many participants in these studies come from platforms such as Amazon Mechanical Turk, where many workers spend their day doing studies like these. How many times do they read in an experimental debrief that the wool was pulled over their eyes? What does that do to their future interactions? Given that human-computer interaction researchers and experimental economists are fishing in the same stream, practices such as this can impose a negative externality across multiple fields.</p>
<p>I don’t know the answers, but these deceptive practices introduce another layer of doubt as to whether we should trust these results.</p>
</section>
<section id="what-to-do" class="level2">
<h2 class="anchored" data-anchor-id="what-to-do">What to do?</h2>
<p>The human-computer and human-AI interaction literature is shaky. As I noted <a href="../posts/why-i-dont-trust-most-human-ai-interaction-experimental-research.html">elsewhere</a>, experimental practices look like those in psychology circa 2005: small sample sizes, no pre-registration, no data openness. All the hallmarks of a replication crisis.</p>
<p>At the same time, the field is flooded. My Google alerts and literature searches deliver dozens of papers every week, and I’m not catching all of them. Most are trivial, but even when they have an interesting or useful hypothesis, I typically don’t trust them.</p>
<p>On top of this, the literature is accumulating findings from fake AI that may not describe interaction with real AI at all. The findings are useful and generalise only if the deception was successful and the substitute generated the same behaviour as the real thing. Those assumptions are rarely tested.</p>
<p>I don’t have a full solution to these problems, but one starting point is for researchers to slow down. The technical excuse for synthetic AI has weakened, as LLMs make it easier to build a working AI for an experiment. Most of the deception could be eliminated with some thought and work, and we’d get a much more valuable literature.</p>



</section>

<div id="quarto-appendix" class="default"><section class="quarto-appendix-contents" role="doc-bibliography" id="quarto-bibliography"><h2 class="anchored quarto-appendix-heading">References</h2><div id="refs" class="references csl-bib-body hanging-indent" data-entry-spacing="0" data-line-spacing="2" role="list">
<div id="ref-buçinca2021" class="csl-entry" role="listitem">
Buçinca, Z., Malaya, M. B., and Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. <em>Proceedings of the ACM on Human-Computer Interaction</em>, <em>5</em>(CSCW1), 188:1188:21. <a href="https://doi.org/10.1145/3449287">https://doi.org/10.1145/3449287</a>
</div>
<div id="ref-khadpe2020" class="csl-entry" role="listitem">
Khadpe, P., Krishna, R., Fei-Fei, L., Hancock, J. T., and Bernstein, M. S. (2020). Conceptual metaphors impact perceptions of human-AI collaboration. <em>Proceedings of the ACM on Human-Computer Interaction</em>, <em>4</em>(CSCW2), 1–26. <a href="https://doi.org/10.1145/3415234">https://doi.org/10.1145/3415234</a>
</div>
<div id="ref-lai2022" class="csl-entry" role="listitem">
Lai, V., Carton, S., Bhatnagar, R., Liao, Q. V., Zhang, Y., …. (2022). Human-AI collaboration via conditional delegation: A case study of content moderation. <em>arXiv</em>. <a href="https://doi.org/10.48550/arXiv.2204.11788">https://doi.org/10.48550/arXiv.2204.11788</a>
</div>
<div id="ref-logg2019" class="csl-entry" role="listitem">
Logg, J. M., Minson, J. A., and Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. <em>Organizational Behavior and Human Decision Processes</em>, <em>151</em>, 90–103. <a href="https://doi.org/10.1016/j.obhdp.2018.12.005">https://doi.org/10.1016/j.obhdp.2018.12.005</a>
</div>
<div id="ref-longoni2023" class="csl-entry" role="listitem">
Longoni, C., Cian, L., and Kyung, E. J. (2023). Algorithmic transference: People overgeneralize failures of AI in the government. <em>Journal of Marketing Research</em>, <em>60</em>(1), 170–188. <a href="https://doi.org/10.1177/00222437221110139">https://doi.org/10.1177/00222437221110139</a>
</div>
<div id="ref-ortmann2019" class="csl-entry" role="listitem">
Ortmann, A. (2019). <em>Deception</em> (A. Schram and A. Ule, Eds.). Edward Elgar Publishing. <a href="https://china.elgaronline.com/view/edcoll/9781788110556/9781788110556.00009.xml">https://china.elgaronline.com/view/edcoll/9781788110556/9781788110556.00009.xml</a>
</div>
<div id="ref-rastogi2022" class="csl-entry" role="listitem">
Rastogi, C., Zhang, Y., Wei, D., Varshney, K. R., Dhurandhar, A., …. (2022). Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making. <em>Proc. ACM Hum.-Comput. Interact.</em>, <em>6</em>(CSCW1), 83:183:22. <a href="https://doi.org/10.1145/3512930">https://doi.org/10.1145/3512930</a>
</div>
<div id="ref-yin2024" class="csl-entry" role="listitem">
Yin, Y., Jia, N., and Wakslak, C. J. (2024). AI can help people feel heard, but an AI label diminishes this impact. <em>Proceedings of the National Academy of Sciences</em>, <em>121</em>(14), e2319112121. <a href="https://doi.org/10.1073/pnas.2319112121">https://doi.org/10.1073/pnas.2319112121</a>
</div>
</div></section></div>
{{< /html >}}
