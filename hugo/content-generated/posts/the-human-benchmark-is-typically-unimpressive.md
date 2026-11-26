---
title: 'The human benchmark is typically unimpressive'
author: "Jason Collins"
date: 2024-10-28 09:00:00+10:00
draft: false
image: "img/ayers-et-al-2023-figure.png"
sync_source: "posts/the-human-benchmark-is-typically-unimpressive.md"
sync_route: "quarto"
sync_hash: "973aa6a23653"
---

{{< html >}}
<p>If you ever read a claim of an AI outperforming a human, dig into the performance data to check out the human benchmark. The mediocrity of the human is often more salient than the competence of the AI. The AI has an easy job.</p>
<p>Here’s an example from a paper by Ayers and friends <span class="citation" data-cites="ayers2023">(<a href="#ref-ayers2023" role="doc-biblioref">2023</a>)</span>. They sampled 195 question and response exchanges on Reddit’s <a href="https://www.reddit.com/r/AskDocs">r/AskDocs</a> and entered those same questions into ChatGPT 3.5. Responses by the Reddit physicians and ChatGPT were then independently rated for quality and empathy.</p>
<p>ChatGPT responses were rated as higher quality, with 78% of ChatGPT responses rated as good or very good quality. 22% of physician responses had that rating. Similarly, 45% of ChatGPT responses were rated empathetic or very empathetic, compared to 5% for the physicians.</p>
<div class="quarto-figure quarto-figure-center">
<figure class="figure">
<figcaption>Distribution of Average Quality and Empathy Ratings for Chatbot and Physician Responses to Patient Questions</figcaption>
<p><a href="img/ayers-et-al-2023-figure.png" class="lightbox" data-gallery="quarto-lightbox-gallery-1" title="Distribution of Average Quality and Empathy Ratings for Chatbot and Physician Responses to Patient Questions">{{< img src="img/ayers-et-al-2023-figure.png" class="img-fluid figure-img" alt="Distribution of Average Quality and Empathy Ratings for Chatbot and Physician Responses to Patient Questions" >}}</a></p>
</figure>
</div>
<p>I <a href="https://doi.org/10.7910/DVN/BZARC3">downloaded the csv file</a> of the responses. The most striking feature was the brevity and curtness of the humans (52 words average compared to 211 for ChatGPT). Here are a few of the human responses.</p>
<p>A friend’s uninsured mother needs a liver transplant. What should she do?</p>
<blockquote class="blockquote">
<p>Its not just a work around the insurance, she will need lifelong expensive meds after surgery as well. Why does she not have insurance?</p>
</blockquote>
<p>Should they be worried about arm pain when they sneeze?</p>
<blockquote class="blockquote">
<p>The answer simply is no..</p>
</blockquote>
<p>Are they crazy for thinking they have pancreatic or some other cancer given a list of symptoms?</p>
<blockquote class="blockquote">
<p>Why do you think you have pancreatic cancer?</p>
</blockquote>
<p>Where can someone from a family of anti-vaxers get information on vaccines?</p>
<blockquote class="blockquote">
<p>See your general practitioner. They’ll understand and will sort you out bro.</p>
</blockquote>
<p>Does smelly poop and less frequent bowel movements indicate cancer?</p>
<blockquote class="blockquote">
<p>This does not sound like cancer. I would advise stop googling.</p>
</blockquote>
<p>In contrast, ChatGPT gave long, involved answers that inevitably began with a statement of concern for the medical condition. “I’m sorry to hear about your friend’s mom.” Funnily enough, that verbosity annoys me the most in using LLMs. One person’s verbosity is another’s empathy.</p>
<p>I don’t mean the above to be read as a criticism of AI performance. (This is ChatGPT 3.5 after all!) But there’s an interesting contrast between performance benchmarking and discussions of the role of AI. In benchmarking exercises, we use actual human performance as the standard. But when discussing whether AI should replace or augment human decisions, we often compare AI to an idealised human. We have a mental image of a high-quality physician with excellent bedside manner, not the distribution of skills and empathy we actually have. Scrutinising the performance data for some of these benchmarking exercises is a good reminder that AI doesn’t always have to be great to be better.</p>




<div id="quarto-appendix" class="default"><section class="quarto-appendix-contents" role="doc-bibliography" id="quarto-bibliography"><h2 class="anchored quarto-appendix-heading">References</h2><div id="refs" class="references csl-bib-body hanging-indent" data-entry-spacing="0" data-line-spacing="2" role="list">
<div id="ref-ayers2023" class="csl-entry" role="listitem">
Ayers, J. W., Poliak, A., Dredze, M., Leas, E. C., Zhu, Z., … Smith, D. M. (2023). Comparing physician and artificial intelligence chatbot responses to patient questions posted to a public social media forum. <em>JAMA Internal Medicine</em>, <em>183</em>(6), 589–596. <a href="https://doi.org/10.1001/jamainternmed.2023.1838">https://doi.org/10.1001/jamainternmed.2023.1838</a>
</div>
</div></section></div>
{{< /html >}}
