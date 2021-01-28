---
author: jasonacollins
comments: true
date: 2018-01-24 08:00:50+00:00
draft: no
link: https://jasoncollins.blog/2018/01/24/ai-in-medicine-outperforming-humans-since-the-1970s/
slug: ai-in-medicine-outperforming-humans-since-the-1970s
title: 'AI in medicine: Outperforming humans since the 1970s'
wordpress_id: 22395
---

From an interesting a16z podcast episode [Putting AI in Medicine, in Practice](https://a16z.com/2017/11/03/ai-medicine/) (I hope I got the correct names against who is saying what):


<blockquote>_Mintu Turakhia (cardiologist at Stanford and Director of the Centre for Digital Health):_ AI is not new to medicine. Automated systems in healthcare have been described since the 1960s. And they went through various iterations of expert systems and neural networks and called many different things.

_Hanne Tidnam:_ In what way would those show up in the 60s and 70s.

_Mintu Turakhia:_ So at that time there was no high resolution, there weren't too many sensors, and it was about a synthetic brain that could take what a patient describes as the inputs and what a doctor finds on the exam as the inputs.

_Hanne Tidnam:_ Using verbal descriptions?

_Mintu Turakhia:_ Yeah, basically words. People created, you know, what are called ontologies and classification structures. But you put in the ten things you felt and a computer would spit out the top 10 diagnoses in order of probability and even back then, they were outperforming sort of average physicians. So this is not a new concept.</blockquote>


This point about "average physicians" is interesting. In some circumstances you might be able to find someone who outperforms the AI. The truly extraordinary doctor. But most people are not treated by that star.

They continue:


<blockquote>_Brandon Ballinger (CEO and founder of Cardiogram):_ So an interesting case study is the [Mycin system](https://en.wikipedia.org/wiki/Mycin) which is from 1978 I believe. And so, this was an expert system trained at Stanford. It would take inputs that were just typed in manually and it would essentially try to predict what a pathologist would show. And it was put to the test against five pathologists. And it beat all five of them.

_Hanne Tidnam:_ And it was already outperforming.

_Brandon Ballinger:_ And it was already outperforming doctors, but when you go to the hospital they don't use Mycin or anything similar. And I think this illustrates that sometimes the challenge isn't just the technical aspects or the accuracy. It's the deployment path, and so some of the issues around there are, OK, is there convenient way to deploy this to actual physicians. Who takes the risk? What's the financial model for reimbursement? And so if you look at the way the financial incentives work there are some things that are backwards, right. For example, if you think about kindof a hospital from the CFO's perspective, misdiagnosis actually earns them more money because when you misdiagnose you do follow up tests, right, and those, and our billing system is fee for service, so every little test that's done is billed for.

_Hanne Tidnam:_ But nobody wants to be giving out wrong diagnoses. So where is the incentive. The incentive is just in the system, the money that results from it.

_Brandon Ballinger:_ No-one wants to give incorrect diagnosis. On the other hand there's no budget to invest in making better diagnosis. And so I think that's been part of the problem. And things like fee for value are interesting because now you're paying people for, say, an accurate diagnosis, or for a reduction in hospitalisations, depending on the exact system, so I think that's a case where accuracy is rewarded with greater payment, which sets up the incentives so that AI can actually win in this circumstance.

_Vijay Pande (a16z General Partner):_ Where I think AI has come back at us with a force is it came to healthcare as as a hammer looking for a nail. What we're trying to figure out is where you can implement it easily and safely with not too much friction and with not a lot of physicians going crazy, and where it's going to be very very hard.</blockquote>


For better diagnoses, I'd be willing to drive a few physicians crazy.

The section on the types of error was also interesting:


<blockquote>_Mintu Turakhia:_ There may be a point that it truly outperforms the cognitive abilities of physicians, and we have seen that with imaging so far. And some of the most promising aspects of the imaging studies and the EKG studies are that the confusion matrices, the way humans misclassify things, is recapitulated by the convolutional neural networks. ...

A confusion matrix is a way to graph the errors and which directions they go. And so for rhythms on an EKG, a rhythm that's truly atrial fibrillation could get classified as normal sinus rhythm, or atrial tachycardia, or super-ventricular tachycardia, the names are not important. What's important is that the algorithms are making the same type of mistakes that humans are doing. It's not that its making a mistake that's necessarily more lethal, and just nonsensical so to speak. It recapitulates humans. And to me that's the core thesis of AI in medicine, because if you can show that you are recapitulating human error, you're not going to make it perfect, but that tells you that, in check and with control, you can allow this to scale safely since its liable to do what humans do. ....

_Hanne Tidnam:_ And so you're just saying it doesn't have to be better. It just has to be making the same kinds of mistakes to feel that you can trust the decision maker.

_Mintu Turakhia:_ Right. And you dip your toe in the water by having it be assistive. And then at some point we as a society will decide if it can go fully auto, right, fully autonomous without a doctor in the loop. That's a societal issue. That's not a technical hurdle at this point.</blockquote>


Certainly a heavy bias to the status quo. I'd certainly prefer something with better net performance even if some of the mistakes are different.
