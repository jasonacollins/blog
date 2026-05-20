---
title: "Gary Marcus's Kluge: the benchmark for Marcus is perfection"
author: "Jason Collins"
date: 2026-05-20 09:00:00+10:00
draft: true
toc: false
image: "img/kluge.png"
bibliography: references.bib
---

As Gary Marcus so often appears in debates about the future of artificial intelligence, I decided to grab his 2008 book [Kluge: The Haphazard Construction of the Human Mind](https://en.wikipedia.org/wiki/Kluge_(book)) from my overgrown reading pile. I'm glad I did, as it gave context to his critique of generative AI. It didn't, however, teach me much about the human mind.

Marcus's argument is that the human mind is a 'kluge', a clumsy or inelegant yet surprisingly effective solution to a problem. Like our backward-installed retina and spine suited to quadrupedal walking, the human mind is - while impressive - flawed. (Random aside: like me, Marcus is a big user of em-dashes.)

The accumulation of kluges comes from the path dependent nature of evolution. There is no grand designer constructing an optimal human (or human mind) from scratch. Rather, humans evolved through a series of incremental tweaks, each built upon the last. If we think of evolution as climbing a mountain toward higher fitness, each change that spreads will take us closer to the peak. However, that peak may not be the highest, with other higher peaks not attainable if we only walk up the slope we are on.

On one level, this is uncontroversial. Few would disagree that evolution is a path dependent process or that we have mental structures that would not be "designed".[^1] The debate emerges around the specifics, where Marcus critiques adaptationist streams of evolutionary thinking. Much evolutionary psychology literature has a starting point of seeking to understand the purpose of our apparent foibles rather than labelling them as kluges. Why might men overestimate the sexual intentions of potential mates? Asymmetric errors. The genes of the man who misses true opportunities is no longer with us. This behaviour reflects adaptation. Marcus, however sees a kluge.

[^1]: The exception to that are creationists, who Marcus targets in the final chapter. No "intelligent designer" would have put us together that way. This does give a slightly dated feel to the book as those creationist-atheist debates of the late 'aughts' have largely withered away.

I have sympathy for both the adaptationist approach - don't immediately assume error - and Marcus's critique. Either way, we should build the evidentiary base underlying our assessment. However, through the book, Marcus rarely convinced me on the specifics. He straw-mans the strongest adaptationist arguments, sidesteps questions about trade-offs, and repeatedly benchmarks the mind against a standard of perfection - one that I doubt even computers can meet. We are left wondering whether he has genuinely identified a kluge, an adaptation, or a design trade-off.

Take his discussion of whether mental illness could have an evolutionary advantage. He refers to:

> the somewhat dubious suggestion that schizophrenia might have been selected for by natural selection because of a purported benefit that visions conveyed to tribal shamans, but there are many others.
>
> ... If you're like me, you won't find these examples particularly compelling. Were schizophrenics really more likely than other people to become shamans?

A fair question, but that's it. No discussion of the rich literature on the evolutionary foundations to mental illness. (Which in fairness to Marcus has become much richer since he wrote his book. Read Marco del Giudice's [Evolutionary Psychopathology](https://marcodg.net/evolutionary-psychopathology/) as an illustration.) Instead we get thought experiments about how people could motivate themselves without depression, anxiety or desire for status by simple rational thought. Maybe, but thought experiments fall well short of a solid case.

Marcus also doesn't establish that the problems are a 'kluge'. Most chapters end with a hand-wavy statement about how a more recent deliberative system is bolted onto a reflexive ancient system (the System 1 - System 2 dichotomy made famous by Kahneman), rather than a description of the evolutionary path that led to this outcome. We get a few mentions of the old cerebellum, amygdala or basal ganglia or the newer pre-frontal cortex, but rarely any evidence of how these cause the behaviour we see.

His chapter on choice illustrates. The chapter contains a parade of classic illustrations of our irrationality. We get the Asian disease problem, the Allais paradox, the use of Christmas clubs to save (as a kluge against our lack of self control) and the trolley problem.[^2] I agree that there is something not quite right with some of these decisions. There are interesting debates about which of these are systemic errors and which represent the outcomes of a decision strategy that is optimal given the sparse and noisy data available for the decision. That is, what decision strategies are "ecologically rational"? But Marcus doesn't go there. Error is simply taken to mean kluge. Similarly, there is no discussion of evolutionary mismatch, whereby once optimal strategies have backfire in a new environment (which I would distinguish from a kluge).

[^2]: From the perspective of 2026 (or even 2016), the cited psychology research is weak. Many of the experiments have not replicated. These include:

    -   Priming people with words relating to the elderly [does not make them walk slower](https://doi.org/10.1371/journal.pone.0029081) (unless the person doing the timing was in on the experiment...).
    -   Holding a pen between your teeth to force a smile [does not make a cartoon funnier](https://doi.org/10.1177/1745691616674458).
    -   Priming people with terms relating to professor - as opposed to soccer hooligan - [does not make them better at trivia](https://doi.org/10.1177/1745691618755704).

    Even those studies without the accompanying failed replication should be treated similarly. They come from an era where our [default should be disbelief](/posts/a-default-of-disbelief).

    That said, if Marcus rewrote the book today, he could find enough experiments to back his point. It would have a very different feel however, with much of the novelty that made those experiments such great fodder of popular science books gone.

Underlying much of his critique is Marcus's definition of optimality, which largely consists of what he believes he could build with a computer. For instance, the benchmark against which our fallible memories are compared is "postal-code memory", where a computer assigns an address to each memory. When it needs to access to that memory, it simply goes there. He states that "Having postal-code memory would have been terrifically useful for us, but evolution never discovered the right part of the mountain range."

This benchmark of perfection, however, does not acknowledge any trade-offs. How much storage space do we have? What is the cost of that space? If we had perfect memory, how long would it take to search across it and retrieve what we need?

Those trade-offs are also apparent in the world of deep learning. A deep learning algorithm that simply memorises is useless. It overfits the data. You want generalisation. You want it to [grok](https://pair.withgoogle.com/explorables/grokking/). Is this also the case for humans? While Marcus's book well predates today's algorithms and LLMs, there was plenty of research relevant to this point even then.

For example, @elman1993 sought to train a neural network to understand grammatical relationships. The network with extensive memory failed to pick up core concepts. Elman then restricted the memory of the network such that it forgot everything after a few words, possibly mimicking the memory of young children when they first learned to speak. This constrained network was able to learn basic rules. As its memory was then increased, it was ultimately able to learn a fuller set of relationships than the unconstrained model.

Discussions of research such as this would have made for compelling reading. Is limited memory a kluge or a necessary element of learning? Unfortunately, we're not exposed to that debate.

After reading Marcus's arguments and seeing the benchmark of perfection permeating his critique of the human mind, his views on generative AI makes more sense to me. He sees perfection as achievable with computers. Perfect post-code memory. Searching all relevant data. Deterministic outputs. Computer-based parsers that slot each noun and verb into its proper place. With that expectation, it is no wonder that he sees the hallucinations by large language models as a failure. We could have perfection.

But could we? Is some level of hallucination or imperfect memory an inevitable consequence of the learning process? Are the most robust heuristics imperfect in some environments? Unfortunately, this question is sidestepped.

In the closing chapter Marcus offers us 13 ways to be better thinkers. Chapters like this typically feel like a request from the publisher to end on a positive, practical note, and this is no exception. Consider alternative hypotheses. Compare costs and benefits. Sound advice, but you don't need to think of the mind as a kluge to come up any of the items on this list. When the recommendations don't need the book that comes before them, have you learnt anything useful?