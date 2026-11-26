---
title: 'What can we infer about someone who rejects a 50:50 bet to win $110 or lose $100? The Rabin paradox explored'
author: "Jason Collins"
date: 2019-11-06 09:00:00+00:00
draft: false
sync_source: "posts/what-can-we-infer-about-someone-who-rejects-a-5050-bet-to-win-110-or-lose-100-the-rabin-paradox-explored.qmd"
sync_route: "quarto"
sync_hash: "f2bfa2f99bd9"
---

{{< html >}}
<p>Consider the following claim:</p>
<blockquote class="blockquote">
<p>We don’t need loss aversion to explain a person’s decision to reject a 50:50 bet to win $110 or lose $100. That is just risk aversion as in expected utility theory.</p>
</blockquote>
<p>Risk aversion is the concept that we prefer certainty to a gamble with the same expected value. For example, a risk-averse person would prefer $100 for certain over a 50-50 gamble between $0 and $200, which has an expected value of $100. The higher their risk aversion, the less they would value the 50:50 bet. They would also be willing to reject some positive expected value bets.</p>
<p>Loss aversion is the concept that losses loom larger than gains. If the loss is weighted more heavily than the gain - it is often said that losses hurt twice as much as gains bring us joy - then this could also explain the decision to reject a 50:50 bet of the type above. Loss aversion is distinct from risk aversion as its full force applies to the first dollar on either side of the reference point from which the person is assessing the change (and at which point risk aversion should be negligible).</p>
<p>So, do we need loss aversion to explain the rejection of this bet, or does risk aversion suffice?</p>
<p>One typical response to the above claim is loosely based on the Rabin Paradox, which comes from a paper published in 2000 by Matthew Rabin:</p>
<blockquote class="blockquote">
<p>An expected utility maximiser who rejects this bet is exhibiting a level of risk aversion that would lead them to reject bets that no one in their right mind would reject. It can’t be the case that this is simply risk aversion.</p>
</blockquote>
<p>For the remainder of this post I am going to pull apart Rabin’s argument from his justifiably famous paper <a href="https://doi.org/10.1111/1468-0262.00158">Risk Aversion and Expected-Utility Theory: A Calibration Theorem</a> (<a href="http://dklevine.com/archive/refs47667.pdf">pdf</a>). A more readable version of this argument was also published in 2001 in <a href="https://www.aeaweb.org/articles?id=10.1257/jep.15.1.219">an article by Rabin and Richard Thaler</a>.</p>
<p>To understand Rabin’s point, I have worked through the maths in his paper. You can see my mathematical workings in an Appendix at the bottom of this post. There were quite a few minor errors in the paper - and some major errors in the formulas - but I believe I’ve captured the crux of the argument. (I’d be grateful for some second opinions on this).</p>
<p>I started working through these two articles with the impression that Rabin’s argument was a fatal blow to the idea that expected utility theory accurately describes the rejection of bets such as that above. I would have been comfortable making the above response. However, after playing with the numbers and developing a better understanding of the paper, I would say that the above response is not strictly true. Rabin’s paper makes an important point, but it is far from a fatal blow by itself. (That fatal blow does come, just not solely from here.)</p>
<section id="describing-rabins-argument" class="level2">
<h2 class="anchored" data-anchor-id="describing-rabins-argument">Describing Rabin’s argument</h2>
<p>Rabin’s argument starts with a simple bet: suppose you are offered a 50:50 bet to win $110 or lose $100, and you turn it down. Suppose further that you would reject this bet no matter what your wealth (this is an assumption we will turn to in more detail later). What can you infer about your response to other bets?</p>
<p>This depends on what decision-making model you are using.</p>
<p>For an expected utility maximiser - someone who maximises the probability-weighted subjective value of these bets - we can infer that they will turn down any 50:50 bet of losing $1,000 and gaining any amount of money. For example, they would reject a 50:50 bet to lose $1,000, win one billion dollars.</p>
<p>On face value, that is ridiculous, and that is the crux of Rabin’s argument. Rejection of the low-value bet to win $110 and lose $100 would lead to absurd responses to higher-value bets. This leads Rabin to argue that risk aversion or the diminishing value of money has nothing to do with the rejection of the low-value bets.</p>
<p>The intuition behind Rabin’s argument is relatively simple. Suppose we have someone that rejects a 50:50 bet for gain $11, lose $10. They are an expected utility maximiser with a weakly concave utility curve: that is, they are risk neutral or risk averse at all levels of wealth.</p>
<p>From this, we can infer that they weight the average of each dollar between their current wealth (W) and their wealth if they win the bet (W+11) only 10/11 as much as they weight the average dollar of the last $10 of their current wealth (between W-10 and W). We can also say that they therefore weight their W+11th dollar at most 10/11 as much as their W-10th dollar (relying on the weak concavity here).</p>
<p>Suppose their wealth is now W+21. We have assumed that they will reject the bet at all levels of wealth, so they will also reject at this wealth. Iterating the previous calculations, we can say that they will weight their W+32nd dollar only 10/11 as much as their W+11th dollar. This means they value their W+32nd dollar only (10/11)<sup>2</sup> as much as their W-10th dollar.</p>
<p>Keep iterating in this way and you end up with some ridiculous results. You value the 210th dollar above your current wealth only 40% as much as your last current dollar of your wealth [reducing by a constant factor of 10/11 every $21 - (10/11)<sup>10</sup>]. Or you value the 900th dollar above your current wealth at only 2% of your last current dollar [(10/11)<sup>40</sup>]. This is an absurd rate of discounting.</p>
<p>Those numbers are from the 2001 Rabin and Thaler paper. In his 2000 paper, Rabin gives figures of 3/20 for the 220th and 1/2000 for the 880th dollar, effectively calculating (10/11)<sup>20</sup> and (10/11)<sup>80</sup>, which is a reduction by a factor of 10/11 every 11 dollars. This degree of discounting could be justified and reflects the equations provided in the Appendix to his paper, but it requires a slightly different intuition than the one relating to the comparison between every 21st dollar. If instead you note that the $11 above a reference point is valued less than the $10 below, you only need to iterate up $11 to get another discount of 10/11, as the next $11 is valued at most as much as the previous $10.</p>
<p>Regardless of whether you use the numbers from the 2000 or 2001 paper, taking this iteration to the extreme, it doesn’t take long for additional money to have effectively zero value. Hence the result, reject the 50:50 win $110, lose $100 and you’ll reject the win any amount, lose $1,000 bet.</p>
</section>
<section id="what-is-the-utility-curve-of-this-person" class="level2">
<h2 class="anchored" data-anchor-id="what-is-the-utility-curve-of-this-person">What is the utility curve of this person?</h2>
<p>This argument sounds compelling, but we need to examine the assumption that you will reject the bet at all levels of wealth.</p>
<p>If someone rejects the bet at all levels of wealth, what is the least risk averse they could be? They would be close to indifferent to the bet at all levels of wealth. If that were the case across the whole utility curve, their absolute level of risk aversion is constant.</p>
<p>The equation used to represent utility with constant absolute risk aversion is <a href="https://en.wikipedia.org/wiki/Exponential_utility">exponential utility</a> (with a&gt;0). A feature of the exponential utility function is that, for a risk averse person, utility caps out at a maximum. Beyond a certain level of wealth, they gain no additional utility - hence Rabin’s ability to define bets where they reject infinite gains.</p>
<p>The need for utility to cap out is also apparent from the fact that someone might reject a bet that involves the potential for infinite gain. The utility of infinite wealth cannot be infinite, as any bet involving the potential for infinite utility would be accepted, no matter how small the probability of that infinite gain.</p>
<p>In the 2000 paper, Rabin brings the constant absolute risk aversion function into his argument more explicitly when he examines what proportion of their portfolio a person with an exponential utility function would invest in stocks (under some particular return assumptions). There he shows a ridiculous level of risk aversion and states that “While it is widely believed that investors are too cautious in their investment behavior, no one believes they are this risk averse.”</p>
<p>However, this effective (or explicit) assumption of constant absolute risk aversion is not particularly well grounded. Most empirical evidence is that people exhibit decreasing absolute risk aversion, not constant. Exponential utility functions are used more for mathematical tractability than for realistically reflecting the decision making processes that people use.</p>
<p>Yet, under Rabin’s assumption of rejecting the bet at all levels of wealth, constant absolute risk aversion and a utility function such as the exponential is the most accommodating assumption we can make. While Rabin states that “no one believes they are this risk averse”, it’s not clear that anyone believes Rabin’s underlying assumption either.</p>
<p>This ultimately means that the ridiculous implications for rejecting low-value bets is the result of Rabin’s unrealistic assumption of rejecting the bet no matter what their wealth.</p>
</section>
<section id="relaxing-the-all-levels-of-wealth-assumption" class="level2">
<h2 class="anchored" data-anchor-id="relaxing-the-all-levels-of-wealth-assumption">Relaxing the “all levels of wealth” assumption</h2>
<p>Rabin is, of course, aware that the assumption of rejecting the bet at all levels of wealth is a weakness, so he provides a further example that applies to someone who only rejects this bet for all levels of wealth below $300,000.</p>
<p>This generates less extreme but still clearly problematic bets that the bettor can be inferred to also reject.</p>
<p>For example, consider someone who rejects the 50:50 bet to win $110, lose $100 when they have $290,000 of wealth, and who would also reject that bet up to a wealth of $300,000. As for the previous example, each time you iterate up $110, each dollar in that $110 is valued at most 10/11 of the previous $110. It takes 90 iterations of $110 to cover that $10,000, meaning that a dollar around wealth $300,000 will be valued only (10/11)<sup>90</sup> (0.02%) of a dollar at wealth $290,000. Each dollar above $300,000 is not discounted any further, but by then the damage has already been done, with that money of almost no utility.</p>
<p>For instance, this person will reject a bet of gain $718,190, lose $1,000. Again, this person would be out of their mind.</p>
<p>You might now ask whether a person with a wealth of $290,000 to $300,000 actually rejects bets of this nature? If not, isn’t this just another unjustifiable assumption designed to generate a ridiculous result?</p>
<p>It is possible to make this scenario more realistic. Rabin doesn’t mention this in his paper (nor do Rabin and Thaler), but we can generate the same result at much lower levels of wealth. All we need to find is someone who will reject that bet over a range of $10,000, and still have enough wealth to bear the loss - say someone who will reject that bet up to a wealth of $11,000. That person will also reject a win $718,190 lose $1,000 bet.</p>
<p>Rejection of the win $110, lose $100 bet over that range does not seem as unrealistic, and I could imagine a person with that preference existing. If we empirically tested this, we would also need to examine liquid wealth and cash flow, but the example does provide a sense that we could find some people whose rejection of low-value bets would generate absurd results under expected utility maximisation.</p>
</section>
<section id="the-log-utility-function" class="level2">
<h2 class="anchored" data-anchor-id="the-log-utility-function">The log utility function</h2>
<p>Let’s compare Rabin’s example utility function with a more commonly assumed utility function, that of log utility. Log utility has decreasing absolute risk aversion (and constant relative risk aversion), so is both more empirically defensible and does not generate utility that asymptotes to a maximum like the exponential utility function.</p>
<p>A person with log utility would reject the 50:50 bet to win $110, lose $100 up to a wealth of $1,100. Beyond that, they would accept the bet. So, for log utility we should see most people accept this bet.</p>
<p>A person with log utility will reject some quite unbalanced bets: such as a 50:50 bet to win $1 million, lose $90,900, but only up to a wealth of $100,000, beyond which they would accept. Rejection only occurs when a loss is near ruinous.</p>
<p>The result is that log utility does not generate the types of rejected bets that Rabin labels as ridiculous, but would also fail to provide much of an explanation for the rejection of low-value bets with positive expected value.</p>
</section>
<section id="the-empirical-evidence" class="level2">
<h2 class="anchored" data-anchor-id="the-empirical-evidence">The empirical evidence</h2>
<p>Do people actually turn down 50:50 bets of win $110, lose $100? Surprisingly, I couldn’t find an example of this bet (if someone knows a paper that directly tests this, let me know).</p>
<p>Most examinations of loss aversion examine symmetric 50:50 bets where the potential gain and the loss are the same. They compare a bet centred around 0 (e.g.&nbsp;gain $100 or lose $100) and a similar bet in a gain frame (e.g.&nbsp;gain $100 or gain $300, or take $200 for certain). If more people reject the first bet than the latter, then this is evidence of loss aversion.</p>
<p>It makes sense that this is the experimental approach. If the bet is not symmetric, it becomes hard to tease out loss aversion from risk aversion.</p>
<p>However, there is a pattern in the literature that people often reject risky bets with a positive expected value in the ranges explored by Rabin. We don’t know a lot about their wealth (or liquidity), but Rabin’s illustrative numbers for rejected bets don’t seem completely unrealistic. It’s the range of wealth over which the rejection occurs that is questionable.</p>
<p>Rather than me floundering around on this point, some papers explicitly ask whether we can observe a set of bets for a group of experimental subjects and map a curve to those choices that resembles expected utility.</p>
<p>For instance, <a href="https://doi.org/10.1257/000282802762024700">Holt and Laury’s 2002 AER paper</a> (<a href="https://econweb.ucsd.edu/~jandreon/Econ264/papers/Holt%20Laury%20AER%202002.pdf">pdf</a>) examined a set of hypothetical and incentivised bets over a range of stakes (finding among other things that hypothetical predictions of their response to incentivised high-stakes bets were not very accurate). They found that if you are flexible about the form of the expected utility function that is used, rejection of small gambles does not result in absurd conclusions on large gambles. The pattern of bets could be made consistent with expected utility, assuming you correctly parameterise the equation. Over subsequent years there was some back and forth on whether this finding was robust [see <a href="https://doi.org/10.1257/0002828054201378">here</a> (<a href="http://pdfs.semanticscholar.org/924d/fb5180d98767b630e3ae468da0c166a0890a.pdf?_ga=2.18923384.1759154274.1571603876-1728413697.1571603876">pdf</a>) and <a href="https://doi.org/10.1257/0002828054201459">here</a> (<a href="http://home.cerge-ei.cz/ortmann/trentocourse/Holt_Laury_Incentive_Effects_AER_2005.pdf">pdf</a>)], but the basic result seemed to hold.</p>
<p>The utility curve that best matched Holt and Laury’s experimental findings had increasing relative risk aversion, and decreasing absolute risk aversion. By having decreasing absolute risk aversion, the absurd implications of Rabin’s paper are avoided.</p>
<p>Papers such as this suggest that while Rabin’s paper makes an important point, its underlying assumptions are not consistent with empirical evidence. It is possible to have an expected utility maximiser reject low-value bets without generating ridiculous outcomes.</p>
<p>So what can you infer about our bettor who has rejected the win $110, lose $100 bet?</p>
<p>From the argument above, I would say not much. We could craft a utility function to accommodate this bet without leading to ridiculous consequences. I feel this defence is laboured (that’s a subject for another day), but the bet is not in itself fatal to the argument that they are an expected utility maximiser.</p>
<p>My other posts on loss aversion can be found here:</p>
<ol type="1">
<li><a href="../posts/kahneman-and-tverskys-debatable-loss-aversion-assumption.html">Kahneman and Tversky’s debatable loss aversion assumption</a></li>
<li><a href="../posts/what-can-we-infer-about-someone-who-rejects-a-5050-bet-to-win-110-or-lose-100-the-rabin-paradox-explored.html">What can we infer about someone who rejects a 50:50 bet to win $110 or lose $100? The Rabin paradox explored</a> (this post)</li>
<li><a href="../posts/the-case-against-loss-aversion.html">The case against loss aversion</a></li>
<li><a href="../posts/ergodicity-economics-a-primer.html">Ergodicity economics - a primer</a></li>
</ol>
<p>–</p>
</section>
<section id="appendix" class="level2">
<h2 class="anchored" data-anchor-id="appendix">Appendix</h2>
<section id="the-utility-of-a-gain" class="level3">
<h3 class="anchored" data-anchor-id="the-utility-of-a-gain">The utility of a gain</h3>
<p>Let’s suppose someone will reject a 50:50 bet with gain {{< math >}}g{{< /math >}} and loss {{< math >}}l{{< /math >}} for any level of wealth. What utility will they get from a gain of {{< math >}}x{{< /math >}}? Rabin defines an upper bound of the utility of gaining {{< math >}}x{{< /math >}} to be:</p>
<p>{{< math display >}}U(w+x)-U(w)\leq\sum_{i=0}^{k^{**}(x)}\left(\frac{l}{g}\right)^ir(w){{< /math >}}</p>
<p>{{< math display >}}k^{**}(x)=int\left(\frac{x}{g}\right){{< /math >}}</p>
<p>{{< math display >}}r(w)=U(w)-U(w-l){{< /math >}}</p>
<p>This formula effectively breaks down {{< math >}}x{{< /math >}} into {{< math >}}g{{< /math >}} size components, successively discounting each additional {{< math >}}g{{< /math >}} at {{< math >}}l/g{{< /math >}} of the previous {{< math >}}g{{< /math >}}.</p>
<p>You need {{< math >}}k^{**}(x)+1{{< /math >}} lots of {{< math >}}g{{< /math >}} to cover {{< math >}}x{{< /math >}}. For instance, if {{< math >}}x{{< /math >}} was 32 and we had a 50:50 bet for win $11, lose $10, {{< math >}}32/11=2{{< /math >}}. You need 2+1 lots of 11 to fully cover 32. It actually covers a touch more than 32, hence the calculation being for an upper bound.</p>
<p>In the paper, Rabin defines {{< math >}}k^{**}(x)=int((x/g)+1){{< /math >}}. This seems to better capture the required number of {{< math >}}g{{< /math >}} to fully cover {{< math >}}x{{< /math >}}, but the iterations in the above formula start at {{< math >}}i=0{{< /math >}}. The calculations I run below with my version of the formula replicate Rabin’s, supporting the suggestion that the addition of 1 in the paper is an error.</p>
<p>{{< math >}}r(w){{< /math >}} is shorthand for the amount of utility sacrificed from losing the gamble (i.e.&nbsp;losing {{< math >}}l{{< /math >}}). We know that the utility of the gain {{< math >}}g{{< /math >}} is less than this, as the bet is rejected. If we let {{< math >}}r(w)=1{{< /math >}}, the equation can be thought of as giving you the maximum utility you could get from the gain of {{< math >}}x{{< /math >}} relative to the utility of the loss of {{< math >}}l{{< /math >}}.</p>
<p>Putting this together, the upper bound of the utility of the possible gain {{< math >}}x{{< /math >}} is therefore less than, first, the upper bound of the relative utility from the first $11, {{< math >}}(10/11)^0r(w)=r(w){{< /math >}}, the upper bound of utility from the next $11, {{< math >}}(10/11)^1r(w){{< /math >}}, and the upper bound of the utility from the remaining $10 - taking a conservative approach this is calculated as though it were a full $11: {{< math >}}(10/11)^2r(w){{< /math >}}.</p>
</section>
<section id="the-utility-of-a-loss" class="level3">
<h3 class="anchored" data-anchor-id="the-utility-of-a-loss">The utility of a loss</h3>
<p>Rabin also gives us a lower bound of the utility of a loss of {{< math >}}x{{< /math >}} for this person who will reject a 50:50 bet with gain {{< math >}}g{{< /math >}} and loss {{< math >}}l{{< /math >}} for any level of wealth:</p>
<p>{{< math display >}}U(w)-U(w-x)\geq{2}\sum_{i=1}^{k^{*}(x)}\left(\frac{g}{l}\right)^{i-1}{r(w)}{{< /math >}}</p>
<p>{{< math display >}}k^{*}(x)=int\left(\frac{x}{2l}\right){{< /math >}}</p>
<p>The intuition behind {{< math >}}k^{*}(x){{< /math >}} comes from Rabin’s desire to provide a relatively uncomplicated proof for the proposition. Effectively, the utility scales down with each step of {{< math >}}g{{< /math >}} by at least {{< math >}}g/l{{< /math >}}. Since Rabin wants to express this in terms of losses, he defines {{< math >}}2l\geq{g}\geq{l}{{< /math >}}. He can thereby say that utility scales down by at least {{< math >}}\frac{g}{l}{{< /math >}} every 2 lots of {{< math >}}l{{< /math >}}.</p>
<p>Otherwise, the intuition for this loss formula is the same as that for the gain. The summation starts at {{< math >}}i=1{{< /math >}} as this formula is providing a lower bound, so does not require the final iteration to fully cover {{< math >}}x{{< /math >}}. The formula is also multiplied by 2 as each iteration covers two lots of {{< math >}}l{{< /math >}}, whereby r(w) is for a single span of {{< math >}}l{{< /math >}}.</p>
</section>
<section id="running-some-numbers" class="level3">
<h3 class="anchored" data-anchor-id="running-some-numbers">Running some numbers</h3>
<p>The below code implements the above two formulas as a function, calculating the potential utility gain for a win of {{< math >}}G{{< /math >}} or a loss of {{< math >}}L{{< /math >}} for a person who rejects a 50:50 bet win {{< math >}}g{{< /math >}}, lose {{< math >}}l{{< /math >}} at all levels of wealth. It then states whether we know the person will reject a win {{< math >}}G{{< /math >}}, lose {{< math >}}L{{< /math >}} bet - we can’t state they will accept as we have upper and lower bounds of the utility change from the gain and loss.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb1"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a>Rabin_bet <span class="ot">&lt;-</span> <span class="cf">function</span>(g, l, G, L){</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a>  k_2star <span class="ot">&lt;-</span> <span class="fu">as.integer</span>(G<span class="sc">/</span>g)</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a>  k_star <span class="ot">&lt;-</span> <span class="fu">as.integer</span>(L<span class="sc">/</span>(<span class="dv">2</span><span class="sc">*</span>l))</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a>  U_gain <span class="ot">&lt;-</span> <span class="dv">0</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a>  <span class="cf">for</span> (i <span class="cf">in</span> <span class="dv">0</span><span class="sc">:</span>k_2star) {</span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a>    U_step <span class="ot">&lt;-</span> (l<span class="sc">/</span>g)<span class="sc">^</span>i</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a>    U_gain <span class="ot">&lt;-</span> U_gain <span class="sc">+</span> U_step</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a>  U_loss <span class="ot">&lt;-</span> <span class="dv">0</span></span>
<span id="cb1-13"><a href="#cb1-13" aria-hidden="true" tabindex="-1"></a>  <span class="cf">for</span> (i <span class="cf">in</span> <span class="dv">1</span><span class="sc">:</span>k_star) {</span>
<span id="cb1-14"><a href="#cb1-14" aria-hidden="true" tabindex="-1"></a>    U_step <span class="ot">&lt;-</span> <span class="dv">2</span><span class="sc">*</span>(g<span class="sc">/</span>l)<span class="sc">^</span>(i<span class="dv">-1</span>)</span>
<span id="cb1-15"><a href="#cb1-15" aria-hidden="true" tabindex="-1"></a>    U_loss <span class="ot">&lt;-</span> U_loss <span class="sc">+</span> U_step</span>
<span id="cb1-16"><a href="#cb1-16" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb1-17"><a href="#cb1-17" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-18"><a href="#cb1-18" aria-hidden="true" tabindex="-1"></a>  <span class="fu">ifelse</span>(U_gain <span class="sc">&lt;</span> U_loss,</span>
<span id="cb1-19"><a href="#cb1-19" aria-hidden="true" tabindex="-1"></a>         <span class="fu">print</span>(<span class="st">"REJECT"</span>),</span>
<span id="cb1-20"><a href="#cb1-20" aria-hidden="true" tabindex="-1"></a>         <span class="fu">print</span>(<span class="st">"CANNOT CONFIRM REJECT"</span>)</span>
<span id="cb1-21"><a href="#cb1-21" aria-hidden="true" tabindex="-1"></a>         )</span>
<span id="cb1-22"><a href="#cb1-22" aria-hidden="true" tabindex="-1"></a>  <span class="fu">print</span>(<span class="fu">paste0</span>(<span class="st">"Max U from gain ="</span>, U_gain))</span>
<span id="cb1-23"><a href="#cb1-23" aria-hidden="true" tabindex="-1"></a>  <span class="fu">print</span>(<span class="fu">paste0</span>(<span class="st">"Min U from loss ="</span>, U_loss))</span>
<span id="cb1-24"><a href="#cb1-24" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></div>
</details>
</div>
<p>Take a person who will reject a 50:50 bet to win $110, lose $100. Taking the table from the paper, they would reject a win $1,000,000,000, lose $1,000 bet.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb2"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">Rabin_bet</span>(<span class="dv">110</span>, <span class="dv">100</span>, <span class="dv">1000000000</span>, <span class="dv">1000</span>)</span></code></pre></div></div>
</details>
<div class="cell-output cell-output-stdout">
<pre><code>[1] "REJECT"
[1] "Max U from gain =11"
[1] "Min U from loss =12.2102"</code></pre>
</div>
</div>
</section>
</section>
<section id="relaxing-the-wealth-assumption" class="level2">
<h2 class="anchored" data-anchor-id="relaxing-the-wealth-assumption">Relaxing the wealth assumption</h2>
<p>In the Appendix of his paper, Rabin defines his proof where the bet is rejected over a range of wealth {{< math >}}w\in(\bar w, \underline{w}){{< /math >}}. In that case, relative utility for each additional gain of size {{< math >}}g{{< /math >}} is {{< math >}}l/g{{< /math >}} of the previous {{< math >}}g{{< /math >}} until {{< math >}}\bar w{{< /math >}}. Beyond that point, each additional gain of {{< math >}}g{{< /math >}} gives constant utility until {{< math >}}x{{< /math >}} is reached. The formula for the upper bound on the utility gain is:</p>
<p>{{< math display >}}U(w+x)-U(w)\leq
\left\{
\begin{matrix*}[l]
\displaystyle \sum_{i=0}^{k^{**}(x)} \left(\frac{l}{g}\right)^ir(w) & \text{if}&\quad x\leq{\bar w}-w\\[18pt]
\displaystyle\sum_{i=0}^{k^{**}(\bar w)}\left(\frac{l}{g}\right)^{i}r(w)+\left[\frac{x-(\bar w-w)}{g}\right]\left(\frac{l}{g}\right)^{k^{**}(\bar w)}r(w) & \text{if}&\quad x\geq{\bar w}-w
\end{matrix*}
\right.{{< /math >}}</p>
<p>The first term of the equation where {{< math >}}x\geq\bar w-w{{< /math >}} involves iterated discounting as per the situation where the bet is rejected for all levels of wealth, but here the iteration is only up to wealth {{< math >}}\bar w{{< /math >}}. The second term of that equation captures the gain beyond {{< math >}}\bar w{{< /math >}} discounted at a constant rate.</p>
<p>There is an error in Rabin’s formula in the paper. Rather than the term {{< math >}}(x-(\bar w-w))/g{{< /math >}} in the second equation, Rabin has it as {{< math >}}x-\bar w{{< /math >}}. As for the previous equations, we need to know the number of iterations of the gain, not total dollars, and we need this between {{< math >}}\bar w{{< /math >}} and {{< math >}}w+x{{< /math >}}.</p>
<p>When Rabin provides the examples in Table II of the paper, from the numbers he provides I believe he uses a formula of the type {{< math >}}int[(x-(w-\underline w))/g+1]{{< /math >}}, which reflects a desire to calculate the upper-bound utility across the stretch above {{< math >}}\bar w{{< /math >}} in a similar manner to below, although this is not strictly necessary given the discount is constant across this range. I have implemented as per my formula, which means that bets are still rejected {{< math >}}g{{< /math >}} higher than for Rabin (which given their scale is not material).</p>
<p>Similarly, for the loss:</p>
<p>{{< math display >}}U(w)-U(w-x)\geq
\left
\{\begin{matrix*}[l]
2\displaystyle\sum_{i=1}^{k^{*}(x)}\left(\frac{g}{l}\right)^{i-1}r(w)\quad &\text{if}\quad {w-\underline w+2l}\geq{x}\geq{2l}\\[18pt]
2\displaystyle\sum_{i=1}^{k^{*}(w-\underline w+2l)}\left(\frac{g}{l}\right)^{i-1}{r(w)}+\\[12pt]
\displaystyle\qquad\left[\frac{x-(w-\underline w+l)}{2l}\right]\left(\frac{g}{l}\right)^{k^{*}(w-\underline w+2l)}{r(w)} &\text{if}\quad x\geq{w-\underline w+2l}
\end{matrix*}
\right.{{< /math >}}</p>
<p>There is a similar error here, with Rabin using the term {{< math >}}x-(w-\underline w+l){{< /math >}} rather than {{< math >}}(x-(w-\underline w+l))/2l{{< /math >}}. I can’t determine how this was implemented by Rabin as his examples do not examine behaviour below a lower bound {{< math >}}\underline w{{< /math >}}.</p>
<section id="running-some-more-numbers" class="level3">
<h3 class="anchored" data-anchor-id="running-some-more-numbers">Running some more numbers</h3>
<p>The below R code implements the above two formulas as a function, calculating the potential utility gain for a win of {{< math >}}G{{< /math >}} or a loss of {{< math >}}L{{< /math >}} for a person who rejects a 50:50 bet win {{< math >}}g{{< /math >}}, lose {{< math >}}l{{< /math >}} at wealth {{< math >}}w\in(\bar w, \underline{w}){{< /math >}}. It then states whether we know the person will reject a win {{< math >}}G{{< /math >}}, lose {{< math >}}L{{< /math >}} bet - as before, we can’t state they will accept as we have upper and lower bounds of the utility change from the gain and loss.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb4"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>Rabin_bet_general <span class="ot">&lt;-</span> <span class="cf">function</span>(g, l, G, L, w, w_max, w_min){</span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>  <span class="fu">ifelse</span>(</span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>    G <span class="sc">&lt;=</span> (w_max<span class="sc">-</span>w),</span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a>    k_2star <span class="ot">&lt;-</span> <span class="fu">as.integer</span>(G<span class="sc">/</span>g),</span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>    k_2star <span class="ot">&lt;-</span> <span class="fu">as.integer</span>((w_max<span class="sc">-</span>w)<span class="sc">/</span>g)</span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>  )</span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-9"><a href="#cb4-9" aria-hidden="true" tabindex="-1"></a>   <span class="fu">ifelse</span>(</span>
<span id="cb4-10"><a href="#cb4-10" aria-hidden="true" tabindex="-1"></a>    w<span class="sc">-</span>w_min<span class="sc">+</span><span class="dv">2</span><span class="sc">*</span>l <span class="sc">&gt;=</span> L,</span>
<span id="cb4-11"><a href="#cb4-11" aria-hidden="true" tabindex="-1"></a>    k_star <span class="ot">&lt;-</span> <span class="fu">as.integer</span>(L<span class="sc">/</span>(<span class="dv">2</span><span class="sc">*</span>l)),</span>
<span id="cb4-12"><a href="#cb4-12" aria-hidden="true" tabindex="-1"></a>    k_star <span class="ot">&lt;-</span> <span class="fu">as.integer</span>((w<span class="sc">-</span>w_min<span class="sc">+</span><span class="dv">2</span><span class="sc">*</span>l)<span class="sc">/</span>(<span class="dv">2</span><span class="sc">*</span>l))</span>
<span id="cb4-13"><a href="#cb4-13" aria-hidden="true" tabindex="-1"></a>  )</span>
<span id="cb4-14"><a href="#cb4-14" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-15"><a href="#cb4-15" aria-hidden="true" tabindex="-1"></a>  U_gain <span class="ot">&lt;-</span> <span class="dv">0</span></span>
<span id="cb4-16"><a href="#cb4-16" aria-hidden="true" tabindex="-1"></a>  <span class="cf">for</span> (i <span class="cf">in</span> <span class="dv">0</span><span class="sc">:</span>k_2star) {</span>
<span id="cb4-17"><a href="#cb4-17" aria-hidden="true" tabindex="-1"></a>    U_step <span class="ot">&lt;-</span> (l<span class="sc">/</span>g)<span class="sc">^</span>i</span>
<span id="cb4-18"><a href="#cb4-18" aria-hidden="true" tabindex="-1"></a>    U_gain <span class="ot">&lt;-</span> U_gain <span class="sc">+</span> U_step</span>
<span id="cb4-19"><a href="#cb4-19" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb4-20"><a href="#cb4-20" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-21"><a href="#cb4-21" aria-hidden="true" tabindex="-1"></a>  <span class="fu">ifelse</span>(</span>
<span id="cb4-22"><a href="#cb4-22" aria-hidden="true" tabindex="-1"></a>    G <span class="sc">&lt;=</span> (w_max<span class="sc">-</span>w),</span>
<span id="cb4-23"><a href="#cb4-23" aria-hidden="true" tabindex="-1"></a>    U_gain <span class="ot">&lt;-</span> U_gain,</span>
<span id="cb4-24"><a href="#cb4-24" aria-hidden="true" tabindex="-1"></a>    U_gain <span class="ot">&lt;-</span> U_gain <span class="sc">+</span> ((G<span class="sc">-</span>(w_max<span class="sc">-</span>w))<span class="sc">/</span>g)<span class="sc">*</span>(l<span class="sc">/</span>g)<span class="sc">^</span>k_2star</span>
<span id="cb4-25"><a href="#cb4-25" aria-hidden="true" tabindex="-1"></a>  )</span>
<span id="cb4-26"><a href="#cb4-26" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-27"><a href="#cb4-27" aria-hidden="true" tabindex="-1"></a>  U_loss <span class="ot">&lt;-</span> <span class="dv">0</span></span>
<span id="cb4-28"><a href="#cb4-28" aria-hidden="true" tabindex="-1"></a>  <span class="cf">for</span> (i <span class="cf">in</span> <span class="dv">1</span><span class="sc">:</span>k_star) {</span>
<span id="cb4-29"><a href="#cb4-29" aria-hidden="true" tabindex="-1"></a>    U_step <span class="ot">&lt;-</span> <span class="dv">2</span><span class="sc">*</span>(g<span class="sc">/</span>l)<span class="sc">^</span>(i<span class="dv">-1</span>)</span>
<span id="cb4-30"><a href="#cb4-30" aria-hidden="true" tabindex="-1"></a>    U_loss <span class="ot">&lt;-</span> U_loss <span class="sc">+</span> U_step</span>
<span id="cb4-31"><a href="#cb4-31" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb4-32"><a href="#cb4-32" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-33"><a href="#cb4-33" aria-hidden="true" tabindex="-1"></a>  <span class="fu">ifelse</span>(</span>
<span id="cb4-34"><a href="#cb4-34" aria-hidden="true" tabindex="-1"></a>    w<span class="sc">-</span>w_min<span class="sc">+</span><span class="dv">2</span><span class="sc">*</span>l <span class="sc">&gt;=</span> L,</span>
<span id="cb4-35"><a href="#cb4-35" aria-hidden="true" tabindex="-1"></a>    U_loss <span class="ot">&lt;-</span> U_loss,</span>
<span id="cb4-36"><a href="#cb4-36" aria-hidden="true" tabindex="-1"></a>    U_loss <span class="ot">&lt;-</span> U_loss <span class="sc">+</span> ((L<span class="sc">-</span>(w<span class="sc">-</span>w_min<span class="sc">+</span>l))<span class="sc">/</span>(<span class="dv">2</span><span class="sc">*</span>l))<span class="sc">*</span>(g<span class="sc">/</span>l)<span class="sc">^</span>k_star</span>
<span id="cb4-37"><a href="#cb4-37" aria-hidden="true" tabindex="-1"></a>  )</span>
<span id="cb4-38"><a href="#cb4-38" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-39"><a href="#cb4-39" aria-hidden="true" tabindex="-1"></a>  <span class="fu">ifelse</span>(U_gain <span class="sc">&lt;</span> U_loss,</span>
<span id="cb4-40"><a href="#cb4-40" aria-hidden="true" tabindex="-1"></a>         <span class="fu">print</span>(<span class="st">"REJECT"</span>),</span>
<span id="cb4-41"><a href="#cb4-41" aria-hidden="true" tabindex="-1"></a>         <span class="fu">print</span>(<span class="st">"CANNOT CONFIRM REJECT"</span>)</span>
<span id="cb4-42"><a href="#cb4-42" aria-hidden="true" tabindex="-1"></a>         )</span>
<span id="cb4-43"><a href="#cb4-43" aria-hidden="true" tabindex="-1"></a>  <span class="fu">print</span>(<span class="fu">paste0</span>(<span class="st">"Max U from gain ="</span>, U_gain))</span>
<span id="cb4-44"><a href="#cb4-44" aria-hidden="true" tabindex="-1"></a>  <span class="fu">print</span>(<span class="fu">paste0</span>(<span class="st">"Min U from loss ="</span>, U_loss))</span>
<span id="cb4-45"><a href="#cb4-45" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></div>
</details>
</div>
<p>Imagine someone who turns down the win $110, lose $100 bet with a wealth of $290,000, but who would only reject this bet up to $300,000. They will reject a win $718,190, lose $1000 bet.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb5"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a><span class="fu">Rabin_bet_general</span>(<span class="dv">110</span>, <span class="dv">100</span>, <span class="dv">718190</span>, <span class="dv">1000</span>, <span class="dv">290000</span>, <span class="dv">300000</span>, <span class="dv">0</span>)</span></code></pre></div></div>
</details>
<div class="cell-output cell-output-stdout">
<pre><code>[1] "REJECT"
[1] "Max U from gain =12.2098745626936"
[1] "Min U from loss =12.2102"</code></pre>
</div>
</div>
<p>The nature of Rabin’s calculation means that we can scale this calculation to anywhere on the wealth curve. We need only say that someone who rejects this bet over (roughly) a range of $10,000 plus the size of the potential loss will exhibit the same decisions. For example a person with $10,000 wealth who would reject the bet up to $20,000 wealth would also reject the win $718,190, lose $1000 bet.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb7"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1"></a><span class="fu">Rabin_bet_general</span>(<span class="dv">110</span>, <span class="dv">100</span>, <span class="dv">718190</span>, <span class="dv">1000</span>, <span class="dv">10000</span>, <span class="dv">20000</span>, <span class="dv">0</span>)</span></code></pre></div></div>
</details>
<div class="cell-output cell-output-stdout">
<pre><code>[1] "REJECT"
[1] "Max U from gain =12.2098745626936"
[1] "Min U from loss =12.2102"</code></pre>
</div>
</div>
</section>
<section id="comparison-with-log-utility" class="level3">
<h3 class="anchored" data-anchor-id="comparison-with-log-utility">Comparison with log utility</h3>
<p>The below is an example with log utility, which is {{< math >}}U(W)=ln(W){{< /math >}}. This function determines whether someone of wealth {{< math >}}w{{< /math >}} will reject or accept a 50:50 bet for gain {{< math >}}g{{< /math >}} and loss {{< math >}}l{{< /math >}}.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb9"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb9-1"><a href="#cb9-1" aria-hidden="true" tabindex="-1"></a>log_utility <span class="ot">&lt;-</span> <span class="cf">function</span>(g, l, w){</span>
<span id="cb9-2"><a href="#cb9-2" aria-hidden="true" tabindex="-1"></a>  log_gain <span class="ot">&lt;-</span> <span class="fu">log</span>(w<span class="sc">+</span>g)</span>
<span id="cb9-3"><a href="#cb9-3" aria-hidden="true" tabindex="-1"></a>  log_loss <span class="ot">&lt;-</span> <span class="fu">log</span>(w<span class="sc">-</span>l)</span>
<span id="cb9-4"><a href="#cb9-4" aria-hidden="true" tabindex="-1"></a>  EU_bet <span class="ot">&lt;-</span> <span class="fl">0.5</span><span class="sc">*</span>log_gain <span class="sc">+</span> <span class="fl">0.5</span><span class="sc">*</span>log_loss</span>
<span id="cb9-5"><a href="#cb9-5" aria-hidden="true" tabindex="-1"></a>  EU_certain <span class="ot">&lt;-</span> <span class="fu">log</span>(w)</span>
<span id="cb9-6"><a href="#cb9-6" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb9-7"><a href="#cb9-7" aria-hidden="true" tabindex="-1"></a>  <span class="cf">if</span>(EU_certain <span class="sc">==</span> EU_bet){</span>
<span id="cb9-8"><a href="#cb9-8" aria-hidden="true" tabindex="-1"></a>    <span class="fu">print</span>(<span class="st">"INDIFFERENT"</span>)</span>
<span id="cb9-9"><a href="#cb9-9" aria-hidden="true" tabindex="-1"></a>  } <span class="cf">else</span> <span class="cf">if</span>(EU_certain <span class="sc">&gt;</span> EU_bet){</span>
<span id="cb9-10"><a href="#cb9-10" aria-hidden="true" tabindex="-1"></a>    <span class="fu">print</span>(<span class="st">"REJECT"</span>)</span>
<span id="cb9-11"><a href="#cb9-11" aria-hidden="true" tabindex="-1"></a>  } <span class="cf">else</span> <span class="cf">if</span>(EU_certain <span class="sc">&lt;</span> EU_bet){</span>
<span id="cb9-12"><a href="#cb9-12" aria-hidden="true" tabindex="-1"></a>    <span class="fu">print</span>(<span class="st">"ACCEPT"</span>)</span>
<span id="cb9-13"><a href="#cb9-13" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb9-14"><a href="#cb9-14" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb9-15"><a href="#cb9-15" aria-hidden="true" tabindex="-1"></a>  <span class="fu">print</span>(<span class="fu">paste0</span>(<span class="st">"Expected utility of bet = "</span>, EU_bet))</span>
<span id="cb9-16"><a href="#cb9-16" aria-hidden="true" tabindex="-1"></a>  <span class="fu">print</span>(<span class="fu">paste0</span>(<span class="st">"Utility of current wealth = "</span>, EU_certain))</span>
<span id="cb9-17"><a href="#cb9-17" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></div>
</details>
</div>
<p>Testing a few numbers, someone with log utility is indifferent about a 50:50 win $110, lose $100 bet at wealth $1100. They would accept for any level of wealth above that level.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb10"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb10-1"><a href="#cb10-1" aria-hidden="true" tabindex="-1"></a><span class="fu">log_utility</span>(<span class="dv">110</span>, <span class="dv">100</span>, <span class="dv">1100</span>)</span></code></pre></div></div>
</details>
<div class="cell-output cell-output-stdout">
<pre><code>[1] "INDIFFERENT"
[1] "Expected utility of bet = 7.00306545878646"
[1] "Utility of current wealth = 7.00306545878646"</code></pre>
</div>
</div>
<p>That same person will always accept a 50:50 win $1100, lose $1000 bet above $11,000 in wealth.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb12"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb12-1"><a href="#cb12-1" aria-hidden="true" tabindex="-1"></a><span class="fu">log_utility</span>(<span class="dv">1100</span>, <span class="dv">1000</span>, <span class="dv">11000</span>)</span></code></pre></div></div>
</details>
<div class="cell-output cell-output-stdout">
<pre><code>[1] "ACCEPT"
[1] "Expected utility of bet = 9.30565055178051"
[1] "Utility of current wealth = 9.30565055178051"</code></pre>
</div>
</div>
<p>Can we generate any bets that don’t seem quite right? It’s quite hard unless you have a bet that will bring the person to ruin or near ruin. For instance, for a 50:50 bet with a chance to win $1 million, a person with log utility and $100,000 wealth would still accept the bet with a potential loss of $90,900, which brings them to less than 10% of their wealth.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb14"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb14-1"><a href="#cb14-1" aria-hidden="true" tabindex="-1"></a><span class="fu">log_utility</span>(<span class="dv">1000000</span>, <span class="dv">90900</span>, <span class="dv">100000</span>)</span></code></pre></div></div>
</details>
<div class="cell-output cell-output-stdout">
<pre><code>[1] "ACCEPT"
[1] "Expected utility of bet = 11.5134252151368"
[1] "Utility of current wealth = 11.5129254649702"</code></pre>
</div>
</div>
<p>The problem with log utility is not the ability to generate ridiculous bets that would be rejected. Rather, it’s that someone with log utility would tend to accept most positive value bets (in fact, they would always take a non-zero share if they could). Only if the bet brings them near ruin (either through size or their lack of wealth) would they turn down the bet.</p>
<p>The isoelastic utility function - of which log utility is a special case - is a broader class of function that exhibits constant relative risk aversion:</p>
<p>{{< math display >}}U(x)=\frac{w^{1-\rho}-1}{1-\rho}{{< /math >}}</p>
<p>If {{< math >}}\rho=1{{< /math >}}, this simplifies to log utility (you need to use L’Hopital’s rule to get this as the fraction is undefined when {{< math >}}\rho=1{{< /math >}}.) The higher {{< math >}}\rho{{< /math >}}, the higher the level of risk aversion. We implement this function as follows:</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb16"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb16-1"><a href="#cb16-1" aria-hidden="true" tabindex="-1"></a>CRRA_utility <span class="ot">&lt;-</span> <span class="cf">function</span>(g, l, w, <span class="at">rho=</span><span class="dv">2</span>){</span>
<span id="cb16-2"><a href="#cb16-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb16-3"><a href="#cb16-3" aria-hidden="true" tabindex="-1"></a>  <span class="cf">if</span>(rho<span class="sc">==</span><span class="dv">1</span>){</span>
<span id="cb16-4"><a href="#cb16-4" aria-hidden="true" tabindex="-1"></a>    <span class="fu">print</span>(<span class="st">"function undefined"</span>)</span>
<span id="cb16-5"><a href="#cb16-5" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb16-6"><a href="#cb16-6" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb16-7"><a href="#cb16-7" aria-hidden="true" tabindex="-1"></a>  log_gain <span class="ot">&lt;-</span> ((w<span class="sc">+</span>g)<span class="sc">^</span>(<span class="dv">1</span><span class="sc">-</span>rho)<span class="sc">-</span><span class="dv">1</span>)<span class="sc">/</span>(<span class="dv">1</span><span class="sc">-</span>rho)</span>
<span id="cb16-8"><a href="#cb16-8" aria-hidden="true" tabindex="-1"></a>  log_loss <span class="ot">&lt;-</span> ((w<span class="sc">-</span>l)<span class="sc">^</span>(<span class="dv">1</span><span class="sc">-</span>rho)<span class="sc">-</span><span class="dv">1</span>)<span class="sc">/</span>(<span class="dv">1</span><span class="sc">-</span>rho)</span>
<span id="cb16-9"><a href="#cb16-9" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb16-10"><a href="#cb16-10" aria-hidden="true" tabindex="-1"></a>  EU_bet <span class="ot">&lt;-</span> <span class="fl">0.5</span><span class="sc">*</span>log_gain <span class="sc">+</span> <span class="fl">0.5</span><span class="sc">*</span>log_loss</span>
<span id="cb16-11"><a href="#cb16-11" aria-hidden="true" tabindex="-1"></a>  EU_certain <span class="ot">&lt;-</span> (w<span class="sc">^</span>(<span class="dv">1</span><span class="sc">-</span>rho)<span class="sc">-</span><span class="dv">1</span>)<span class="sc">/</span>(<span class="dv">1</span><span class="sc">-</span>rho)</span>
<span id="cb16-12"><a href="#cb16-12" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb16-13"><a href="#cb16-13" aria-hidden="true" tabindex="-1"></a>  <span class="cf">if</span>(EU_certain <span class="sc">==</span> EU_bet){</span>
<span id="cb16-14"><a href="#cb16-14" aria-hidden="true" tabindex="-1"></a>    <span class="fu">print</span>(<span class="st">"INDIFFERENT"</span>)</span>
<span id="cb16-15"><a href="#cb16-15" aria-hidden="true" tabindex="-1"></a>  } <span class="cf">else</span> <span class="cf">if</span>(EU_certain <span class="sc">&gt;</span> EU_bet){</span>
<span id="cb16-16"><a href="#cb16-16" aria-hidden="true" tabindex="-1"></a>    <span class="fu">print</span>(<span class="st">"REJECT"</span>)</span>
<span id="cb16-17"><a href="#cb16-17" aria-hidden="true" tabindex="-1"></a>  } <span class="cf">else</span> <span class="cf">if</span>(EU_certain <span class="sc">&lt;</span> EU_bet){</span>
<span id="cb16-18"><a href="#cb16-18" aria-hidden="true" tabindex="-1"></a>    <span class="fu">print</span>(<span class="st">"ACCEPT"</span>)</span>
<span id="cb16-19"><a href="#cb16-19" aria-hidden="true" tabindex="-1"></a>  }</span>
<span id="cb16-20"><a href="#cb16-20" aria-hidden="true" tabindex="-1"></a>  </span>
<span id="cb16-21"><a href="#cb16-21" aria-hidden="true" tabindex="-1"></a>  <span class="fu">print</span>(<span class="fu">paste0</span>(<span class="st">"Expected utility of bet = "</span>, EU_bet))</span>
<span id="cb16-22"><a href="#cb16-22" aria-hidden="true" tabindex="-1"></a>  <span class="fu">print</span>(<span class="fu">paste0</span>(<span class="st">"Utility of current wealth = "</span>, EU_certain))</span>
<span id="cb16-23"><a href="#cb16-23" aria-hidden="true" tabindex="-1"></a>}</span></code></pre></div></div>
</details>
</div>
<p>If we increase {{< math >}}\rho{{< /math >}}, we can increase the proportion of low-value bets that are rejected.</p>
<p>For example, a person with {{< math >}}\rho=2{{< /math >}} will reject the 50:50 win $110, lose $100 bet up to a wealth of $2200. The rejection point scales with {{< math >}}\rho{{< /math >}}.</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb17"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb17-1"><a href="#cb17-1" aria-hidden="true" tabindex="-1"></a><span class="fu">CRRA_utility</span>(<span class="dv">110</span>, <span class="dv">100</span>, <span class="dv">2200</span>, <span class="dv">2</span>)</span></code></pre></div></div>
</details>
<div class="cell-output cell-output-stdout">
<pre><code>[1] "INDIFFERENT"
[1] "Expected utility of bet = 0.999545454545455"
[1] "Utility of current wealth = 0.999545454545455"</code></pre>
</div>
</div>
<p>For a 50:50 chance to win $1 million at wealth $100,000, the person with {{< math >}}\rho=2{{< /math >}} is willing to risk a far smaller loss, and rejects even when the loss is only $48,000, or less than half their wealth (which admittedly is still a fair chunk).</p>
<div class="cell">
<details class="code-fold">
<summary>Code</summary>
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb19"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb19-1"><a href="#cb19-1" aria-hidden="true" tabindex="-1"></a><span class="fu">CRRA_utility</span>(<span class="dv">1000000</span>, <span class="dv">48000</span>, <span class="dv">100000</span>, <span class="dv">2</span>)</span></code></pre></div></div>
</details>
<div class="cell-output cell-output-stdout">
<pre><code>[1] "REJECT"
[1] "Expected utility of bet = 0.99998993006993"
[1] "Utility of current wealth = 0.99999"</code></pre>
</div>
</div>
<p>Higher values of {{< math >}}\rho{{< /math >}} start to become completely unrealistic as utility is almost flat beyond an initial level of wealth.</p>
<p>It is also possible to have values of {{< math >}}\rho{{< /math >}} between 0 (risk neutrality) and 1. These would result in even fewer rejected low-value bets than log utility, and fewer rejected bets with highly unbalanced potential gains and losses.</p>


</section>
</section>
{{< /html >}}
