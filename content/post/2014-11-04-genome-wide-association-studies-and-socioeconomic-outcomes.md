---
author: jasonacollins
comments: true
date: 2014-11-04 08:31:27+00:00
draft: no
link: https://jasoncollins.blog/genome-wide-association-studies-and-socioeconomic-outcomes/
slug: genome-wide-association-studies-and-socioeconomic-outcomes
title: Genome Wide Association Studies and socioeconomic outcomes
wordpress_id: 20406
---

A few months back, I posted about a [Conference on Genetics and Behaviour](https://hceconomics.uchicago.edu/events/conference-genetics-and-behavior) held by the Human Capital and Economic Opportunity Global Working Group at the University of Chicago. [In that post](https://jasoncollins.blog/genes-and-socioeconomic-aggregates/), I linked to a series of videos from the first session on the effect of genes on socioeconomic aggregates.

Over the last couple of days, I watched the videos from the session on Genome Wide Association Studies (GWAS). As for the first set of videos, they are technical (as you might expect for a bunch of academics) - particularly the questions - but cover some important points.

In early studies linking genetic factors to behaviour and socioeconomic outcomes, candidate gene studies were the dominant method. In a candidate gene study, a gene is hypothesised to have an effect, and that hypothesis is tested directly. However, there are some major problems with candidate gene studies, with the literature littered with claims of the "gene for X" that simply can't be replicated.

David Cesarini opened the session by pointing to this low level of replication of candidate gene studies. He suggests three problems might be causing this failure to replicate. These are multiple hypothesis testing coupled with publication bias, population stratification, and the low power of the small samples typically used.

Multiple hypothesis testing in candidate gene studies arises because more than one gene tends to be tested. In that case, the significance level of the tests should be adjusted to account for the multiple tests. But the reality is that the many negative tests never see the light of day, with the successful ones presented as successfully meeting a threshold appropriate for a single test. Publication bias exacerbates that problem as negative results tend not the be published and you don't know how many tests have been conducted.

In contrast, GWAS is a hypothesis free approach. All SNPs in a sample (single nucleotide polymorphisms - DNA sequence variations in which a single nucleotide varies in the population) are tested for association with a trait. As there are as many hypotheses being tested as there are SNPs, very high significance thresholds are applied to avoid false positives. But as the number of SNPs in an array is known from the start, there is no doubt about the appropriate threshold.

Cesarini's talk focused on the second problem, population stratification. This occurs where allele (variants of a gene) frequencies correlate with confounding variables. A classic example is analysing a mixed population of Asians and Caucasians and discovering the chopsticks gene. This can be overcome in GWAS by a technique called principal components analysis, which can be used to model the ancestry of the population and correct for stratification before conducting the analysis.

http://youtu.be/mbRItXENYkE

The next speaker, Daniel Benjamin, spoke on the third problem - the low power of candidate gene studies. Power is the ability to statistically demonstrate an association when that association exists. A test with low power will miss the associations most of the time.

The low power of candidate gene studies is partly due to their typically low sample size, usually between 50 and 3,000 people. Benjamin points out that there may not be any genes in social science with effects large enough to be detected in samples of this size.

The low power of a study has an important implication beyond the inability to find any effects that exist. If real results are rare, they will be swamped by the false positives, which would occur for 1 in 20 tests using the typical significance level. Benjamin runs through some numerical examples and shows that given the expected effect sizes of genes on social science outcomes, you simply shouldn't trust most candidate gene study results. False positives will drown the real findings. This contrasts with GWAS. Once you get to decent sample sizes in the order of 100,000, you can be relatively confident that what you do find (even though you miss a lot) will be true.

Benjamin also talks about the [Social Science Genetic Association Consortium (SSGAC)](http://www.ssgac.org/), which is an attempt to build datasets large enough to apply GWAS to social outcomes such as IQ and risk aversion. The proof of concept was on educational attainment, which the next speaker covers in more detail.

http://youtu.be/vPDqFB2GMUk

Philipp Koellinger opens by asking why there are so many null results in the search for genetic influences. Is it because the effects are small? Because they are non-linear? Or there are gene-environment interactions? Maybe the results of twin studies showing most social outcomes are heritable are wrong?

Part of the answer was given by a study of educational attainment in which Koellinger and the previous two speakers were involved. They used a GWAS to search for SNPs that affected educational attainment in an initial sample of 100,000 people. They then replicated the result in another sample of 25,000 people. All three SNPs found in the discovery stage were replicated.

Importantly, the effect sizes were smaller than expected, with those three SNPs explaining 0.02% of the variation in educational attainment. If you added up the effects of all the SNPs in their sample, you could explain around 2 to 2.5% of the variation.

While this sounds low, it provides a basis for hope. Based on projections for larger sample size, it should be possible to explain 20% of the variation in education attainment through genetic factors.

http://youtu.be/opGrHm4v_9o

Jason Fletcher was next, and he asked two main questions. First, how much should we believe GWAS results given how differently GWAS is done compared to normal science procedure. Second, what use are GWAS results? He spends more time on the second question and points out the usual possibilities, such as providing measures for latent variables. For example, if you don't know the IQ of your sample but have their genomes and know how this affects intelligence, the genetic information could be used to attempt to determine the effect of IQ on a certain outcome.

Fletcher also points to the potential for exploration of gene-environment effects. He gives the example of people responding differently to tobacco taxation based on having different alleles. His paper on this topic is [here](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0050576).

Within his talk, Fletcher asks an interesting question about whether the SSGAC will become a natural monopoly in GWAS. Do we need a second SSGAC to enable people to check the results, and is it feasible for one to emerge? Others may be more viable as genetic testing becomes cheaper, but the tendency for one to dominate may still remain.

In the questions to Fletcher's presentation, Benjamin makes the important point that the use of GWAS results as control variables could give much more precision to the estimates of the effect that a social science experiment is designed to measure. He gives the example of the Perry pre-school project - expensive educational interventions with a small sample, in which any added precision as to their effects would be of great value.

http://youtu.be/eA52b-PzGx4

The last speaker, Dalton Conley, returned to the population stratification problem. His argument is that it may not be as easy to solve as it seems. Conley refers mainly to a technique called Genomic-relatedness-matrix restricted maximum likelihood (GREML) or Genome-wide complex trait analysis (GCTA) (which I have [posted about before](https://jasoncollins.blog/the-genetic-architecture-of-economic-and-political-preferences/)). This technique seeks to determine the contribution of all the sampled SNPs combined to variation in a trait. The output is a lower bound estimate of heritability. This technique relies, however, on an assumption that among those who are less related than second cousins (higher degrees of relatedness are removed), they share alleles in a way that is uncorrelated with any similarity in environment.

Conley argues that this assumption is false, and shows that using GREML, he can obtain a finding that birth in an urban or rural environment is heritable, in direct violation of the assumption. This result does not disappear after controlling for population stratification.

To deal with this problem, consideration should be given to testing for variation within families - any differences in genes between siblings will truly be random. The problem with this is that most massive datasets for which GWAS is performed don't have pedigree data of that nature. The good news, however, is that the violation of the assumption does not seem to puncture the GWAS results. It is violated but the consequences are trivial. A paper by Conley and friends on this paper can be found [here](http://www.nature.com/jhg/journal/v59/n6/full/jhg201414a.html).

http://youtu.be/HUhXHCHqIXQ
