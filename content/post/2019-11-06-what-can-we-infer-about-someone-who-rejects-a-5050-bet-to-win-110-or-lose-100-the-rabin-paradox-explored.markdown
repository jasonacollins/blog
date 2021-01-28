---
title: "What can we infer about someone who rejects a 50:50 bet to win $110 or lose $100? The Rabin paradox explored"
author: "Jason Collins"
date: '2019-11-06  01:00:00+00:00'
draft: no
comments: true
slug: what-can-we-infer-about-someone-who-rejects-a-5050-bet-to-win-110-or-lose-100-the-rabin-paradox-explored
---

Consider the following claim:

>We don't need loss aversion to explain a person's decision to reject a 50:50 bet to win \$110 or lose \$100. That just simple risk aversion as in expected utility theory.

Risk aversion is the concept that we prefer certainty to a gamble with the same expected value. For example, a risk averse person would prefer \$100 for certain over a 50-50 gamble between \$0 and \$200, which has an expected value of \$100. The higher their risk aversion, the less they would value the 50:50 bet. They would also be willing to reject some positive expected value bets.

Loss aversion is the concept that losses loom larger than gains. If the loss is weighted more heavily that the gain - it is often said that losses hurt twice as much as gains bring us joy - then this could also explain the decision to reject a 50:50 bet of the type above. Loss aversion is distinct from risk aversion as its full force applies to the first dollar either side of the reference point from which the person is assessing the change (and at which point risk aversion should be negligible).

So, do we need loss aversion to explain the rejection of this bet, or does risk aversion suffice?

One typical response to the above claim is loosely based on the Rabin Paradox, which comes from a paper published in 2000 by Matthew Rabin:

>An expected utility maximiser who rejects this bet is exhibiting a level of risk aversion that would lead them to reject bets that no one in their right mind would reject. It can't be the case that this is simply risk aversion.

For the remainder of this post I am going to pull apart Rabin's argument from his justifiably famous paper [Risk Aversion and Expected-Utility Theory: A Calibration Theorem](https://doi.org/10.1111/1468-0262.00158) ([pdf](http://dklevine.com/archive/refs47667.pdf)). A more more readable version of this argument was also published in 2001 in [an article by Rabin and Richard Thaler](https://www.aeaweb.org/articles?id=10.1257/jep.15.1.219).

