---
title: "A gradual disempowerment reading list"
author: "Jason Collins"
date: 2026-05-27 11:00:00+10:00
draft: false
toc: false
images: [""]
bibliography: references.bib
link-citations: true
---

```{=html}
<style>
#quarto-appendix {
  display: none;
}
</style>
```

I recently completed BlueDot Impact's [AGI Strategy Course](https://bluedot.org/courses/agi-strategy). (I recommend it.) Through the weekly discussions, I went down the rabbit hole of [gradual disempowerment](https://gradual-disempowerment.ai/). I find many AI threats compelling, but gradual disempowerment is the risk where my background perhaps offers the most insight.

I find an interesting tension in this topic. I have written in the past about how more decisions should be handed to AI (e.g. [here](https://behavioralscientist.org/dont-touch-computer/), [here](https://behavioralscientist.org/what-to-do-when-algorithms-rule/) and [here](https://behavioralscientist.org/principles-for-the-application-of-human-intelligence/)). Since Paul Meehl's [Clinical Versus Statistical Prediction](https://doi.org/10.1037/11281-000) in 1954, a large body of research has shown that statistical prediction can outperform human judgement in some domains. We should be capturing those benefits.

However, I can see an endpoint where this doesn't end well. Competitive pressures between companies and states could drive the adoption of AI decision-making to the point where humans are completely out of the
loop. The result is a disempowered humanity. This handover magnifies risks from misaligned AI or rogue actors.

As a follow-up to the BlueDot course, I have pulled together the gradual disempowerment reading list below.

The list reflects my worldview, so later entries may not appear in standard AI safety reading lists. It contains core readings on gradual disempowerment, plus adjacent work on automation, human control, and deskilling that helps explain how humans might lose meaningful influence.

I'll add more papers as I find them.

## The core thesis

@christiano2019 [What failure looks like](https://www.alignmentforum.org/posts/HBxe6wdjxK239zajf/what-failure-looks-like): A precursor to the gradual disempowerment thesis. Humanity goes “out with a whimper” as human reasoning ceases to be able to compete with AI.

@brynjolfsson2022 [The Turing Trap: The Promise & Peril of Human-Like Artificial Intelligence](https://doi.org/10.1162/daed_a_01915): Human-like AI can push development toward substitution rather than augmentation, reducing human bargaining power.

@critch2023 [TASRA: a Taxonomy and Analysis of Societal-Scale Risks from AI](https://doi.org/10.48550/arXiv.2306.06924): See Risk Type I Diffusion of Responsibility.

@kulveit2025 [Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development](https://arxiv.org/abs/2501.16946): The anchor paper.

@chakravorty2025 [Gradual Disempowerment Summary](https://blog.bluedot.org/p/gradual-disempowerment-summary): BlueDot Impact's summary of the Kulveit et al. paper. A quick way to get across it.

@drago2025 [The Intelligence Curse](https://intelligence-curse.ai/) ([pdf](https://intelligence-curse.ai/intelligence-curse.pdf)): If states and companies don't need people, they won't care about them. Chapters 2 and 3 are particularly relevant to the gradual disempowerment thesis.

@fenwick2025 [Gradual disempowerment](https://80000hours.org/problem-profiles/gradual-disempowerment/): A summary of the gradual disempowerment thesis on 80,000 Hours. Includes links to other readings.

@davidson2025 [Thoughts on Gradual Disempowerment](https://www.alignmentforum.org/posts/ct6SMDuexe9uBwDoL/thoughts-on-gradual-disempowerment): Some rough notes testing the edges of the thesis.

@sharma2026a [Who's in Charge? Disempowerment Patterns in Real-World LLM Usage](https://doi.org/10.48550/arXiv.2601.19062): Claude conversations show patterns of user autonomy being undermined. Disempowerment potential appears to be increasing. See also the [related blog post](https://www.anthropic.com/research/disempowerment-patterns) by @sharma2026b.

@wiblin2026 [#234 – David Duvenaud on why ‘aligned AI’ could still kill democracy](https://80000hours.org/podcast/episodes/david-duvenaud-gradual-disempowerment/): Robert Wiblin interviews David Duvenaud, one of the authors of @kulveit2025.

## Automation bias and the erosion of human capability

Despite all the talk about people becoming deskilled as AI takes over, there isn't a lot of great literature concerning the latest AI. However, there is a rich, older literature on automation that we can draw on.

@bainbridge1983 [Ironies of automation](https://doi.org/10.1016/0005-1098(83)90046-8) ([ungated pdf](https://static1.squarespace.com/static/644321e78cd2dd37613af33e/t/6694873f71612132a84371c7/1721009983702/Ironies+of+Automation_Bainbridge_1983.pdf)): When you automate the routine and leave the exceptions to the human, the operator has fewer opportunities to practise in preparation for those exceptional circumstances.

@endsley1995 [The Out-of-the-Loop Performance Problem and Level of Control in Automation](https://doi.org/10.1518/001872095779064555) ([ungated pdf](https://www.researchgate.net/profile/Mica-Endsley/publication/238726310_The_Out-of-the-Loop_Performance_Problem_and_Level_of_Control_in_Automation/links/56426ab008aebaaea1f8e7a9/The-Out-of-the-Loop-Performance-Problem-and-Level-of-Control-in-Automation.pdf)): Operators "out of the loop" have a harder time detecting errors and stepping in when automation errs than those who manually perform the same tasks.

@parasuraman1997 [Humans and Automation: Use, Misuse, Disuse, Abuse](https://doi.org/10.1518/001872097778543886) ([ungated pdf](https://andy-blog.oss-cn-beijing.aliyuncs.com/blog/2021-08-02-parasurman-humans-and-automation-use-misuse-disuse-abuse.pdf)): A classic paper on automation. The use, misuse, disuse, abuse split helpful is helpful.

@skitka1999 [Does automation bias decision-making?](https://doi.org/10.1006/ijhc.1999.0252) ([ungated pdf](https://www.researchgate.net/profile/Kathleen-Mosier/publication/222507469_Does_automation_bias_decision-making/links/5a1b614c4585155c26adec90/Does-automation-bias-decision-making.pdf)): Participants given an imperfect decision aid did worse than those given none.

@parasuraman2010 [Complacency and Bias in Human Use of Automation: An Attentional Integration](https://doi.org/10.1177/0018720810376055) ([ungated pdf](https://www.researchgate.net/profile/Raja-Parasuraman/publication/47792928_Complacency_and_Bias_in_Human_Use_of_Automation_An_Attentional_Integration/links/09e4150c09890db4c6000000/Complacency-and-Bias-in-Human-Use-of-Automation-An-Attentional-Integration.pdf)): Review of automation complacency and automation bias.

@barr2015 [The brain in your pocket: Evidence that Smartphones are used to supplant thinking](https://doi.org/10.1016/j.chb.2015.02.029): People offload thinking to the device.

@sarkar2024 [When Copilot Becomes Autopilot: Generative AI’s Critical Risk to Knowledge Work and a Critical Solution](https://doi.org/10.48550/arXiv.2412.15030): A research agenda for AI as a critic or provocateur.

@lee2025 [The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers](https://doi.org/10.1145/3706598.3713778): Higher confidence in generative AI is associated with less critical thinking.

@krook2025 [When Autonomy Breaks: The Hidden Existential Risk of AI](https://doi.org/10.1007/s00146-025-02397-5) ([ungated pdf](https://doi.org/10.48550/arXiv.2503.22151)): Humans may lose skills such as critical thinking, decision-making and social care in an AGI world. This paper puts some of the above references into context, arguing why the deskilling matters.