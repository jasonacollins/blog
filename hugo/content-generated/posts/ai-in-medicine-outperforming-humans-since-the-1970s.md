---
title: 'AI in medicine: Outperforming humans since the 1970s'
author: "Jason Collins"
date: 2018-01-24 08:00:50+00:00
draft: false
sync_source: "posts/ai-in-medicine-outperforming-humans-since-the-1970s.md"
sync_route: "pandoc"
sync_hash: "e77d09196d62"
---

{{< html >}}
<p>From an interesting a16z podcast episode <a href="https://a16z.com/2017/11/03/ai-medicine/">Putting AI in Medicine, in Practice</a> (I hope I got the correct names against who is saying what):</p>
<blockquote>
<p><em>Mintu Turakhia (cardiologist at Stanford and Director of the Centre for Digital Health):</em> AI is not new to medicine. Automated systems in healthcare have been described since the 1960s. And they went through various iterations of expert systems and neural networks and called many different things.</p>
<p><em>Hanne Tidnam:</em> In what way would those show up in the 60s and 70s.</p>
<p><em>Mintu Turakhia:</em> So at that time there was no high resolution, there weren’t too many sensors, and it was about a synthetic brain that could take what a patient describes as the inputs and what a doctor finds on the exam as the inputs.</p>
<p><em>Hanne Tidnam:</em> Using verbal descriptions?</p>
<em>Mintu Turakhia:</em> Yeah, basically words. People created, you know, what are called ontologies and classification structures. But you put in the ten things you felt and a computer would spit out the top 10 diagnoses in order of probability and even back then, they were outperforming sort of average physicians. So this is not a new concept.
</blockquote>
<p>This point about “average physicians” is interesting. In some circumstances you might be able to find someone who outperforms the AI. The truly extraordinary doctor. But most people are not treated by that star.</p>
<p>They continue:</p>
<blockquote>
<p><em>Brandon Ballinger (CEO and founder of Cardiogram):</em> So an interesting case study is the <a href="https://en.wikipedia.org/wiki/Mycin">Mycin system</a> which is from 1978 I believe. And so, this was an expert system trained at Stanford. It would take inputs that were just typed in manually and it would essentially try to predict what a pathologist would show. And it was put to the test against five pathologists. And it beat all five of them.</p>
<p><em>Hanne Tidnam:</em> And it was already outperforming.</p>
<p><em>Brandon Ballinger:</em> And it was already outperforming doctors, but when you go to the hospital they don’t use Mycin or anything similar. And I think this illustrates that sometimes the challenge isn’t just the technical aspects or the accuracy. It’s the deployment path, and so some of the issues around there are, OK, is there convenient way to deploy this to actual physicians. Who takes the risk? What’s the financial model for reimbursement? And so if you look at the way the financial incentives work there are some things that are backwards, right. For example, if you think about kindof a hospital from the CFO’s perspective, misdiagnosis actually earns them more money because when you misdiagnose you do follow up tests, right, and those, and our billing system is fee for service, so every little test that’s done is billed for.</p>
<p><em>Hanne Tidnam:</em> But nobody wants to be giving out wrong diagnoses. So where is the incentive. The incentive is just in the system, the money that results from it.</p>
<p><em>Brandon Ballinger:</em> No-one wants to give incorrect diagnosis. On the other hand there’s no budget to invest in making better diagnosis. And so I think that’s been part of the problem. And things like fee for value are interesting because now you’re paying people for, say, an accurate diagnosis, or for a reduction in hospitalisations, depending on the exact system, so I think that’s a case where accuracy is rewarded with greater payment, which sets up the incentives so that AI can actually win in this circumstance.</p>
<em>Vijay Pande (a16z General Partner):</em> Where I think AI has come back at us with a force is it came to healthcare as as a hammer looking for a nail. What we’re trying to figure out is where you can implement it easily and safely with not too much friction and with not a lot of physicians going crazy, and where it’s going to be very very hard.
</blockquote>
<p>For better diagnoses, I’d be willing to drive a few physicians crazy.</p>
<p>The section on the types of error was also interesting:</p>
<blockquote>
<p><em>Mintu Turakhia:</em> There may be a point that it truly outperforms the cognitive abilities of physicians, and we have seen that with imaging so far. And some of the most promising aspects of the imaging studies and the EKG studies are that the confusion matrices, the way humans misclassify things, is recapitulated by the convolutional neural networks. …</p>
<p>A confusion matrix is a way to graph the errors and which directions they go. And so for rhythms on an EKG, a rhythm that’s truly atrial fibrillation could get classified as normal sinus rhythm, or atrial tachycardia, or super-ventricular tachycardia, the names are not important. What’s important is that the algorithms are making the same type of mistakes that humans are doing. It’s not that its making a mistake that’s necessarily more lethal, and just nonsensical so to speak. It recapitulates humans. And to me that’s the core thesis of AI in medicine, because if you can show that you are recapitulating human error, you’re not going to make it perfect, but that tells you that, in check and with control, you can allow this to scale safely since its liable to do what humans do. ….</p>
<p><em>Hanne Tidnam:</em> And so you’re just saying it doesn’t have to be better. It just has to be making the same kinds of mistakes to feel that you can trust the decision maker.</p>
<em>Mintu Turakhia:</em> Right. And you dip your toe in the water by having it be assistive. And then at some point we as a society will decide if it can go fully auto, right, fully autonomous without a doctor in the loop. That’s a societal issue. That’s not a technical hurdle at this point.
</blockquote>
<p>Certainly a heavy bias to the status quo. I’d certainly prefer something with better net performance even if some of the mistakes are different.</p>
{{< /html >}}
