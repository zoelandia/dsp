[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> The mean number of children in a household is 1.024, compared to a biased mean of 2.404.

import thinkplot
import thinkstats2
import nsfg
import math

resp = nsfg.ReadFemResp()

numkdhh = resp.numkdhh
print(numkdhh.value_counts())

hist = thinkstats2.Hist(numkdhh)
print(hist)

pmf_numkdhh = thinkstats2.Pmf(numkdhh, label='actual')
print(pmf_numkdhh)

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        new_pmf.Normalize()
    return new_pmf

biased_pmf_numkdhh = BiasPmf(pmf_numkdhh, label='observed')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_numkdhh, biased_pmf_numkdhh])
thinkplot.Show(xlabel='children in household', ylabel='PMF')

print('Actual mean number of children: ', round(pmf_numkdhh.Mean(), 3), 'vs. Biased mean number of children: ', round(biased_pmf_numkdhh.Mean(), 3))
