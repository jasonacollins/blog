---
title: 'An evolutionary projection of global fertility and population: My new paper (with Lionel Page) in Evolution & Human Behavior'
author: jasonacollins
date: 2018-10-11 08:00:36+00:00
draft: no
slug: an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior
---

Forecasting fertility is a mug's game. Here is a picture of fertility forecasts by the US Census Bureau through the baby boom and subsequent fertility drop (from Lee and Tuljapurkar's _[Population Forecasting for Fiscal Planning: Issues and Innovations](http://www.demog.berkeley.edu/~rlee/papers/leetulja2b.pdf)_). The dark line is actual, the dotted line the various forecasts.

![US Census forecasts](/img/2018-10-11-an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/us-census-forecasts.jpg)

I am not sure that the science of fertility forecasting in developed countries has made substantial progress since any of those forecasts were made. But that doesn't stop a lot of people from trying.

One of the most high profile forecasts of fertility and population comes from the United Nations, which publishes global population forecasts through to 2100. Individual country forecasts are currently developed using a Bayesian methodology, which are then aggregated to form a global picture. The development of this methodology led to a heavily cited 2014 paper titled "[World population stabilization unlikely this century](http://doi.org/10.1126/science.1257469)" ([pdf](http://www.demographic-challenge.com/files/downloads/452fbf0a4300800ec6cc4af4315c11ca/science-1257469-full.pdf)) and the conclusion that there was only a 30% probability that global population growth would cease this century.

These projections contain an important fertility assumption. For countries that have undergone the demographic transition to low fertility, the assumption is that their fertility rate will oscillate around a long-term mean. While there has been some debate around whether this long-term mean would be the replacement rate or lower, the (almost theory-free) assumption of oscillation around a long-term level dominates the forecasts.

There is at least one theoretical basis for doubting this assumption. In a [2013 working paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2208886) (co-authored with Oliver Richards), we argued that as fertility was heritable, this would tend to increase fertility and population growth. Those with a preference for higher fertility would have more children, with their children in turn having a preference for more children. This high-fertility type would eventually come to dominate the population, leading to markedly higher population that forecast.

As I noted when the working paper was released, we were hardly the first to propose this idea. Fisher noted the power of higher fertility groups in [The Genetical Theory of Natural Selection](https://en.wikipedia.org/wiki/The_Genetical_Theory_of_Natural_Selection). I had seen [Razib Khan](http://blogs.discovermagazine.com/gnxp/2011/01/the-inevitable-rise-of-amish-machines/#.UQjwAUp4b_Q), [Robin Hanson](http://www.overcomingbias.com/2009/09/future-fertility.html) and [John Hawks](http://johnhawks.net/weblog/reviews/demography/population-size-shrinking-future-2013.html) mention the idea. Murphy and Wang examined the concept in [a microsimulation](http://link.springer.com/chapter/10.1007%2F978-1-4615-1137-3_11). Many papers on the heritability of fertility hint at it. [Rowthorn’s paper on fertility and religiosity](https://www.jasoncollins.blog/heritability-of-religion-and-fertility/) also points in this direction. We simply added a touch of quantitative modelling to explore the speed of the change, and have now been followed by others with different approaches (such as [this)](http://doi.org/10.1098/rspb.2013.2561).

Shortly after [I posted about the working paper](https://www.jasoncollins.blog/fertility-is-going-to-go-up/), I received an email from [Lionel Page](https://twitter.com/page_eco) suggesting that we should turn this idea into more detailed simulation of world population. Five years after Lionel's email, that simulation has just been released in a [paper published in Evolution & Human Behavior](https://doi.org/10.1016/j.evolhumbehav.2018.09.001). Here is the abstract:

>The forecasting of the future growth of world population is of critical importance to anticipate and address a wide range of global challenges. The United Nations produces forecasts of fertility and world population every two years. As part of these forecasts, they model fertility levels in post-demographic transition countries as tending toward a long-term mean, leading to forecasts of flat or declining population in these countries. We substitute this assumption of constant long-term fertility with a dynamic model, theoretically founded in evolutionary biology, with heritable fertility. Rather than stabilizing around a long-term level for post-demographic transition countries, fertility tends to increase as children from larger families represent a larger share of the population and partly share their parents' trait of having more offspring. Our results suggest that world population will grow larger in the future than currently anticipated.

Our methodology is almost identical to the United Nations methodology, except we substitute the equation by which fertility converges to a long-term mean with the [breeder's equation](https://en.wikipedia.org/wiki/Heritability#Response_to_selection), which captures the response to selection of a trait.

And here are a few charts showing the simulation results: grey is the base United Nations simulation, black the evolutionary simulations, the dashed lines the 90% confidence intervals. First, European total fertility rate (TFR) and population, which shifts from terminal decline to growth:

![908TFR](/img/2018-10-11-an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/908tfr.jpg?w=1024)![908pop](/img/2018-10-11-an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/908pop.jpg?w=1024)

Next, North America, which increases its rate of growth:

![905TFR](/img/2018-10-11-an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/905tfr.jpg?w=1024)![905pop](/img/2018-10-11-an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/905pop.jpg?w=1024)

Next, Asia:

![935TFR](/img/2018-10-11-an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/935tfr.jpg?w=1024)![935pop](/img/2018-10-11-an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/935pop.jpg?w=1024)

And finally, the global result:

![900TFR](/img/2018-10-11-an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/900tfr.jpg?w=1024)![900pop](/img/2018-10-11-an-evolutionary-projection-of-global-fertility-and-population-my-new-paper-with-lionel-page-in-evolution-human-behavior/900pop.jpg?w=1024)

The punchline is that the probability of global population stabilisation this century becomes less than 5%. Europe and North America that are most effected within this century. Asia is less effected, but still shifts from a scenario of decline to one of growth, and due to its size has the largest effect on the global projections.

Having opened by saying that fertility forecasting is a mug's game, should the same be said about these forecasts? The answer to that question is largely yes. Cultural and technological change, environmental shocks and the like will almost certainly lead to a different outcome to the one the United Nations or we have forecast. We effectively argue this in the section of the paper on cultural evolution (which was added following some helpful reviewer comments).

But to get lost in the specific numbers is to lose sight of the exercise. We are arguing that an important assumption underpinning the United Nations exercise should be reconsidered. We've given a rough idea of how far that assumption could shift the fertility and population outcomes, and they are of a magnitude that would see some parts of the world looking quite different by the end of the century. If we assume constant fertility despite this evolutionary dynamic, we risk a material downward bias in projecting future fertility and population.

---

As an aside, the [freely available methodology and R packages](https://bayespop.csss.washington.edu/) that underpin the United Nations forecasts greatly facilitated our efforts. We spent a lot of time considering how to implement the simulations, but on discovering the openness of the United Nations approach, we found a great place to implement our tweaked approach. In that spirit, you can access our modified packages and the data used to generate them [here at OSF](https://osf.io/4r3kh/).

If you can't access the [paper](https://doi.org/10.1016/j.evolhumbehav.2018.09.001) through the paywall and would like me to email you a copy, let me know.
