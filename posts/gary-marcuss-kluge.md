---
title: "Gary Marcus's Kluge and the benchmark of perfection"
author: "Jason Collins"
date: 2026-05-21 09:00:00+10:00
draft: false
toc: false
image: "img/kluge.png"
bibliography: references.bib
---

As Gary Marcus so often appears in debates about the future of artificial intelligence, I decided to grab his 2008 book [Kluge: The Haphazard Construction of the Human Mind](https://en.wikipedia.org/wiki/Kluge_(book)) from my overgrown reading pile. I'm glad I did, though not because it taught me much about the human mind. It helped me understand Marcus's critique of generative AI.

Marcus's argument is that the human mind is a 'kluge', a clumsy or inelegant yet surprisingly effective solution to a problem. Like our backward-installed retina and spine suited to quadrupedal walking, the human mind is - while impressive - flawed. (Random aside: like me, Marcus is a big user of em-dashes.)

The accumulation of kluges comes from the path dependent nature of evolution. There is no grand designer constructing an optimal human (or human mind) from scratch. Rather, humans evolved through a series of incremental tweaks, each built upon the last. If we think of evolution as climbing a mountain toward higher fitness, each change that spreads will take us closer to the peak. However, that peak may not be the highest. Other higher peaks may not be attainable as we would first be required to walk through a valley of lower fitness.

On one level, this is uncontroversial. Few would disagree that evolution is a path dependent process or that we have mental structures that would not be "designed".[^1] The debate emerges around the specifics. An apparent flaw in the mind could be at least four different things. It could be a kluge, a clumsy workaround resulting from evolutionary path dependence. It could be an adaptation that, while appearing off, solves a recurring problem. It could be a design trade-off, where improving one feature worsens another. Or it could be evolutionary mismatch, whereby a once useful strategy backfires in a modern environment. 

[^1]: The exception to that is creationists, who Marcus targets in the final chapter. No "intelligent designer" would have put us together that way. This does give a slightly dated feel to the book as those creationist-atheist debates of the late 'aughts' have largely withered away.

Marcus moves too quickly from “this produces errors” to “this is a kluge”. Much evolutionary psychology literature has a different instinct, taking the adaptationist approach. Seek to understand the purpose of our apparent foibles. Why might men overestimate the sexual intentions of potential mates? One possibility is asymmetric errors. The genes of the man who misses true opportunities are no longer with us. On that account, this behaviour reflects adaptation. Marcus, however, sees a kluge.

I have sympathy for Marcus's critique. However, through the book, Marcus rarely convinced me on the specifics. He is quick to jump from seeing an error to identifying a kluge, straw-manning the strongest adaptationist arguments, sidestepping questions about trade-offs, and benchmarking the mind against a standard of perfection - one that I doubt even computers can meet. We are left wondering whether he has genuinely identified a kluge, an adaptation, a design trade-off or a mismatch.

Take his discussion of whether mental illness could have an evolutionary advantage. He refers to:

> the somewhat dubious suggestion that schizophrenia might have been selected for by natural selection because of a purported benefit that visions conveyed to tribal shamans, but there are many others.
>
> ... If you're like me, you won't find these examples particularly compelling. Were schizophrenics really more likely than other people to become shamans?

A fair question, but that's it. We are barely exposed to the rich literature on the evolutionary foundations of mental illness. (Which in fairness to Marcus has become much richer since he wrote his book. Read Marco del Giudice's [Evolutionary Psychopathology](https://marcodg.net/evolutionary-psychopathology/) as an illustration.) Instead we get thought experiments about how people could motivate themselves without depression, anxiety or desire for status by simple rational thought. Maybe, but thought experiments fall well short of a solid case.

Marcus also doesn't establish that the problems are due to the path dependence of evolution. Most chapters end with a statement about how a more recent deliberative system is bolted onto a reflexive ancient system (the System 1 - System 2 dichotomy made famous by Kahneman), rather than a description of the evolutionary path that led to this outcome. We get a few mentions of older structures such as the cerebellum, amygdala or basal ganglia, or newer regions such as the pre-frontal cortex, but rarely any evidence of how these cause the behaviour we see.

His chapter on choice illustrates. The chapter contains a parade of classic illustrations of our irrationality. We get the Asian disease problem, the Allais paradox, the use of Christmas clubs to save (as a kluge against our lack of self control) and the trolley problem.[^2] I agree that there is something not quite right with some of these decisions. There are interesting debates about which of these are systemic errors and which represent the outcomes of a decision strategy that is optimal given the sparse and noisy data available for the decision. That is, what decision strategies are "ecologically rational"? But Marcus doesn't go there. Error is simply taken to mean kluge. Similarly, there is no discussion of evolutionary mismatch, whereby once-optimal strategies backfire in a new environment.

[^2]: From the perspective of 2026 (or even 2016), the cited psychology research is weak. Many of the experiments have not replicated. These include:

    -   Priming people with words relating to the elderly [does not make them walk slower](https://doi.org/10.1371/journal.pone.0029081) (unless the person doing the timing was in on the experiment...).
    -   Holding a pen between your teeth to force a smile [does not make a cartoon funnier](https://doi.org/10.1177/1745691616674458).
    -   Priming people with terms relating to professor - as opposed to soccer hooligan - [does not make them better at trivia](https://doi.org/10.1177/1745691618755704).

    Even those studies without the accompanying failed replication should be treated similarly. They come from an era where our [default should be disbelief](/posts/a-default-of-disbelief.md).

    That said, if Marcus rewrote the book today, he could find enough experiments to back his point. It would have a very different feel however, with much of the novelty that made those experiments such great fodder of popular science books gone.

Underlying much of his critique is Marcus's definition of optimality, which largely consists of what he believes he could build with a computer. For instance, the benchmark against which our fallible memories are compared is "postal-code memory", where a computer assigns an address to each memory. When it needs access to that memory, it simply goes there. He states that "Having postal-code memory would have been terrifically useful for us, but evolution never discovered the right part of the mountain range."

This benchmark of perfection, however, does not acknowledge any trade-offs. How much storage space do we have? What is the cost of that space? If we had perfect memory, how long would it take to search across it and retrieve what we need?

Those trade-offs are also apparent in the world of deep learning. A deep learning algorithm that simply memorises is useless. It overfits the data. You want generalisation. You want it to [grok](https://pair.withgoogle.com/explorables/grokking/). Is this also the case for humans? While Marcus's book well predates today's algorithms and LLMs, there was plenty of research relevant to this point even then.

For example, @elman1993 sought to train a neural network to understand grammatical relationships. The network with extensive memory failed to pick up core concepts. Elman then restricted the memory of the network such that it forgot everything after a few words, possibly mimicking the memory of young children when they first learned to speak. This constrained network was able to learn basic rules. As its memory was then increased, it was ultimately able to learn a fuller set of relationships than the unconstrained model.

Discussions of research such as this would have made for compelling reading. Is limited memory a kluge or a necessary element of learning? Unfortunately, we're not exposed to that debate.

After reading Marcus's arguments and seeing the benchmark of perfection permeating his critique of the human mind, his views on generative AI make more sense to me. He sees perfection as achievable with computers. Perfect postal-code memory. Searching all relevant data. Deterministic outputs. Computer-based parsers that slot each noun and verb into its proper place. With that expectation, it is no wonder that he sees the hallucinations produced by large language models as a failure. We could have perfection.

But could we? Is some level of hallucination or imperfect memory an inevitable consequence of the learning process? Are the most robust heuristics imperfect in some environments? Unfortunately, this question is sidestepped.

In the closing chapter Marcus offers us 13 ways to be better thinkers. Chapters like this typically feel like a request from the publisher to end on a positive, practical note, and this is no exception. Consider alternative hypotheses. Compare costs and benefits. Sound advice, but you don't need to think of the mind as a kluge to come up with any of the items on this list.

A more useful lesson is not that the mind is full of kluges. Rather, apparent defects need to be judged against realistic alternatives. This applies to both evolved minds and artificial ones.