---
title: 'An evolutionary projection of global fertility and population: My new paper (with Lionel Page) in Evolution & Human Behavior'
author: "Jason Collins"
date: 2018-10-11 08:00:36+00:00
draft: false
sync_source: "posts/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior.qmd"
sync_route: "quarto"
sync_hash: "0e166ea12a27"
---

{{< html >}}
<p>Forecasting fertility is a mug’s game. Here is a picture of fertility forecasts by the US Census Bureau through the baby boom and subsequent fertility drop (from&nbsp;Lee and&nbsp;Tuljapurkar’s <em><a href="http://www.demog.berkeley.edu/~rlee/papers/leetulja2b.pdf">Population Forecasting for Fiscal Planning: Issues and Innovations</a></em>). The dark line is actual, the dotted line the various forecasts.</p>
<div class="quarto-figure quarto-figure-center">
<figure class="figure">
<figcaption>US Census forecasts</figcaption>
<p><a href="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/us-census-forecasts.jpg" class="lightbox" data-gallery="quarto-lightbox-gallery-1" title="US Census forecasts">{{< img src="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/us-census-forecasts.jpg" class="img-fluid figure-img" alt="US Census forecasts" >}}</a></p>
</figure>
</div>
<p>I am not sure that the science of fertility forecasting in developed countries has made substantial progress since any of those forecasts were made. But that doesn’t stop a lot of people from trying.</p>
<p>One of the most high profile forecasts of fertility and population comes from the United Nations, which publishes global population forecasts through to 2100. Individual country forecasts are currently developed using a Bayesian methodology, which are then aggregated to form a global picture. The development of this methodology led to a heavily cited 2014 paper titled “<a href="http://doi.org/10.1126/science.1257469">World population stabilization unlikely this century</a>” (<a href="http://www.demographic-challenge.com/files/downloads/452fbf0a4300800ec6cc4af4315c11ca/science-1257469-full.pdf">pdf</a>) and the conclusion that there was only a 30% probability that global population growth would cease this century.</p>
<p>These projections contain an important fertility assumption. For countries that have undergone the demographic transition to low fertility, the assumption is that their fertility rate will oscillate around a long-term mean. While there has been some debate around whether this long-term mean would be the replacement rate or lower, the (almost theory-free) assumption of oscillation around a long-term level dominates the forecasts.</p>
<p>There is at least one theoretical basis for doubting this assumption. In a <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2208886">2013 working paper</a> (co-authored with Oliver Richards), we argued that as fertility was heritable, this would tend to increase fertility and population growth. Those with a preference for higher fertility would have more children, with their children in turn having a preference for more children. This high-fertility type would eventually come to dominate the population, leading to markedly higher population than forecast.</p>
<p>As I noted when the working paper was released, we were hardly the first to propose this idea. Fisher noted the power of higher fertility groups in <a href="https://en.wikipedia.org/wiki/The_Genetical_Theory_of_Natural_Selection">The Genetical Theory of Natural Selection</a>. I had seen <a href="http://blogs.discovermagazine.com/gnxp/2011/01/the-inevitable-rise-of-amish-machines/#.UQjwAUp4b_Q">Razib Khan</a>, <a href="http://www.overcomingbias.com/2009/09/future-fertility.html">Robin Hanson</a> and <a href="http://johnhawks.net/weblog/reviews/demography/population-size-shrinking-future-2013.html">John Hawks</a> mention the idea. Murphy and Wang examined the concept in <a href="http://link.springer.com/chapter/10.1007%2F978-1-4615-1137-3_11">a microsimulation</a>. Many papers on the heritability of fertility hint at it. <a href="../posts/heritability-of-religion-and-fertility.html">Rowthorn’s paper on fertility and religiosity</a> also points in this direction. We simply added a touch of quantitative modelling to explore the speed of the change, and have now been followed by others with different approaches (such as <a href="http://doi.org/10.1098/rspb.2013.2561">this)</a>.</p>
<p>Shortly after <a href="../posts/fertility-is-going-to-go-up.html">I posted about the working paper</a>, I received an email from <a href="https://twitter.com/page_eco">Lionel Page</a> suggesting that we should turn this idea into a more detailed simulation of world population. Five years after Lionel’s email, that simulation has just been released in a <a href="https://doi.org/10.1016/j.evolhumbehav.2018.09.001">paper published in Evolution &amp; Human Behavior</a>. Here is the abstract:</p>
<blockquote class="blockquote">
<p>The forecasting of the future growth of world population is of critical importance to anticipate and address a wide range of global challenges. The United Nations produces forecasts of fertility and world population every two years. As part of these forecasts, they model fertility levels in post-demographic transition countries as tending toward a long-term mean, leading to forecasts of flat or declining population in these countries. We substitute this assumption of constant long-term fertility with a dynamic model, theoretically founded in evolutionary biology, with heritable fertility. Rather than stabilizing around a long-term level for post-demographic transition countries, fertility tends to increase as children from larger families represent a larger share of the population and partly share their parents’ trait of having more offspring. Our results suggest that world population will grow larger in the future than currently anticipated.</p>
</blockquote>
<p>Our methodology is almost identical to the United Nations methodology, except we substitute the equation by which fertility converges to a long-term mean with the <a href="https://en.wikipedia.org/wiki/Heritability#Response_to_selection">breeder’s equation</a>, which captures the response to selection of a trait.</p>
<p>And here are a few charts showing the simulation results: grey is the base United Nations simulation, black is the evolutionary simulation, and the dashed lines are the 90% confidence interval.</p>
<p>First, European total fertility rate (TFR) and population, which shifts from terminal decline to growth:</p>
<div class="quarto-layout-panel" data-layout-ncol="2">
<div class="quarto-layout-row">
<div class="quarto-layout-cell" style="flex-basis: 50.0%;justify-content: center;">
<p><a href="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/908tfr.jpg" class="lightbox" data-gallery="quarto-lightbox-gallery-2">{{< img src="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/908tfr.jpg" class="img-fluid" >}}</a></p>
</div>
<div class="quarto-layout-cell" style="flex-basis: 50.0%;justify-content: center;">
<p><a href="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/908pop.jpg" class="lightbox" data-gallery="quarto-lightbox-gallery-3">{{< img src="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/908pop.jpg" class="img-fluid" >}}</a></p>
</div>
</div>
</div>
<p>Next, North America, which increases its rate of growth:</p>
<div class="quarto-layout-panel" data-layout-ncol="2">
<div class="quarto-layout-row">
<div class="quarto-layout-cell" style="flex-basis: 50.0%;justify-content: center;">
<p><a href="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/905tfr.jpg" class="lightbox" data-gallery="quarto-lightbox-gallery-4">{{< img src="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/905tfr.jpg" class="img-fluid" >}}</a></p>
</div>
<div class="quarto-layout-cell" style="flex-basis: 50.0%;justify-content: center;">
<p><a href="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/905pop.jpg" class="lightbox" data-gallery="quarto-lightbox-gallery-5">{{< img src="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/905pop.jpg" class="img-fluid" >}}</a></p>
</div>
</div>
</div>
<p>Next, Asia:</p>
<div class="quarto-layout-panel" data-layout-ncol="2">
<div class="quarto-layout-row">
<div class="quarto-layout-cell" style="flex-basis: 50.0%;justify-content: center;">
<p><a href="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/935tfr.jpg" class="lightbox" data-gallery="quarto-lightbox-gallery-6">{{< img src="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/935tfr.jpg" class="img-fluid" >}}</a></p>
</div>
<div class="quarto-layout-cell" style="flex-basis: 50.0%;justify-content: center;">
<p><a href="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/935pop.jpg" class="lightbox" data-gallery="quarto-lightbox-gallery-7">{{< img src="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/935pop.jpg" class="img-fluid" >}}</a></p>
</div>
</div>
</div>
<p>And finally, the global result:</p>
<div class="quarto-layout-panel" data-layout-ncol="2">
<div class="quarto-layout-row">
<div class="quarto-layout-cell" style="flex-basis: 50.0%;justify-content: center;">
<p><a href="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/900tfr.jpg" class="lightbox" data-gallery="quarto-lightbox-gallery-8">{{< img src="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/900tfr.jpg" class="img-fluid" >}}</a></p>
</div>
<div class="quarto-layout-cell" style="flex-basis: 50.0%;justify-content: center;">
<p><a href="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/900pop.jpg" class="lightbox" data-gallery="quarto-lightbox-gallery-9">{{< img src="img/an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/900pop.jpg" class="img-fluid" >}}</a></p>
</div>
</div>
</div>
<p>The punchline is that the probability of global population stabilisation this century becomes less than 5%. Europe and North America are most affected within this century. Asia is less affected, but still shifts from a scenario of decline to one of growth, and due to its size has the largest effect on the global projections.</p>
<p>Having opened by saying that fertility forecasting is a mug’s game, should the same be said about these forecasts? The answer to that question is largely yes. Cultural and technological change, environmental shocks and the like will almost certainly lead to a different outcome to the one the United Nations or we have forecast. We effectively argue this in the section of the paper on cultural evolution (which was added following some helpful reviewer comments).</p>
<p>But to get lost in the specific numbers is to lose sight of the exercise. We are arguing that an important assumption underpinning the United Nations exercise should be reconsidered. We’ve given a rough idea of how far that assumption could shift the fertility and population outcomes, and they are of a magnitude that would see some parts of the world looking quite different by the end of the century. If we assume constant fertility despite this evolutionary dynamic, we risk a material downward bias in projecting future fertility and population.</p>
<hr>
<p>As an aside, the <a href="https://bayespop.csss.washington.edu/">freely available methodology and R packages</a> that underpin the United Nations forecasts greatly facilitated our efforts. We spent a lot of time considering how to implement the simulations, but on discovering the openness of the United Nations approach, we found a great place to implement our tweaked approach. In that spirit, you can access our modified packages and the data used to generate them <a href="https://osf.io/4r3kh/">here at OSF</a>.</p>
<p>If you can’t access the <a href="https://doi.org/10.1016/j.evolhumbehav.2018.09.001">paper</a> through the paywall and would like me to email you a copy, let me know.</p>
{{< /html >}}
