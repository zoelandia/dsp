[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> About 34% of the U.S. male population is eligible to be in Blue Man Group.

import scipy

def EvalNormalCdf(x, mu=178, sigma=7.7):
    return scipy.stats.norm.cdf(x, loc=mu, scale=sigma)

def ConvertCm(x):
    return x * 2.54

blue_max = ConvertCm(12 * 6 + 1)
blue_min = ConvertCm(12 * 5 + 10)

print(round((EvalNormalCdf(blue_max) - EvalNormalCdf(blue_min)) * 100, 3))

# It turns out that roughly 34% of the U.S. male population is height-eligible to be part of Blue Man Group. My answer is slightly lower than the answer given in ThinkStats2, probably due to the slightly different order in which we computed things.
