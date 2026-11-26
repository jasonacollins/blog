---
title: 'The preregistration halo'
author: "Jason Collins"
date: 2024-01-26 17:00:00+10:00
draft: false
sync_source: "posts/the-preregistration-halo.qmd"
sync_route: "quarto"
sync_hash: "7178f825c32d"
---

{{< html >}}
<p>When we analyse experimental data, we have many choices. What observations do we exclude? What variables do we compare? What statistical tests do we use? And so on. These choices lead us into what is often called the <a href="http://www.stat.columbia.edu/~gelman/research/unpublished/p_hacking.pdf">garden of forking paths</a>.</p>
<p>The problem is that some paths lead to a “significant” result. Hurrah! Publication on the way. Others lead nowhere. So when we read a published paper, you might ask: did they choose their path because it led to a significant result?</p>
<p>One solution to this problem is to <a href="https://en.wikipedia.org/wiki/Preregistration_(science)">preregister</a> the analysis. Specify the analysis before seeing the data.</p>
<p>If preregistration is made public, we can see all research on a topic. We won’t be limited to just the studies authors get published. Preregistration constrains the analysis by making it harder for authors to p-hack or hypothesise their way to a significant result. Or, at least, it makes it transparent that they have done so.</p>
<p>But, preregistration is no guarantee of good science. It doesn’t solve many of the real problems in science (<a href="https://worksinprogress.co/issue/biases-the-wrong-model/">for example</a>). Preregistration can’t rescue weak theory. Many preregistrations remain private. Other preregistrations are left to wither on the vine. Here’s a plot of the status of preregistrations submitted to the <a href="https://www.socialscienceregistry.org">American Economic Association’s RCT registry</a>. The data goes up to 1 January 2024.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb1"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">library</span>(readr)</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="fu">library</span>(ggplot2)</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="fu">library</span>(tidyverse)</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="co"># load data file, which is a subset of the AEA registry to 1 January 2024, available from https://doi.org/10.7910/DVN/HPYPGH</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="co"># code to create subset from the raw csv file as follows, although not executed as part of this document - raw file too large to maintain on website</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a><span class="co"># trials &lt;- read_csv("trials.csv")</span></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a><span class="co">#remove columns not used in this analysis + RCT_ID</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a><span class="co"># trials &lt;- trials %&gt;% </span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a><span class="co">#  select(RCT_ID, "First registered on", "Intervention end date", "End date", Status)</span></span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a><span class="co">#save as cvs named "trials-processed-jan-2024.csv"</span></span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a><span class="co"># write_csv(trials, "trials-subset-jan-2024.csv")</span></span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>trials <span class="ot">&lt;-</span> <span class="fu">read_csv</span>(<span class="st">"data/trials-subset-jan-2024.csv"</span>)</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a><span class="co"># set order for charts so completed is first, then abandoned, then other</span></span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>trials <span class="ot">&lt;-</span> trials <span class="sc">%&gt;%</span></span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>  <span class="fu">rename</span>(</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>    <span class="at">intervention_end_date =</span> <span class="st">"Intervention end date"</span>,</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>    <span class="at">first_registered_on =</span> <span class="st">"First registered on"</span>,</span>
<span id="cb1-25"><a href="#cb1-25" aria-hidden="true" tabindex="-1"></a>    <span class="at">end_date =</span> <span class="st">"End date"</span></span>
<span id="cb1-26"><a href="#cb1-26" aria-hidden="true" tabindex="-1"></a>    ) <span class="sc">%&gt;%</span></span>
<span id="cb1-27"><a href="#cb1-27" aria-hidden="true" tabindex="-1"></a>  <span class="fu">mutate</span>(</span>
<span id="cb1-28"><a href="#cb1-28" aria-hidden="true" tabindex="-1"></a>    <span class="at">first_registered_year =</span> <span class="fu">year</span>(first_registered_on),</span>
<span id="cb1-29"><a href="#cb1-29" aria-hidden="true" tabindex="-1"></a>    <span class="at">intervention_end_year =</span> <span class="fu">year</span>(intervention_end_date),</span>
<span id="cb1-30"><a href="#cb1-30" aria-hidden="true" tabindex="-1"></a>    <span class="at">end_year =</span> <span class="fu">year</span>(end_date)</span>
<span id="cb1-31"><a href="#cb1-31" aria-hidden="true" tabindex="-1"></a>    ) <span class="sc">%&gt;%</span></span>
<span id="cb1-32"><a href="#cb1-32" aria-hidden="true" tabindex="-1"></a>  <span class="fu">mutate</span>(<span class="at">Status =</span> <span class="fu">ifelse</span>(Status <span class="sc">==</span> <span class="st">"abandoned"</span> <span class="sc">|</span> Status <span class="sc">==</span> <span class="st">"withdrawn"</span>, <span class="st">"abandoned_or_withdrawn"</span>, Status)) <span class="sc">%&gt;%</span></span>
<span id="cb1-33"><a href="#cb1-33" aria-hidden="true" tabindex="-1"></a>  <span class="fu">mutate</span>(<span class="at">Status =</span> <span class="fu">factor</span>(Status, <span class="at">levels =</span> <span class="fu">c</span>(<span class="st">"on_going"</span>, <span class="st">"abandoned_or_withdrawn"</span>, <span class="st">"in_development"</span>, <span class="st">"completed"</span>)))</span>
<span id="cb1-34"><a href="#cb1-34" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-35"><a href="#cb1-35" aria-hidden="true" tabindex="-1"></a><span class="co"># colourblind palette</span></span>
<span id="cb1-36"><a href="#cb1-36" aria-hidden="true" tabindex="-1"></a>cbPalette <span class="ot">&lt;-</span> <span class="fu">c</span>(<span class="st">"#999999"</span>, <span class="st">"#E69F00"</span>, <span class="st">"#56B4E9"</span>, <span class="st">"#009E73"</span>, <span class="st">"#F0E442"</span>, <span class="st">"#0072B2"</span>, <span class="st">"#D55E00"</span>, <span class="st">"#CC79A7"</span>)</span>
<span id="cb1-37"><a href="#cb1-37" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-38"><a href="#cb1-38" aria-hidden="true" tabindex="-1"></a><span class="co"># plot of status by year of registration</span></span>
<span id="cb1-39"><a href="#cb1-39" aria-hidden="true" tabindex="-1"></a><span class="fu">ggplot</span>(trials, <span class="fu">aes</span>(<span class="at">fill=</span>Status, <span class="at">x=</span>first_registered_year)) <span class="sc">+</span> </span>
<span id="cb1-40"><a href="#cb1-40" aria-hidden="true" tabindex="-1"></a>  <span class="fu">geom_bar</span>(<span class="at">position=</span><span class="st">"fill"</span>, <span class="at">stat=</span><span class="st">"count"</span>) <span class="sc">+</span> </span>
<span id="cb1-41"><a href="#cb1-41" aria-hidden="true" tabindex="-1"></a>  <span class="fu">scale_x_continuous</span>(<span class="at">limits =</span> <span class="fu">c</span>(<span class="fl">2012.5</span>, <span class="fl">2023.5</span>), <span class="at">breaks =</span> <span class="fu">seq</span>(<span class="dv">2013</span>, <span class="dv">2023</span>)) <span class="sc">+</span></span>
<span id="cb1-42"><a href="#cb1-42" aria-hidden="true" tabindex="-1"></a>  <span class="fu">scale_fill_manual</span>(<span class="at">values=</span>cbPalette) <span class="sc">+</span></span>
<span id="cb1-43"><a href="#cb1-43" aria-hidden="true" tabindex="-1"></a>  <span class="fu">scale_y_continuous</span>(<span class="at">labels =</span> scales<span class="sc">::</span><span class="fu">percent_format</span>()) <span class="sc">+</span></span>
<span id="cb1-44"><a href="#cb1-44" aria-hidden="true" tabindex="-1"></a>  <span class="fu">labs</span>(<span class="at">x =</span> <span class="st">"Year of registration"</span>, <span class="at">y =</span> <span class="st">"Percentage of trials"</span>) <span class="sc">+</span></span>
<span id="cb1-45"><a href="#cb1-45" aria-hidden="true" tabindex="-1"></a>  <span class="fu">theme_minimal</span>()</span></code></pre></div></div>
</details>
<div class="cell-output-display">
<div>
<figure class="figure">
<p><a href="the-preregistration-halo_files/figure-html/unnamed-chunk-1-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-1"><img src="the-preregistration-halo_files/figure-html/unnamed-chunk-1-1.png" class="img-fluid figure-img" width="672"></a></p>
</figure>
</div>
</div>
</div>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb2"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co"># plot of status by reported end year</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="fu">ggplot</span>(trials, <span class="fu">aes</span>(<span class="at">fill=</span>Status, <span class="at">x=</span>end_year)) <span class="sc">+</span> </span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>  <span class="fu">geom_bar</span>(<span class="at">position=</span><span class="st">"fill"</span>, <span class="at">stat=</span><span class="st">"count"</span>) <span class="sc">+</span> </span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a>  <span class="fu">scale_x_continuous</span>(<span class="at">limits =</span> <span class="fu">c</span>(<span class="fl">2012.5</span>, <span class="fl">2025.5</span>), <span class="at">breaks =</span> <span class="fu">seq</span>(<span class="dv">2013</span>, <span class="dv">2025</span>)) <span class="sc">+</span> </span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>  <span class="fu">scale_fill_manual</span>(<span class="at">values=</span>cbPalette) <span class="sc">+</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>  <span class="fu">scale_y_continuous</span>(<span class="at">labels =</span> scales<span class="sc">::</span><span class="fu">percent_format</span>()) <span class="sc">+</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>  <span class="fu">labs</span>(<span class="at">x =</span> <span class="st">"End date"</span>, <span class="at">y =</span> <span class="st">"Percentage of trials"</span>) <span class="sc">+</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>  <span class="fu">theme_minimal</span>()</span></code></pre></div></div>
</details>
<div class="cell-output-display">
<div>
<figure class="figure">
<p><a href="the-preregistration-halo_files/figure-html/unnamed-chunk-2-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-2"><img src="the-preregistration-halo_files/figure-html/unnamed-chunk-2-1.png" class="img-fluid figure-img" width="672"></a></p>
</figure>
</div>
</div>
</div>
<p>The proposed “end date” entered by registrants is likely the best benchmark for when we should see a result. Around half of the trials proposed to end between 2014 and 2019 have been marked as completed. The completion rate declines in more recent years. The registry gives a glimpse of the file drawer, but we see a non-random selection of what’s in it.</p>
<p>Eliot Abrams, Jonathan Libgober and John List <span class="citation" data-cites="abrams2020">(<a href="#ref-abrams2020" role="doc-biblioref">2020</a>)</span> also catalogued some of the issues with the AEA Registry. Over 90% of RCTs don’t register. Only 50% of those who register do so before the intervention begins. And most preregistrations lack detail.</p>
<p>Now to the recent story, via <a href="https://statmodeling.stat.columbia.edu/2023/11/21/of-course-its-preregistered-just-give-me-a-sec/">Jessica Hullman</a></p>
<p>John Protzko and friends <span class="citation" data-cites="protzko2023">(<a href="#ref-protzko2023" role="doc-biblioref">2023</a>)</span> published a paper in Nature Human Behaviour, <em>High replicability of newly discovered social-behavioural findings is achievable</em>. Part of the abstract reads:</p>
<blockquote class="blockquote">
<p>This paper reports an investigation by four coordinated laboratories of the prospective replicability of 16 novel experimental findings using rigour-enhancing practices: confirmatory tests, large sample sizes, preregistration and methodological transparency. In contrast to past systematic replication efforts that reported replication rates averaging 50%, replication attempts here produced the expected effects with significance testing (P &lt; 0.05) in 86% of attempts, slightly exceeding the maximum expected replicability based on observed effect sizes and sample sizes.</p>
</blockquote>
<p>In the text, they note that they preregistered their analyses. We have a preregistered analysis of the benefits of preregistration (or so it seems):</p>
<blockquote class="blockquote">
<p>All confirmatory tests, replications and analyses were preregistered both in the individual studies (Supplementary Information section 3 and Supplementary Table 2) and for this meta-project.</p>
</blockquote>
<p>However, Joseph Bak-Coleman and Berna Devezer <span class="citation" data-cites="bak-coleman2023">(<a href="#ref-bak-coleman2023" role="doc-biblioref">2023</a>)</span> noted there are many forking paths in the analysis. This is particularly the case around the choice of metrics. Those chosen do not match past practice. Bak-Coleman and Devezer note that “preregistration could provide a justification for preferring one metric over another”. However, a problem arises when we look at the preregistration:</p>
<blockquote class="blockquote">
<p>Although the authors claim “All confirmatory tests, replications and analyses were preregistered”, the analysis on which titular claim depends was not preregistered. There is no mention of examining the relationship between replicability and rigor-improving methods, nor even how replicability would be operationalized despite extensive descriptions of the calculations of other quantities. With nothing indicating this comparison or metric it rests on were planned a priori, it is hard to distinguish the core claim in this paper from selective reporting and hypothesizing after the results are known.</p>
</blockquote>
<p>It seems the reviewers didn’t bother to check that the analysis matched the pre-registration.</p>
<p>Protzko and friends are now searching for a preregistration that might match their analysis. An editor’s note now appended to the paper reads:</p>
<blockquote class="blockquote">
<p>Editor’s Note: Readers are alerted that this paper is subject to criticisms that are being considered by the editors. The criticisms relate to the preregistration and corresponding reporting of hypotheses, predictions, and analyses. We are investigating the concerns raised and an editorial response will follow the resolution of these issues.</p>
</blockquote>
<p>Funnily enough, Protzko and friends provide evidence in support of preregistration. We have an analysis with many forking paths. A preregistration might have provided some constraint. Unfortunately, this case for preregistration is not the one that they intended.</p>




