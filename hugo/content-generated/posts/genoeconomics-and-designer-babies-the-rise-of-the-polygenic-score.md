---
author: "Jason Collins"
date: 2018-11-23 08:00:38+00:00
draft: false
title: 'Genoeconomics and designer babies: The rise of the polygenic score'
sync_source: "posts/genoeconomics-and-designer-babies-the-rise-of-the-polygenic-score.md"
sync_route: "pandoc"
sync_hash: "34126a3fdafe"
---

{{< html >}}
<p>When <a href="https://en.wikipedia.org/wiki/Genome-wide_association_study">genome-wide association studies</a> (GWAS) were first used to study complex polygenic traits, the results were underwhelming. Few genes with any predictive power were found, and those that were typically explained only a fraction of the genetic effects that <a href="https://en.wikipedia.org/wiki/Twin_study">twin studies</a> suggested were there.</p>
<p>This led to divergent responses, ranging from continued resistance to the idea that genes affect anything, to a quiet confidence that once sample sizes became large enough those genetic effects would be found.</p>
<p>Increasingly large samples are now showing that the <a href="http://infoproc.blogspot.com/2017/08/estimation-of-genetic-architecture-for.html">quiet confidence was justified</a>, with a steady flow of papers emerging finding material genetic effects on traits including educational attainment, intelligence and height.</p>
<p>One source of this work are “genoeconomists”. From Jacob Ward in the <a href="https://www.nytimes.com/interactive/2018/11/16/magazine/tech-design-economics-genes.html">New York Times</a>:</p>
<blockquote>
<p>Once a G.W.A.S. shows genetic effects across a group, a “polygenic score” can be assigned to individuals, summarizing the genetic patterns that correlate to outcomes found in the group. Although no one genetic marker might predict anything, this combined score based on the entire genome can be a predictor of all sorts of things. And here’s why it’s so useful: People <em>outside</em> that sample can then have their DNA screened, and are assigned their own polygenic score, and the predictions tend to carry over. This, Benjamin realized, was the sort of statistical tool an economist could use.</p>
<p>…</p>
<p>As an economist, however, Benjamin wasn’t interested in medical outcomes. He wanted to see if our genes predict social outcomes.</p>
<p>In 2011, with a grant from the National Science Foundation, Benjamin launched the Social Science Genetic Association Consortium, an unprecedented effort to gather unconnected genetic databases into one enormous sample that could be studied by researchers from outside the world of genetic science. In July 2018, Benjamin and four senior co-authors, drawing on that database, published a landmark study in Nature Genetics. More than 80 authors from more than 50 institutions, including the private company 23andMe, gathered and studied the DNA of over 1.1 million people. It was the largest genetics study ever published, and the subject was not height or heart disease, but how far we go in school.</p>
<p>The researchers assigned each participant a polygenic score based on how broad genetic variations correlated with what’s called “educational attainment.” (They chose it because intake forms in medical offices tend to ask patients what education they’ve completed.) The predictive power of the polygenic score was very small — it predicts more accurately than the parents’ income level, but not as accurately as the parents’ own level of educational attainment — and it’s useless for making individual predictions.</p>
</blockquote>
<p>One of the most interesting possibilities for using polygenic scores is to use them to control for heterogeneity in research subjects. Ward writes:</p>
<blockquote>
<p>Several researchers involved in the project mentioned to me the possibility of using polygenic scores to sharpen the results of studies like the ongoing Perry Preschool Project, which, starting in the early 1960s, began tracking 123 preschool students and suggested that early education plays a large role in determining a child’s success in school and life. Benjamin and other co-authors say that perhaps sampling the DNA of the Perry Preschool participants could improve the accuracy of the findings, by controlling for those in the group that were genetically predisposed to go further in school.</p>
</blockquote>
<p>In a world with easy access to genetic samples, it could become common to include genetic controls in analysis of interesting societal outcomes, in the same way we now control for parental traits.</p>
<p>A couple of times in the article, Ward notes that “scores aren’t individually predictive”. He writes that “The predictive power of the polygenic score was very small — it predicts more accurately than the parents’ income level, but not as accurately as the parents’ own level of educational attainment — and it’s useless for making individual predictions.”</p>
<p>I’m not sure what Ward’s definition of “predictive” is for an individual, but take this example from the article:</p>
<blockquote>
<p>The authors calculated, for instance, that those in the top fifth of polygenic scores had a 57 percent chance of earning a four-year degree, while those in the bottom fifth had a 12 percent chance. And with that degree of correlation, the authors wrote, polygenic scores can improve the accuracy of other studies of education.</p>
</blockquote>
<p>That looks like predictive power to me. Take an individual from the sample or an equivalent population, look at their polygenic score, and then assign a probability of whether they will obtain a four-year degree.</p>
<p>I recommend reading the whole <a href="https://www.nytimes.com/interactive/2018/11/16/magazine/tech-design-economics-genes.html">article</a>.</p>
<p>A related story getting ample press is that <a href="https://genomicprediction.com/">Genomic Prediction</a> has started to offer intelligence screening for embryos. Polygenic scores have been used with success in livestock breeding for a while now, which is often a better place to look for evidence of the future possibilities than listening to those afraid of the human implications of genetic research. From Philip Ball in <a href="https://www.theguardian.com/commentisfree/2018/nov/19/designer-babies-ethical-genetic-selection-intelligence">The Guardian</a>:</p>
<blockquote>
<p>The company says it is only offering such testing to spot embryos with an IQ low enough to be classed as a disability, and won’t conduct analyses for high IQ. But the technology the company is using will permit that in principle, and co-founder Stephen Hsu, who has long advocated for the prediction of traits from genes, is quoted as saying: “If we don’t do it, some other company will.”</p>
<p>The development must be set, too, against what is already possible and permitted in IVF embryo screening. The procedure called pre-implantation genetic diagnosis (PGD) involves extracting cells from embryos at a very early stage and “reading” their genomes before choosing which to implant. It has been enabled by rapid advances in genome-sequencing technology, making the process fast and relatively cheap. In the UK, PGD is strictly regulated by the Human Fertilisation and Embryology Authority (HFEA), which permits its use to identify embryos with several hundred rare genetic diseases of which the parents are known to be carriers. PGD for other purposes is illegal.</p>
<p>In the US it’s a very different picture. Restrictive laws about what can be done in embryo and stem-cell research using federal funding sit alongside a largely unregulated, laissez-faire private sector, including IVF clinics. PGD to select an embryo’s sex for “family balancing” is permitted, for example. There is nothing in US law to prevent PGD for selecting embryos with “high IQ”.</p>
</blockquote>
<p>Ball also expresses a scepticism about the value of the polygenic scores:</p>
<blockquote>
<p>These relationships are, however, statistical. If you have a polygenic score that places you in the top 10% of academic achievers, that doesn’t mean you will ace your exams without effort. Even setting aside the substantial proportion of intelligence (typically around 50%) that seems to be due to the environment and not inherited, there are wide variations for a given polygenic score, one reason being that there’s plenty of unpredictability in brain wiring during growth and development.</p>
<p>So the service offered by Genomic Prediction, while it might help to spot extreme low-IQ outliers, is of very limited value for predicting which of several “normal” embryos will be smartest. Imagine, though, the misplaced burden of expectation on a child “selected” to be bright who doesn’t live up to it. If embryo selection for high IQ goes ahead, this will happen.</p>
</blockquote>
<p>Despite Ball’s scepticism about comparing “normal” embryos, I expect it won’t be long before Genomic Prediction or a counterpart is doing just that.</p>
<p>Steve Hsu, co-founder of Genomic Prediction, comments on the press <a href="http://infoproc.blogspot.com/2018/11/super-smart-designer-babies-guardian-uk.html">here</a> (and provides some links to other articles). He closes by saying:</p>
<blockquote>
<p>“Expert” opinion seems to have evolved as follows:</p>
<ol type="1">
<li><p><em>Of course</em> babies can’t be “designed” because genes don’t really affect anything – <em>we’re all products of our environment!</em></p></li>
<li><p><em>Gulp</em>, even if genes do affect things it’s <em>much too complicated to ever figure out!</em></p></li>
<li><p>Anyone who wants to use this technology (<em>hmm… it works</em>) needs to tread carefully, and to seriously consider the ethical issues.</p></li>
</ol>
<p>Only point 3 is actually correct, although there are still plenty of people who believe 1 and 2 :-(</p>
</blockquote>
{{< /html >}}
