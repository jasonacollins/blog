---
title: 'Using generative AI as an academic - July 2024 edition'
author: "Jason Collins"
date: 2024-07-15 19:00:00+10:00
draft: false
image: "img/gen-AI.webp"
toc: true
sync_source: "posts/using-generative-AI-as-academic-july-2024-edition.qmd"
sync_route: "quarto"
sync_hash: "0924d182ef2b"
---

{{< html >}}
<div class="toc" data-pagefind-ignore><ul>
<li><a href="#my-toolkit">My toolkit</a></li>
<li><a href="#thinking">Thinking</a></li>
<li><a href="#coding-and-data-analysis">Coding and data analysis</a></li>
<ul>
<li><a href="#data-exploration">Data exploration</a></li>
<li><a href="#extracting-pdf-data">Extracting pdf data</a></li>
</ul>
<li><a href="#writing">Writing</a></li>
<ul>
<li><a href="#lecture-notes">Lecture notes</a></li>
<li><a href="#writing-organisational-fluff">Writing organisational fluff</a></li>
<li><a href="#generating-quiz-questions">Generating quiz questions</a></li>
</ul>
<li><a href="#ai-voiced-lectures">AI-voiced lectures</a></li>
<li><a href="#accessing-github-copilot">Accessing GitHub Copilot</a></li>
</ul></div>
<p>I first wrote <a href="../posts/using-large-language-models-as-academic.html">a version of this post in April 2023</a>. A lot has changed since then in both the tools and how I use them.</p>
<p>As was the case then, if you want a sense of the frontier, others such as <a href="https://www.oneusefulthing.org/">Ethan Mollick</a> will give you a better flavour. But if you’re after some practical examples, you might find this useful.</p>
<section id="my-toolkit" class="level2">
<h2 class="anchored" data-anchor-id="my-toolkit">My toolkit</h2>
<p>I use multiple tools, switching between them depending on the task and comparing the responses. I want to gain a sense of the frontier.</p>
<p>As an academic, I gain free access to <a href="https://github.com/features/copilot">GitHub Copilot</a>. (Students can also get free access.) Copilot provides code suggestions in coding environments. But while badged this way, Copilot also provides text suggestions more broadly. To access Copilot, I write markdown documents in <a href="https://code.visualstudio.com">Visual Studio Code</a> or <a href="https://posit.co/download/rstudio-desktop/">RStudio</a>. (For those who want more specific guidance on how to set this up, I’ve added that at the bottom of this post.) If you use Copilot in Visual Studio Code you also gain access to <a href="https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide">Copilot Chat</a>.</p>
<p>I also work with <a href="https://chat.openai.com/">ChatGPT Plus</a> and <a href="https://www.anthropic.com/claude">Claude Pro</a> open in a browser. I subscribe to the Pro/Plus version of both: it is worth it for the superior tools. As you’ll see from the below, I use them all the time, although more recently I lean toward Claude.</p>
<p>I run some other large language models locally on my computer using <a href="https://ollama.com/">Ollama</a>. I do this more to get a feel for them than for current utility. Most of my recent experimentation has been with <a href="https://ollama.com/library/llama3">Llama 3</a>. I use these models via the command line or the <a href="https://github.com/logancyang/obsidian-copilot">Copilot plugin</a> in <a href="https://obsidian.md/">Obsidian</a>.</p>
<p>I also subscribe to <a href="https://elevenlabs.io/">ElevenLabs</a> for its voice-generation capabilities. More on that below.</p>
<p>I’ve experimented with other tools, but they haven’t yet formed a large part of my workflow. I don’t use Bing much, except for images if ChatGPT isn’t giving me what I want. I like that it gives four images for every prompt. I experimented with Google Gemini but haven’t found a reason for it to supplant the Claude plus ChatGPT combination. I revisit it every month or two to see whether I should add it to the mix.</p>
</section>
<section id="thinking" class="level2">
<h2 class="anchored" data-anchor-id="thinking">Thinking</h2>
<ul>
<li>Efficiency gain: uncertain</li>
</ul>
<p>I am increasingly using Claude and ChatGPT as interactive <a href="https://en.wikipedia.org/wiki/Rubber_duck_debugging">rubber ducks</a>. When thinking through something new, I’ll often state my thoughts and ask for comments. I’ll often ask them to explain a concept to me, then I will ask follow-up questions. Sometimes I’ll do this in ChatGPT with voice mode when I am walking. I know that I’m not getting 100% accurate information, but I wouldn’t talking to a friend either.</p>
<p>Similarly, after reading an article and forming my own views on its message, strengths and weaknesses, I’ll ask Claude or ChatGPT their views. I find this can be hit and miss, but on net worth doing. Sometimes the description is spot on, and the critiques hit points I haven’t thought of.</p>
<p>Finally, if I have a technical question, I’ll ask before googling. It’s faster and, I would say, more accurate than the top Google hits.</p>
</section>
<section id="coding-and-data-analysis" class="level2">
<h2 class="anchored" data-anchor-id="coding-and-data-analysis">Coding and data analysis</h2>
<ul>
<li>Efficiency gain: 10x</li>
<li>Quality gain: 50%</li>
</ul>
<p>Despite spending a lot of time in R, I am a crap coder. As a result, my typical approach is to write a comment and let Copilot do the first cut of the code. I will then tweak the code until it is in shape. That tweaking isn’t manual tweaking either. If there is an error or problem that I can’t resolve, I’ll use Copilot Chat to get a solution. Chat will usually provide code solving the problem.</p>
<p>Copilot is also great in helping me understand someone else’s code. I’ll highlight sections and ask Copilot Chat to explain what it does. Often, I’ll paste poorly documented code into Claude or ChatGPT and ask it to write comments. Further, if the code looks overly complicated, a request to simplify often yields good results. (I’ve been asking ChatGPT to review some of my old code recently. I’m a bit embarrassed at how much more efficiently I could have written it.)</p>
<p>One large benefit has come from cross-language translation. Last year I wanted to reproduce the results in Berkeley Dietvorst’s <a href="https://doi.org/10.1037/xge0000033">Algorithm aversion: People erroneously avoid algorithms after seeing them err</a>. Data and the code for analysis were <a href="https://researchbox.org/379&amp;PEER_REVIEW_passcode=MOQTEQ">available on ResearchBox</a>. The problem was that the code was in Stata, and I have no desire to learn Stata.</p>
<p>I pasted the Stata code into ChatGPT and asked for a conversion to R. What I received was 90% of the way there. Initially, there was an error, but pasting the error into ChatGPT gave me the solution first shot. I then tweaked a couple of the variable manipulations and specified that some of the t-tests were paired t-tests. That was it. In less than 10 minutes I had code that reproduced exactly the results from Study 1. I’ve now done this translation dozens of times when examining and reproducing studies by others.</p>
<p>I’m increasingly asking ChatGPT and Claude to provide me with working programs. For example, I am building a website with an underlying database and model for predicting AFL games. (I wanted to experiment with how far I could go with these tools.) I obtained a web interface and underlying code from Claude to access the database. I used ChatGPT for the first version of the predictive model. I’m now playing with the details, but the core is there. I wouldn’t even attempt it without these tools.</p>
<section id="data-exploration" class="level3">
<h3 class="anchored" data-anchor-id="data-exploration">Data exploration</h3>
<ul>
<li>Efficiency gain: 2x</li>
</ul>
<p>Any time I am about to work with new data, confidentiality permitting, I’ll give the data to ChatGPT and ask about it. I’ll start generally: “tell me about this file”. Then I’ll work down to the details and ask for basic visualisations and analysis. Finally, I’ll export the Python code (or ask for an R version of the code).</p>
<p>Ever since the <a href="https://datacolada.org/98">Dan Ariely car insurance data fraud</a>, which is obvious from a simple plot, I’ve made it a habit of looking at the data before jumping into analysis (which I didn’t do as often as I should have in the past). It’s surprising how often I find that something is not quite right or as expected. Having ChatGPT on hand makes this first step quick and easy.</p>
</section>
<section id="extracting-pdf-data" class="level3">
<h3 class="anchored" data-anchor-id="extracting-pdf-data">Extracting pdf data</h3>
<ul>
<li>Efficiency gain: 10x</li>
</ul>
<p>This is a small one in that I don’t need to do that often, but it’s a massive time saver. If there is a large table in a PDF, I ask ChatGPT to output it as a CSV. Recently, I had data spread across half a dozen PDFs in poorly formatted tables. I used ChatGPT to combine and arrange the data. I check the accuracy as I don’t fully trust ChatGPT, but the accuracy is typically great, saving me a lot of time.</p>
</section>
</section>
<section id="writing" class="level2">
<h2 class="anchored" data-anchor-id="writing">Writing</h2>
<ul>
<li>Efficiency gain: 20%</li>
<li>Quality gain: 10%</li>
</ul>
<p>When I first started using GitHub Copilot, I would have it on whenever I was writing. I would receive suggestions as I typed. Today, I generally turn it off when writing a first draft. The distraction in filtering suggestions was too costly, and I was worried about getting dragged in random directions.</p>
<p>However, I use Claude and ChatGPT a lot to improve my writing. When I’m having trouble getting a sentence or paragraph right, I’ll often hand it over and ask for 10 possible rewrites. Similarly, I will ask for simpler, shorter or more conversational text. I’ll rarely take a rewrite as provided, but it often gives me a word or turn of phrase that does the job.</p>
<section id="lecture-notes" class="level3">
<h3 class="anchored" data-anchor-id="lecture-notes">Lecture notes</h3>
<p>For more mechanical lecture notes, there are some clear gains. The notes for my undergraduate behavioural economics subject (which you can access <a href="https://be.jcx.au">here</a>) were produced with Copilot assistance.</p>
<p>Here are a few instances where Copilot has been useful.</p>
<p>Often the notes include a statement of a concept followed by a step-by-step example or illustration. The gain comes when you’re writing those steps.</p>
<p>For example, in a section about decision making under risk, I might write:</p>
<blockquote class="blockquote">
<p>Bill is a risk-averse agent with utility function {{< math >}}u(x)=\text{ln}(x){{< /math >}} and wealth of $100. He is offered a 50:50 bet to win $100, lose $50.</p>
<p>Will Bill accept the bet?</p>
</blockquote>
<p>If I write the first couple of words of the answer “First, we calculate…”, Copilot is away.</p>
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
<p>I might beef this up with a better explanation, or paste the question into ChatGPT directly, where I tend to get more detailed answers. Copilot has done OK with the maths here - the logs are correct!</p>
<p>Copilot is also great when I’m doing repetitive tasks such as describing the elements of an equation or diagram. Start describing the first element and it might give you the rest. And if you write a point followed by “Conversely, …”, Copilot is often on the money.</p>
<p>I also use Copilot with <a href="https://ggplot2.tidyverse.org">ggplot</a> to produce graphs for the notes. When I wanted to generate a chart showing a <a href="https://be.jcx.au/prospect-theory/probability-weighting">probability weighting function</a> from prospect theory, I created an R code block and typed a comment:</p>
<blockquote class="blockquote">
<p>#Plot of probability weighting function using ggplot2</p>
</blockquote>
<p>Here’s the result that ChatGPT produced with the diagram rendered below:</p>
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
<p><a href="using-generative-AI-as-academic-july-2024-edition_files/figure-html/unnamed-chunk-1-1.png" class="lightbox" data-gallery="quarto-lightbox-gallery-1"><img src="using-generative-AI-as-academic-july-2024-edition_files/figure-html/unnamed-chunk-1-1.png" class="img-fluid figure-img" width="672"></a></p>
</figure>
</div>
</div>
</div>
<p>Exactly what I wanted. When I implemented this in the notes, I only tweaked the style and added a 45-degree line.</p>
<p>Copilot’s offering uses Prelec’s <span class="citation" data-cites="prelec1998">(<a href="#ref-prelec1998" role="doc-biblioref">1998</a>)</span> probability weighting function. Whether it picked that up from earlier text in my notes or just gave the most common function for probability weighting, I don’t know, but it’s what I would have used if doing it manually. However, in writing this post I wasn’t able to replicate what I did when writing the lecture notes. I got better results in the lecture notes themselves. A few paragraphs about probability weighting before I ask for the code generated better results than asking for the chart straight up.</p>
<p>Copilot didn’t offer this full chunk of code at once. Each comment was offered, then the piece of code after it, one after the other. But the only work I did was writing the first comment and pressing tab several times as each succeeding comment or chunk of code was suggested. (Copilot has certainly increased the level of comments in my code too.)</p>
</section>
<section id="writing-organisational-fluff" class="level3">
<h3 class="anchored" data-anchor-id="writing-organisational-fluff">Writing organisational fluff</h3>
<p>Work in any decent-sized modern organisation and you will have to write some level of fluff to satisfy the higher-ups, clients, government requirements and the like. I am hopeless at those tasks. I have to invest heavily to make fluff sound decent.</p>
<p>My approach to these exercises depends on the degree of pointlessness.</p>
<p>If the task relates to a process that will have zero impact on what anyone will do, I simply give the task to ChatGPT, let it do the first cut and then tweak as required. One or two sentences of guidance often get you 80% of the way there.</p>
<p>If I think there is a positive benefit to the task, or it’s for public consumption, I’ll be more proactive first up. I will write a rough draft, not caring much about the writing but making sure the concepts I want to include are there. It might be in dot points. Then I’ll ask ChatGPT for a version that is “clearer”, “simpler” or “better written” or “for a ten-year-old”.</p>
<p>Recently, I needed to describe how a program met a set of quality criteria. I uploaded some documents describing the program and a pdf that contained the criteria (in a table). I then asked Claude to provide me with short paragraphs describing how the program met the criteria. Some mild tweaking and I was there.</p>
</section>
<section id="generating-quiz-questions" class="level3">
<h3 class="anchored" data-anchor-id="generating-quiz-questions">Generating quiz questions</h3>
<ul>
<li>Efficiency gain: 3x</li>
</ul>
<p>One of the best ways to learn is to be tested. As a result, I offer students in my undergraduate subject a series of practice quizzes that they can work through.</p>
<p>It’s hard work to generate questions in bulk, and I struggle to generate plausible-sounding but incorrect answers to multiple-choice questions. I now ask ChatGPT to generate them. I upload my subject notes and ask that they be used as the basis of the questions. In the prompts, I vary in the specificity of the questions. “Give me 20 multiple choice questions testing the concept of loss aversion.” “Give me 20 multiple choice questions testing prospect theory.” Out of each batch, only a few will be suitable. But by tweaking my instruction by, say, describing the level of the students (undergraduate) or more explicitly defining the concept, it doesn’t take long to get 10 or so good questions.</p>
<p>I have also used ChatGPT to generate question ideas for assessable quizzes and exams. That exam is a closed-book AI-invigilated exam, so is less vulnerable to someone simply feeding the questions back to ChatGPT. One helpful approach was to upload some previous exams plus my subject notes and ask for new exam questions at the same level of difficulty or on the same concepts.</p>
</section>
</section>
<section id="ai-voiced-lectures" class="level2">
<h2 class="anchored" data-anchor-id="ai-voiced-lectures">AI-voiced lectures</h2>
<ul>
<li>Efficiency gain: 10%</li>
<li>Quality gain: 50%</li>
</ul>
<p>Last year I decided to base my undergraduate behavioural economics subject around <a href="https://www.youtube.com/@jasonacollins">short pre-recorded videos</a>, interactive online seminars and tutorials. To produce the videos I wrote scripts, which also form the <a href="https://be.jcx.au">subject notes</a>. I read the notes accompanied by slides.</p>
<p>There are three pain points in this exercise. First, I speak too fast (even when I think I’m speaking slow) and I enunciate many words poorly. Second, recording takes a lot of time. I rarely get a two to five-minute video in a single take that I’m happy with. Third, if I want to tweak the recording, I need to either re-record solid chunks of text or fiddle around with video edits.</p>
<p>So, why not get an artificial voice to do the speaking? When I wrote my last post, AI-voiced lectures were the future. It’s now a core part of my subject delivery.</p>
<p>I experimented with <a href="https://murf.ai">Murf.ai</a>, <a href="https://speechify.com">Speechify</a>, <a href="https://play.ht/">play.ht</a> and <a href="https://beta.elevenlabs.io">ElevenLabs</a>. Initially I used Murf.ai to make some videos, as it allowed me to pair slides and text easily. I could also integrate with Google Slides. However, the voices sound a bit robotic, so I currently use ElevenLabs, even though all I get is an audio file. ElevenLabs has fantastic voices. Even a hint of AI voicing gets a negative reaction from students, so voice quality needs to be my primary criterion. If the Murf.ai voices improve and Eleven doesn’t develop video integration, I may shift back.</p>
<p>The production process is easy. I paste the text into an ElevenLabs project chapter and render the voice. Typically, the pacing won’t be quite right, so I’ll add some commas and dashes to create some pauses. I then export the voice file and combine it with images in Final Cut Pro. I can normally create a five to 10 minute video from text and slides in less than an hour.</p>
<p>The fantastic part is that if I want to update a section or change a sentence, I update the script in ElevenLabs, re-render the relevant sentences, load a new voice file into the Final Cut Pro project and tweak the slide timings (if the voice edits require it). It’s fast, simple and gives me a consistently high-quality video.</p>
<p>ElevenLabs can “clone” your voice. I tried a quick clone on play.ht, but it gave me an American accent. On ElevenLabs, you can get a professional clone of a voice by uploading three or more hours of audio. I did that, and it sounds just like me, even with the Australian accent. Unfortunately, it comes with my faults, particularly speaking too fast. ElevenLabs doesn’t have an option to slow down the speaking outside of putting a mountain of dashes through the text. It also reflects the quality of my home recording setup and sounds a bit echoey. So, for now, I’m using one of their off-the-shelf Australian voices.</p>
<p>Here are two samples of the above paragraph, an off-the-shelf Australian voice and my “cloned” voice.</p>
<audio controls="" src="img/ElevenLabs_2024-07-15T09_03_10_Charlie_pre_s50_sb75_m1.mp3">
</audio>
<audio controls="" src="img/ElevenLabs_JC.mp3">
</audio>
<p>I’ve also started looking at options to create an AI avatar based on videos or photos of me for some parts of the videos. I’m leaving that one for the moment but can see myself revisiting it in the next year.</p>
</section>
<section id="accessing-github-copilot" class="level2">
<h2 class="anchored" data-anchor-id="accessing-github-copilot">Accessing GitHub Copilot</h2>
<p>The below gives the basic steps to access GitHub Copilot.</p>
<p>If you are an academic, you can sign up for (free) academic access to Copilot at <a href="https://education.github.com/discount_requests/application">this link</a>. If you’re not an academic or student, sign up for a free trial as described <a href="https://docs.github.com/en/billing/managing-billing-for-github-copilot/managing-your-github-copilot-subscription-for-your-personal-account">here</a>. You’ll need a GitHub account to do this. The $10 a month is worth it.</p>
<p>Visual Studio Code is available <a href="https://code.visualstudio.com">here</a>. (I use the Mac version.) Download and install.</p>
<p>Install the GitHub Copilot extension into Visual Studio Code. Instructions on installing the extension are <a href="https://docs.github.com/en/copilot/quickstart#installing-the-github-copilot-extension-for-visual-studio-code">here</a>. On installation you’ll be prompted to log in to GitHub to gain access to authorise Copilot.</p>
<p>Once you have done that, using Copilot is easy. You simply type. As you type, you will be given suggestions.</p>
<p>The setup in RStudio is even easier. Download RStudio from <a href="https://posit.co/download/rstudio-desktop/">here</a>. Under Tools/Global Options is a Copilot menu item. Enable Copilot there. You will be asked to enter your GitHub login details to get it running.</p>
<p>I write in markdown (and at the moment, a flavour of markdown called <a href="https://quarto.org">Quarto</a>). It allows me to include {{< math >}}\LaTeX{{< /math >}} maths and R computations within any document (as I have in this post). If you’re an academic stuck in the {{< math >}}\LaTeX{{< /math >}} ecosystem, you can also write in Visual Studio Code wholly in {{< math >}}\LaTeX{{< /math >}}. You can also just get Copilot in Word. I’m looking forward to my university moving beyond the experimental stage and giving us access. (I took a one-month free trial of Microsoft Copilot on the home computer, but didn’t find the time to give it a proper go.)</p>



</section>

<div id="quarto-appendix" class="default"><section class="quarto-appendix-contents" role="doc-bibliography" id="quarto-bibliography"><h2 class="anchored quarto-appendix-heading">References</h2><div id="refs" class="references csl-bib-body hanging-indent" data-entry-spacing="0" data-line-spacing="2" role="list">
<div id="ref-prelec1998" class="csl-entry" role="listitem">
Prelec, D. (1998). The probability weighting function. <em>Econometrica</em>, <em>66</em>(3), 497–527. <a href="https://doi.org/10.2307/2998573">https://doi.org/10.2307/2998573</a>
</div>
</div></section></div>
{{< /html >}}
