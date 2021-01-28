---
author: jasonacollins
comments: true
date: 2018-06-21 09:00:08+00:00
draft: no
link: https://jasoncollins.blog/2018/06/21/wealth-and-genes/
slug: wealth-and-genes
title: Wealth and genes
wordpress_id: 22879
---

Go back ten years, and most published attempts to link specific genetic variants to a trait were false. These [candidate-gene studies](https://en.wikipedia.org/wiki/Candidate_gene) were your classic, yet typically rubbish, "gene for X" paper.

The proliferation of poor papers was in part because the studies were too small to discover the effects they were looking for (see [here](https://jasoncollins.blog/2014/11/04/genome-wide-association-studies-and-socioeconomic-outcomes/) for some good videos describing the problems). As has become increasingly evident, most human traits are affected by thousands of genes, each with tiny effects. With a small sample - many of the early candidate-gene studies involved hundreds of people - all you can discover is noise.

But there was some optimism that robust links would eventually be drawn. Get genetic samples from a large enough population (say, hundreds of thousands), and you can detect these weak genetic effects. You can also replicate the findings across multiple samples to ensure the results are robust

In recent years that promise has started to be realised through [genome-wide association studies](https://en.m.wikipedia.org/wiki/Genome-wide_association_study) (GWAS). Although more than 99% of the human genome is common across people, there are certain locations at which the DNA base pair can differ. These locations are known as single-nucleotide polymorphisms (SNPs). A GWAS involves looking across all of the sampled SNPs (typically one million or so SNPs for each person) and estimating the effect of each SNP against an outcome of interest. Those SNPs that meet certain statistical thresholds are treated as positive findings.

A steady flow of GWAS papers are now being published, linking SNPs with traits such as [cognitive function](https://www.nature.com/articles/s41467-018-04362-x) and outcomes such as [educational attainment](https://www.nature.com/articles/nature17671). A typical study title is "[Study of 300,486 individuals identifies 148 independent genetic loci influencing general cognitive function](https://www.nature.com/articles/s41467-018-04362-x)".

One innovation from this work is the use of "polygenic scores". The effect of all measured SNPs from a GWAS is used to produce a single score for a person. That score is used to predict their trait or outcome. Polygenic scores are used regularly in animal breeding, and are now starting to be used to look at human outcomes, including those of interest to economists.

The latest example of this is an examination of the link between wealth and a polygenic score for education. An extract from the abstract of the [NBER working paper](http://www.nber.org/papers/w24642) by Daniel Barth, Nicholas Papageorge and Kevin Thom states:


<blockquote>We show that genetic endowments linked to educational attainment strongly and robustly predict wealth at retirement. The estimated relationship is not fully explained by flexibly controlling for education and labor income. ... The associations we report provide preliminary evidence that genetic endowments related to human capital accumulation are associated with wealth not only through educational attainment and labor income, but also through a facility with complex financial decision-making.

</blockquote>

(If you can't access the NBER paper, here is an ungated [pdf of a slightly earlier working paper](https://nicholaswpapageorge.files.wordpress.com/2018/05/genes_wealth.pdf))

In more detail:


<blockquote>We first establish a robust relationship between household wealth in retirement and the average household polygenic score for educational attainment. A one-standard-deviation increase in the score is associated with a 33.1 percent increase in household wealth (approximately $144,000 in 2010 dollars). ... Measures of educational attainment, including years of education and completed degrees, explain over half of this relationship. Using detailed income data from the Social Security Administration (SSA) as well as self-reported labor earnings from the HRS, we find that labor income can explain only a small part of the gene-wealth gradient that remains after controlling for education. These results indicate that while education and labor market earnings are important sources of variation in house-hold wealth, they explain only a portion of the relationship between genetic endowments and wealth.

</blockquote>

The finding that the genes that affect education also affect other outcomes - in this case wealth - is no surprise. Whether these genes relate to, say, cognitive ability or conscientiousness, it is easy to imagine that they affect all of education, workplace performance, savings behaviour and a host of other factors that would in turn influence wealth.

To tease this out, I would be interested in seeing studies that examine the predictive power of polygenic scores for more fundamental characteristics, such as IQ and the [big five personality traits](https://en.m.wikipedia.org/wiki/Big_Five_personality_traits). These would likely capture a good deal of the variation in outcomes being attributed to education. You might also look at some fundamental economic traits, such as risk or time preferences (to the extent these are not just reflections of IQ and the big five). If you know these more fundamental traits, most other behaviours are simply combinations of that.

This was a lesson learnt from research on heritability, where you could find studies calculating the heritability of everything from opinions on gun control to leisure interests. Although this had some value in that it led to the first law of behavioural genetics, namely that all human behavioural traits are heritable, a lot of these studies were simply capturing manifestations of differences in IQ and the big five. (It also benefited academics with padded CVs).

Moving on, what does analysis using polygenic scores add to other work?


<blockquote>Our work contributes to an existing literature on endowments, economic traits, and household wealth. One strand of this work examines how various measures of “ability,” such as IQ or cognitive test scores, predict household wealth and similar outcomes ... However, parental investments and other environmental factors can directly affect test performance, making it difficult to separate the effects of endowed traits from endogenous human capital investments. A second strand of this literature focuses on genetic endowments, and seeks to estimate their collective importance using twin studies. Twin studies have shown that genetics play a non-trivial role in explaining financial behavior such as savings and portfolio choices ... However, while twin studies can decompose the variance of an outcome into genetic and non-genetic contributions, they do not identify which particular markers influence economic outcomes. Moreover, it is typically impossible to apply twin methods to large and nationally representative longitudinal studies, such as the HRS, which offer some of the richest data on household wealth and related behavioral traits.

</blockquote>

Twin studies are fantastic at teasing out the role of genetics, but if you want to take genetic samples from a new population and use the genetic markers as controls in your analysis or to predict outcomes, you need something of the nature of these polygenic scores.


<blockquote>We note two important differences between the EA score and a measure like IQ that make it valuable to study polygenic scores. First, a polygenic score like the EA score can overcome some interpretational challenges related to IQ and other cognitive test scores. Environmental factors have been found to influence intelligence test results and to moderate genetic influences on IQ (Tucker-Drob and Bates, 2015). It is true that differences in the EA score may reflect differences in environments or investments because parents with high EA scores may also be more likely to invest in their children. However, the EA score is fixed at conception, which means that post-birth investments cannot causally change the value of the score. A measure like IQ suffers from both of these interpretational challenges.

</blockquote>

The interpretational challenge with IQ doesn't need to be viewed in isolation. Between twin and adoption studies and these studies, you can start to tease out how much a measure like IQ is practically (as opposed to theoretically) hampered by those challenges. An even better option might be an IQ polygenic score.

The paper ends with a warning that we know should have been attached to many papers for decades now, but this time with an increasingly tangible solution.


<blockquote>Economic research using information on genetic endowments is useful for understanding what has heretofore been a form of unobserved heterogeneity that persists across generations, since parents provide genetic material for their children. Studies that ignore this type of heterogeneity when studying the intergenerational persistence of economic outcomes, such as income or wealth, could place too much weight on other mechanisms such as attained education or direct monetary transfers between parents and children. The use of observed genetic information helps economists to develop a more accurate and complete understanding of inequality across generations.

</blockquote>

Examining intergenerational outcomes while ignoring genetic effects is generally a waste of time.
