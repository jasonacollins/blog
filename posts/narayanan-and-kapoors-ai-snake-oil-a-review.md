---
title: "Narayanan and Kapoor's AI Snake Oil: a review"
author: "Jason Collins"
date: 2026-10-16 09:00:00+10:00
draft: false
toc: false
image: "img/ai-snake-oil.png"
bibliography: references.bib
---

For those who want a credible critique of AI hype or the idea that superintelligent AI is an existential threat (and who have realised that Gary Marcus doesn't fit that bill), Arvind Narayanan and Sayash Kapoor are not a bad place to turn. They appear thoughtful, engage with those they disagree with (such as the [AI 2027](https://asteriskmag.substack.com/p/common-ground-between-ai-2027-and) crew) and do a great job getting into the weeds.

Written after a [presentation](https://www.cs.princeton.edu/~arvindn/talks/MIT-STS-AI-snakeoil.pdf)[^1] went viral, Narayanan and Kapoor's [AI Snake Oil: What Artificial Intelligence Can Do, What It Can't, and How to Tell the Difference](https://www.normaltech.ai/p/starting-reading-the-ai-snake-oil) takes the potential of AI seriously while not waiting for singularity. Although some arguments are shallow, the book is worth reading. Their critique of business practice is excellent. However, their less-developed arguments that AI does not present an existential threat (albeit developed a lot more since the book was published) are not as strong.

[^1]: The original 2019 presentation was not recorded, but it led to many later [re-runs](https://www.cs.princeton.edu/news/how-recognize-ai-snake-oil).

## What is AI?

Narayanan and Kapoor start the book by critiquing the umbrella term "artificial intelligence". This is a useful beginning. In many business contexts, products sold as AI can involve anything from simple decision rules or linear regression to random forests or support vector machines to large language models. In other circles, artificial intelligence and generative AI are synonyms, despite the huge range of approaches to AI that don't fall under the generative AI banner.[^aifn]

[^aifn]: The 2022 edition of Russell and Norvig's *Artificial Intelligence: A Modern Approach* sitting on my dinner table has 58 of its 1166 pages dedicated to language and 10 pages to the transformer architecture that underlies modern LLMs.

To cut through this nomenclature issue, Narayanan and Kapoor draw a line between "predictive AI" and "generative AI". Predictive AI is the use of AI to predict outcomes, particularly human behaviour, to support decision making (think predicting whether someone will buy a product or breach their bail conditions). Generative AI is the generation of content we have become increasingly familiar with via large language models such as ChatGPT or image generation tools like Midjourney or DALL-E.[^2]

[^2]: This boundary between predictive and generative AI is often blurred. There is no shortage of people giving generative AI predictive tasks (e.g. [ForecastBench](https://www.forecastbench.org/)).

While I would be tempted to slice predictive AI even finer - there's a big gap between an automated decision rule and a random forest algorithm - for the purposes of a book, their distinction is useful. What is interesting, however, are their views on these two approaches. Their critique of predictive AI is essentially that it isn't any good. In contrast, they are much more positive about generative AI.

## Predictive AI

A good illustration of their predictive AI critique concerns a competition led by Matt Salganik (Narayanan's regular research partner). Salganik and friends [-@salganik2020] provided 160 teams with data from the [Fragile Families and Child Wellbeing Study](https://en.wikipedia.org/wiki/Future_of_Families_and_Child_Wellbeing_Study) and asked them to predict six life outcomes, such as the child's grade point average, household material hardship and primary caregiver participation in job training. The result is typically quoted - as it is by Narayanan and Kapoor - as a failure of prediction. The paper abstract states that "the best predictions were not very accurate and were only slightly better than those from a simple benchmark model". Narayanan and Kapoor state "the best models were only slightly better than a coin flip". In more technical terms, the R<sup>2</sup> of the best predictions was around 0.2 for material hardship and GPA, and around 0.05 for the other four. That means that between 5% and 20% of the variation in those outcomes is "explained" by the models.

There's a glass half-empty view of prediction - and that is certainly the one Narayanan and Kapoor take. Their third chapter is titled "Why Can’t AI Predict the Future?". But there's also a half-full perspective.

Although an R<sup>2</sup> of 0.2 doesn't sound very good, under certain assumptions it means there is a correlation of around 0.45 between the predicted and actual outcomes. Suppose student marks average 65 out of 100, with a standard deviation of 15. Under certain assumptions, the 10% of students ranked highest by the model would average around 77. That’s much better than picking students at random.

Using a model with this level of accuracy in risk identification could also substantially boost your accuracy. If you wanted to pick the 10% of students who most need help, picking randomly would have you only identify 10% of them. Using the model would boost this to close to 30%. Still a lot of uncertainty, but better than pretending you haven't learned anything.

The four outcomes for which there was an R<sup>2</sup> of 0.05 provide less scope for benefit. However, three of those four are binary outcomes, which tends to result in low R<sup>2</sup> even when the model ranks relatively well.

Narayanan and Kapoor's discussion of the COMPAS case study provides another illustration of their view. COMPAS is a private algorithm, based on 137 questions answered by defendants, used to predict appearance in court or future arrest for a crime. They note the [report by ProPublica](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) which (among other things) found that when comparing pairs of people, one of whom would go on to commit a crime and the other would not, the algorithm only rated the person arrested in the future higher 64% of the time. As they say, that's "only slightly better than deciding a defendant's fate based on a coin flip". (Which is kind of ridiculous considering the algorithm ranks the one who reoffends higher 2 out of 3 times. I'm guessing those two aren't bettors.) They further mention that COMPAS does not outperform an algorithm using only age and prior offences as inputs or the judgement of non-experts (who probably have the sense to see that repeat offenders will continue to offend).

Narayanan and Kapoor also raise the headline ProPublica critique that the COMPAS algorithm had a higher false positive rate for black than white defendants, without noting that is an inevitable consequence of equal precision but disparate re-arrest rates. You have to trade off the various definitions of fairness![^3] (Here's [Robert VerBruggen making this point](https://www.theamericanconservative.com/does-pre-crime-have-a-race-problem/) and a more technical analysis by @kleinberg2016.)

[^3]: Narayanan knows this too. He's a coauthor of [Fairness and Machine Learning](https://fairmlbook.org/), which includes discussion of this trade-off.

I have sympathy for some points of their critique, such as the opaque proprietary nature of the algorithm and its complexity. As they note, there is no shortage of businesses flogging off overly complex and opaque predictive algorithms that will typically deliver a fraction of the benefits they promise. And desperate for an edge, there is no shortage of buyers of snake oil.

But during their critique they also hint at the benefits of predictive algorithms, such as noting the predictive power of age and prior offences as a predictor of future criminal offences. Unfortunately, they don't flip this hint into a recommendation. They don't push the alternative of a simple, transparent (and free!) decision rule — which they have noted exists — leaving a lot of benefit on the table. This new simple algorithm probably has a low R<sup>2</sup> if applied across the whole population, but is likely a good improvement on randomness or the human alternative.[^4]

[^4]: For example, see @kleinberg2018

Beyond accuracy, a simple automated decision tool allows us to have a discussion about what types of fairness trade-offs we are willing to make and, once we have decided on the trade-off we prefer, to actually implement it. With human decision makers, we'll get poor, biased decisions, and to the extent they exhibit any consistency in their decisions, that trade-off will always exist but be out of our control.

## Generative AI

Their other type of AI is generative AI, which Narayanan and Kapoor are surprisingly positive about (considering how it's being packaged by many snake oil salespeople). They state they are enthusiastic users in work and their personal lives. They see its benefits for programmers, knowledge workers and science. They appreciate how it can be accessed by everyone.

They identify risks such as misinformation, surveillance, misappropriation of creative labour and deepfakes, but these are engineering or policy problems for which they see solutions. They believe there has been major progress on problems of bias and offensive outputs, and hallucinations are going down. Exploitation of workers concerns them, but this can be addressed through labour regulation (pushed by collective action). While they believe regulation can be fast, they don't see the need for much new regulation, with most of what's needed being enforcement of existing regulations such as those against deceptive practices.

They even argue that the incoming wave of AI could also just be considered the next stage in a battle between labour and automation, with generative AI providing a new flash point. Big changes might be needed, but they are of the type we have debated many times before.

I don't have a hot take on this perspective on generative AI, except to say that, even ignoring the potential for existential risk, I'm not sure they're ready for just how disruptive it might be. The speed and breadth of coming changes may not look like anything we have seen before.

## Existential risk

Narayanan and Kapoor's technocratic and bureaucratic approach to generative AI is feasible because they don't see AI as an existential threat. Their chapter on why this is the case is the weakest part of the book. They rarely engage with the strongest arguments - although since the publication of this book, they have engaged in more depth through venues such as their [AI as a normal technology](https://www.normaltech.ai/) blog.

For example, they write the following in response to the [paperclip maximiser thought experiment](https://en.wikipedia.org/wiki/Instrumental_convergence#Paperclip_maximizer):

> The main problem with this argument is that it posits an agent that is unfathomably powerful yet lacks an iota of common sense to recognize the absurdity of the request, and will thus interpret it extremely literally, oblivious to the fact that it goes against human safety. This kind of mindless, literal interpretation is characteristic of traditional AI agents, which are programmed with knowledge of only a very narrow domain.

This common-sense objection is old. The literature is full of replies to it. Yet they give no indication of having read and engaged with it. Their response conflates knowing and caring. It doesn't ask whether "common sense" will really result in alignment with human values versus converging on goals such as power accumulation and self-preservation. Narayanan and Kapoor are hoping for alignment by default without making the argument for why it might occur. They could have made this argument, but instead they're stuck in a debate from 2003.

Their treatment of experts who believe that there are existential risks also grates. In noting that their views differ from AI experts - who they then subsequently strawman rather than actually dealing with their arguments - Narayanan and Kapoor present a range of "biases" these experts might have. If AGI is imminent, it adds grandeur to your work. AI experts are "hedgehogs" in [Philip Tetlock's forecasting dichotomy](tetlocks-expert-political-judgment-how-good-is-it-how-can-we-know.md), in that they know one big thing and fail to integrate information from other domains. Those who selected into AI research likely dream of building big, all knowing machines.

This ad hominem junk gives me the shits. Let’s try it on them. Their whole schtick is debunking the threat from AI, so obviously they're going to present this side of the argument. They are hedgehogs in that they're trying to jam everything into their AI as a Normal Technology framework. None of which tells us whether they’re right.

Thankfully, their engagement with AI experts and those worried about existential risk has stepped up since this book. I recommend [having a look](https://www.normaltech.ai).