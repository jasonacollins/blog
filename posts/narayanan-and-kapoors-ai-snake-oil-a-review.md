---
title: "Narayanan and Kapoor's AI Snake Oil: a review"
author: "Jason Collins"
date: 2026-06-16 09:08:42+10:00
draft: true
toc: false
images: [""]
---

For those who want a *credible* critique of AI hype or the idea that superintelligent AI is an existential threat (and who have realised that Gary Marcus doesn't fit that bill), Arvind Narayan and Sayash Kapoor are not a bad place to turn. They appear thoughtful, engage with those they disagree with (such as the [AI 2027](https://asteriskmag.substack.com/p/common-ground-between-ai-2027-and) crew) and do a great job getting into the weeds.

Written after a [presentation](https://www.cs.princeton.edu/~arvindn/talks/MIT-STS-AI-snakeoil.pdf)[^1] went viral, [AI Snake Oil: What Artificial Intelligence Can Do, What It Can't, and How to Tell the Difference](https://www.normaltech.ai/p/starting-reading-the-ai-snake-oil) takes the potential of AI seriously while not waiting for singularity. Although some arguments are shallow, the book is worth reading. Their critique of business practice is excellent. However, their less-developed arguments that AI does not present an existential threat (albeit developed a lot more since the book was published) are not as strong.

[^1]: The original 2019 presentation was not recorded, but it led to many later [re-runs](https://www.cs.princeton.edu/news/how-recognize-ai-snake-oil).

Narayan and Kapoor start the book by critiquing the umbrella term "artificial intelligence". This is a useful beginning. In many business contexts, products sold as AI can have anything from simple decision rules or linear regression through to random forests or vector support machines to large language models under the hood. In other circles, artificial intelligence and generative AI are synonyms, despite the huge range of approaches to AI that don't fall under the generative AI banner. (The 202X edition of Russel and Norvig's *Artificial Intelligence: A Modern Approach* sitting on my dinner table has XX of it's XXXX pages dedicated to language and XX to generative AI in particular).

To cut through this nomenclature issue, Narayan and Kapoor draw a line between "predictive" AI and generative "AI". Predictive AI is the use of AI to predict outcomes, particularly human behaviour, to support decision making (think predicting whether someone will buy a product or breach their bail conditions). Generative AI is the generation of content we have become increasingly familiar with via large language models such as ChatGPT or image generation tools like Midjourney or Dall-E.[^2]

[^2] This boundary between predictive and generative AI is often blurred. There is no shortage of people giving generative AI predictive tasks (e.g. [ForecastBench](https://www.forecastbench.org/)).

While I would be tempted to slice predictive AI even finer - there's a big gap between an automated decision rule and a random forest algorithm - for the purposes of a book, their distinction is useful. What is interesting, however, it their views on these two approaches. Their critique of predictive AI is essentially that it isn't any good. In contrast, they are much more positive about generative AI.

A good illustration of their predictive AI critique concerns research by Matt Salganik (XXX's regular research partner). Salganik and friends (REF) ran a competition in which they provided 160 researchers with data from the xxxx.

The best model The say that "the best models were only slightly better than a coin flip", but that undersells the results.

There's a glass half-empty view of this - and that is certainly the one Narayan and Kapoor take. The third chapter is titled "Why Can’t AI Predict the Future?". But there's also a half-full perspective.

An R<sup>2</sup> of 0.2 doesn't sound very good, and if we're trying to predict an outcome for a particular individual, I might agree with that view. But let's think about it in a different way. An R<sup>2</sup> of 0.2 means where is a correlation of around 0.45 between the predicted and actual outcomes. If we were to take the top 10% of the group, that top 10% would be around 0.8 standard deviations above the average. If this would IQ, that top 10% would have an IQ around 110. 

This is the type of result we see again and again - and in fact, it's a staple of people complaining about - 

What's the R2 of income for ??? in this chart? Around 0.15. Yet, you can see the pattern. 

Here are a few more practical examples. Criminal example. The R2 might be limited, but using that data well we could likely prevent a lot of crime. 

Occasionally Narayan and Kapoor hint at the benefits of algorithms, such as noting the predictive power of age and prior offences as a predictor of future offences. But these observations are generally framed as a critique of more complicated approaches, rather than addressing the question of whether using an automated decision tool might be beneficial. Why not develop a simple decision rule based on prior offences and age? Transparent. Likely fairer than the biased outcomes from a judge or parole officer.

The Compass case study provides a good illustration. They note the report by XXXX which found that xxxxx. They didn't discuss the subsequent discussion showing that this is a trade-off you have to accept if xxxx. There is fair debate to be had about which trade-off we should accept, but it exists. But beyond that, they question its accuracy. 

The sharpest point of critique for Compass relates to the lack of transparency and the likelihood that we could get the same performance with a simple, transparent (and free!) decision rule. 

An automated decision tool allows us to have this discussion and, once we have decided on the trade-off we prefer, to actually implement it. With human decision makers, that trade-off will always be there, but we don't get to have the discussion as society about what we prefer. Further, the human decision makers introduce all the biases we accuse AI of having.

Surprisingly, they are much more positive about generative AI, albeit recognising various risks. They see it's role in xxxx

Their dismissal of AI as an existential threat is weak. They rarely engage with the strongest arguments - although since the publication of this book, they have engaged in more depth through their [AI as a normal technology] blog and other approaches. For example, 

What they believe feasible seems inconsistent. When discussing whether it is possible to prevent proliferation of super-intelligent AI they believe that regulation would require draconian surveillance and unprecedented international cooperation. But when discussing the threat of bioterrorism they're happy to say it's easy: just regulate the lab components needed to engineer viruses. 

There are parts of the book that grate. In noting that their views differ from AI experts, they present a range of "biases" the . This sort of junk gives me the shits - another possibility is that Narayanan and Kapoor are wrong - on top of ignoring that their whose whole schtick is debunking the threat from AI, so obviously they're going to present this side of the argument. Cut with the ad hominem.