<div id="quarto-appendix" class="default"><section class="quarto-appendix-contents" role="doc-bibliography" id="quarto-bibliography"><h2 class="anchored quarto-appendix-heading">References</h2><div id="refs" class="references csl-bib-body hanging-indent" data-entry-spacing="0" data-line-spacing="2" role="list">
<div id="ref-abrams2020" class="csl-entry" role="listitem">
Abrams, E., Libgober, J., and List, J. A. (2020). Research registries: Facts, myths, and possible improvements. <em>NBER Working Paper</em>. <a href="https://doi.org/10.3386/w27250">https://doi.org/10.3386/w27250</a>
</div>
<div id="ref-bak-coleman2023" class="csl-entry" role="listitem">
Bak-Coleman, J., and Devezer, B. (2023). <em>Causal claims about scientific rigor require rigorous causal evidence.</em> <a href="https://doi.org/10.31234/osf.io/5u3kj">https://doi.org/10.31234/osf.io/5u3kj</a>
</div>
<div id="ref-protzko2023" class="csl-entry" role="listitem">
Protzko, J., Krosnick, J., Nelson, L., Nosek, B. A., Axt, J., … Schooler, J. W. (2023). High replicability of newly discovered social-behavioural findings is achievable. <em>Nature Human Behaviour</em>, 1–9. <a href="https://doi.org/10.1038/s41562-023-01749-9">https://doi.org/10.1038/s41562-023-01749-9</a>
</div>
</div></section></div>
{{< /html >}}