To understand Rabin's point, I have worked through the math in his paper. You can see my  mathematical workings in an Appendix at the bottom of this post. There were quite a few minor errors in the paper - and some major errors in the formulas - but I believe I've captured the crux of the argument. (I'd be grateful for some second opinions on this).

I started working through these two articles with an impression that Rabin's argument was a fatal blow to the idea that expected utility theory accurately describes the rejection of bets such as that above. I would have been comfortable making the above response. However, after playing with the numbers and developing a better understanding of the paper, I would say that the above response is not strictly true. Rabin's paper makes an important point, but it is far from a fatal blow by itself. (That fatal blow does come, just not solely from here.)

##Describing Rabin's argument

Rabin's argument starts with a simple bet: suppose you are offered a 50:50 bet to win \$110 or lose \$100, and you turn it down. Suppose further that you would reject this bet no matter what your wealth (this is an assumption we will turn to in more detail later). What can you infer about your response to other bets?

This depends on what decision making model you are using.

For an expected utility maximiser - someone who maximises the probability weighted subjective value of these bets - we can infer that they will turn down any 50:50 bet of losing \$1,000 and gaining any amount of money. For example, they would reject a 50:50 bet to lose \$1,000, win one billion dollars.

On its face value, that is ridiculous, and that is the crux of Rabin's argument. Rejection of the low value bet to win \$110 and lose \$100 would lead to absurd responses to higher value bets. This leads Rabin to argue that risk aversion or the diminishing value of money has nothing to do with rejection of the low value bets.

The intuition behind Rabin's argument is relatively simple. Suppose we have someone that rejects a 50:50 bet for gain \$11, lose \$10. They are an expected utility maximiser with a weakly concave utility curve: that is, they are risk neutral or risk averse at all levels of wealth.

From this, we can infer that they weight the average of each dollar between their current wealth (W) and their wealth if they win the bet (W+11) only 10/11 as much as they weight the average dollar of the last \$10 of their current wealth (between W-10 and W). We can also say that they therefore weight their W+11th dollar at most 10/11 as much as their W-10th dollar (relying on the weak concavity here).

Suppose their wealth is now W+21. We have assumed that they will reject the bet at all levels of wealth, so they will also reject at this wealth. Iterating the previous calculations, we can say that they will weight their W+32nd dollar only 10/11 as much as their W+11th dollar. This means they value their W+32nd dollar only (10/11)<sup>2</sup> as much as their W-10th dollar.

Keep iterating in this way and you end up with some ridiculous results. You value the 210th dollar above your current wealth only 40% as much as your last current dollar of your wealth [reducing by a constant factor of 10/11 every \$21 - (10/11)<sup>10</sup>]. Or you value the 900th dollar above your current wealth at only 2% of your last current dollar [(10/11)<sup>40</sup>]. This is an absurd rate of discounting.

Those numbers are from the 2001 Rabin and Thaler paper. In his 2000 paper, Rabin gives figures of 3/20 for the 220th and 1/2000 for the 880th dollar, effectively calculating (10/11)<sup>20</sup> and (10/11)<sup>80</sup>, which is a reduction by a factor of 10/11 every 11 dollars. This degree of discounting could be justified and reflects the equations provided in the Appendix to his paper, but it requires a slightly different intuition than the one relating to the comparison between every 21st dollar. If instead you note that the \$11 above a reference point are valued less than the \$10 below, you only need iterate up \$11 to get another discount of 10/11, as the next \$11 is valued at most as much as the previous \$10.

Regardless of whether you use the numbers from the 2000 or 2001 paper, taking this iteration to the extreme, it doesn't take long for additional money to have effectively zero value. Hence the result, reject the 50:50 win \$110, lose \$100 and you'll reject the win any amount, lose \$1,000 bet.

##What is the utility curve of this person?

This argument sounds compelling, but we need to examine the assumption that you will reject the bet at all levels of wealth.

If someone rejects the bet at all levels of wealth, what is the least risk averse they could be? They would be close to indifferent to the bet at all levels of wealth. If that was the case across the whole utility curve, their absolute level of risk aversion is constant.

The equation used to represent utility with constant absolute risk aversion is [exponential utility](https://en.wikipedia.org/wiki/Exponential_utility) (with a>0). A feature of the exponential utility function is that, for a risk averse person, utility caps out at a maximum. Beyond a certain level of wealth, they gain no additional utility - hence Rabin's ability to define bets where they reject infinite gains.

The need for utility to cap out is also apparent from the fact that someone might reject a bet that involves the potential for infinite gain.  The utility of infinite wealth cannot be infinite, as any bet involving that the potential for infinite utility would be accepted.

In the 2000 paper, Rabin brings the constant absolute risk aversion function into his argument more explicitly when he examines what proportion of their portfolio a person with an exponential utility function would invest in stocks (under some particular return assumptions). There he shows a ridiculous level of risk aversion and states that "While it is widely believed that investors are too cautious in their investment behavior, no one believes they are this risk averse."

However, this effective (or explicit) assumption of constant absolute risk aversion is not particularly well grounded. Most empirical evidence is that people exhibit decreasing absolute risk aversion, not constant. Exponential utility functions are used more for mathematical tractability than for realistically reflecting the decision making processes that people use.

Yet, under Rabin's assumption of rejecting the bet at all levels of wealth, constant absolute risk aversion and a utility function such as the exponential is the most accommodating assumption we can make. While Rabin states that "no one believes they are this risk averse", it's not clear that anyone believes Rabin's underlying assumption either.

This ultimately means that the ridiculous implications for rejecting low-value bets is the result of Rabin's unrealistic assumption of rejecting the bet no matter what their wealth.

##Relaxing the "all levels of wealth" assumption

Rabin is, of course, aware that the assumption of rejecting the bet at all levels of wealth is a weakness, so he provides a further example that applies to someone who only rejects this bet for all levels of wealth below \$300,000.

This generates less extreme, but still clearly problematic bets that the bettor can be inferred to also reject.

For example, consider someone who rejects the 50:50 bet to win \$110, lose \$100 when they have \$290,000 of wealth, and who would also reject that bet up to a wealth of \$300,000. As for the previous example, each time you iterate up \$110, each dollar in that \$110 is valued at most 10/11 of the previous \$110. It takes 90 iterations of \$110 to cover that \$10,000, meaning that a dollar around wealth \$300,000 will be valued only (10/11)<sup>90</sup> (0.02%) of a dollar at wealth \$290,000. Each dollar above \$300,000 is not discounted any further, but by then the damage has already been done, with that money of almost no utility.

For instance, this person will reject a bet of gain \$718,190, lose \$1,000. Again, this person would be out of their mind.

You might now ask whether a person with a wealth of \$290,000 to \$300,000 actually rejects bets of this nature? If not, isn't this just another unjustifiable assumption designed to generate a ridiculous result?

It is possible to make this scenario more realistic. Rabin doesn't mention this in his paper (nor do Rabin and Thaler), but we can generate the same result at much lower levels of wealth. All we need to find is someone who will reject that bet over a range of \$10,000, and still have enough wealth to bear the loss - say someone who will reject that bet up to a wealth of \$11,000. That person will also reject a win \$718,190 lose \$1,000 bet.

Rejection of the win \$110, lose \$100 bet over that range does not seem as unrealistic, and I could imagine a person with that preference existing. If we empirically tested this, we would also need to examine liquid wealth and cash flow, but the example does provide a sense that we could find some people whose rejection of low value bets would generate absurd results under expected utility maximisation.

##The log utility function

Let's compare Rabin's example utility function with a more commonly assumed utility function, that of log utility. Log utility has decreasing absolute risk aversion (and constant relative risk aversion), so is both more empirically defensible and does not generate utility that asymptotes to a maximum like the exponential utility function.

A person with log utility would reject the 50:50 bet to win \$110, lose \$100 up to a wealth of \$1,100. Beyond that, they would accept the bet. So, for log utility we should see most people accept this bet.

A person with log utility will reject some quite unbalanced bets: such as a 50:50 bet to win \$1 million, lose \$90,900, but only up to a wealth of \$100,000, beyond which they would accept. Rejection only occurs when a loss is near ruinous.

The result is that log utility does not generate the types of rejected bets that Rabin labels as ridiculous, but would also fail to provide much of an explanation for the rejection of low-value bets with positive expected value.

##The empirical evidence

Do people actually turn down 50:50 bets of win \$110, lose \$100? Surprisingly, I couldn't find an example of this bet (if someone knows a paper that directly tests this, let me know).

Most examinations of loss aversion examine symmetric 50:50 bets where the potential gain and the loss are the same. They compare a bet centred around 0 (e.g. gain \$100 or lose \$100) and a similar bet in a gain frame (e.g. gain \$100 or gain \$300, or take \$200 for certain). If more people reject the first bet than the latter, then this is evidence of loss aversion.

It makes sense that this is the experimental approach. If the bet is not symmetric, it becomes hard to tease out loss aversion from risk aversion.

However, there is a pattern in the literature that people often reject risky bets with a positive expected value in the ranges explored by Rabin. We don't know a lot about their wealth (or liquidity), but Rabin's illustrative numbers for rejected bets don't seem completely unrealistic. It's the range of wealth over which the rejection occurs that is questionable.

Rather than me floundering around on this point, there are papers that explicitly ask whether we can observe a set of bets for a group of experimental subjects and map a curve to those choices that resembles expected utility.

For instance, [Holt and Laury's 2002 AER paper](https://doi.org/10.1257/000282802762024700) ([pdf](https://econweb.ucsd.edu/~jandreon/Econ264/papers/Holt%20Laury%20AER%202002.pdf)) examined a set of hypothetical and incentivised bets over a range of stakes (finding among other things that hypothetical predictions of their response to incentivised high-stakes bets were not very accurate). They found that if you are flexible about the form of the expected utility function that is used, rejection of small gambles does not result in absurd conclusions on large gambles. The pattern of bets could be made consistent with expected utility, assuming you correctly parameterise the equation. Over subsequent years there was some back and forth on whether this finding was robust [see [here](https://doi.org/10.1257/0002828054201378) ([pdf](http://pdfs.semanticscholar.org/924d/fb5180d98767b630e3ae468da0c166a0890a.pdf?_ga=2.18923384.1759154274.1571603876-1728413697.1571603876)) and [here](https://doi.org/10.1257/0002828054201459) ([pdf](http://home.cerge-ei.cz/ortmann/trentocourse/Holt_Laury_Incentive_Effects_AER_2005.pdf))], but the basic result seemed to hold.

The utility curve that best matched Holt and Laury's experimental findings had increasing relative risk aversion, and decreasing absolute risk aversion. By having decreasing absolute risk aversion, the absurd implications of Rabin's paper are avoided.

Papers such as this suggest that while Rabin's paper makes an important point, its underlying assumptions are not consistent with empirical evidence. It is possible to have an expected utility maximiser reject low value bets without generating ridiculous outcomes.

So what can you infer about our bettor who has rejected the win \$110, lose \$100 bet?

From the argument above, I would say not much. We could craft a utility function to accommodate this bet without leading to ridiculous consequences. I personally feel this defence is laboured (that's a subject for another day), but the bet is not in itself fatal to the argument that they are an expected utility maximiser.

My other posts on loss aversion can be found here:

1. [Kahneman and Tversky's debatable loss aversion assumption](https://jasoncollins.blog/2019/09/10/kahneman-and-tverskys-debatable-loss-aversion-assumption/)
2. [What can we infer about someone who rejects a 50:50 bet to win \$110 or lose \$100? The Rabin paradox explored](https://jasoncollins.blog/2019/11/06/what-can-we-infer-about-someone-who-rejects-a-5050-bet-to-win-110-or-lose-100-the-rabin-paradox-explored/) (this post)
3. [The case against loss aversion](https://jasoncollins.blog/2019/12/05/the-case-against-loss-aversion/)
4. [Ergodicity economics - a primer](https://jasoncollins.blog/2020/01/22/ergodicity-economics-a-primer/)

--

##Appendix

### The utility of a gain

Let's suppose someone will reject a 50:50 bet with gain _g_ and loss _l_ for any level of wealth. What utility will they get from a gain of _x_? Rabin  defines an upper bound of the utility of gaining _x_ to be:

$$U(w+x)-U(w)\leq\sum_{i=0}^{k^{**}(x)}\left(\frac{l}{g}\right)^ir(w)$$

$$k^{**}(x)=int\left(\frac{x}{g}\right)$$

$$r(w)=U(w)-U(w-l)$$

This formula effectively breaks down $x$ into $g$ size components, successively discounting each additional $g$ at $\frac{l}{g}$ of the previous $g$.

You need $k^{**}(x)+1$ lots of $g$ to cover $x$. For instance, if $x$ was 32 and we had a 50:50 bet for win \$11, lose \$10, $\left(\frac{32}{11}\right)=2$. You need 2+1 lots of 11 to fully cover 32. It actually covers a touch more than 32, hence the calculation being for an upper bound.

In the paper, Rabin defines $k^{**}(x)=int\left(\left(\frac{x}{g}\right)+1\right)$ This seems to better capture the required number of $g$ to fully cover $x$, but the iterations in the above formula start at $i=0$. The calculations I run below with my version of the formula replicate Rabin's, supporting the suggestion that the addition of 1 in the paper is an error.

$r(w)$ is shorthand for the amount of utility sacrificed from losing the gamble (i.e. losing $l$). We know that the utility of the gain $g$ is less than this, as the bet is rejected. If we let $r(w)=1$, the equation can be thought of as giving you the maximum utility you could get from the gain  of $x$ relative to the utility of the loss of $l$.

Putting this together, the upper bound of the utility of the possible gain $x$ is therefore less than, first, the upper bound of the relative utility from the first \$11, $\left(\frac{10}{11}\right)^0r(w)=r(w)$, the upper bound of utility from the next \$11, $\left(\frac{10}{11}\right)^1r(w)$, and the upper bound of the utility from the remaining \$10 - taking a conservative approach this is calculated as though it were a full \$11: $\left(\frac{10}{11}\right)^2r(w)$.

### The utility of a loss

Rabin also gives us a lower bound of the utility of a loss of $x$ for this person who will reject a 50:50 bet with gain $g$ and loss $l$ for any level of wealth:

$$U(w)-U(w-x)\geq{2}\sum_{i=1}^{k^{*}(x)}\left(\frac{g}{l}\right)^{i-1}{r(w)}$$

$$k^{*}(x)=int\left(\frac{x}{2l}\right)$$

The intuition behind $k^{*}(x)$ comes from Rabin's desire to provide a relatively uncomplicated proof for the proposition. Effectively, the utility scales down with each step of $g$ by at least $\frac{g}{l}$. Since Rabin wants to express this in terms of losses, he defines $2l\geq{g}\geq{l}$. He can thereby say that utility scales down by at least $\frac{g}{l}$ every 2 lots of $l$.

Othewrwise, the intuition for this loss formula is the same as that for the gain. The summation starts at $i=1$ as this formula is providing a lower bound, so does not require the final iteration to fully cover $x$. The formula is also multiplied by 2 as each iteration covers two lots of $l$, whereby r(w) is for a single span of $l$.

### Running some numbers

The below code implements the above two formulas as a function, calculating the potential utility gain for a win of $G$ or a loss of $L$ for a person who rejects a 50:50 bet win $g$, lose $l$ at all levels of wealth. It then states whether we know the person will reject a win $G$, lose $L$ bet - we can't state they will accept as we have upper and lower bounds of the utility change from the gain and loss.


```r
Rabin_bet <- function(g, l, G, L){

  k_2star <- as.integer(G/g)
  k_star <- as.integer(L/(2*l))

  U_gain <- 0
  for (i in 0:k_2star) {
    U_step <- (l/g)^i
    U_gain <- U_gain + U_step
  }

  U_loss <- 0
  for (i in 1:k_star) {
    U_step <- 2*(g/l)^(i-1)
    U_loss <- U_loss + U_step
  }

  ifelse(U_gain < U_loss,
         print("REJECT"),
         print("CANNOT CONFIRM REJECT")
         )
  print(paste0("Max U from gain =", U_gain))
  print(paste0("Min U from loss =", U_loss))
}
```

Take a person who will reject a 50:50 bet to win \$110, lose \$100. Taking the table from the paper, they would reject a win \$1,000,000,000, lose \$1,000 bet.


```r
Rabin_bet(110, 100, 1000000000, 1000)
```

```
[1] "REJECT"
[1] "Max U from gain =11"
[1] "Min U from loss =12.2102"
```

## Relaxing the wealth assumption

In the Appendix of his paper, Rabin defines his proof where the bet is rejected over a range of wealth $w\in(\bar w, \underline{w})$. In that case, relative utility for each additional gain of size $g$ is $\frac{l}{g}$ of the previous $g$ until $\bar w$. Beyond that point, each additional gain of $g$ gives constant utility until $x$ is reached. The formula for the upper bound on the utility gain is:

$$U(w+x)-U(w)\leq
\begin{cases}
&\sum_{i=0}^{k^{**}(x)}\left(\frac{l}{g}\right)^ir(w) & if&\quad x\leq{\bar w}-w\\
\\
&\sum_{i=0}^{k^{**}(\bar w)}\left(\frac{l}{g}\right)^{i}r(w)+\left[\frac{x-(\bar w-w)}{g}\right]\left(\frac{l}{g}\right)^{k^{**}(\bar w)}r(w) & if&\quad x\geq{\bar w}-w
\end{cases}$$  

The first term of the equation where $x\geq\bar w-w$ involves iterated discounting as per the situation where the bet is rejected for all levels of wealth, but here the iteration is only up to wealth $\bar w$. The second term of that equation captures the gain beyond $\bar w$ disounted at a constant rate.

There is an error in Rabin's formula in the paper. Rather than the term $\left[\frac{x-(\bar w-w)}{g}\right]$ in the second equation, Rabin has it as $[x-\bar w]$. As for the previous equations, we need to know the number of iterations of the gain, not total dollars, and we need this between $\bar w$ and $ w+x$.

When Rabin provides the examples in Table II of the paper, from the numbers he provides I believe he actually uses a formula of the type $int\left[\frac{x-(w-\underline w)}{g}+1\right]$, which reflects a desire to calculate the upper-bound utility across the stretch above $\bar w$ in a similar manner to below, although this is not strictly necessary given the discount is constant across this range. I have implemented as per my formula, which means that bets are still rejected $g$ higher than for Rabin (which given their scale is not material).

Similarly, for the loss:

<!-- & placed in equations where want alignment -->
$$U(w)-U(w-x)\geq
\begin{cases}
&{2}\sum_{i=1}^{k^{*}(x)}\left(\frac{g}{l}\right)^{i-1}{r(w)} & if&\quad {w-\underline w+2l}\geq{x}\geq{2l}\\
\\
&{2}\sum_{i=1}^{k^{*}(w-\underline w+2l)}\left(\frac{g}{l}\right)^{i-1}{r(w)}+\\[6pt]
&\quad\left[\frac{x-(w-\underline w+l)}{2l}\right]\left(\frac{g}{l}\right)^{k^{*}(w-\underline w+2l)}{r(w)} & if&\quad x\geq{w-\underline w+2l}
\end{cases}$$

There is a similar error here, with Rabin using the term $\left[x-(w-\underline w+l)\right]$ rather than $\left[\frac{x-(w-\underline w+l)}{2l}\right]$. We can't determine how this was implemented by Rabin as his examples do not examine behaviour below a lower bound $\underline w$.

### Running some more numbers

The below R code implements the above two formulas as a function, calculating the potential utility gain for a win of $G$ or a loss of $L$ for a person who rejects a 50:50 bet win $g$, lose $l$ at wealth $w\in(\bar w, \underline{w})$. It then states whether we know the person will reject a win $G$, lose $L$ bet - as before, we can't state they will accept as we have upper and lower bounds of the utility change from the gain and loss.


```r
Rabin_bet_general <- function(g, l, G, L, w, w_max, w_min){

  ifelse(
    G <= (w_max-w),
    k_2star <- as.integer(G/g),
    k_2star <- as.integer((w_max-w)/g)
  )

   ifelse(
    w-w_min+2*l >= L,
    k_star <- as.integer(L/(2*l)),
    k_star <- as.integer((w-w_min+2*l)/(2*l))
  )

  U_gain <- 0
  for (i in 0:k_2star) {
    U_step <- (l/g)^i
    U_gain <- U_gain + U_step
  }

  ifelse(
    G <= (w_max-w),
    U_gain <- U_gain,
    U_gain <- U_gain + ((G-(w_max-w))/g)*(l/g)^k_2star
  )

  U_loss <- 0
  for (i in 1:k_star) {
    U_step <- 2*(g/l)^(i-1)
    U_loss <- U_loss + U_step
  }

  ifelse(
    w-w_min+2*l >= L,
    U_loss <- U_loss,
    U_loss <- U_loss + ((L-(w-w_min+l))/(2*l))*(g/l)^k_star
  )

  ifelse(U_gain < U_loss,
         print("REJECT"),
         print("CANNOT CONFIRM REJECT")
         )
  print(paste0("Max U from gain =", U_gain))
  print(paste0("Min U from loss =", U_loss))
}
```

Imagine someone who turns down the win \$110, lose \$100 bet with a wealth of $290,000, but who would only reject this bet up to \$300,000. They will reject a win \$718,190, lose \$1000 bet.


```r
Rabin_bet_general(110, 100, 718190, 1000, 290000, 300000, 0)
```

```
[1] "REJECT"
[1] "Max U from gain =12.2098745626936"
[1] "Min U from loss =12.2102"
```

The nature of Rabin's calculation means that we can scale this calculation to anywhere on the wealth curve. We need only say that someone who rejects this bet over (roughly) a range of \$10,000 plus the size of the potential loss will exhibit the same decisions. For example a person with \$10,000 wealth who would reject the bet up to \$20,000 wealth would also reject the win \$718,190, lose $1000 bet.

```r
Rabin_bet_general(110, 100, 718190, 1000, 10000, 20000, 0)
```

```
[1] "REJECT"
[1] "Max U from gain =12.2098745626936"
[1] "Min U from loss =12.2102"
```

### Comparison with log utility

The below is an example with log utility, which is $U(W)=ln(W)$. This function determines whether someone of wealth $w$ will reject of accepta 50:50 bet for gain $g$ and loss $l$.

```r
log_utility <- function(g, l, w){
  log_gain <- log(w+g)
  log_loss <- log(w-l)
  EU_bet <- 0.5*log_gain + 0.5*log_loss
  EU_certain <- log(w)

  if(EU_certain == EU_bet){
    print("INDIFFERENT")
  } else if(EU_certain > EU_bet){
    print("REJECT")
  } else if(EU_certain < EU_bet){
    print("ACCEPT")
  }

  print(paste0("Expected utility of bet = ", EU_bet))
  print(paste0("Utility of current wealth = ", EU_certain))
}
```

Testing a few numbers, someone with log utility is indifferent about a 50:50 win \$110, lose \$100 bet at wealth \$1100. They would accept for any level of wealth above that level.

```r
log_utility(110, 100, 1100)
```

```
[1] "INDIFFERENT"
[1] "Expected utility of bet = 7.00306545878646"
[1] "Utility of current wealth = 7.00306545878646"
```

That same person will always accept a 50:50 win \$1100, lose \$1000 bet above \$11,000 in wealth.

```r
log_utility(1100, 1000, 11000)
```

```
[1] "ACCEPT"
[1] "Expected utility of bet = 9.30565055178051"
[1] "Utility of current wealth = 9.30565055178051"
```

Can we generate any bets that don't seem quite right? It's quite hard unless you have a bet that will bring the person to ruin or near ruin. For instance, for a 50:50 bet with a chance to win \$1 million, a person with log utility and \$100,000 wealth would still accept the bet with a potential loss of \$90,900, which brings them to less than 10% of their wealth.

```r
log_utility(1000000, 90900, 100000)
```

```
[1] "ACCEPT"
[1] "Expected utility of bet = 11.5134252151368"
[1] "Utility of current wealth = 11.5129254649702"
```

The problem with log utility is not the ability to generate ridiculous bets that would be rejected. Rather, it's that someone with log utility would tend to accept most positive value bets (in fact, they would always take a non-zero share if they could). Only if the bet brings them near ruin (either through size or their lack of wealth) would they turn down the bet.

The isoelastic utility function - of which log utility is a special case - is a broader class of function that exhibits constant relative risk aversion:

$$U(x)=\frac{w^{1-\rho}-1}{1-\rho}$$
If $\rho=1$, this simplifies to log utility (you need to use L'Hopital's rule to get this as the fraction is undefined when $\rho=1$.) The higher $\rho$, the higher the level of risk aversion. We implement this function as follows:

```r
CRRA_utility <- function(g, l, w, rho=2){

  if(rho==1){
    print("function undefined")
  }

  log_gain <- ((w+g)^(1-rho)-1)/(1-rho)
  log_loss <- ((w-l)^(1-rho)-1)/(1-rho)

  EU_bet <- 0.5*log_gain + 0.5*log_loss
  EU_certain <- (w^(1-rho)-1)/(1-rho)

  if(EU_certain == EU_bet){
    print("INDIFFERENT")
  } else if(EU_certain > EU_bet){
    print("REJECT")
  } else if(EU_certain < EU_bet){
    print("ACCEPT")
  }
  
  print(paste0("Expected utility of bet = ", EU_bet))
  print(paste0("Utility of current wealth = ", EU_certain))
}
```

If we increase $\rho$, we can increase the proportion of low value bets that are rejected.

For example, a person with $\rho=2$ will reject the 50:50 win \$110, lose \$100 bet up to a wealth of \$2200. The rejection point scales with $\rho$.

```r
CRRA_utility(110, 100, 2200, 2)
```

```
[1] "INDIFFERENT"
[1] "Expected utility of bet = 0.999545454545455"
[1] "Utility of current wealth = 0.999545454545455"
```

For a 50:50 chance to win \$1 million at wealth \$100,000, the person with $\rho=2$ is willing to risk a far smaller loss, and rejects even when the loss is only $48,000, or less than half their wealth (which admittedly is still a fair chunk).

```r
CRRA_utility(1000000, 48000, 100000, 2)
```

```
[1] "REJECT"
[1] "Expected utility of bet = 0.99998993006993"
[1] "Utility of current wealth = 0.99999"
```

Higher values of $\rho$ start to become completely unrealistic as utility is almost flat beyond an initial level of wealth.

It is also possible to have values of $\rho$ between 0 (risk neutrality) and 1. These would result in even fewer rejected low value bets than log utility, and fewer rejected bets with highly unbalanced potential gains and losses.
