[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The difference in birth weight between first babies and later babies has an effect size
(Cohen's D) of -0.089.

# Figure out Cohen's D for the difference in birth weight between first babies and later babies

import thinkplot
import thinkstats2
import nsfg
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

mean_wgt_all = round(live.totalwgt_lb.mean(), 3)
var_wgt_all = round(live.totalwgt_lb.var(), 3)
std_wgt_all = round(live.totalwgt_lb.std(), 3)
print('Mean: ', mean_wgt_all, 'Variance: ', var_wgt_all, 'Standard deviation: ', std_wgt_all)

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)

    return d

mean_firsts = round(firsts.totalwgt_lb.mean(), 3)
mean_others = round(others.totalwgt_lb.mean(), 3)
print('Mean of first babies: ', mean_firsts, 'vs. Mean of other babies: ', mean_others)

d_weight = round(CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb), 3)
print(d_weight)

# Compare to Cohen's D for the difference in pregnancy length

d_prglngth = round(CohenEffectSize(firsts.prglngth, others.prglngth), 3)
print(d_prglngth)

print(round(d_weight/d_prglngth, 3))

# So, first babies differ from later babies more in terms of birthweight than in terms of the length of pregnancy (about three times more).
