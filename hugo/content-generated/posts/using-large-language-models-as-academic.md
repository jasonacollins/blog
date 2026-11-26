---
title: 'Using large language models as an academic'
author: "Jason Collins"
date: 2023-04-28 09:00:00+10:00
draft: false
sync_source: "posts/using-large-language-models-as-academic.qmd"
sync_route: "quarto"
sync_hash: "20c6e751b3cf"
---

{{< html >}}
<p>This post started as a draft email to my colleagues about how I was using large language models in my work to achieve some fairly large efficiency gains. I realised that this was easier to send as a blog post. And why not share more broadly?</p>
<p>I am a long way from the frontier in how I am using these tools. If you want to see the frontier, go read <a href="https://www.oneusefulthing.org/">Ethan Mollick</a> among others. But I would estimate I’m using these tools more than 95% of academics, so hopefully there is something in there for many of you.</p>
<section id="my-toolkit" class="level2">
<h2 class="anchored" data-anchor-id="my-toolkit">My toolkit</h2>
<p>As an academic, I gain free access to <a href="https://github.com/features/copilot">GitHub Copilot</a>. (It’s only $10 a month otherwise.) Copilot is badged as “your coding companion”, providing code suggestions in coding environments. But while badged this way, Copilot also provides text suggestions more broadly, and that is how I largely use it.</p>
<p>Copilot gives me access to whatever language models Microsoft is running behind it. I’m not sure if <a href="https://openai.com/product/gpt-4">GPT-4</a> is available through Copilot yet, but I would say performance on Copilot has improved over the six months I have been using it.</p>
<p>To access Copilot, I write markdown documents in <a href="https://code.visualstudio.com">Visual Studio Code</a>. Since I started blogging (12 years now!) I have always written in markdown (and at the moment a particular flavour of markdown, <a href="https://quarto.org">Quarto</a>). Before the emergence of Copilot, I also used <a href="https://posit.co/download/rstudio-desktop/">RStudio</a> and other text editors that support markdown. But with Copilot not available in RStudio, I’m almost exclusively in Visual Studio Code now. For those who want more specific guidance on how to set this up, I’ve added that at the bottom of this post.</p>
<p>I also work with <a href="https://chat.openai.com/">ChatGPT</a> open in a browser. If Copilot isn’t giving me what I want, ChatGPT often will. If I can frame my requirement as a standalone question, ChatGPT tends to do a better job. But when working on a document, Copilot’s suggestions are normally better (unless I paste the whole document into ChatGPT).</p>
<p>I’ve tried Bing, but find it harder work to get what I want unless I have a question for which I want references.</p>
</section>
<section id="writing-lecture-notes-efficiency-gain-10-to-30" class="level2">
<h2 class="anchored" data-anchor-id="writing-lecture-notes-efficiency-gain-10-to-30">Writing lecture notes (efficiency gain: 10 to 30%)</h2>
<p>I don’t find Copilot particularly useful if I’m writing something original such as a blog post. In writing this post I wouldn’t say Copilot has increased my efficiency at all (outside of helping me create the examples). I sometimes accepted suggestions from Copilot, but the need to filter through the various suggestions resulted in negligible efficiency gain.</p>
<p>But for lecture notes, which are more mechanical, there are some clear gains. The notes for my undergraduate behavioural economics subject (which you can access <a href="https://be.jcx.au">here</a>) were produced with Copilot.</p>
<p>Here are a few instances where Copilot has been useful.</p>
<p>Often the notes include a statement of a concept followed by a step-by-step example or illustration. The gain comes when you’re writing those steps.</p>
<p>For example, in a section about decision making under risk, I might write:</p>
<blockquote class="blockquote">
<p>Bill is a risk-averse agent with utility function {{< math >}}u(x)=\text{ln}(x){{< /math >}} and wealth of $100. He is offered a 50:50 bet to win $100, lose $50.</p>
<p>Will Bill accept the bet?</p>
</blockquote>
<p>Copilot will sometimes write something like:</p>
<blockquote class="blockquote">
<p>Can someone please help me answer the following question: “Will Bill accept the bet?”</p>
</blockquote>
<p>There must be a lot of study cheat sites forming part of the training data.</p>
<p>But if Copilot does that, simply write the first couple of words of the answer “First, we calculate…” and then Copilot is away.</p>
<blockquote class="blockquote">
<p>First, we calculate the expected utility of each option. The expected utility of the bet is:</p>
</blockquote>
<div class="code-copy-outer-scaffold"><div class="sourceCode" id="cb1"><pre class="sourceCode markdown code-with-copy"><code class="sourceCode markdown"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="in">```{=tex}</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="in">\begin{aligned}</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="in">EU(\text{bet}) &amp;= 0.5 \times u(100) + 0.5 \times u(-50) \\</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="in">&amp;= 0.5 \times \text{ln}(100) + 0.5 \times \text{ln}(50) \\</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="in">&amp;= 4.259</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="in">\end{aligned}</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="in">```</span></span></code></pre></div></div>
<blockquote class="blockquote">
<p>The expected utility of not taking the bet is:</p>
</blockquote>
<div class="code-copy-outer-scaffold"><div class="sourceCode" id="cb2"><pre class="sourceCode markdown code-with-copy"><code class="sourceCode markdown"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="in">```{=tex}</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="in">\begin{aligned}</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="in">EU(\text{no bet}) &amp;= U(100) \\</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="in">&amp;= \text{ln}(100) \\</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a><span class="in">&amp;= 4.605</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a><span class="in">\end{aligned}</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a><span class="in">```</span></span></code></pre></div></div>
<blockquote class="blockquote">
<p>As the expected utility of the bet is less than the expected utility of not taking the bet, Bill will not accept the bet.</p>
</blockquote>
<p>Not bad for a few seconds of work. For those unfamiliar with the mathematical notation, this is {{< math >}}\LaTeX{{< /math >}}, which renders into nice equations like this.</p>
{{< math display >}}\begin{aligned}
EU(\text{bet}) &= 0.5 \times u(100) + 0.5 \times u(-50) \\
&= 0.5 \times \text{ln}(100) + 0.5 \times \text{ln}(50) \\
&= 4.259
\end{aligned}{{< /math >}}
<p>I might beef this up with a better explanation, or paste the question into ChatGPT direct, where I tend to get more detailed answers. GPT-4 also tends to be better at maths. (Copilot has done OK here - the logs are correct! Maybe more evidence of improvement in Copilot, although the answer still needs tweaking.)</p>
<p>Copilot is also great when I’m doing repetitive tasks such as describing the elements of an equation or diagram. Start describing the first element and it might give you the rest. And if you write a point followed by “Conversely, …”, Copilot is often on the money.</p>
</section>
<section id="coding-efficiency-gain-10x" class="level2">
<h2 class="anchored" data-anchor-id="coding-efficiency-gain-10x">Coding (efficiency gain: 10x)</h2>
<p>Despite spending a lot of time in R, I am a crap coder. The simplest errors have me crawling Stack Overflow for hours. I struggle to build a structure when looking at a blank screen.</p>
<p>My typical approach now is to write a comment, let Copilot do the first cut and then tweak the code until it is in shape.</p>
<p>That tweaking isn’t manual tweaking either.</p>
<p>If there is an error or problem that I can’t resolve, I’ll simply write:</p>
<blockquote class="blockquote">
<p>The above code generates the error “PASTE ERROR”. I fix it by …</p>
</blockquote>
<p>And a solution appears. Sometimes I’ll also paste the code and the error into ChatGPT and ask for code that does not have that error.</p>
<p>If the code looks overly complicated, a request to simplify often yields good results. (I’ve been asking ChatGPT to review some of my old code recently. I’m a bit embarrassed at how much more efficiently I could have written it.)</p>
<p>Here are two recent coding applications that I was particularly excited about.</p>
<section id="creating-diagrams" class="level3">
<h3 class="anchored" data-anchor-id="creating-diagrams">Creating diagrams</h3>
<p>In my lecture notes, I use <a href="https://ggplot2.tidyverse.org">ggplot</a> to produce nice-looking graphs. (I’m slowly replacing old PowerPoint diagrams that still litter the notes).</p>
<p>Recently I wanted to generate a chart showing a <a href="https://be.jcx.au/prospect-theory/probability-weighting">probability weighting function</a> from prospect theory.</p>
<p>I created an R code block and typed a comment:</p>
<blockquote class="blockquote">
<p>#Plot of probability weighting function using ggplot2</p>
</blockquote>
<p>Here’s the result with the diagram rendered below:</p>
<div class="cell">
<div class="code-copy-outer-scaffold"><div class="sourceCode cell-code" id="cb3"><pre class="sourceCode r code-with-copy"><code class="sourceCode r"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="co">#Plot of probability weighting function using ggplot2</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="fu">library</span>(ggplot2)</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="co">#Define probability weighting function</span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a>prob_weight <span class="ot">&lt;-</span> <span class="cf">function</span>(p, alpha){</span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a>  <span class="fu">exp</span>(<span class="sc">-</span>(<span class="sc">-</span><span class="fu">log</span>(p))<span class="sc">^</span>alpha)</span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a>}</span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a><span class="co">#Create data frame of probabilities and weights</span></span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a>prob <span class="ot">&lt;-</span> <span class="fu">seq</span>(<span class="dv">0</span>, <span class="dv">1</span>, <span class="fl">0.001</span>)</span>
<span id="cb3-11"><a href="#cb3-11" aria-hidden="true" tabindex="-1"></a>prob_df <span class="ot">&lt;-</span> <span class="fu">data.frame</span>(<span class="at">prob =</span> prob, <span class="at">weight =</span> <span class="fu">prob_weight</span>(prob, <span class="fl">0.6</span>))</span>
<span id="cb3-12"><a href="#cb3-12" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-13"><a href="#cb3-13" aria-hidden="true" tabindex="-1"></a><span class="co">#Plot</span></span>
<span id="cb3-14"><a href="#cb3-14" aria-hidden="true" tabindex="-1"></a><span class="fu">ggplot</span>(prob_df, <span class="fu">aes</span>(<span class="at">x =</span> prob, <span class="at">y =</span> weight)) <span class="sc">+</span></span>
<span id="cb3-15"><a href="#cb3-15" aria-hidden="true" tabindex="-1"></a>  <span class="fu">geom_line</span>() <span class="sc">+</span></span>
<span id="cb3-16"><a href="#cb3-16" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-17"><a href="#cb3-17" aria-hidden="true" tabindex="-1"></a>  <span class="co">#Add labels</span></span>
<span id="cb3-18"><a href="#cb3-18" aria-hidden="true" tabindex="-1"></a>  <span class="fu">labs</span>(<span class="at">x =</span> <span class="st">"Probability"</span>, <span class="at">y =</span> <span class="st">"Weight"</span>)</span></code></pre></div></div>
<div class="cell-output-display">
<div>
<figure class="figure">
<p><a href="using-large-language-models-as-academic_files/figure-html/unnamed-chunk-1-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-1"><img src="using-large-language-models-as-academic_files/figure-html/unnamed-chunk-1-1.png" class="img-fluid figure-img" width="672"></a></p>
</figure>
</div>
</div>
</div>
<p>Exactly what I wanted. When I implemented this in the notes, all I did was tweak the style and add a 45-degree line.</p>
<p>Copilot’s offering uses Prelec’s <span class="citation" data-cites="prelec1998">(<a href="#ref-prelec1998" role="doc-biblioref">1998</a>)</span> probability weighting function. Whether it picked that up from earlier text or just gave the most common function for probability weighting, I don’t know, but it’s what I would have used if doing it manually.</p>
<p>Copilot didn’t offer this full chunk of code at once. Each comment was offered, then the piece of code after it, one after the other. But the only work I did was writing the first comment and pressing tab several times as each succeeding comment or chunk of code was suggested. (Copilot has certainly increased the level of comments in my code too.)</p>
<p>One thing I have noted is that Copilot uses all of the text in the document in giving its suggestions. In writing this post I wasn’t able to replicate what I did when writing the lecture notes. I got better results in the lecture notes themselves. A few paragraphs about probability weighting before I ask for the code generate much better results than asking for the chart straight up.</p>
</section>
<section id="converting-code-across-languages" class="level3">
<h3 class="anchored" data-anchor-id="converting-code-across-languages">Converting code across languages</h3>
<p>My second example relates to a proposed reproduction of the results in Berkeley Dietvorst’s <a href="https://doi.org/10.1037/xge0000033">Algorithm aversion: People erroneously avoid algorithms after seeing them err</a>. Data and the code for analysis were <a href="https://researchbox.org/379&amp;PEER_REVIEW_passcode=MOQTEQ">available on ResearchBox</a>.</p>
<p>The problem was that the code was in Stata, I don’t have Stata, and I have no desire to learn Stata. So, I pasted the code into ChatGPT and asked for a conversion to R. What I received was 90% of the way there. Initially there was an error, but ChatGPT solved the error first shot. I then had to tweak a couple of the variable manipulations and specify that some of the t-tests were paired t-tests, and that was it. In less than 10 minutes I had code that was reproducing exactly the results from Study 1.</p>
</section>
</section>
<section id="generating-quiz-questions-efficiency-gain-3x" class="level2">
<h2 class="anchored" data-anchor-id="generating-quiz-questions-efficiency-gain-3x">Generating quiz questions (efficiency gain: 3x)</h2>
<p>One of the best ways to learn is to be tested. As a result, I offer students in my undergraduate subject a series of practice quizzes that they can work through. In the first class I tell the students about the effectiveness of spaced repetition as a learning technique. They can then use the practice quiz questions on an intermittent basis to test whether they have learnt core concepts. (When I find the bandwidth, I plan to implement those quiz questions in <a href="https://withorbit.com">Orbit</a> or something similar, and place them through the <a href="https://be.jcx.au">online notes</a>.)</p>
<p>Some questions are easy to generate: definitions and the like. But it’s hard work to generate questions in bulk and I struggle to generate plausible-sounding but incorrect answers to multiple-choice questions.</p>
<p>I now ask ChatGPT to generate them. In the prompts, I vary in the specificity of the questions. “Give me 20 multiple choice questions testing the concept of loss aversion.” “Give me 20 multiple choice questions testing prospect theory.” And so on. Out of each batch of 20, only a few will be suitable. There might be no correct answer or two correct answers, or ChatGPT might confuse concepts. But by tweaking my instruction by, say, describing the level of the students (undergraduate) or more explicitly defining the concept, it doesn’t take long to get 10 or so good questions.</p>
<p>I haven’t used ChatGPT to generate assessable quiz questions yet, but I’m planning to use it for the upcoming final exam. That exam is a closed-book AI-invigilated exam, so is less vulnerable to someone simply feeding the questions back to ChatGPT. One idea I’m tempted to try is to feed it some previous year’s exams and ask for new exams on the same concepts.</p>
</section>
<section id="writing-organisational-fluff-efficiency-gain-2x" class="level2">
<h2 class="anchored" data-anchor-id="writing-organisational-fluff-efficiency-gain-2x">Writing organisational fluff (efficiency gain: 2x)</h2>
<p>Work in any decent-sized modern organisation and you will have to write some level of fluff to satisfy the higher-ups, clients, government requirements and the like.</p>
<p>I am hopeless at those tasks. I have to invest heavily to make fluff sound decent.</p>
<p>My approach to these exercises depends on the degree of pointlessness.</p>
<p>If the task relates to a process that will have zero impact on what anyone will do, I simply give the task to ChatGPT, let it do the first cut and then tweak as required. One or two sentences of guidance often get you 80% of the way there.</p>
<p>If I think there is a positive benefit to the task, or it’s for public consumption, I’ll be more proactive first up. I will write a rough draft first, not caring much about the writing but making sure the concepts I want to include are there. It might be in dot points. Then I’ll ask ChatGPT for a version that is “clearer”, “simpler” or “better written” or “for a ten-year-old”. I often find this process works best in two stages. The “clearer” version often uses the same words as me, but structures them better. Then I ask ChatGPT to write it again, but instructing it to “forget about the original text.” I’ve been pleasantly surprised at how good some of those second versions are.</p>
</section>
<section id="slide-filler-efficiency-gain-2x" class="level2">
<h2 class="anchored" data-anchor-id="slide-filler-efficiency-gain-2x">Slide filler (efficiency gain 2x)</h2>
<p>I’m not a big fan of pointless eye candy in slide decks. But if you’re doing pre-recorded material (see below) and you don’t want your mug on the screen, you sometimes need some filler. In that case, I head straight to <a href="https://labs.openai.com">DALL-E</a>. I’ve adopted a theme for my lecture slides - black and white line drawings - so I ask for a black and white line drawing of something related to what I am talking about.</p>
<p>This is much quicker than hunting for images with open usage rights.</p>
<p>Compared to ChatGPT, DALL-E seems pretty lame. It still struggles with concepts such as “on” or “ten” or “without writing”. Sometimes I’ll give up on a more complex concept (a deck of cards on a table) and go for something simpler (a deck of cards). I’m looking forward to GPT-4 sitting behind an image generator.</p>
<p>I’ve also tried <a href="https://stablediffusionweb.com/">Stable Diffusion</a> but found it was much harder work to get something I can use.</p>
</section>
<section id="whats-next" class="level2">
<h2 class="anchored" data-anchor-id="whats-next">What’s next?</h2>
<section id="ai-voiced-lectures" class="level3">
<h3 class="anchored" data-anchor-id="ai-voiced-lectures">AI-voiced lectures</h3>
<p>My next frontier is artificial voice generation for my pre-recorded lectures.</p>
<p>Last year - my first year taking the undergraduate behavioural economics subject - the subject was structured as two hours of live (but online) lectures and one hour of tutorials (either online or in-person). Both lectures and the online tutorial were recorded, so students could watch at another time. The net result was limited attendance - and most students didn’t watch the videos either.</p>
<p>This year I thought I’d move the subject out of the 1950s and make it a combination of some <a href="https://www.youtube.com/@jasonacollins">short pre-recorded videos</a>, interactive online seminars and tutorials. This approach has backfired - the students don’t watch the videos and don’t want to interact - but that’s a story for another post, perhaps in combination with my review of Bryan Caplan’s The Case Against Education.</p>
<p>To produce the videos I’ve written scripts, which also form the <a href="https://be.jcx.au">subject notes</a>. I read that accompanied by slides. I’m a hopeless off-the-cuff speaker, so for anything that’s going to be recorded and treated as a long-term asset, I’m scripting.</p>
<p>There are three pain points in this exercise. First, I speak too fast (even when I think I’m speaking slow) and I enunciate many words poorly. Second, recording takes a lot of time. I rarely get a two to five-minute video in a single take. Third, if I want to tweak the recording, I need to either re-record solid chunks of text or fiddle around with video edits.</p>
<p>So, why not get an artificial voice to do the speaking?</p>
<p>I’ve been experimenting with <a href="https://murf.ai">Murf.ai</a>, <a href="https://speechify.com">Speechify</a>, <a href="https://play.ht/">play.ht</a> and <a href="https://beta.elevenlabs.io">Eleven</a>. Eleven has comfortably the most realistic voices but doesn’t yet appear to have an easy way to create video using slides. If they introduce that, I’m fully on board. Murf.ai allows me to pair slides and text to create videos, but the voices still sound a bit robotic. But with the ability to pace their speech, Murf.ai is already a better option than me. And they’ll only get better.</p>
<p>The production process is then easy. Upload the text (although I do have to write out the equations in the course notes in text). Upload the slides and match to the text. Click play and the new video is generated.</p>
<p>With a setup such as this, if I want to tweak parts of the videos, I can simply edit the written text and generate a new version. Adding or editing slides is also simple as they are uploaded and matched to the new text. I’m also able to run much sharper slide changes as I can time exactly the transitions.</p>
<p>An interesting question about the artificial voice-over is how the university (and students) will take it. Do they see it as a lazy option? (When I taught at the University of Sydney in 2020 during the early stages of the pandemic, you weren’t allowed to use pre-recorded videos from one semester in a later semester. Someone hated the idea that the academics might not be working hard enough …) If I were able to clone my voice, this could become a moot issue. play.ht and Eleven have the ability to “clone” your voice, but neither can handle non-American accents. The rhythm of my cloned voice (maybe my natural rhythm) also seemed a bit clunky.</p>
<p>I think the artificial voice-over is a great option. Academics should be investing in developing high-quality assets that can be re-used rather than bumbling along with low-quality off-the-cuff lectures. They can then invest their time in the other parts of teaching: the in-person seminars and tutorials where students can get the personalised bit of their education.</p>
<p>This approach does point to a challenge for higher education providers. Once you’ve got high-quality recorded material for basic courses, why would you want them generated by each lecturer in each university? Someone could produce an amazing Behavioural Economics 101 (I want the Dave Malan <a href="https://www.edx.org/course/introduction-computer-science-harvardx-cs50x">CS50</a> version of this), other lecturers can subscribe to the service and they can now focus on those human bits (not that most students want that…).</p>
<p>I’ve also started looking at options to create an AI avatar - either based on videos/photos of me or a random AI avatar - for some parts of the videos. I’m leaving that one for the moment but can see myself revisiting in the next year.</p>
</section>
<section id="chat-integrated-with-copilot-and-other-microsoft-tools" class="level3">
<h3 class="anchored" data-anchor-id="chat-integrated-with-copilot-and-other-microsoft-tools">Chat integrated with Copilot (and other Microsoft tools)</h3>
<p>At the moment I have multiple streams of access to these tools. I’m looking forward to chat appearing in Copilot - I’m on the waiting list to access - which will remove the need for the separate browser with ChatGPT.</p>
<p>GPT-4 is also coming to other Microsoft tools soon. If I don’t have to exit PowerPoint to get my images, that’s an extra efficiency.</p>
<p>I’m largely in the Mac ecosystem, but Apple seems absolutely crap in the world of assistants/chat. (“Hey Siri, tell me this most basic fact about the world.” “I’ve sent some irrelevant web results to your iPhone…..”) If at some point these tools become tied to Microsoft hardware or Windows, I’m moving.</p>
<p>(I exited the Google ecosystem when I had trouble sharing a file from Google Drive because it breached the terms of service. It was a document that included the words “vaccination” and “scepticism”, although if you see the <a href="../posts/megastudy-scepticism.html">resulting post</a>, you can see the Google algorithm was pretty crude. At that point I opted for what I hope is a bit more privacy and jettisoned Google…)</p>
</section>
</section>
<section id="getting-going-with-github-copilot" class="level2">
<h2 class="anchored" data-anchor-id="getting-going-with-github-copilot">Getting going with GitHub Copilot</h2>
<p>The below gives the basic steps to achieve my setup.</p>
<p>If you are an academic, you can sign up for (free) academic access to Copilot at <a href="https://education.github.com/discount_requests/application">this link</a>. If you’re not an academic or student, sign up for $10 a month as described <a href="https://docs.github.com/en/billing/managing-billing-for-github-copilot/managing-your-github-copilot-subscription-for-your-personal-account">here</a>. You’ll need a GitHub account to do this. I think the $10 a month is worth it, but the free ChatGPT will give you most of these gains with a bit more work.</p>
<p>Visual Studio Code is available <a href="https://code.visualstudio.com">here</a>. (I use the Mac version.) Download and install.</p>
<p>Install the GitHub Copilot extension into Visual Studio Code (or the GitHub Copilot Nightly extension if you want access to features earlier). Instructions on installing the extension are <a href="https://docs.github.com/en/copilot/quickstart#installing-the-github-copilot-extension-for-visual-studio-code">here</a>. On installation you’ll be prompted to log in to GitHub to gain access to authorise Copilot.</p>
<p>Once you have done that, using Copilot is easy. You simply type. As you type, you will be given suggestions.</p>
<p>I write in markdown (or as noted above, a flavour of markdown called <a href="https://quarto.org">Quarto</a>). It allows me to include {{< math >}}\LaTeX{{< /math >}} maths and R computations within any document (as I have in this post). If you’re an academic stuck in the {{< math >}}\LaTeX{{< /math >}} ecosystem, you can also write in Visual Studio Code wholly in {{< math >}}\LaTeX{{< /math >}}. (Although I say jettison that dinosaur and use {{< math >}}\LaTeX{{< /math >}} maths in a markdown document - that ability to add computations is worth it, and the readability and experience are so much easier.) You can also just wait until GPT-4 appears in Word. I expect that’s not too far away.</p>



</section>

<div id="quarto-appendix" class="default"><section class="quarto-appendix-contents" role="doc-bibliography" id="quarto-bibliography"><h2 class="anchored quarto-appendix-heading">References</h2><div id="refs" class="references csl-bib-body hanging-indent" data-entry-spacing="0" data-line-spacing="2" role="list">
<div id="ref-prelec1998" class="csl-entry" role="listitem">
Prelec, D. (1998). The probability weighting function. <em>Econometrica</em>, <em>66</em>(3), 497–527. <a href="https://doi.org/10.2307/2998573">https://doi.org/10.2307/2998573</a>
</div>
</div></section></div>
{{< /html >}}
