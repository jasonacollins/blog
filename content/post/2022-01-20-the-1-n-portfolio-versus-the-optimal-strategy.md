---
title: 'The 1/N portfolio versus the optimal strategy: Does a simple heuristic outperform?'
author: jasonacollins
date: 2022-01-21 09:00:00+00:00
lastmod: 2022-01-21 09:00:00+00:00
draft: false
comments: true
slug: the-1-n-portfolio-versus-the-optimal-strategy-does-a-simple-heuristic-outperform
---

Gerd Gigerenzer is fond of telling a story about [Harry Markowitz](https://en.wikipedia.org/wiki/Harry_Markowitz), modern portfolio design pioneer and winner of the 1990 Nobel Memorial Prize in Economic Sciences.

Here's one version of the story, from [Risk Savvy](https://www.jasoncollins.blog/nudging-citizens-to-be-risk-savvy/):

>Assume you have a chunk of money and want to invest it. You do not want to put all your eggs into one basket and are considering a number of stocks. You want to diversify. But how?
>
>Harry Markowitz won a Nobel Prize in economics for solving this problem. The solution is known as the mean-variance portfolio. The portfolio maximizes the gain (mean) for a given risk or minimizes the risk (variance) for a given return. Many banks rely on this and similar investment methods and warn customers against relying on their intuitions instead.
>
>But when Markowitz made his own investments for his retirement, he did not use his Nobel Prize–winning method. Instead, he employed a simple rule of thumb called 1/N:
>
>*Allocate your money equally to each of N funds.*
>
>Why did he rely on a hunch instead of crunching the numbers? In an interview, Markowitz said he wanted to avoid regrets: “I thought, ‘You know, if the stock market goes way up and I’m not in, I’ll feel stupid. And if it goes way down and I’m in it, I’ll feel stupid.’ So I went 50-50.” He did what many investors do: Make it simple. And 1/N is not only simple, it is the purest form of diversification. (Gigerenzer's source is an [interview of Markowitz by Bruce Bower](https://doi.org/10.1002/scin.5591791221).)
>
>How good is this rule of thumb? In a study, it was compared to mean-variance and a dozen other complex investment methods. Seven situations were analyzed, such as investing in ten American industry funds. The mean-variance portfolio made use of ten years of stock data, while 1/N did not need any. What was the result? In six of the seven tests, 1/N scored better than mean-variance in common performance criteria. Moreover, none of the other twelve complex methods was consistently better at predicting the future value of the stocks.
>
>Does this mean that the Nobel Prize–winning method is a sham? No. It is optimal in an ideal world of known risks, but not necessarily in the uncertain world of the stock market, where so much is unknown. To use such a complex formula requires us to estimate a large number of parameters based on past data. Yet as we have seen, ten years is too short a time to get reliable estimates. Say you invested in fifty funds. How many years of stock data would be needed before the mean-variance method finally does better than 1/N? A computer simulation provides the answer: about five hundred years!
>
>That means that in the year 2500, investors can turn from the simple rule to the high-level math of the mean-variance model and hope to win. But this holds only if the same stocks—and the stock market—are still around.

It's a great story about the power of simple heuristics. But if you follow the academic trail behind it, the story gets messier.

The study that Gigerenzer references is a well-cited [2007 paper by Victor DeMiguel, Lorenzo Garlappi and Raman Uppal](https://doi.org/10.1093/rfs/hhm075) ([pdf](http://faculty.london.edu/avmiguel/DeMiguel-Garlappi-Uppal-RFS.pdf)). They described a comparison of performance between the 1/N rule and 14 other asset allocation models. These included Markowitz’s famous model and a number of its derivatives. The result across seven empirical datasets was that none of the 14 models consistently outperformed the 1/N rule when tested out-of-sample; that is, tested against new data that hadn’t been used to develop the model.

But if you follow Gigerenzer's footnote referencing the DeMiguel and friends study, you also see the following note:

>The conditions under which 1/N is superior to optimization methods are still debated; see Kritzman, Page, and Turkington 2010.

So what do [Kritzman and friends](https://doi.org/10.2469/faj.v66.n2.6) say?

>The ostensible superiority of the 1/N approach arises not from limitations in optimization but, rather, from reliance on rolling short-term samples for estimating expected returns. This approach often yields implausible expectations. By relying on longer-term samples for estimating expected returns or even naively contrived yet plausible assumptions, optimized portfolios outperform equally weighted portfolios out of sample.

The rolling short-term samples referred to relate to DeMiguel and friends' use of a rolling 60- or 120-month history to determine the input parameters for the optimisation exercise.

Kritzman and friends argue that the use of this rolling average leads to problems. For example, in February 2009, the 60-month trailing return of the S&P 500 Index was –5.66 percent. The return of a major bond index was around 3 percent. If you took this previous 5-years as your future expectation, the observed stock and bond holdings implies that most people prefer more risk to less risk for the same return. Why would you otherwise hold the riskier stocks if you expected a negative return when a safer positive return was available? As input assumptions for an optimisation exercise, they are implausible. Kritzman and friends state that in such a situation no investor would simply take the recent historial return as their future expectation.

Kritzman and friends argued that the consequence of these implausible assumptions could be demonstrated by inputting some arbitrarily decided but reasonable sounding expected returns instead of using the recent short-term history. In that case, the superiority of the optimisation approaches re-emerges.

I have some sympathy for this argument. As Kritzman and friends point out, Markowitz did not intend for a naive extrapolation of past returns to form the basis of expectations for the optimisation exercise. Rolling averages make the exercise mechanical and feasible, reducing the number of decisions by the researchers. But simplifying the exercise in this way has a cost.

Alas, the story goes further. A quick Google Scholar search of the papers citing Kritzman and friends shows that this has turned into a huge academic debate.

Here's a quick taste of some of the other papers that I found. I haven't read them in detail and this is out of my area of expertise, so assume I haven't get everything right here:

- [Behr and friends (2013)](https://doi.org/10.1016/j.jbankfin.2012.11.020) ([pdf](https://isiarticles.com/bundles/Article/pre/pdf/5812.pdf)) developed a "constrained minimum-variance strategy" that outperformed a 1/N policy across 6 datasets.

- [Jacobs and friends (2014)](https://doi.org/10.1016/j.finmar.2013.07.004) ([pdf](https://daneshyari.com/article/preview/960996.pdf)) argue that "prominent Markowitz extensions do not outperform several heuristic weighting schemes (1/N heuristic, market value-weighting and GDP-weighting)." While Jacobs and friends extend the range of simple heuristics that are competitive against optimised portfolios, they appear to rely on the same 60-month rolling average to develop input parameters that was criticised by Kritzman and friends.

- [Valeriy Zakamulin (2017)](https://doi.org/10.1016/j.frl.2016.12.007) suggested that those studies which find superior performance of optimised portfolios are doing so because of the particular datasets that tend to be used. The "Kenneth French datasets" tend to have a "low volatility effect", an effect whereby low volatility stocks tend to outperform. The optimisation approaches capitalise on the low volatility effect. I am not convinced that this is a problematic argument. If the optimisation approaches capitalise on an anomaly or established factor premium to outperform, so be it. It suggests there is a way to beat the simple heuristic. But on the other hand, it points to possible alternative heuristics that can capitalise on the anomaly without mean-variance optimisation.

- [Hsu and friends (2018)](https://doi.org/10.1016/j.jbankfin.2018.09.021) suggest that nearly all papers claiming a superiority for optimisation approaches suffer from "data snooping". Data snooping captures publication bias, p-hacking, the garden of forking paths and other phenomena that yield unrepresentative published results. Get rid of "data snooping" and most of the outperformance of optimised methods disappears. This paper is a good reminder that when people claim good "out-of-sample" results, they tell us about the exercise only after they had seen the results themselves. "Out-of-sample" would be far more impressive if that was a future sample.

- [David Allen and friends (2019)](https://doi.org/10.1080/0015198X.2019.1600958) find that if investors have "modest" forecasting ability, mean-variance optimisation is superior. I'm somewhat sceptical of the concept that people have forecasting ability in the sense defined. The paper makes a fairly token attempt to make the case that they do. That said, Allen and friends also provide another take-down of the DeMiguel and friends paper, arguing their result is the result of their modelling approach. Loosen some constraints and optimisation outperforms even without forecasting ability. (This paper itself spawned a debate, with [Michaud and friends](https://doi.org/10.1080/0015198X.2019.1701323) claiming they omitted certain forms of error, and [Allen and friends responding](https://doi.org/10.1080/0015198X.2019.1703984) that they did not and that they use richer, higher-frequency data that many other comparisons.)

As said above, messy. And that is without also exploring the approach to measuring outperformance. I'm not convinced the measures used answer the question at heart. But that's an issue for another day.

Absent a deeper dive into these papers, and as someone who has often told the Markowitz story in a similar manner to Gigerenzer - with a reference to DeMiguel and friends paper and all - I am updating the story I tell somewhat:

- DeMiguel and friends demonstrated that 1/N performed on par with more complex optimisation approaches under a fairly limited set of assumptions and the result may be a peculiarity of their model. I should stop stating that their model establishes the need for 500-years of data.

- However, no-one has clearly shown that more complex optimisation methods are better. In particular, "data snooping" brings many of the results claiming outperformance into question.

- I don't believe it is possible to definitively settle this debate with historic data. Some future oriented bets would be  more informative and could substantially shift my beliefs, but even then it may not be conclusive. You can get a high Sharpe ratio by picking up pennies in front of a steamroller if the period of measurement doesn't include you getting hit by the steamroller. I am sure I have read (somewhere) Nassim Taleb claiming that high Sharpe ratios are a sign that someone will blow up.

Deep down, I still believe that a 1/N heuristic can be sound  even when compared to more sophisticated approaches. This is not a question of getting enough data - as appears implied by Gigerenzer in the quoted passage - but one of of robustness in the face of uncertainty and an unstable future with the potential for structural changes. This belief is buttressed by the broader evidence on the [power of simple heuristics](https://behavioralscientist.org/simple-heuristics-that-make-algorithms-smart/).

But as a starting point I should be weakening - at least slightly - my belief about the 1/N heuristic given the specific paper I have regularly quoted in support of that claim isn't as general or robust as I thought it was.

One factor that constrains that weakening is an observation from this latest perusal of the literature. The 1/N heuristic appears to have a degree of respect. It is often used as the benchmark against which portfolio optimisation techniques are assessed. Most of the papers I found exploring the performance of 1/N were using it as a benchmark rather than genuinely exploring its robustness.

Finally, with all this said, there remains one issue that looms large over this exercise. If deciding a 1/N strategy, what should N be?

If there are two bonds and three stocks, does N equal two (stocks and bonds) or five. What of an N of two with crypto- and non-crypto-assets? Should we group domestic and international stocks? What of different sectors?

Most of the papers mentioned above have relatively sophisticated people picking what comprises N. What of the average investor? How does their portfolio hold up with a 1/N rule?

In Risk Savvy, Gigerenzer is sensitive to this question of choosing N. He discussed a time when an organisation's head of investment asked whether his customers might just invest themselves if all they need is a 1/N rule. Gigerenzer's writes:

>I reassured him that there are plenty of open questions, such as how large N should be, what kind of stocks, when to rebalance, and most important, to figure out when and where 1/N is a successful strategy.

That's not an easy task. But maybe there's another simple heuristic by which we choose N?