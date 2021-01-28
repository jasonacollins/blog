---
author: jasonacollins
comments: true
date: 2017-08-22 09:00:08+00:00
draft: no
link: https://jasoncollins.blog/2017/08/22/oneils-weapons-of-math-destruction-how-big-data-increases-inequality-and-threatens-democracy/
slug: oneils-weapons-of-math-destruction-how-big-data-increases-inequality-and-threatens-democracy
title: 'Cathy O''Neil''s Weapons of Math Destruction: How Big Data Increases Inequality
  and Threatens Democracy'
wordpress_id: 22159
---

In her interesting [Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy](http://amzn.to/2vwrt3c), Cathy O'Neil defines Weapons of Math Destruction based on three criteria - opacity, unfairness and scale.

Opacity makes it hard to assess the fairness of mathematical models (I'll use the term algorithms through most of this post), and it facilitates (or might even be a key component of) an algorithm's effectiveness if it relies on naive subjects. "These bonds have been rated by maths geniuses - buy them." Unfairness relates to whether the algorithm operates in the interest of the modelled subject. Scale is not just that algorithms can affect large numbers of people. Scale can also lead to the establishment of norms that do not allow anyone to escape the operation of the algorithm.

These three factors are common across most of the problematic algorithms O'Neil discusses, and she makes a strong and persuasive case that many algorithms could be developed or used better. But the way she combines many of her points, together with her politics, often makes it unclear what exactly the problem is or what potential solutions could (should) be.

A distinction that might have made this clearer (or at least that I found useful) is between algorithms that don't do what the developer intends, algorithms working as intended but that have poor consequences for those on the wrong side of their application, and algorithms that have unintended consequences once released into the wild. The first is botched math, the second is math done well to the detriment of others, while the third is good or bad math with naive application.

For this post I am going to break O'Neil's case into these three categories.

**Math done poorly**

When it comes to the botched math, O'Neil is at her best. Her tale of teacher scoring algorithms in Washington DC is a case where the model is not helping anyone. Teachers were scored based on the deviations of student test scores from those predicted by models of the students. The bottom 2% to 5% of teachers were fired. But the combination of modelled target student scores and small classrooms made the scoring of teachers little better than random. There was almost no correlation in a teacher's scores from one year to the next.

Her critique of the way many models are developed is also important. Are we checking the model is working, rather than just assuming that the teachers we fired are the right ones? She contrasts the effort typically spent testing a recidivism model (for use in determining prison sentences) to the way Amazon learns about its customers. Amazon doesn't simply develop a single "recidivism score" equivalent and take that as determinative. Instead they continue to test and learn as much as they can about their interactions with customers to make the best models they can.

The solutions to the botched math are simpler (at least in theory) than many of the other problems she highlights. The teacher scoring models simply require someone with competence to consider what it is they might want to care about and measure, and if it can be done, work out whether it can be done in a statistically meaningful way. If it can't, so be it. The willingness to concede that they can't develop a meaningful model is important if that is the case, particularly if it is designed to inform high-stakes decisions. Similarly, recidivism scoring algorithms should be subject to constant scrutiny.

But this raises the question of how you assess an algorithm. What is the appropriate benchmark? Perfection? Or the system it is replacing? At times O'Neil places a heavy focus on the errors of the algorithm, with little focus on the errors of the alternative - the humans it replaced. Many of O'Neil's stories involve false positives, leading to a focus on the obvious algorithm errors, with the algorithm's greater accuracy and the human errors unseen. A better approach might be to simply compare alternative approaches and see which is better, rather than having the human as the default. Once the superior alternative is selected, we also need to remain cognisant that the best option still might not be very good.

As O'Neil argues, some of the poor models would also be less harmful if they were transparent. People could pull the models apart and see whether they were working as intended. A still cleaner version might be to just release the data and let people navigate it themselves (e.g. education data), although this is not without problems. Whatever is the most salient way of sorting and ranking will become the new defacto model. If we don't do it ourselves, someone will take that data and give us the ranking we crave.

**Math done well (for the user anyhow)**

When comes to math done well, O'Neil's three limbs of the WMD definition - opacity, unfairness and scale - are a good description of the problems she sees. O'Neil's critique is usually not so much about the maths, but the unfair use of the models for purposes such as targeting of the poor (think predatory advertising by private colleges or payday lenders) or treating workers as cogs in the machine through the use of scheduling software.

In these cases, it is common that the person being modelled does not even know about the model (opacity). And if they could see the model, it may be hard to understand what characteristics are driving the outcome (although this is not so different to the opacity of human decision-making). The outcome then determines how we are treated, the ads we see, the prices we see, and so on.

One of O'Neil's major concerns about fairness is that the models discriminate. She suggests they discriminate against the poor, African-Americans and those with mental illness. This is generally not through a direct intention to discriminate against these groups, although O'Neil gives the example of a medical school algorithm rejecting applicants based on birthplace due to biased training data. Rather, the models use proxies for the variables of interest, and those proxies also happen to correlate with certain group features.

This points to the tension in the use of many of these algorithms. Their very purpose is to discriminate. They are developed to identify the features that, say, employers or lenders want. Given there is almost always a correlation between those features and some groups, you will inevitably "discriminate" against them.

So what is appropriate discrimination? O'Neil objects to tarring someone with group features. If you live in a certain postcode, is it fair to be categorised with everyone else in that postcode? Possibly not. But if you have an IQ that is judged likely to result in poor job performance or creditworthiness based on the past performance of other people with that IQ, is that acceptable? What of having a degree?

The use of features such as postcodes, IQ or degrees come from the need to identify proxies for the traits people want to identify, such as whether they will pay back the loan or deliver good work performance. Each proxy varies in the strength of prediction, so the obvious solution seems to be to get more data and better proxies. Which of these is going to give us the best prediction of what we actually care about?

But O'Neil often balks at this step. She tells the story of a chap who can't get minimum wage job due to his results on a five-factor model personality test, despite his "near perfect SAT". The scale of the use of this test means he runs into this barrier with most employers. When O'Neil points out that personality is only one-third as predictive as cognitive tests, she doesn't make the argument that employers should be allowed to use cognitive tests. She even suggests that employers are rightfully barred from using IQ tests in recruitment (as per a 1971 Supreme Court case). But absent the cognitive tests, do employers simply turn to the next best thing?

Similarly, when O'Neil complains about the use of "e-scores" (proxies for credit scores) in domains where entities are not legally allowed to use credit scores to discriminate, she complains that they are using a "sloppy substitute". But again she does not complain about the ban on using the more direct measures.

There are also two sides to the use of these proxies. While the use of the proxies may result in some people being denied a job or a loan, it may allow someone else to get that job or loan, or to pay a better price, when a cruder measure might have seen that person being rejected.

O'Neil gives the example of ZestFinance, a payday lender that typically charges 60% lower than the industry standard. ZestFinance does this by finding every proxy for creditworthiness it can, picking out proxies such as correct use of capitalisation on the application form, and whether the applicant read the terms and conditions. O'Neil complains about those who are accepted for a loan but have to pay higher fees because of, say, poor spelling. This is something the poor and uneducated are more likely to incur. But her focus is on one type of outcome, those with more expensive loans (although probably still cheaper than from other payday lenders), leaving those people receiving the cheapest loans unseen. Should we deny this class of people the access to the cheaper finance these algorithms allow?

One interesting case in the book concerns the pricing of car insurance. An insurer wants to know who is the better driver, so they develop algorithms to price the risk appropriately. Credit scores are predictive of driving performance, so those with worse credit scores end up paying more for this.

But insurers also want to price discriminate to the extent that they can. That is, they want to charge each individual the highest price they will tolerate. Price discrimination can be positive for the poor. Price discrimination allows many airlines to offer cheap seats in the back of the plane when the business crowd insists on paying extra for a few inches of leg room. I benefited from the academic pricing of software for years, and we regularly see discounted pricing for students and seniors. But price discrimination can also allow the uninformed, lazy and those without options to be stripped of a few extra dollars. In the case of the insurer pricing algorithms, they are designed to price discriminate in addition to price the policy based on risk.

It turns out that credit score is not just predictive of driving performance, but also of buyer response to price changes. The resultant insurance pricing is an interaction of these two dimensions. O'Neil gives an example from Florida, where adults with clean driving records but poor credit scores paid $1,552 more (on average) than drivers with excellent credit but a drunk driving conviction, although it is unclear how much of this reflects risk and how much price discrimination.

**Naive math**

One of O'Neil's examples of a what I will call naive math are those algorithms that create a self-reinforcing feedback loop. The model does what it is supposed to do - say, predict an event - but once used in a system, the model's classification of a certain cohort becomes self-fulfilling or self-reinforcing.

For example, if longer prison sentences make someone more likely to offend on their release, any indicator that results in longer sentences will in effect become more strongly correlated with re-offending. Even if the model is updated to disentangle this problem, allowing the effect of the longer sentences to be isolated, the person who received a longer sentence is doomed the next time they are scored.

In a sense, the model does exactly what it should, predicting who will re-offend or not, and there is ample evidence that they do better than humans. But the application of the model does more than simply predicting recidivism. It might ultimately affirm itself.

Another example of a feedback loop is a person flagged as a poor credit risk. As they can't get access to cheap credit, they then go to an expensive payday lender and ultimately run into trouble. That trouble is flagged in the credit scoring system, making it even harder for them to access financial services. If the algorithm made an error in the first instance - the person was actually a good credit risk - that person might then become a poor risk because the model effectively pushed them into more expensive products.

The solutions to these feedback loops are difficult. On the one hand, vigilant investigation and updating the models will help ameliorate the problems. O'Neil persuasively argues that we don't do this enough. Entities such as ZestFinance that use a richer set of data can also break the cycle for some people.

But it is hard to solve the case for individual mis-classification. Any model will have false positives and false negatives. The model development process can only try to limit them, often with a trade-off between the two.

In assessing this problem we also need to focus on the alternative. Before these algorithms were developed, people would be denied credit, parole and jobs for all sorts of whimsical decisions on the part of the human decision makers. Those decisions would then result in feedback loops as their failures are reflected in future outcomes. The algorithms might be imperfect, but can be an improvement.

This is where O'Neil's scale point becomes interesting. In a world of diverse credit scoring mechanisms, a good credit risk who is falsely identified as a poor risk under one measure might by accurately classified under another. The false positive is not universal, allowing them to shop around for the right deal. But if every credit provider uses the same scoring system, someone could be universally barred. The pre-algorithm world, for all its flaws, possibly provided more opportunities for someone to find the place where they are not incorrectly classified.

A final point on naive models (although O'Neil has more) is that models reflect goals and ideology. Sometimes this is uncontroversial - we want to keep dangerous criminals off the street. Sometimes this is more complicated - what risk of false positives are we willing to tolerate in keeping those criminals off the street? In many ways the influence of O'Neil's politics on her critique provide the case in support of this point.

**Solutions**

Before reading the book, I listened to O'Neil on an [Econtalk episode with Russ Roberts](http://www.econtalk.org/archives/2016/10/cathy_oneil_on_1.html). There she makes the point that where we run into flawed algorithms, we shouldn't always be going back to the old way of doing things (she made that comment in the context of judges). We should be making the algorithms better.

That angle was generally absent from the book. O'Neil takes the occasional moment to acknowledge that many algorithms are not disrupting perfect decision-making systems, but are replacing biased judges, bank managers who favoured their friends, and unstructured job interviews with no predictive power. But through the book she seems quite willing to rip those gains down in the name of fairness.

More explicitly, O'Neil asks whether we should sacrifice efficiency for fairness. For instance, should we leave some data out? In many cases we already do this, by not including factors such as race. But should this extend to factors such as who someone knows, their job or their credit score.

O'Neil's choice of factors in this instance is telling. She asks whether someone's connections, job or credit score should be used in a recidivism model, and suggests no as they would be inadmissible in court. But this is a misunderstanding of the court process. Those factors are inadmissible in determining guilt or innocence, but form a central part of sentencing decisions. Look at the use of referees or stories about someone's tough upbringing. So is O'Neil's complaint about the algorithm, or the way we dispense criminal justice in general? This reflects a feeling I had many times in the book that O'Neil's concerns are much deeper than the effect of algorithms and extend to the nature of the systems themselves.

Possibly the point on which I disagree with O'Neil most is her suggestion that human decision-making has a benefit in that it can evolve and adapt. In contrast, a biased algorithm does not adapt until someone fixes it. The simple question I ask is where is the evidence of human adaptation? You just need to look at all the programs to eliminate workplace bias with no evidence of effectiveness for a taste of how hard it is to deliberately change people. We continue to be prone to seeing spurious correlations, and making inconsistent and unreliable decisions. For many human decisions there is simply no feedback loop as to whether we made the right decision. How will a human lender ever know they rejected a good credit risk?

While automated systems are stuck until someone fixes them, someone can fix them. And that is often what happens. Recently several people forwarded to me an article on the inability of some facial recognition systems to recognise non-Caucasian faces. But beyond the point that humans also have this problem (yes, "[they all look alike](https://en.m.wikipedia.org/wiki/Cross-race_effect)"), the problem with facial recognition algorithms has been identified and, even though it is a tough problem, there are major efforts to fix it. (Considering some of the major customers of this technology are police and security services, there is an obvious interest in solving it.) In the meantime, those of us raised in a largely homogeneous population are stuck with our cross-racial face blindness.
