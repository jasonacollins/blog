---
title: "The psychological and genes' eye view of ergodicity economics"
author: "Jason Collins"
date: 2024-07-08 20:00:00+10:00
draft: false
sync_source: "posts/the-psychological-and-genes-eye-view-of-ergodicity-economics.qmd"
sync_route: "quarto"
sync_hash: "7518273dc3c0"
---

{{< html >}}
<p>This post was my plan for a presentation at the <a href="https://www.furconference.org/fur-2024/">Foundation of Utility and Risk Conference</a>. I drew on my previous posts laying out the <a href="../posts/ergodicity-economics-a-primer.html">foundations of ergodicity economics</a> and examining <a href="../posts/risk-and-loss-aversion-in-ergodicity-economics.html">what ergodicity economics states about risk preferences</a>. This varied somewhat from delivery (I’m easily waylaid and skipped a couple of sections). Given it’s to a technical audience, there are a few moments that might lose the lay reader.</p>
<p>–</p>
<section id="introduction" class="level2">
<h2 class="anchored" data-anchor-id="introduction">Introduction</h2>
<p>This presentation started with a blog post. Around five years ago when I was ensconced in the corporate world, I wrote a couple of posts on an idea called ergodicity economics. A random physicist, <a href="https://x.com/ole_b_peters">Ole Peters</a>, was riling people up on twitter about how economists were doing it wrong, how expected utility theory was fatally flawed, how you don’t need to introduce psychology to explain human decisions under risk, and how all the anomalies in behavioural economics could be reconciled with his new theory.</p>
<p>There were plenty of people countering the stronger statements, but I thought that by writing a post or two I could understand the idea better myself. So I ignored the hyperbole and tried to give a fair hearing to the underlying idea. Since I had some background in evolutionary biology, I also tried to view it from an evolutionary lens.</p>
<p>In the spirit of those original posts, I am going to avoid today’s presentation from becoming an exercise in attacking the most outlandish statements. There are a couple of published critiques of ergodicity economics, one by Jason Doctor et al <span class="citation" data-cites="doctor2020">(<a href="#ref-doctor2020" role="doc-biblioref">2020</a>)</span> in Nature Physics and one more recent by Matthew Ford and John Kay <span class="citation" data-cites="ford2023">(<a href="#ref-ford2023" role="doc-biblioref">2023</a>)</span> in Econ Journal Watch that do a good job of addressing the claims about economics and expected utility theory. Instead, I’m going to give a flat description of ergodicity economics, before laying out some psychological and evolutionary observations.</p>
<section id="the-bet" class="level3">
<h3 class="anchored" data-anchor-id="the-bet">The bet</h3>
<p>So let me start with the classic example used to illustrate what ergodicity economics is about. You may have seen this before.</p>
<blockquote class="blockquote">
<p>Suppose you are offered a series of 100 bets on the flip of a coin. You win 50% of your wealth on heads. You lose 40% of your wealth on tails. Do you take the bet?</p>
</blockquote>
<p>The expected value of the bet is 5% of your wealth each flip. Continue playing for many rounds and your expected wealth is very large.</p>
<p>However, what is the most probable outcome over many repeats of this bet?</p>
<p>This plot is the result of a simulation of 10,000 people, each starting with $100, experiencing the 100 flips. The black line is the average wealth of the population. The red lines are paths of the first 20 people in the simulation.</p>
<div class="cell">
<details class="code-fold">
<summary>Setup code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb1"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Load the required packages</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="fu">library</span>(ggplot2)</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="fu">library</span>(scales) <span class="co">#use the percent scale later</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="fu">library</span>(dplyr) <span class="co">#use the filter function later</span></span></code></pre></div></div>
</details>
</div>
<div class="cell">
<details class="code-fold">
<summary>Code for bet function</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb2"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Create a function for running of the bets.</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a>bet <span class="ot">&lt;-</span> <span class="cf">function</span>(p, n, t, <span class="at">start=</span><span class="dv">100</span>, gain, loss, <span class="at">ergodic=</span><span class="cn">FALSE</span>, <span class="at">absorbing=</span><span class="cn">FALSE</span>){</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a>  <span class="co">#p is probability of a gain</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a>  <span class="co">#n is how many people in the simulation</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a>  <span class="co">#t is the number of coin flips simulated for each person</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a>  <span class="co">#start is the number of dollars each person starts with</span></span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a>  <span class="co">#if ergodic=FALSE, gain and loss are the multipliers</span></span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a>  <span class="co">#if ergodic=TRUE, gain and loss are the dollar amounts</span></span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a>  <span class="co">#if absorbing=TRUE, zero wealth ends the series of flips for that person</span></span>
<span id="cb2-12"><a href="#cb2-12" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-13"><a href="#cb2-13" aria-hidden="true" tabindex="-1"></a>  params <span class="ot">&lt;-</span> <span class="fu">as.data.frame</span>(<span class="fu">c</span>(p, n, t, start, gain, loss, ergodic, absorbing))</span>
<span id="cb2-14"><a href="#cb2-14" aria-hidden="true" tabindex="-1"></a>  <span class="fu">rownames</span>(params) <span class="ot">&lt;-</span> <span class="fu">c</span>(<span class="st">"p"</span>, <span class="st">"n"</span>, <span class="st">"t"</span>, <span class="st">"start"</span>, <span class="st">"gain"</span>, <span class="st">"loss"</span>, <span class="st">"ergodic"</span>, <span class="st">"absorbing"</span>)</span>
<span id="cb2-15"><a href="#cb2-15" aria-hidden="true" tabindex="-1"></a>  <span class="fu">colnames</span>(params) <span class="ot">&lt;-</span> <span class="st">"value"</span></span>
<span id="cb2-16"><a href="#cb2-16" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-17"><a href="#cb2-17" aria-hidden="true" tabindex="-1"></a>  sim <span class="ot">&lt;-</span> <span class="fu">matrix</span>(<span class="at">data =</span> <span class="cn">NA</span>, <span class="at">nrow =</span> t, <span class="at">ncol =</span> n)</span>
<span id="cb2-18"><a href="#cb2-18" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-19"><a href="#cb2-19" aria-hidden="true" tabindex="-1"></a>  <span class="cf">if</span>(ergodic<span class="sc">==</span><span class="cn">FALSE</span>){</span>
<span id="cb2-20"><a href="#cb2-20" aria-hidden="true" tabindex="-1"></a>    <span class="cf">for</span> (j <span class="cf">in</span> <span class="dv">1</span><span class="sc">:</span>n) {</span>
<span id="cb2-21"><a href="#cb2-21" aria-hidden="true" tabindex="-1"></a>      x <span class="ot">&lt;-</span> start</span>
<span id="cb2-22"><a href="#cb2-22" aria-hidden="true" tabindex="-1"></a>      <span class="cf">for</span> (i <span class="cf">in</span> <span class="dv">1</span><span class="sc">:</span>t) {</span>
<span id="cb2-23"><a href="#cb2-23" aria-hidden="true" tabindex="-1"></a>      outcome <span class="ot">&lt;-</span> <span class="fu">rbinom</span>(<span class="at">n=</span><span class="dv">1</span>, <span class="at">size=</span><span class="dv">1</span>, <span class="at">prob=</span>p)</span>
<span id="cb2-24"><a href="#cb2-24" aria-hidden="true" tabindex="-1"></a>      <span class="fu">ifelse</span>(outcome<span class="sc">==</span><span class="dv">0</span>, x <span class="ot">&lt;-</span> x<span class="sc">*</span>loss, x <span class="ot">&lt;-</span> x<span class="sc">*</span>gain)</span>
<span id="cb2-25"><a href="#cb2-25" aria-hidden="true" tabindex="-1"></a>      sim[i,j] <span class="ot">&lt;-</span> x</span>
<span id="cb2-26"><a href="#cb2-26" aria-hidden="true" tabindex="-1"></a>      }</span>
<span id="cb2-27"><a href="#cb2-27" aria-hidden="true" tabindex="-1"></a>    }</span>
<span id="cb2-28"><a href="#cb2-28" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb2-29"><a href="#cb2-29" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-30"><a href="#cb2-30" aria-hidden="true" tabindex="-1"></a> <span class="cf">if</span>(ergodic<span class="sc">==</span><span class="cn">TRUE</span>){</span>
<span id="cb2-31"><a href="#cb2-31" aria-hidden="true" tabindex="-1"></a>    <span class="cf">for</span> (j <span class="cf">in</span> <span class="dv">1</span><span class="sc">:</span>n) {</span>
<span id="cb2-32"><a href="#cb2-32" aria-hidden="true" tabindex="-1"></a>      x <span class="ot">&lt;-</span> start </span>
<span id="cb2-33"><a href="#cb2-33" aria-hidden="true" tabindex="-1"></a>      <span class="cf">for</span> (i <span class="cf">in</span> <span class="dv">1</span><span class="sc">:</span>t) {</span>
<span id="cb2-34"><a href="#cb2-34" aria-hidden="true" tabindex="-1"></a>      outcome <span class="ot">&lt;-</span> <span class="fu">rbinom</span>(<span class="at">n=</span><span class="dv">1</span>, <span class="at">size=</span><span class="dv">1</span>, <span class="at">prob=</span>p)</span>
<span id="cb2-35"><a href="#cb2-35" aria-hidden="true" tabindex="-1"></a>      <span class="fu">ifelse</span>(outcome<span class="sc">==</span><span class="dv">0</span>, x <span class="ot">&lt;-</span> x<span class="sc">-</span>loss, x <span class="ot">&lt;-</span> x<span class="sc">+</span>gain)</span>
<span id="cb2-36"><a href="#cb2-36" aria-hidden="true" tabindex="-1"></a>      sim[i,j] <span class="ot">&lt;-</span> x</span>
<span id="cb2-37"><a href="#cb2-37" aria-hidden="true" tabindex="-1"></a>      <span class="cf">if</span>(absorbing<span class="sc">==</span><span class="cn">TRUE</span>){</span>
<span id="cb2-38"><a href="#cb2-38" aria-hidden="true" tabindex="-1"></a>        <span class="cf">if</span>(x<span class="sc">&lt;</span><span class="dv">0</span>){</span>
<span id="cb2-39"><a href="#cb2-39" aria-hidden="true" tabindex="-1"></a>          sim[i<span class="sc">:</span>t,j] <span class="ot">&lt;-</span> <span class="dv">0</span></span>
<span id="cb2-40"><a href="#cb2-40" aria-hidden="true" tabindex="-1"></a>            <span class="cf">break</span></span>
<span id="cb2-41"><a href="#cb2-41" aria-hidden="true" tabindex="-1"></a>        }</span>
<span id="cb2-42"><a href="#cb2-42" aria-hidden="true" tabindex="-1"></a>        }</span>
<span id="cb2-43"><a href="#cb2-43" aria-hidden="true" tabindex="-1"></a>      }</span>
<span id="cb2-44"><a href="#cb2-44" aria-hidden="true" tabindex="-1"></a>    }</span>
<span id="cb2-45"><a href="#cb2-45" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb2-46"><a href="#cb2-46" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-47"><a href="#cb2-47" aria-hidden="true" tabindex="-1"></a>  sim <span class="ot">&lt;-</span> <span class="fu">rbind</span>(<span class="fu">rep</span>(start,n), sim) <span class="co">#placing the starting sum in the first row</span></span>
<span id="cb2-48"><a href="#cb2-48" aria-hidden="true" tabindex="-1"></a>  sim <span class="ot">&lt;-</span> <span class="fu">cbind</span>(<span class="fu">seq</span>(<span class="dv">0</span>,t), sim) <span class="co">#number each period</span></span>
<span id="cb2-49"><a href="#cb2-49" aria-hidden="true" tabindex="-1"></a>  sim <span class="ot">&lt;-</span> <span class="fu">data.frame</span>(sim)</span>
<span id="cb2-50"><a href="#cb2-50" aria-hidden="true" tabindex="-1"></a>  <span class="fu">colnames</span>(sim) <span class="ot">&lt;-</span> <span class="fu">c</span>(<span class="st">"period"</span>, <span class="fu">paste0</span>(<span class="st">"p"</span>, <span class="dv">1</span><span class="sc">:</span>n))</span>
<span id="cb2-51"><a href="#cb2-51" aria-hidden="true" tabindex="-1"></a>  sim <span class="ot">&lt;-</span> <span class="fu">list</span>(<span class="at">params=</span>params, <span class="at">sim=</span>sim)</span>
<span id="cb2-52"><a href="#cb2-52" aria-hidden="true" tabindex="-1"></a>  sim</span>
<span id="cb2-53"><a href="#cb2-53" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></div>
</details>
</div>
<div class="cell">
<details class="code-fold">
<summary>Code to run simulation</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb3"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Simulate 10,000 people who accept a series of 1000 50:50 bets to win \$50 or lose \$40 from a starting wealth of \$100.</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="fu">set.seed</span>(<span class="dv">20240705</span>)</span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a>nonErgodic <span class="ot">&lt;-</span> <span class="fu">bet</span>(<span class="at">p=</span><span class="fl">0.5</span>, <span class="at">n=</span><span class="dv">10000</span>, <span class="at">t=</span><span class="dv">1000</span>, <span class="at">gain=</span><span class="fl">1.5</span>, <span class="at">loss=</span><span class="fl">0.6</span>, <span class="at">ergodic=</span><span class="cn">FALSE</span>)</span></code></pre></div></div>
</details>
</div>
<div class="cell">
<details class="code-fold">
<summary>Code for plot</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb4"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Function to plot individual paths and average wealth over a set number of periods.</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>plotWealth <span class="ot">&lt;-</span> <span class="cf">function</span>(sim, <span class="at">t =</span> <span class="dv">100</span>, <span class="at">people =</span> <span class="cn">NULL</span>) {</span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>  basePlot <span class="ot">&lt;-</span> <span class="fu">ggplot</span>(sim<span class="sc">$</span>sim[<span class="dv">1</span><span class="sc">:</span>(t<span class="sc">+</span><span class="dv">1</span>),], <span class="fu">aes</span>(<span class="at">x =</span> period)) <span class="sc">+</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>    <span class="fu">labs</span>(<span class="at">y =</span> <span class="st">"Wealth ($)"</span>)</span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Add lines for individual paths if specified</span></span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>  <span class="cf">if</span> (<span class="sc">!</span><span class="fu">is.null</span>(people)) {</span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a>    <span class="cf">for</span> (i <span class="cf">in</span> <span class="dv">1</span><span class="sc">:</span>people) {</span>
<span id="cb4-9"><a href="#cb4-9" aria-hidden="true" tabindex="-1"></a>      basePlot <span class="ot">&lt;-</span> basePlot <span class="sc">+</span></span>
<span id="cb4-10"><a href="#cb4-10" aria-hidden="true" tabindex="-1"></a>        <span class="fu">geom_line</span>(<span class="fu">aes</span>(<span class="at">y =</span> <span class="sc">!!</span>sim<span class="sc">$</span>sim[<span class="fu">c</span>(<span class="dv">1</span><span class="sc">:</span>(t<span class="sc">+</span><span class="dv">1</span>)), i<span class="sc">+</span><span class="dv">1</span>]), <span class="at">color =</span> <span class="st">"red"</span>)</span>
<span id="cb4-11"><a href="#cb4-11" aria-hidden="true" tabindex="-1"></a>    }</span>
<span id="cb4-12"><a href="#cb4-12" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb4-13"><a href="#cb4-13" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-14"><a href="#cb4-14" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Add line for average wealth</span></span>
<span id="cb4-15"><a href="#cb4-15" aria-hidden="true" tabindex="-1"></a>  basePlot <span class="ot">&lt;-</span> basePlot <span class="sc">+</span></span>
<span id="cb4-16"><a href="#cb4-16" aria-hidden="true" tabindex="-1"></a>    <span class="fu">geom_line</span>(<span class="fu">aes</span>(<span class="at">y =</span> <span class="fu">rowMeans</span>(sim<span class="sc">$</span>sim[<span class="dv">1</span><span class="sc">:</span>(t<span class="sc">+</span><span class="dv">1</span>), <span class="dv">2</span><span class="sc">:</span>(sim<span class="sc">$</span>params[<span class="dv">2</span>,]<span class="sc">+</span><span class="dv">1</span>)])), <span class="at">color =</span> <span class="st">"black"</span>, <span class="at">linewidth =</span> <span class="dv">1</span>)</span>
<span id="cb4-17"><a href="#cb4-17" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb4-18"><a href="#cb4-18" aria-hidden="true" tabindex="-1"></a>  basePlot</span>
<span id="cb4-19"><a href="#cb4-19" aria-hidden="true" tabindex="-1"></a>}</span>
<span id="cb4-20"><a href="#cb4-20" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-21"><a href="#cb4-21" aria-hidden="true" tabindex="-1"></a><span class="co"># Generate the plot with individual paths and average wealth</span></span>
<span id="cb4-22"><a href="#cb4-22" aria-hidden="true" tabindex="-1"></a>nonErgodicPlot <span class="ot">&lt;-</span> <span class="fu">plotWealth</span>(<span class="at">sim =</span> nonErgodic, <span class="at">t =</span> <span class="dv">100</span>, <span class="at">people =</span> <span class="dv">20</span>)</span>
<span id="cb4-23"><a href="#cb4-23" aria-hidden="true" tabindex="-1"></a>nonErgodicPlot</span></code></pre></div></div>
</details>
<div class="cell-output-display">
<div id="fig-ergodicity-presentation-1" class="quarto-float quarto-figure quarto-figure-center anchored">
<figure class="quarto-float quarto-float-fig figure">
<figcaption class="quarto-float-caption-top quarto-float-caption quarto-float-fig" id="fig-ergodicity-presentation-1-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;1: Plot of first 20 people against average wealth
</figcaption>
<div aria-describedby="fig-ergodicity-presentation-1-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<a href="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-1-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-1" title="Figure&nbsp;1: Plot of first 20 people against average wealth"><img src="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-1-1.png" class="img-fluid figure-img" width="672"></a>
</div>
</figure>
</div>
</div>
</div>
<p>The sudden drop in mean wealth toward the end of the sequence is an interesting feature that I will ignore for the moment. But look at the red lines. At the end of 100 periods, all are below the mean wealth, and only one of the 20 agents has enough wealth at the end that you can discern the line from the x-axis.</p>
<p>Let us now use a log scale to enable us to see the pattern more clearly.</p>
<div class="cell">
<details class="code-fold">
<summary>Code for log plot</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb5"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Plot both the average outcome and first twenty people on the same plot.</span></span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a>logNonErgodicPlot <span class="ot">&lt;-</span> <span class="fu">plotWealth</span>(<span class="at">sim=</span>nonErgodic, <span class="at">t=</span><span class="dv">100</span>, <span class="at">people=</span><span class="dv">20</span>)<span class="sc">+</span></span>
<span id="cb5-4"><a href="#cb5-4" aria-hidden="true" tabindex="-1"></a>    <span class="fu">scale_y_log10</span>(<span class="at">breaks =</span> <span class="fu">c</span>(<span class="fl">0.0001</span>, <span class="fl">0.1</span>, <span class="dv">100</span>, <span class="dv">100000</span>), <span class="at">labels =</span> <span class="fu">c</span>(<span class="st">"0.0001"</span>, <span class="st">"0.1"</span>, <span class="st">"100"</span>, <span class="st">"100000"</span>))</span>
<span id="cb5-5"><a href="#cb5-5" aria-hidden="true" tabindex="-1"></a>logNonErgodicPlot</span></code></pre></div></div>
</details>
<div class="cell-output-display">
<div id="fig-ergodicity-presentation-2" class="quarto-float quarto-figure quarto-figure-center anchored">
<figure class="quarto-float quarto-float-fig figure">
<figcaption class="quarto-float-caption-top quarto-float-caption quarto-float-fig" id="fig-ergodicity-presentation-2-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;2: Plot of first 20 people against average wealth (log scale)
</figcaption>
<div aria-describedby="fig-ergodicity-presentation-2-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<a href="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-2-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-2" title="Figure&nbsp;2: Plot of first 20 people against average wealth (log scale)"><img src="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-2-1.png" class="img-fluid figure-img" width="672"></a>
</div>
</figure>
</div>
</div>
</div>
<p>All 20 of these people are below the mean wealth. Only one is ahead of where they started.</p>
<div class="cell">
<details class="code-fold">
<summary>Code to create function to generate summary statistics</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb6"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Create a function to generate summary statistics.</span></span>
<span id="cb6-2"><a href="#cb6-2" aria-hidden="true" tabindex="-1"></a>summaryStats <span class="ot">&lt;-</span> <span class="cf">function</span>(sim, <span class="at">t =</span> <span class="dv">100</span>) {</span>
<span id="cb6-3"><a href="#cb6-3" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb6-4"><a href="#cb6-4" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Extract the wealth data for the specified time</span></span>
<span id="cb6-5"><a href="#cb6-5" aria-hidden="true" tabindex="-1"></a>  wealth_data <span class="ot">&lt;-</span> <span class="fu">as.matrix</span>(sim<span class="sc">$</span>sim[(t <span class="sc">+</span> <span class="dv">1</span>), <span class="dv">2</span><span class="sc">:</span>(sim<span class="sc">$</span>params[<span class="dv">2</span>, ] <span class="sc">+</span> <span class="dv">1</span>)])</span>
<span id="cb6-6"><a href="#cb6-6" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb6-7"><a href="#cb6-7" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Calculate mean wealth</span></span>
<span id="cb6-8"><a href="#cb6-8" aria-hidden="true" tabindex="-1"></a>  mean_wealth <span class="ot">&lt;-</span> <span class="fu">mean</span>(wealth_data)</span>
<span id="cb6-9"><a href="#cb6-9" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb6-10"><a href="#cb6-10" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Calculate median wealth</span></span>
<span id="cb6-11"><a href="#cb6-11" aria-hidden="true" tabindex="-1"></a>  median_wealth <span class="ot">&lt;-</span> <span class="fu">median</span>(wealth_data)</span>
<span id="cb6-12"><a href="#cb6-12" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb6-13"><a href="#cb6-13" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Number and percentage who lost more than 99% of their wealth</span></span>
<span id="cb6-14"><a href="#cb6-14" aria-hidden="true" tabindex="-1"></a>  num_lost_99 <span class="ot">&lt;-</span> <span class="fu">sum</span>(wealth_data <span class="sc">&lt;</span> (sim<span class="sc">$</span>params[<span class="dv">4</span>, ] <span class="sc">/</span> <span class="dv">100</span>))</span>
<span id="cb6-15"><a href="#cb6-15" aria-hidden="true" tabindex="-1"></a>  perc_lost_99 <span class="ot">&lt;-</span> (num_lost_99 <span class="sc">/</span> sim<span class="sc">$</span>params[<span class="dv">2</span>, ]) <span class="sc">*</span> <span class="dv">100</span></span>
<span id="cb6-16"><a href="#cb6-16" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb6-17"><a href="#cb6-17" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Number and percentage who gained wealth</span></span>
<span id="cb6-18"><a href="#cb6-18" aria-hidden="true" tabindex="-1"></a>  num_gain <span class="ot">&lt;-</span> <span class="fu">sum</span>(wealth_data <span class="sc">&gt;</span> sim<span class="sc">$</span>params[<span class="dv">4</span>, ])</span>
<span id="cb6-19"><a href="#cb6-19" aria-hidden="true" tabindex="-1"></a>  perc_gain <span class="ot">&lt;-</span> (num_gain <span class="sc">/</span> sim<span class="sc">$</span>params[<span class="dv">2</span>, ]) <span class="sc">*</span> <span class="dv">100</span></span>
<span id="cb6-20"><a href="#cb6-20" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb6-21"><a href="#cb6-21" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Number who increased their wealth more than 100-fold</span></span>
<span id="cb6-22"><a href="#cb6-22" aria-hidden="true" tabindex="-1"></a>  num_increased_100 <span class="ot">&lt;-</span> <span class="fu">sum</span>(wealth_data <span class="sc">&gt;</span> (sim<span class="sc">$</span>params[<span class="dv">4</span>, ] <span class="sc">*</span> <span class="dv">100</span>))</span>
<span id="cb6-23"><a href="#cb6-23" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb6-24"><a href="#cb6-24" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Wealth and wealth share of the wealthiest person</span></span>
<span id="cb6-25"><a href="#cb6-25" aria-hidden="true" tabindex="-1"></a>  max_wealth <span class="ot">&lt;-</span> <span class="fu">max</span>(wealth_data)</span>
<span id="cb6-26"><a href="#cb6-26" aria-hidden="true" tabindex="-1"></a>  perc_max_wealth_share <span class="ot">&lt;-</span> max_wealth <span class="sc">/</span> <span class="fu">sum</span>(wealth_data) <span class="sc">*</span> <span class="dv">100</span></span>
<span id="cb6-27"><a href="#cb6-27" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb6-28"><a href="#cb6-28" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Combine all statistics into a data frame</span></span>
<span id="cb6-29"><a href="#cb6-29" aria-hidden="true" tabindex="-1"></a>  stats <span class="ot">&lt;-</span> <span class="fu">data.frame</span>(</span>
<span id="cb6-30"><a href="#cb6-30" aria-hidden="true" tabindex="-1"></a>    <span class="at">mean_wealth =</span> mean_wealth,</span>
<span id="cb6-31"><a href="#cb6-31" aria-hidden="true" tabindex="-1"></a>    <span class="at">median_wealth =</span> median_wealth,</span>
<span id="cb6-32"><a href="#cb6-32" aria-hidden="true" tabindex="-1"></a>    <span class="at">num_lost_99 =</span> num_lost_99,</span>
<span id="cb6-33"><a href="#cb6-33" aria-hidden="true" tabindex="-1"></a>    <span class="at">perc_lost_99 =</span> perc_lost_99,</span>
<span id="cb6-34"><a href="#cb6-34" aria-hidden="true" tabindex="-1"></a>    <span class="at">num_gain =</span> num_gain,</span>
<span id="cb6-35"><a href="#cb6-35" aria-hidden="true" tabindex="-1"></a>    <span class="at">perc_gain =</span> perc_gain,</span>
<span id="cb6-36"><a href="#cb6-36" aria-hidden="true" tabindex="-1"></a>    <span class="at">num_increased_100 =</span> num_increased_100,</span>
<span id="cb6-37"><a href="#cb6-37" aria-hidden="true" tabindex="-1"></a>    <span class="at">max_wealth =</span> max_wealth,</span>
<span id="cb6-38"><a href="#cb6-38" aria-hidden="true" tabindex="-1"></a>    <span class="at">perc_max_wealth_share =</span> perc_max_wealth_share</span>
<span id="cb6-39"><a href="#cb6-39" aria-hidden="true" tabindex="-1"></a>  )</span>
<span id="cb6-40"><a href="#cb6-40" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb6-41"><a href="#cb6-41" aria-hidden="true" tabindex="-1"></a>  <span class="fu">return</span>(stats)</span>
<span id="cb6-42"><a href="#cb6-42" aria-hidden="true" tabindex="-1"></a>}</span>
<span id="cb6-43"><a href="#cb6-43" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb6-44"><a href="#cb6-44" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb6-45"><a href="#cb6-45" aria-hidden="true" tabindex="-1"></a>nonErgodicStats <span class="ot">&lt;-</span> <span class="fu">summaryStats</span>(nonErgodic, <span class="dv">100</span>)</span></code></pre></div></div>
</details>
</div>
<p>These 20 people are representative of the broader population. Across the 10,000 agents in this simulation, 86 per cent lost money. The mean wealth was $22303, but the median wealth was $0.52.</p>
<p>What is the intuition behind this?</p>
<p>The black line reflects the expected gain of 5% per flip.</p>
<p>But for the red lines, over the long term, an individual will tend to get around half heads and half tails. As the number of flips goes to infinity, the proportion of heads or tails “<a href="https://en.wikipedia.org/wiki/Almost_surely">almost surely</a>” converges to 0.5. This means that each person will tend to get a 50% increase half the time (or 1.5 times the initial wealth), and a 40% decrease half the time (60% of the initial wealth). The time average growth in wealth for an individual is {{< math >}}(1.5\times 0.6)^{0.5} \sim 0.95{{< /math >}}, or approximately a 5% decline in wealth each period. Every individual’s wealth will tend to decay at that rate. The black line is held up by a very lucky few.</p>
<p>A system where the time average converges to the ensemble average (our population mean) is known as an ergodic system. The sequence of gambles I have just shown you is non-ergodic as the time average and the ensemble average diverge. (I’ll ignore the finer debates about whether this problem even involves ergodicity to the side.)</p>
<p>This leads to the following claim: as we cannot individually experience the ensemble average, the ensemble average is not what humans consider in their decision making. Instead, people maximise the time average growth rate of wealth. For this bet, as the time average growth rate is negative, an ergodicity economics agent would reject the bet.</p>
<p>Contrast this with the expected utility approach, where the utility of each outcome is weighted by its probability and summed to give the expected utility. Expected utility theory would be consistent with both accepting and rejecting the bet depending on the particular utility function.</p>
<p>There is, however, an incidental alignment between ergodicity economics and expected utility theory. If a person has log utility - that is, they maximise the probability-weighted logarithm of the possible outcomes - they will maximise the time average growth rate.</p>
</section>
<section id="additive-versus-multiplicative" class="level3">
<h3 class="anchored" data-anchor-id="additive-versus-multiplicative">Additive versus multiplicative</h3>
<p>One important feature of the bet I have just shown is that the outcomes are multiplicative. A win on one flip leads to a larger stake flip on the next bet. The size of the bet scales up or down with wealth.</p>
<p>What if I offered you the following bet instead?</p>
<blockquote class="blockquote">
<p>You have $100 and are offered a gamble involving a series of 100 coin flips. For each flip, heads will increase your wealth by $50. Tails will decrease it by $40. Do you take the bet?</p>
</blockquote>
<p>You can see the tweak from the original bet, with dollar sums rather than percentages. For someone with $100 in wealth, the first flip is effectively identical, but future bets will be additive on that result and always involve the same shift of $50 up or $40 down.</p>
<p>This second series of flips is ergodic. The expected value of each flip is $5 ({{< math >}}0.5\times \$50-0.5\times \$40=\$5{{< /math >}}). The time-average growth rate is also $5.</p>
<p>Let’s simulate as we did for multiplicative bets, with 10,000 people starting with $100 and flipping the coin 100 times. This plot shows the average wealth of the population, together with the paths of the first 20 of the 10,000 people (in red).</p>
<div class="cell">
<details class="code-fold">
<summary>Code to simulate ergodic environment</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb7"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Simulate 10,000 people who accept a series of 1000 50:50 bets to win \$50 or lose \$40 from a starting wealth of \$100.</span></span>
<span id="cb7-2"><a href="#cb7-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb7-3"><a href="#cb7-3" aria-hidden="true" tabindex="-1"></a><span class="fu">set.seed</span>(<span class="dv">20240705</span>)</span>
<span id="cb7-4"><a href="#cb7-4" aria-hidden="true" tabindex="-1"></a>ergodic <span class="ot">&lt;-</span> <span class="fu">bet</span>(<span class="at">p=</span><span class="fl">0.5</span>, <span class="at">n=</span><span class="dv">10000</span>, <span class="at">t=</span><span class="dv">100</span>, <span class="at">gain=</span><span class="dv">50</span>, <span class="at">loss=</span><span class="dv">40</span>, <span class="at">ergodic=</span><span class="cn">TRUE</span>, <span class="at">absorbing=</span><span class="cn">FALSE</span>)</span></code></pre></div></div>
</details>
</div>
<div class="cell">
<details class="code-fold">
<summary>Code to plot ergodic simulation</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb8"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Plot both the average outcome and first twenty people on the same plot.</span></span>
<span id="cb8-2"><a href="#cb8-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb8-3"><a href="#cb8-3" aria-hidden="true" tabindex="-1"></a>ergodicPlot <span class="ot">&lt;-</span> <span class="fu">plotWealth</span>(<span class="at">sim=</span>ergodic, <span class="at">t=</span><span class="dv">100</span>, <span class="at">people=</span><span class="dv">20</span>)</span>
<span id="cb8-4"><a href="#cb8-4" aria-hidden="true" tabindex="-1"></a>ergodicPlot</span></code></pre></div></div>
</details>
<div class="cell-output-display">
<div id="fig-ergodicity-presentation-3" class="quarto-float quarto-figure quarto-figure-center anchored">
<figure class="quarto-float quarto-float-fig figure">
<figcaption class="quarto-float-caption-top quarto-float-caption quarto-float-fig" id="fig-ergodicity-presentation-3-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;3: Average wealth of population and path of first 20 people
</figcaption>
<div aria-describedby="fig-ergodicity-presentation-3-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<a href="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-3-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-3" title="Figure&nbsp;3: Average wealth of population and path of first 20 people"><img src="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-3-1.png" class="img-fluid figure-img" width="672"></a>
</div>
</figure>
</div>
</div>
</div>
<div class="cell">
<details class="code-fold">
<summary>Code to generate ergodic summary statistics</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb9"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb9-1"><a href="#cb9-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Generate summary statistics for the population and wealthiest person after 100 and 1000 flips}</span></span>
<span id="cb9-2"><a href="#cb9-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb9-3"><a href="#cb9-3" aria-hidden="true" tabindex="-1"></a>summaryErgodic100 <span class="ot">&lt;-</span> <span class="fu">summaryStats</span>(<span class="at">sim=</span>ergodic, <span class="at">t=</span><span class="dv">100</span>)</span></code></pre></div></div>
</details>
</div>
<p>The individual growth paths cluster on either side of the population average. After 100 flips, the mean wealth is $602 and the median $600. 87% of the population has gained in wealth. This alignment between the mean and median wealth, and the relatively equal distribution of wealth, are characteristic of an ergodic system.</p>
<div class="cell">
<details class="code-fold">
<summary>Code to calculate number with zero wealth</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb10"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb10-1"><a href="#cb10-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Determine how many people (in the first people out of n) experienced zero wealth or less during the simulation.</span></span>
<span id="cb10-2"><a href="#cb10-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb10-3"><a href="#cb10-3" aria-hidden="true" tabindex="-1"></a>numZero <span class="ot">&lt;-</span> <span class="cf">function</span>(sim, t, <span class="at">subset=</span><span class="dv">0</span>){</span>
<span id="cb10-4"><a href="#cb10-4" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb10-5"><a href="#cb10-5" aria-hidden="true" tabindex="-1"></a>  <span class="co">#subset</span></span>
<span id="cb10-6"><a href="#cb10-6" aria-hidden="true" tabindex="-1"></a>  data <span class="ot">&lt;-</span> <span class="cf">if</span>(subset<span class="sc">==</span><span class="dv">0</span> <span class="sc">|</span> subset<span class="sc">&gt;</span>sim<span class="sc">$</span>params[<span class="dv">2</span>,]){</span>
<span id="cb10-7"><a href="#cb10-7" aria-hidden="true" tabindex="-1"></a>    sim<span class="sc">$</span>sim[<span class="dv">1</span><span class="sc">:</span>t,<span class="dv">2</span><span class="sc">:</span>(sim<span class="sc">$</span>params[<span class="dv">2</span>,]<span class="sc">+</span><span class="dv">1</span>)]</span>
<span id="cb10-8"><a href="#cb10-8" aria-hidden="true" tabindex="-1"></a>  } <span class="cf">else</span> {</span>
<span id="cb10-9"><a href="#cb10-9" aria-hidden="true" tabindex="-1"></a>    sim<span class="sc">$</span>sim[<span class="dv">1</span><span class="sc">:</span>t,<span class="dv">2</span><span class="sc">:</span>(subset<span class="sc">+</span><span class="dv">1</span>)]</span>
<span id="cb10-10"><a href="#cb10-10" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb10-11"><a href="#cb10-11" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb10-12"><a href="#cb10-12" aria-hidden="true" tabindex="-1"></a>  <span class="co"># number of people who experienced zero wealth or less</span></span>
<span id="cb10-13"><a href="#cb10-13" aria-hidden="true" tabindex="-1"></a>  numZero <span class="ot">&lt;-</span> <span class="fu">length</span>(data) <span class="sc">-</span> <span class="fu">sum</span>(<span class="fu">sapply</span>(data, <span class="cf">function</span>(x) <span class="fu">all</span>(x<span class="sc">&gt;</span><span class="dv">0</span>)))</span>
<span id="cb10-14"><a href="#cb10-14" aria-hidden="true" tabindex="-1"></a>  numZero</span>
<span id="cb10-15"><a href="#cb10-15" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb10-16"><a href="#cb10-16" aria-hidden="true" tabindex="-1"></a>}</span>
<span id="cb10-17"><a href="#cb10-17" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb10-18"><a href="#cb10-18" aria-hidden="true" tabindex="-1"></a>numZeroTwenty100 <span class="ot">&lt;-</span> <span class="fu">numZero</span>(<span class="at">sim=</span>ergodic, <span class="at">t=</span><span class="dv">100</span>, <span class="at">subset=</span><span class="dv">20</span>)</span>
<span id="cb10-19"><a href="#cb10-19" aria-hidden="true" tabindex="-1"></a>numZeroTwenty1000 <span class="ot">&lt;-</span> <span class="fu">numZero</span>(<span class="at">sim=</span>ergodic, <span class="at">t=</span><span class="dv">1000</span>, <span class="at">subset=</span><span class="dv">20</span>)</span>
<span id="cb10-20"><a href="#cb10-20" aria-hidden="true" tabindex="-1"></a>numZero100 <span class="ot">&lt;-</span> <span class="fu">numZero</span>(<span class="at">sim=</span>ergodic, <span class="at">t=</span><span class="dv">100</span>)</span>
<span id="cb10-21"><a href="#cb10-21" aria-hidden="true" tabindex="-1"></a>numZero1000 <span class="ot">&lt;-</span> <span class="fu">numZero</span>(<span class="at">sim=</span>ergodic, <span class="at">t=</span><span class="dv">1000</span>)</span></code></pre></div></div>
</details>
</div>
<p>Now for a wrinkle, which we can see in the plotted figure. Of those first 20 people plotted on the chart, 11(!) had their wealth go into the negative over those 100 periods. We see the same phenomenon across the broader population, with 5433 dropping below zero in those first 100 periods.</p>
<p>To the extent zero wealth is ruinous when it occurs, that event is severe. If the player only incurs the consequences of their final position, the bet is unlikely to result in ruin but still presents a non-zero threat of catastrophe.</p>
<p>What would an expected utility maximiser do here? For a person with log utility, any probability of ruin during the flips would lead them to reject the gamble. The log of zero is negative infinity, which outweighs all other possible outcomes, whatever their magnitude or probability.</p>
<p>The growth-rate maximiser would accept the bet if they didn’t fear ruin. The time-average growth of $5 per flip would pull them in. If ruin was feared and consequential, then they might also reject.</p>
</section>
<section id="the-ergodicity-economics-hypothesis" class="level3">
<h3 class="anchored" data-anchor-id="the-ergodicity-economics-hypothesis">The ergodicity economics hypothesis</h3>
<p>This brings us to the core hypotheses in ergodicity economics.</p>
<p>First, people act to maximise the time-average growth rate of their wealth.</p>
<p>Second, the optimal action to maximise the time-average growth rate varies between multiplicative and additive environments. In multiplicative environments, people have log utility. In additive environments, they are risk neutral.</p>
</section>
<section id="what-are-the-implications-of-this-finding" class="level3">
<h3 class="anchored" data-anchor-id="what-are-the-implications-of-this-finding">What are the implications of this finding?</h3>
<p>The advocates of ergodicity economics have applied this claim to a range of economics problems.</p>
<p><span class="citation" data-cites="peters2023">Peters (<a href="#ref-peters2023" role="doc-biblioref">2023</a>)</span> argues that we can think of insurance as a tool to make wealth grow faster rather than as protection for the risk averse. This plot shows the outcomes for agents facing a 5% probability of a loss of 95% of their wealth each period. Uninsured agents experience a ruinous path over time, losing far more than would be implied by the expected value. Those who insure at a cost experience a slower decline.</p>
<p>As an aside, I do find these numbers quite comical: 2500 periods with a 5% probability of loss, leading to an expected value of around {{< math >}}10^{-70}{{< /math >}} times the initial wealth even under the insured scenario. The expected-value optimisers, even if they started with every atom in the universe, would be left with a fraction of an atom by the end.</p>
<p><a href="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/peters-2023-figure-3.png" class="lightbox" data-gallery="quarto-lightbox-gallery-4">{{< img src="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/peters-2023-figure-3.png" class="img-fluid" style="width:60.0%" >}}</a></p>
<p><span class="citation" data-cites="peters2022">Peters and Adamou (<a href="#ref-peters2022" role="doc-biblioref">2022</a>)</span> similarly propose a desire to maximise the growth rate as the origin of cooperative behaviour. Here, the green trajectories are the selfish agents, the blue line the cooperators. In some ways, this is just the insurance problem reframed.</p>
<p><a href="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/peters-and-adamou-2022-figure-2.png" class="lightbox" data-gallery="quarto-lightbox-gallery-5">{{< img src="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/peters-and-adamou-2022-figure-2.png" class="img-fluid" style="width:60.0%" >}}</a></p>
<p>One of the more interesting examples concerns time preference. <span class="citation" data-cites="adamou2021">Adamou et al. (<a href="#ref-adamou2021" role="doc-biblioref">2021</a>)</span> use growth rate maximisation as an explanation for exponential discounting, hyperbolic discounting and preference reversals, depending on the particular wealth dynamic.</p>
<p>I won’t cover all the scenarios, but this image captures a situation where an agent in an additive world has a choice between a smaller sooner and a larger later pay-off. This agent seeks to maximise the growth rate of their wealth. From the perspective of {{< math >}}t_0{{< /math >}} the larger later pay-off provides a higher growth rate, which is equal to the slope of the line extended to the top of that pay-off. By the third frame, as the agent moves closer to the smaller, sooner pay-off, the higher growth rate now comes from that early pay-off. They have reversed their preference.</p>
<p><a href="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/adamou-et-al-2021-figure-3.png" class="lightbox" data-gallery="quarto-lightbox-gallery-6">{{< img src="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/adamou-et-al-2021-figure-3.png" class="img-fluid" >}}</a></p>
<p>It is when seeing ideas such as this that the suggestion that ergodicity economics is “psychology free” seems slightly ridiculous. The agent must be myopic to be unable to see their upcoming preference reversal, or to realise the foregone larger opportunity on the other side of that smaller sooner payment.</p>
</section>
</section>
<section id="the-experiment" class="level2">
<h2 class="anchored" data-anchor-id="the-experiment">The experiment</h2>
<p>But rather than going down that rabbit-hole, I want to present an experimental result. In 2019, a working paper was released examining whether shifting between an additive and multiplicative environment would change risk preferences. One of my blog posts was on that working paper. The paper was ultimately published in 2021 in PLOS Computational Biology <span class="citation" data-cites="meder2021">(<a href="#ref-meder2021" role="doc-biblioref">Meder et al., 2021</a>)</span>.</p>
<p>That first experiment was subject to many criticisms, including by me, so <span class="citation" data-cites="skjold">Skjold et al. (<a href="#ref-skjold" role="doc-biblioref">2024</a>)</span> designed a new experiment. A pre-print describing the results from this experiment was released at the end of May. Some of the criticisms have been addressed in this new experiment, and the result is interesting.</p>
<p>Experimental participants were randomised to an additive or multiplicative environment where they were asked to make a series of bets. After making the bets in one environment, they were crossed over to the other.</p>
<p>At the beginning of the additive and multiplicative session, participants were trained on a set of fractal images, each of which had a specific effect on their endowment: multiplication by some fraction in the multiplicative session, or addition or subtraction of some sum in the additive session. Participants were then tested on whether they had learnt the ordering of the fractals, with the subset of participants with low learning excluded from the analysis. This image shows the training procedure, which essentially comprises exposure to the fractal and then an update to their wealth.</p>
<p><a href="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/skjold-et-al-2024-figure-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-7">{{< img src="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/skjold-et-al-2024-figure-1.png" class="img-fluid" >}}</a></p>
<p>This use of fractals instead of numbers is one of the confounding factors that could influence the results: we have introduced ambiguity into the subsequent decisions. It was one of my critiques of the original experiment, but I clearly wasn’t very persuasive. Anyhow, let’s ignore that for now.</p>
<p>Participants then proceeded to their decision task, where they had to choose between gambles, each of which is represented by two of the fractal images. Over a sequence of 160 decisions, they would be shown the gambles, make their choice, be shown the outcome of the gamble, then see the effect of the outcome on their wealth.</p>
<p><a href="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/skjold-et-al-2024-figure-4.png" class="lightbox" data-gallery="quarto-lightbox-gallery-8">{{< img src="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/skjold-et-al-2024-figure-4.png" class="img-fluid" >}}</a></p>
<p>You can watch a video of the training and decision task below. (I didn’t show this video in the presentation.)</p>
<div class="quarto-video ratio ratio-16x9"><iframe data-external="1" src="https://www.youtube.com/embed/uLGA4Ym-OYA" title="" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe></div>
<p>Participants were incentivised by being paid their relative proportion of points compared to a rolling window of 10 participants. Another exhibit of “why do we make experimental incentives so complicated” and another confound to the experimental result. By rewarding on proportional access to a pool, they have introduced diminishing gains and a cap on winnings. But again, I’ll ignore that for today.</p>
<p>So, to the result. The research team modelled participants as having an isoelastic utility function (a reasonably strong assumption), with the parameter {{< math >}}\eta{{< /math >}} calculated by Bayesian cognitive modelling.</p>
<p>{{< math display >}}f_{\eta}(x)=\begin{cases}
\frac{x^{1-\eta} - 1}{1-\eta} & \text{if } \eta \neq 1 \\[6pt]
\ln(x) & \text{if } \eta = 1
\end{cases}{{< /math >}}</p>
<p>What would we predict the value of {{< math >}}\eta{{< /math >}} to be in this experiment? Expected utility theory is quiet on the precise value. The ergodicity economics approach, however, gives us a prediction. First, {{< math >}}\eta{{< /math >}} will be one in the multiplicative condition, as log utility maximises the growth rate. Second, {{< math >}}\eta{{< /math >}} will be zero in the additive condition. The growth rate is maximised in an additive environment by risk neutral behaviour.</p>
<p>This chart shows the result. Thin lines represent individual participants. The thick lines represent the aggregate. For the additive scenario, participants were close to risk neutral: the aggregate estimate of {{< math >}}\eta{{< /math >}} was 0.1. For the multiplicative condition, although there was a wider distribution of values, the central estimate of {{< math >}}\eta{{< /math >}} was one.</p>
<p><a href="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/skjold-et-al-2024-figure-7c.png" class="lightbox" data-gallery="quarto-lightbox-gallery-9">{{< img src="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/skjold-et-al-2024-figure-7c.png" class="img-fluid" >}}</a></p>
<p>Despite the elements of this experiment that I would do differently - I have only hinted at a couple - this is a strong result.</p>
<p>If the ergodicity economics hypothesis is correct, it is worth thinking about what this means psychologically.</p>
<p>When modelling the utility function, the researchers took the value of {{< math >}}x{{< /math >}} to be the participant’s experimental wealth at the time the participant makes their decision. It is the initial endowment, plus or minus the results of the previous bets. {{< math >}}x{{< /math >}} does not include outside wealth.</p>
<p>But if this use of {{< math >}}x{{< /math >}} is an accurate characterisation of the decision making process of the agents, it suggests a form of narrow bracketing or a degree of myopia. Agents are maximising the growth rate <em>within</em> the experiment, not more generally. We need to introduce some psychology to explain this. (This phenomenon is common across lab experiments involving risky decisions.)</p>
<p>Similarly, this experiment is part of a broader environment with either multiplicative or additive characteristics. Experimental participants can take their payment from the experiment and invest it. Maximising the growth rate in the additive condition by maximising expected value may not maximise the total growth rate if the world outside the experiment is multiplicative.</p>
</section>
<section id="an-evolutionary-analysis" class="level2">
<h2 class="anchored" data-anchor-id="an-evolutionary-analysis">An evolutionary analysis</h2>
<p>Now, via a rather long and winding path, I want to turn to a couple of evolutionary observations about ergodicity economics. There is a large literature in the evolution of preferences, not to mention in the evolutionary biology literature itself, that is relevant to an analysis of growth rate maximisation. Since the concepts are already there, I’m going to lean on them and turn them to my own purpose.</p>
<p>The first evolutionary angle concerns what happens when we take a gene’s eye view. And to assist me in making this point, let me show a quote from a Nature Physics paper in which Ole Peters <span class="citation" data-cites="peters2019">(<a href="#ref-peters2019" role="doc-biblioref">2019</a>)</span> summarises his work:</p>
<blockquote class="blockquote">
<p>[I]n maximizing the expectation value - an ensemble average over all possible outcomes of the gamble - expected utility theory implicitly assumes that individuals can interact with copies of themselves, effectively in parallel universes (the other members of the ensemble). An expectation value of a non-ergodic observable physically corresponds to pooling and sharing among many entities. That may reflect what happens in a specially designed large collective, but it doesn’t reflect the situation of an individual decision-maker.</p>
</blockquote>
<p>Ignoring the fact that Peters mis-characterises expected utility theory, this idea of interacting with copies of themselves is what happens at the level of genes. By the presence of multiple copies of a gene across individuals, the gene can experience the ensemble average. The following toy model and simulation illustrates.</p>
<section id="a-toy-model" class="level3">
<h3 class="anchored" data-anchor-id="a-toy-model">A toy model</h3>
<p>Suppose two types of agents lived in a non-ergodic world.</p>
<p>One type of agent seeks to maximise the time-average growth rate of its number of descendants. This desire to maximise the time-average growth rate is a function of its genotype, and is transmitted to its children.</p>
<p>The other type of agent seeks to maximise the expected number of offspring. Similarly, this agent’s preferences are set genetically.</p>
<p>In the environment in which these agents live, they have a choice of strategy. One strategy is to have a single offspring asexually with certainty before they die. The other strategy is a 50:50 bet of having either 0.6 or 1.5 offspring. Part offspring sounds weird, but with a large population of agents, you can think of this as the average number of offspring. The simulation works out largely the same if I make the number of children probabilistic in accord with those numbers. You can see I have effectively mimicked the classic ergodicity economics bet.</p>
<p>One final feature in this environment will be that each individual experiences its own flip. You might think of this environment as involving idiosyncratic risk. This is an important assumption that I will return to.</p>
<p>Given this setup, the type that maximises the expected number of offspring always accepts the bet. The time-average growth maximiser always rejects it. Which would come to dominate the population?</p>
<p>The time-average growth rate maximiser population stays constant. One offspring to each asexual parent.</p>
<p>This is a chart of the population of the accepting type for a simulation of 100 generations, starting with a population of 10,000.</p>
<div class="cell">
<details class="code-fold">
<summary>Code for evolutionary simulation</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb11"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb11-1"><a href="#cb11-1" aria-hidden="true" tabindex="-1"></a><span class="fu">set.seed</span>(<span class="dv">20240705</span>)</span>
<span id="cb11-2"><a href="#cb11-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb11-3"><a href="#cb11-3" aria-hidden="true" tabindex="-1"></a><span class="co"># create function to round probabilistically - important when small numbers involved</span></span>
<span id="cb11-4"><a href="#cb11-4" aria-hidden="true" tabindex="-1"></a>probabilistic_round <span class="ot">&lt;-</span> <span class="cf">function</span>(x) {</span>
<span id="cb11-5"><a href="#cb11-5" aria-hidden="true" tabindex="-1"></a>  <span class="cf">if</span> (<span class="fu">runif</span>(<span class="dv">1</span>) <span class="sc">&lt;</span> x <span class="sc">-</span> <span class="fu">floor</span>(x)) {</span>
<span id="cb11-6"><a href="#cb11-6" aria-hidden="true" tabindex="-1"></a>    <span class="fu">ceiling</span>(x)</span>
<span id="cb11-7"><a href="#cb11-7" aria-hidden="true" tabindex="-1"></a>  } <span class="cf">else</span> {</span>
<span id="cb11-8"><a href="#cb11-8" aria-hidden="true" tabindex="-1"></a>    <span class="fu">floor</span>(x)</span>
<span id="cb11-9"><a href="#cb11-9" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb11-10"><a href="#cb11-10" aria-hidden="true" tabindex="-1"></a>}</span>
<span id="cb11-11"><a href="#cb11-11" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb11-12"><a href="#cb11-12" aria-hidden="true" tabindex="-1"></a><span class="co"># Function to simulate evolution betting</span></span>
<span id="cb11-13"><a href="#cb11-13" aria-hidden="true" tabindex="-1"></a>evolutionBet <span class="ot">&lt;-</span> <span class="cf">function</span>(p, n, t, gain, loss) {</span>
<span id="cb11-14"><a href="#cb11-14" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb11-15"><a href="#cb11-15" aria-hidden="true" tabindex="-1"></a>  <span class="co">#p is probability of a gain</span></span>
<span id="cb11-16"><a href="#cb11-16" aria-hidden="true" tabindex="-1"></a>  <span class="co">#region  is how many people in the simulation</span></span>
<span id="cb11-17"><a href="#cb11-17" aria-hidden="true" tabindex="-1"></a>  <span class="co">#t is the number of generations simulated</span></span>
<span id="cb11-18"><a href="#cb11-18" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb11-19"><a href="#cb11-19" aria-hidden="true" tabindex="-1"></a>  params <span class="ot">&lt;-</span> <span class="fu">data.frame</span>(<span class="at">value =</span> <span class="fu">c</span>(p, n, t, gain, loss))</span>
<span id="cb11-20"><a href="#cb11-20" aria-hidden="true" tabindex="-1"></a>  <span class="fu">rownames</span>(params) <span class="ot">&lt;-</span> <span class="fu">c</span>(<span class="st">"p"</span>, <span class="st">"n"</span>, <span class="st">"t"</span>, <span class="st">"gain"</span>, <span class="st">"loss"</span>)</span>
<span id="cb11-21"><a href="#cb11-21" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb11-22"><a href="#cb11-22" aria-hidden="true" tabindex="-1"></a>  sim <span class="ot">&lt;-</span> <span class="fu">numeric</span>(t <span class="sc">+</span> <span class="dv">1</span>)</span>
<span id="cb11-23"><a href="#cb11-23" aria-hidden="true" tabindex="-1"></a>  sim[<span class="dv">1</span>] <span class="ot">&lt;-</span> n <span class="co"># Start population</span></span>
<span id="cb11-24"><a href="#cb11-24" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb11-25"><a href="#cb11-25" aria-hidden="true" tabindex="-1"></a>  <span class="cf">for</span> (i <span class="cf">in</span> <span class="dv">1</span><span class="sc">:</span>t) {</span>
<span id="cb11-26"><a href="#cb11-26" aria-hidden="true" tabindex="-1"></a>    <span class="cf">for</span> (j <span class="cf">in</span> <span class="dv">1</span><span class="sc">:</span><span class="fu">round</span>(n)) {</span>
<span id="cb11-27"><a href="#cb11-27" aria-hidden="true" tabindex="-1"></a>      outcome <span class="ot">&lt;-</span> <span class="fu">rbinom</span>(<span class="dv">1</span>, <span class="dv">1</span>, p)</span>
<span id="cb11-28"><a href="#cb11-28" aria-hidden="true" tabindex="-1"></a>      n <span class="ot">&lt;-</span> n <span class="sc">+</span> (<span class="fu">ifelse</span>(outcome <span class="sc">==</span> <span class="dv">1</span>, gain, loss) <span class="sc">-</span> <span class="dv">1</span>)</span>
<span id="cb11-29"><a href="#cb11-29" aria-hidden="true" tabindex="-1"></a>    }</span>
<span id="cb11-30"><a href="#cb11-30" aria-hidden="true" tabindex="-1"></a>    n <span class="ot">&lt;-</span> <span class="fu">probabilistic_round</span>(n)</span>
<span id="cb11-31"><a href="#cb11-31" aria-hidden="true" tabindex="-1"></a>    sim[i <span class="sc">+</span> <span class="dv">1</span>] <span class="ot">&lt;-</span> n</span>
<span id="cb11-32"><a href="#cb11-32" aria-hidden="true" tabindex="-1"></a>    <span class="cf">if</span> (n <span class="sc">==</span> <span class="dv">0</span>) <span class="cf">break</span></span>
<span id="cb11-33"><a href="#cb11-33" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb11-34"><a href="#cb11-34" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb11-35"><a href="#cb11-35" aria-hidden="true" tabindex="-1"></a>  sim <span class="ot">&lt;-</span> <span class="fu">data.frame</span>(<span class="at">period =</span> <span class="dv">0</span><span class="sc">:</span>t, <span class="at">n =</span> sim)</span>
<span id="cb11-36"><a href="#cb11-36" aria-hidden="true" tabindex="-1"></a>  <span class="fu">list</span>(<span class="at">params =</span> params, <span class="at">sim =</span> sim)</span>
<span id="cb11-37"><a href="#cb11-37" aria-hidden="true" tabindex="-1"></a>}</span>
<span id="cb11-38"><a href="#cb11-38" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb11-39"><a href="#cb11-39" aria-hidden="true" tabindex="-1"></a>evolution <span class="ot">&lt;-</span> <span class="fu">evolutionBet</span>(<span class="at">p=</span><span class="fl">0.5</span>, <span class="at">n=</span><span class="dv">10000</span>, <span class="at">t=</span><span class="dv">100</span>, <span class="at">gain=</span><span class="fl">1.5</span>, <span class="at">loss=</span><span class="fl">0.6</span>) <span class="co">#more than 100 periods can take a very long time, simulation slows markedly as population grows</span></span></code></pre></div></div>
</details>
</div>
<div class="cell">
<details class="code-fold">
<summary>Code for evolutionary plot</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb12"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb12-1"><a href="#cb12-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Plot the population growth for the evolutionary scenario (Figure 8).</span></span>
<span id="cb12-2"><a href="#cb12-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb12-3"><a href="#cb12-3" aria-hidden="true" tabindex="-1"></a>basePlotEvo <span class="ot">&lt;-</span> <span class="fu">ggplot</span>(evolution<span class="sc">$</span>sim[<span class="fu">c</span>(<span class="dv">1</span><span class="sc">:</span><span class="dv">101</span>),], <span class="fu">aes</span>(<span class="at">x=</span>period))</span>
<span id="cb12-4"><a href="#cb12-4" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb12-5"><a href="#cb12-5" aria-hidden="true" tabindex="-1"></a>expectationPlotEvo <span class="ot">&lt;-</span> basePlotEvo <span class="sc">+</span></span>
<span id="cb12-6"><a href="#cb12-6" aria-hidden="true" tabindex="-1"></a>  <span class="fu">geom_line</span>(<span class="fu">aes</span>(<span class="at">y=</span>n), <span class="at">color =</span> <span class="dv">1</span>, <span class="at">linewidth=</span><span class="dv">1</span>) <span class="sc">+</span></span>
<span id="cb12-7"><a href="#cb12-7" aria-hidden="true" tabindex="-1"></a>  <span class="fu">labs</span>(<span class="at">y =</span> <span class="st">"Population"</span>)</span>
<span id="cb12-8"><a href="#cb12-8" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb12-9"><a href="#cb12-9" aria-hidden="true" tabindex="-1"></a>expectationPlotEvo</span></code></pre></div></div>
</details>
<div class="cell-output-display">
<div id="fig-ergodicity-presentation-8" class="quarto-float quarto-figure quarto-figure-center anchored">
<figure class="quarto-float quarto-float-fig figure">
<figcaption class="quarto-float-caption-top quarto-float-caption quarto-float-fig" id="fig-ergodicity-presentation-8-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;4: Population of accepting types
</figcaption>
<div aria-describedby="fig-ergodicity-presentation-8-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<a href="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-8-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-10" title="Figure&nbsp;4: Population of accepting types"><img src="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-8-1.png" class="img-fluid figure-img" width="672"></a>
</div>
</figure>
</div>
</div>
</div>
<p>You can see that they have a population growth rate of close to 5%.</p>
<p>Why don’t they experience the decline we saw in earlier simulations of this bet? Because their copies experience the full ensemble of outcomes.</p>
<p>So here we have a toy model that shows that time-average growth rate maximisation may not be the optimal strategy in a multiplicative environment. The constant population of time-average growth rate maximisers is swamped by the spreading population of the expected value maximisers.</p>
<p>This behaviour could also emerge where it did not previously exist. The simulation I just showed you had 10,000 agents with expected value maximising behaviour to start. What if we had a population of time-average growth rate optimisers, and a single expected value maximiser emerged?</p>
<p>I simulated 10,000 instances of a single individual developing the mutation. This plot shows the population of the first ten mutants. For five of them, the mutation appears and disappears. For the other five, however, they grow into a substantial population. It only takes a few agents with this mutation to effectively diversify the results.</p>
<div class="cell">
<details class="code-fold">
<summary>Code for evolutionary simulation</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb13"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb13-1"><a href="#cb13-1" aria-hidden="true" tabindex="-1"></a><span class="co"># run 9 simulations with 1 accepting type to start</span></span>
<span id="cb13-2"><a href="#cb13-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb13-3"><a href="#cb13-3" aria-hidden="true" tabindex="-1"></a><span class="fu">set.seed</span>(<span class="dv">20240705</span>)</span>
<span id="cb13-4"><a href="#cb13-4" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb13-5"><a href="#cb13-5" aria-hidden="true" tabindex="-1"></a>mutations <span class="ot">&lt;-</span> <span class="dv">10000</span></span>
<span id="cb13-6"><a href="#cb13-6" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb13-7"><a href="#cb13-7" aria-hidden="true" tabindex="-1"></a><span class="cf">for</span> (i <span class="cf">in</span> <span class="dv">1</span><span class="sc">:</span>mutations) {</span>
<span id="cb13-8"><a href="#cb13-8" aria-hidden="true" tabindex="-1"></a>  <span class="fu">assign</span>(<span class="fu">paste0</span>(<span class="st">"evolution_"</span>, i), <span class="fu">evolutionBet</span>(<span class="at">p=</span><span class="fl">0.5</span>, <span class="at">n=</span><span class="dv">1</span>, <span class="at">t=</span><span class="dv">100</span>, <span class="at">gain=</span><span class="fl">1.5</span>, <span class="at">loss=</span><span class="fl">0.6</span>))</span>
<span id="cb13-9"><a href="#cb13-9" aria-hidden="true" tabindex="-1"></a>}</span>
<span id="cb13-10"><a href="#cb13-10" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb13-11"><a href="#cb13-11" aria-hidden="true" tabindex="-1"></a><span class="co"># Create a data frame for each simulation and store in a list</span></span>
<span id="cb13-12"><a href="#cb13-12" aria-hidden="true" tabindex="-1"></a>data_frames <span class="ot">&lt;-</span> <span class="fu">list</span>()</span>
<span id="cb13-13"><a href="#cb13-13" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb13-14"><a href="#cb13-14" aria-hidden="true" tabindex="-1"></a><span class="cf">for</span> (i <span class="cf">in</span> <span class="dv">1</span><span class="sc">:</span>mutations) {</span>
<span id="cb13-15"><a href="#cb13-15" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Dynamically retrieve the variable and select the first 101 rows of $sim</span></span>
<span id="cb13-16"><a href="#cb13-16" aria-hidden="true" tabindex="-1"></a>  current_data <span class="ot">&lt;-</span> <span class="fu">get</span>(<span class="fu">paste0</span>(<span class="st">"evolution_"</span>, i))<span class="sc">$</span>sim[<span class="dv">1</span><span class="sc">:</span><span class="dv">101</span>, ]</span>
<span id="cb13-17"><a href="#cb13-17" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb13-18"><a href="#cb13-18" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Add a column for 'i' to use as color in plotting</span></span>
<span id="cb13-19"><a href="#cb13-19" aria-hidden="true" tabindex="-1"></a>  current_data<span class="sc">$</span>i <span class="ot">&lt;-</span> i</span>
<span id="cb13-20"><a href="#cb13-20" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb13-21"><a href="#cb13-21" aria-hidden="true" tabindex="-1"></a>  <span class="co"># Append to the list</span></span>
<span id="cb13-22"><a href="#cb13-22" aria-hidden="true" tabindex="-1"></a>  data_frames[[i]] <span class="ot">&lt;-</span> current_data</span>
<span id="cb13-23"><a href="#cb13-23" aria-hidden="true" tabindex="-1"></a>}</span>
<span id="cb13-24"><a href="#cb13-24" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb13-25"><a href="#cb13-25" aria-hidden="true" tabindex="-1"></a><span class="co"># Combine all data frames into one</span></span>
<span id="cb13-26"><a href="#cb13-26" aria-hidden="true" tabindex="-1"></a>combined_data <span class="ot">&lt;-</span> <span class="fu">do.call</span>(rbind, data_frames)</span></code></pre></div></div>
</details>
</div>
<div class="cell">
<details class="code-fold">
<summary>Code to count mutation spread</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb14"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb14-1"><a href="#cb14-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Count the number of simulations where the mutation spread (where n &gt; 1 when i = 100)</span></span>
<span id="cb14-2"><a href="#cb14-2" aria-hidden="true" tabindex="-1"></a>mutation_count <span class="ot">&lt;-</span> <span class="fu">sum</span>(combined_data[combined_data<span class="sc">$</span>period <span class="sc">==</span> <span class="dv">100</span>,]<span class="sc">$</span>n <span class="sc">&gt;</span> <span class="dv">1</span>, <span class="at">na.rm =</span> <span class="cn">TRUE</span>)</span></code></pre></div></div>
</details>
</div>
<div class="cell">
<details class="code-fold">
<summary>Code for evolutionary plot with mutation</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb15"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb15-1"><a href="#cb15-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Plot first 10 lines</span></span>
<span id="cb15-2"><a href="#cb15-2" aria-hidden="true" tabindex="-1"></a>mutationPlotEvo <span class="ot">&lt;-</span> <span class="fu">ggplot</span>(combined_data[combined_data<span class="sc">$</span>i <span class="sc">&gt;=</span> <span class="dv">1</span> <span class="sc">&amp;</span> combined_data<span class="sc">$</span>i <span class="sc">&lt;=</span> <span class="dv">10</span>,], <span class="fu">aes</span>(<span class="at">x=</span>period, <span class="at">y=</span>n, <span class="at">color=</span><span class="fu">factor</span>(i))) <span class="sc">+</span></span>
<span id="cb15-3"><a href="#cb15-3" aria-hidden="true" tabindex="-1"></a>  <span class="fu">geom_line</span>() <span class="sc">+</span></span>
<span id="cb15-4"><a href="#cb15-4" aria-hidden="true" tabindex="-1"></a>  <span class="fu">labs</span>(<span class="at">y =</span> <span class="st">"Population"</span>) <span class="sc">+</span></span>
<span id="cb15-5"><a href="#cb15-5" aria-hidden="true" tabindex="-1"></a>  <span class="co">#remove legend</span></span>
<span id="cb15-6"><a href="#cb15-6" aria-hidden="true" tabindex="-1"></a>  <span class="fu">theme</span>(<span class="at">legend.position =</span> <span class="st">"none"</span>)</span>
<span id="cb15-7"><a href="#cb15-7" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb15-8"><a href="#cb15-8" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb15-9"><a href="#cb15-9" aria-hidden="true" tabindex="-1"></a>mutationPlotEvo</span></code></pre></div></div>
</details>
<div class="cell-output-display">
<div id="fig-ergodicity-presentation-9" class="quarto-float quarto-figure quarto-figure-center anchored">
<figure class="quarto-float quarto-float-fig figure">
<figcaption class="quarto-float-caption-top quarto-float-caption quarto-float-fig" id="fig-ergodicity-presentation-9-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;5: Population of accepting types with mutation
</figcaption>
<div aria-describedby="fig-ergodicity-presentation-9-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<a href="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-9-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-11" title="Figure&nbsp;5: Population of accepting types with mutation"><img src="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-9-1.png" class="img-fluid figure-img" width="672"></a>
</div>
</figure>
</div>
</div>
</div>
<p>If we zoom into the first 35 periods, you can see the dynamic for those where the mutation did not spread.</p>
<div class="cell">
<details class="code-fold">
<summary>Code for evolutionary plot with mutation (first 30 periods)</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb16"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb16-1"><a href="#cb16-1" aria-hidden="true" tabindex="-1"></a><span class="co"># Plot first 35 periods only</span></span>
<span id="cb16-2"><a href="#cb16-2" aria-hidden="true" tabindex="-1"></a>mutationPlotEvo30 <span class="ot">&lt;-</span> <span class="fu">ggplot</span>(combined_data[combined_data<span class="sc">$</span>i <span class="sc">&gt;=</span> <span class="dv">1</span> <span class="sc">&amp;</span> combined_data<span class="sc">$</span>i <span class="sc">&lt;=</span> <span class="dv">10</span>,], <span class="fu">aes</span>(<span class="at">x=</span>period, <span class="at">y=</span>n, <span class="at">color=</span><span class="fu">factor</span>(i))) <span class="sc">+</span></span>
<span id="cb16-3"><a href="#cb16-3" aria-hidden="true" tabindex="-1"></a>  <span class="fu">geom_line</span>() <span class="sc">+</span></span>
<span id="cb16-4"><a href="#cb16-4" aria-hidden="true" tabindex="-1"></a>  <span class="fu">labs</span>(<span class="at">y =</span> <span class="st">"Population"</span>) <span class="sc">+</span></span>
<span id="cb16-5"><a href="#cb16-5" aria-hidden="true" tabindex="-1"></a>  <span class="fu">xlim</span>(<span class="dv">0</span>, <span class="dv">30</span>) <span class="sc">+</span></span>
<span id="cb16-6"><a href="#cb16-6" aria-hidden="true" tabindex="-1"></a>  <span class="fu">ylim</span>(<span class="dv">0</span>, <span class="dv">35</span>) <span class="sc">+</span></span>
<span id="cb16-7"><a href="#cb16-7" aria-hidden="true" tabindex="-1"></a>  <span class="co">#remove legend</span></span>
<span id="cb16-8"><a href="#cb16-8" aria-hidden="true" tabindex="-1"></a>  <span class="fu">theme</span>(<span class="at">legend.position =</span> <span class="st">"none"</span>)</span>
<span id="cb16-9"><a href="#cb16-9" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb16-10"><a href="#cb16-10" aria-hidden="true" tabindex="-1"></a>mutationPlotEvo30</span></code></pre></div></div>
</details>
<div class="cell-output-display">
<div id="fig-ergodicity-presentation-10" class="quarto-float quarto-figure quarto-figure-center anchored">
<figure class="quarto-float quarto-float-fig figure">
<figcaption class="quarto-float-caption-top quarto-float-caption quarto-float-fig" id="fig-ergodicity-presentation-10-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;6: Population of accepting types with mutation (first 30 periods for first 10 agents)
</figcaption>
<div aria-describedby="fig-ergodicity-presentation-10-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<a href="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-10-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-12" title="Figure&nbsp;6: Population of accepting types with mutation (first 30 periods for first 10 agents)"><img src="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-10-1.png" class="img-fluid figure-img" width="672"></a>
</div>
</figure>
</div>
</div>
</div>
<p>This is a slightly rosier picture than occurs across the full 10,000 simulations, where the mutation did not spread 70% of the time.</p>
<p>These illustrations suggest that time-average growth optimisation may not be the optimal strategy, but it hinges on one critical assumption: that risk is idiosyncratic. Diversification enables the gene to experience the ensemble average. What if such diversification is not possible?</p>
<p>In that case, we are effectively back to the world that I showed you at the beginning. You could consider each line to represent an individual and their children, with their children all bound to the same bet. In almost all cases, this leads to a decline in frequency. An extraordinarily lucky few might boom through many rolls of the dice, but that is a rare chance.</p>
<p>Further, recall the decline toward the end of the 100 periods. This occurred as a small number of genetic lines comprise most of the population - in fact, one single line of the original 10,000 comprises 53% of the population at the end of 100 periods - and they cannot diversify their risk. A few unlucky coin flips and they are gone.</p>
<p>The result is that, over a long enough time horizon, <em>everyone</em> is wiped out. There is no longer a lucky few. Here’s the same simulation plotted through 1000 iterations, over evolutionary time, in both linear and log scales.</p>
<div class="cell">
<details class="code-fold">
<summary>Code for evolutionary plot over 1000 periods</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb17"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb17-1"><a href="#cb17-1" aria-hidden="true" tabindex="-1"></a>nonErgodicPlot <span class="ot">&lt;-</span> <span class="fu">plotWealth</span>(<span class="at">sim=</span>nonErgodic, <span class="at">t=</span><span class="dv">1000</span>, <span class="at">people=</span><span class="dv">20</span>)</span>
<span id="cb17-2"><a href="#cb17-2" aria-hidden="true" tabindex="-1"></a>nonErgodicPlot</span></code></pre></div></div>
</details>
<div class="cell-output-display">
<div id="fig-ergodicity-presentation-11" class="quarto-float quarto-figure quarto-figure-center anchored">
<figure class="quarto-float quarto-float-fig figure">
<figcaption class="quarto-float-caption-top quarto-float-caption quarto-float-fig" id="fig-ergodicity-presentation-11-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;7: Population of accepting types over 1000 periods
</figcaption>
<div aria-describedby="fig-ergodicity-presentation-11-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<a href="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-11-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-13" title="Figure&nbsp;7: Population of accepting types over 1000 periods"><img src="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-11-1.png" class="img-fluid figure-img" width="672"></a>
</div>
</figure>
</div>
</div>
</div>
<div class="cell">
<details class="code-fold">
<summary>Code for evolutionary plot over 1000 periods (log scale)</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb18"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb18-1"><a href="#cb18-1" aria-hidden="true" tabindex="-1"></a>logNonErgodicPlot <span class="ot">&lt;-</span> nonErgodicPlot<span class="sc">+</span></span>
<span id="cb18-2"><a href="#cb18-2" aria-hidden="true" tabindex="-1"></a>    <span class="fu">scale_y_log10</span>(<span class="at">breaks =</span> <span class="fu">c</span>(<span class="fl">0.0001</span>, <span class="fl">0.1</span>, <span class="dv">100</span>, <span class="dv">100000</span>), <span class="at">labels =</span> <span class="fu">c</span>(<span class="st">"0.0001"</span>, <span class="st">"0.1"</span>, <span class="st">"100"</span>, <span class="st">"100000"</span>))</span>
<span id="cb18-3"><a href="#cb18-3" aria-hidden="true" tabindex="-1"></a>logNonErgodicPlot</span></code></pre></div></div>
</details>
<div class="cell-output-display">
<div id="fig-ergodicity-presentation-12" class="quarto-float quarto-figure quarto-figure-center anchored">
<figure class="quarto-float quarto-float-fig figure">
<figcaption class="quarto-float-caption-top quarto-float-caption quarto-float-fig" id="fig-ergodicity-presentation-12-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
Figure&nbsp;8: Population of accepting types over 1000 periods (log scale)
</figcaption>
<div aria-describedby="fig-ergodicity-presentation-12-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<a href="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-12-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-14" title="Figure&nbsp;8: Population of accepting types over 1000 periods (log scale)"><img src="the-psychological-and-genes-eye-view-of-ergodicity-economics_files/figure-html/fig-ergodicity-presentation-12-1.png" class="img-fluid figure-img" width="672"></a>
</div>
</figure>
</div>
</div>
</div>
<p>The result is that with aggregate risk, time-average growth rate maximisation can be the optimal strategy.</p>
</section>
<section id="probability-matching" class="level3">
<h3 class="anchored" data-anchor-id="probability-matching">Probability matching</h3>
<p>To explore this in more detail, I’m going to turn to another example that has a rich history in the biology literature.</p>
<p>The particular example I am going to pick is a bit cartoonish, and comes from Andrew Lo’s <a href="ADD_LINK">Adaptive Markets</a>. This in turn draws on a more technical paper by Thomas Brennan and Lo <span class="citation" data-cites="brennan2011">(<a href="#ref-brennan2011" role="doc-biblioref">2011</a>)</span> published in The Quarterly Journal of Finance to explain the evolution of probability matching. You can find other earlier examples in the literature, such as by <span class="citation" data-cites="cooper1982">Cooper and Kaplan (<a href="#ref-cooper1982" role="doc-biblioref">1982</a>)</span> in The Journal of Theoretical Biology.</p>
<p>The example concerns an animal called the tribble. For amusement, I chucked an earlier draft of this presentation into ChatGPT and asked it to illustrate it. Most of what it produced was unusable, but I’ve kept a couple of images for which I thought it did a good job.</p>
<p>Tribbles live in a region comprising valleys and plateaus. Tribbles reproduce once in their life (producing three offspring asexually) and must choose whether to reproduce in the valley or on the plateau. This is a risky decision, however, as the valleys are affected by floods and the plateaus by drought.</p>
<p><a href="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/tribbles.webp" class="lightbox" data-gallery="quarto-lightbox-gallery-15"><img src="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/tribbles.webp" class="img-fluid" width="512"></a></p>
<p>Each generation there is a 75 per cent probability of sun. In such a case, the tribbles born on the plateau perish. The other 25 per cent of the time, it rains, leading to flood in the valleys and the death of those tribbles breeding there.</p>
<div class="quarto-layout-panel" data-layout-ncol="2">
<div class="quarto-layout-row">
<div class="quarto-layout-cell" style="flex-basis: 50.0%;justify-content: center;">
<p><a href="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/flood.webp" class="lightbox" data-gallery="quarto-lightbox-gallery-16"><img src="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/flood.webp" class="img-fluid"></a></p>
</div>
<div class="quarto-layout-cell" style="flex-basis: 50.0%;justify-content: center;">
<p><a href="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/drought.webp" class="lightbox" data-gallery="quarto-lightbox-gallery-17"><img src="img/the-psychological-and-genes-eye-view-of-ergodicity-economics/drought.webp" class="img-fluid"></a></p>
</div>
</div>
</div>
<p>What, then, is the growth maximising breeding strategy?</p>
<p>Let’s set {{< math >}}q{{< /math >}} as the proportion of tribbles that breed in the valley. If we maximise the expected number of offspring, tribbles would breed in the valley 100 per cent of the time. That is, {{< math >}}q=1{{< /math >}}, leading to an expected {{< math >}}0.75\times 3=2.25{{< /math >}} offspring.</p>
<p>However, in the long run, if all tribbles make this choice, the tribbles will be wiped out. Over the long term, the tribbles will experience droughts 75 per cent of the time and floods 25 per cent of the time. Putting this into the language of ergodicity economics, the time average growth rate is zero.</p>
<p>To find the {{< math >}}q{{< /math >}} that maximises the growth rate, we take the log of G and calculate the derivative. The solution is to breed in the valley 75 per cent of the time and on the plateau 25 per cent of the time.</p>
{{< math display >}}\begin{align*}
G&=3\times q^{0.75}(1-q)^{0.25}\\[6pt]
\\
\log(G)&=\log(3)+0.75\log(q)+0.25\log(1-q)\\[6pt]
\\
\frac{d}{dq}\log(G)&=\frac{0.75}{q}-\frac{0.25}{1-q}=0\\[6pt]
\\
q&=0.75
\end{align*}{{< /math >}}
<p>Probability matching in this world maximises the time-average growth rate.</p>
<p>This result is the same if we approach this from the perspective of log utility. If we maximise log utility as a function of number of offspring, we get the same value of {{< math >}}q{{< /math >}}.</p>
{{< math display >}}\begin{align*}
U(n)&=0.75\times \log(3q)+0.25\times log(3-3q))\\[6pt]
\\
\frac{d}{dq}U(n)&=0.75\times \frac{3}{3q}-0.25\times \frac{3}{3-3q}=0\\[6pt]
\\
q&=0.75
\end{align*}{{< /math >}}
<p>Here we have a world where maximising the time-average growth rate is the optimal solution. In this case, it is achieved via probability matching.</p>
<p>There is one feature of this scenario that might seem off. Probability matching maximises the growth rate for the species. But which individuals are heading off to the plateau where 75% of the time they are going to be fried? Is this an altruistic act for the benefit of the species? Why not head down to the cool valley where they, as an individual, are more likely to survive?</p>
<p>The answer was provided by <span class="citation" data-cites="grafen1999">Grafen (<a href="#ref-grafen1999" role="doc-biblioref">1999</a>)</span>. Suppose we have a large population of size {{< math >}}N{{< /math >}}. If an agent heads to the valley, the expected fraction of the population comprising their offspring ({{< math >}}\pi{{< /math >}}) will be:</p>
<p>{{< math display >}}\pi(\text{valley})\approx\frac{0.75}{qN}=\frac{1}{N}{{< /math >}}</p>
<p>If they stay to fry on the plateau, their offspring will comprise a similar fraction of the smaller remaining population:</p>
<p>{{< math display >}}\pi(\text{plateau})\approx\frac{0.25}{(1-q)N}=\frac{1}{N}{{< /math >}}</p>
<p>Fitness is a relative measure. At equilibrium {{< math >}}q{{< /math >}}, each option delivers the same fitness.</p>
</section>
<section id="idiosyncratic-versus-aggregate-risk" class="level3">
<h3 class="anchored" data-anchor-id="idiosyncratic-versus-aggregate-risk">Idiosyncratic versus aggregate risk</h3>
<p>I have created two hypothetical worlds, one making the case for maximising expected value despite being in a multiplicative world, and another where maximising the time-average growth rate is the optimal strategy. In both cases, the optimal strategy relies on the gene’s eye view. The variation comes from the probability structure of the environment.</p>
<p>I am hardly the first to propose this. I’m drawing on a rich history of research into the evolution of geometric growth rate maximisation in the biological literature. This in turn has been used by economic researchers such as <span class="citation" data-cites="robson2011">Robson and Samuelson (<a href="#ref-robson2011" role="doc-biblioref">2011</a>)</span> in the analysis of the evolution of preferences.</p>
<p>But, I like to think that this ergodicity economics exercise provides a nice opportunity to tie multiple threads together to provide a different perspective.</p>
<p>What’s next? I’ve been building a set of simulations examining mixed environments. What if the probabilistic structure of the environment is a mix of multiplicative and additive bets? You could think of the additive phase of the experiment I described earlier as comprising a few additive gambles in a multiplicative world. What if the environment switches between additive and multiplicative?</p>
<p>There isn’t a simple closed form solution to this problem. If you have a mix of additive and multiplicative bets, or even a non-constant multiplicative growth rate, an “ergodic observable” cannot easily be created. At present, it is best examined via simulation.</p>



</section>
</section>

<div id="quarto-appendix" class="default"><section class="quarto-appendix-contents" role="doc-bibliography" id="quarto-bibliography"><h2 class="anchored quarto-appendix-heading">References</h2><div id="refs" class="references csl-bib-body hanging-indent" data-entry-spacing="0" data-line-spacing="2" role="list">
<div id="ref-adamou2021" class="csl-entry" role="listitem">
Adamou, A., Berman, Y., Mavroyiannis, D., and Peters, O. (2021). Microfoundations of discounting. <em>Decision Analysis</em>, <em>18</em>(4), 257–272. <a href="https://doi.org/10.1287/deca.2021.0436">https://doi.org/10.1287/deca.2021.0436</a>
</div>
<div id="ref-brennan2011" class="csl-entry" role="listitem">
Brennan, T. J., and Lo, A. W. (2011). The origin of behavior. <em>The Quarterly Journal of Finance</em>, <em>01</em>(01), 55–108. <a href="https://doi.org/10.1142/S201013921100002X">https://doi.org/10.1142/S201013921100002X</a>
</div>
<div id="ref-cooper1982" class="csl-entry" role="listitem">
Cooper, W. S., and Kaplan, R. H. (1982). Adaptive <span>“</span>coin-flipping<span>”</span>: A decision-theoretic examination of natural selection for random individual variation. <em>Journal of Theoretical Biology</em>, <em>94</em>(1), 135–151. <a href="https://doi.org/10.1016/0022-5193(82)90336-8">https://doi.org/10.1016/0022-5193(82)90336-8</a>
</div>
<div id="ref-doctor2020" class="csl-entry" role="listitem">
Doctor, J. N., Wakker, P. P., and Wang, T. V. (2020). Economists<span>’</span> views on the ergodicity problem. <em>Nature Physics</em>, <em>16</em>(12), 1168–1168. <a href="https://doi.org/10.1038/s41567-020-01106-x">https://doi.org/10.1038/s41567-020-01106-x</a>
</div>
<div id="ref-ford2023" class="csl-entry" role="listitem">
Ford, M. C., and Kay, J. A. (2023). The limitations of growth- optimal approaches to decision making under uncertainty. <em>Econ Journal Watch</em>, <em>20</em>(2), 314–334. <a href="https://econjwatch.org/articles/the-limitations-of-growth-optimal-approaches-to-decision-making">https://econjwatch.org/articles/the-limitations-of-growth-optimal-approaches-to-decision-making</a>
</div>
<div id="ref-grafen1999" class="csl-entry" role="listitem">
Grafen, A. (1999). Formal darwinism, the individual<span></span>as<span></span>maximizing<span></span>agent analogy and bet<span></span>hedging. <em>Proceedings of the Royal Society of London. Series B: Biological Sciences</em>, <em>266</em>(1421), 799–803. <a href="https://doi.org/10.1098/rspb.1999.0708">https://doi.org/10.1098/rspb.1999.0708</a>
</div>
<div id="ref-meder2021" class="csl-entry" role="listitem">
Meder, D., Rabe, F., Morville, T., Madsen, K. H., Koudahl, M. T., … Hulme, O. J. (2021). Ergodicity-breaking reveals time optimal decision making in humans. <em>PLoS Computational Biology</em>, <em>17</em>(9), e1009217. <a href="https://doi.org/10.1371/journal.pcbi.1009217">https://doi.org/10.1371/journal.pcbi.1009217</a>
</div>
<div id="ref-peters2019" class="csl-entry" role="listitem">
Peters, O. (2019). The ergodicity problem in economics. <em>Nature Physics</em>, <em>15</em>(12), 1216–1221. <a href="https://doi.org/10.1038/s41567-019-0732-0">https://doi.org/10.1038/s41567-019-0732-0</a>
</div>
<div id="ref-peters2023" class="csl-entry" role="listitem">
Peters, O. (2023). Insurance as an ergodicity problem. <em>Annals of Actuarial Science</em>, <em>17</em>(2), 215–218. <a href="https://doi.org/10.1017/S1748499523000131">https://doi.org/10.1017/S1748499523000131</a>
</div>
<div id="ref-peters2022" class="csl-entry" role="listitem">
Peters, O., and Adamou, A. (2022). The ergodicity solution of the cooperation puzzle. <em>Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences</em>, <em>380</em>(2227), 20200425. <a href="https://doi.org/10.1098/rsta.2020.0425">https://doi.org/10.1098/rsta.2020.0425</a>
</div>
<div id="ref-robson2011" class="csl-entry" role="listitem">
Robson, A. J., and Samuelson, L. (2011). <em>The evolutionary foundations of preferences*</em> (J. Benhabib, A. Bisin, and M. O. Jackson, Eds.; Vol. 1, pp. 221–310). North-Holland. <a href="https://doi.org/10.1016/B978-0-444-53187-2.00007-3">https://doi.org/10.1016/B978-0-444-53187-2.00007-3</a>
</div>
<div id="ref-skjold" class="csl-entry" role="listitem">
Skjold, B., Steinkamp, S., Connaughton, C., Hulme, O. J., and Peters, O. (2024). <em>Ergodicity transformations predict human decision-making under risk</em>. <a href="https://doi.org/10.31219/osf.io/c96yd">https://doi.org/10.31219/osf.io/c96yd</a>
</div>
</div></section></div>
{{< /html >}}
