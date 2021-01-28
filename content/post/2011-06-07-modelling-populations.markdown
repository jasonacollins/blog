---
author: jasonacollins
comments: true
date: 2011-06-07 08:06:52+00:00
draft: no
link: https://jasoncollins.blog/2011/06/07/modelling-populations/
slug: modelling-populations
title: Modelling populations
wordpress_id: 1212
---

In my previous two posts, I [described the model](https://jasoncollins.blog/2011/06/natural-selection-and-economic-growth/) contained in Galor and Moav's paper [Natural Selection and the Origin of Economic Growth](http://qje.oxfordjournals.org/content/117/4/1133.short) and [an extension](https://jasoncollins.blog/2011/06/natural-selection-and-the-collapse-of-economic-growth/) in which we introduced genotypes with a low preference for educating their children.

Having been through the process of parametrising and simulating a complex economic model, I would recommend it as a method of increasing understanding of the basic model mechanics. More importantly, it can also highlight issues that are not clear from the mathematical consideration that is traditionally given to models.

When [Nils-Petter Lagerlof simulated](http://doi.org/10.1016/j.red.2005.07.002) a similar model by [Galor and Weil](http://www.jstor.org/stable/117309), he found that the population cycled between generations. If population was low, incomes would jump causing a population boom. In the next generation, that excess population would cause populations to crash. We found a similar result in Galor and Moav's natural selection model. For the parameter values used in [our paper](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1851251), the population jumped or shrank by up to 30 per cent per generation. Many parameter values drove the population extinct. This made it difficult to use parameter values that generated realistic outcomes. The base level of investment per child used in the simulation is probably higher than I would have otherwise chosen, but low values made extinction more likely.

As Robert May discussed in his [important 1976 paper](http://doi.org/10.1038/261459a0), this reflects the fact that simple mathematical models can have very complicated dynamics. May showed that in a simple population model where population growth depends on the potential rate of population growth and the carrying capacity of the environment, the population trend can vary from a stable equilibrium to apparently chaotic population perturbations.

This observation is an important consideration with many economic models. Since simulating the Galor and Moav model, I have played with a few other economic models and have found that many have chaotic behaviour for certain parameter values and functional forms. I have been unable to simulate some models at all without the population crashing into extinction.
