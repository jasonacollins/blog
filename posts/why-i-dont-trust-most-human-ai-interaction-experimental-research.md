---
title: "Why I don't trust most human-AI interaction experimental research"
author: "Jason Collins"
date: 2025-06-12 09:00:00+10:00
draft: false
---

Experimental psychology research before the mid-2010s was a mess. The field was littered with papers with weak to non-existent theoretical foundations. Experimental data was unavailable. (The statement "data is available on request" is [somewhat of a joke](https://osf.io/preprints/psyarxiv/jbu9r_v1).) The experiments involved small samples and barely significant p-values. File drawers were overflowing with the carcasses of experiments that didn't quite get the result hoped for. The [forking paths](https://sites.stat.columbia.edu/gelman/research/unpublished/p_hacking.pdf) in the data analysis allowed multiple shots at goal.

Those poor practices were most starkly revealed with the publication of the Open Science Collaboration's [review](https://doi.org/10.1126/science.aac4716) of the replicability of psychological science. 36% of psychology papers replicated. The stream of failed replications continues.

Today, however, things look better, at least methodologically. Pre-registration and open experimental materials and data are becoming common, if not required. Many journals and reviewers take these elements as table stakes for publication. Registered reports are now an option. Theory is still often weak and those file drawers remain full, but at least the presence of preregistration repositories gives us a sense of what is in them. PNAS and other tabloids continue to be PNAS, but don't hope for miracles.

Psychology was, of course, not the only field to suffer a replication crisis and shift practices. Experimental economics has improved, despite coming through the crisis less tarnished than psychology. Many fields and the associated journals have adopted open science practices. If an experimental field hasn't adjusted its practices in the last decade you need to question what is going on.

Which brings me to my experience in the human-AI and human-computer interaction literature. This literature largely concerns how we get better decisions or actions when people interact with AI, algorithms and other automated decision rules. How do we get people to use beneficial AI? How do we get "complementary performance", where the performance of the human-AI combination is better than the human or AI by themselves? How do we help calibrate user trust in AI tools?

I've been writing and thinking about the topic for close to a decade now. My first article in Behavioural Scientist ([Don't Touch The Computer](https://behavioralscientist.org/dont-touch-computer/)) argued that often we should take the human out of the loop. In the last year or so I've been working on how to use AI in improving financial decision making. I've read 100s of experimental papers in the field looking for ideas and evidence.

What I have seen is depressing. I hoped to find a field that had learned from psychology's mistakes. Instead I found a field operating as if the replication crisis never happened.  Weak theory. Negligible pre-registration. Forking paths. Underpowered experiments. The data is unavailable. (Less than 10% of papers I have read have data openly available in a repository.) Typically, there isn't even a statement that data is available on request. The experimental materials are often well described in the paper - many human-AI interaction papers have quite novel models and software interfaces - but the detail isn't sufficient for you to construct the models or software yourself. And this isn't an old problem. These are papers from the last decade, some even from this year. There are exceptions and a few great papers, but I can't see any trend in the right direction.

I'm always looking for new ideas for practical application. And a first step in that process is replication. Unfortunately, absent open data and experimental materials, we can't reproduce or replicate the experiment. And when you look at the weak theory and forking paths in the analysis, it's hard to give the result sufficient credence to the idea to test it in a lab or field context.

I've emailed a lot of authors asking for the experimental data and materials. In around 20% of cases, I've received an email in less than 24 hours with the materials, plus an offer to help if they could be useful. These are typically academics in economics, management and business schools who I suppose come from a culture where practices have changed. However, in most cases I simply haven't received a response. Computer science and human-computer interaction researchers: it's crickets.

Part of me wants to be understanding. They're busy. Is it worth their taking their time to respond to a random from Australia who has written three sentences along the lines of "I like your paper/idea and am keen to replicate in a financial services context, can you share your data and materials"?

But on the other hand, they've gone to the effort to publish the paper (typically in a conference proceeding) and they want us to take their idea seriously. (Actually, maybe that's not what they want. They just want the publication on their record and have moved on.) Unless their materials are a shambles, it should be minimal effort to share them. (If they don't have it in a state to share, that's another robustness flag.) The data is also of minimal sensitivity, involving bespoke abstract tasks in the lab. Post it to a public repository and you're done with my and every following request.

There isn't much encouragement for data sharing from the major publishing forums either. Here's the data sharing policy of some of the conferences in human-AI interaction, the venues for many of the papers I have read:

> [CHI conference on Human Factors in Computing Systems](https://chi2025.acm.org/for-authors/papers/): "Reproducibility: Where relevant, authors are strongly encouraged to provide supplementary materials to support practices around research reproducibility as much as possible. Please refer to the requirements for supplementary materials below." They indicate how seriously they take it when the supplementary materials section is headed "Step 2. Prepare Supplementary Materials (Optional)".

> [Conference on Neural Information Processing Systems (NeurIPS)](https://neurips.cc/public/guides/CodeSubmissionPolicy): "If any of the main contributions of your paper depends on an experimental result, you are strongly encouraged to submit code that produces this result. If you are using a new dataset, you are also encouraged to submit the dataset."

> [ACM Conference on Intelligent User Interfaces](https://iui.acm.org/2025/call_for_papers.html): "Submitting supplemental material (e.g. questionnaires, demo videos of applications, data sheets) is optional but encouraged."

After a fair bit of digging, I did find the following [ACM policy](https://www.acm.org/publications/policies/digital-artifacts) - it's buried enough I expect most paper submitters wouldn't even read it:

> Submission and Publication of Digital Artifacts as Supplemental Material
> 
> ACM does not require, but strongly recommends, that authors of ACM published Works provide access to the artifacts used to conduct research reported on in their published Works.

I can tell from the lack of data for most experimental papers that this optionality is used by authors. Welcome to 2010.

So, is there a coming replication crisis for human-computer interaction?

Unfortunately, I don't think so. When you need a bespoke machine learning algorithm or software interface, the replication simply isn't going to happen. Although most psychology papers aren't replicated, enough can be replicated at low cost to enable a view of the robustness of the field. I fear too many human-AI interaction papers exceed that cost threshold.

What I expect instead is filtering by practitioners. Many of the readers of the human-AI interaction literature, like me, are after practical solutions. Practitioners are going to filter the good from the bad, as what doesn't work won't get used. The A-B testing culture in AI and design teams allows that. I see the same thing in applied behavioural science (those few external readers of the psychology literature). There are a bunch of ideas that the applied community recognises as ineffective, despite there being no "failed" replication of the original experiment. We'd simply moved on. The "sign at the top" experiment was already dead among practitioners before the [failed replications and fraud emerged](a-default-of-disbelief.md).

In the longer term, I hope some decent practices will eventually filter into the field and we can simply forget about the current body of research. There are a few computer science academics that have open sourced their experimental setups on GitHub (thank you!) and made data available. Surely someone is paying attention and giving greater weight to their work. I am. There are also some platforms built for others to use, although there doesn't seem to be much of a culture of using them yet. (Here's [one](https://github.com/gagb/caja) developed by Gagan Bansal and friends, as described in [this paper](https://doi.org/10.1609/hcomp.v7i1.5285).)

In the meantime, I'm taking what I read with a grain of salt. A while ago I posted that we should approach the psychology literature with a "[default of disbelief](a-default-of-disbelief.md)". If you see an interesting experimental result indicating a new phenomena or result, update your beliefs in only the mildest way. Don't trust it until you see concordant results from independent pre-registered replications. I'm reading the human-AI interaction literature in the same way.