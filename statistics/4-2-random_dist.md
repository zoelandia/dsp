[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> No, the distribution is not perfectly uniform...

import random

randos = []
for i in range(1000):
    randos.append(random.random())

pmf_randos = thinkstats2.Pmf(randos, label="PMF")
thinkplot.Pmf(pmf_randos)
thinkplot.Show(xlabel='random number', ylabel="PMF")

cdf_randos = thinkstats2.Cdf(randos, label='CDF')
thinkplot.Cdf(cdf_randos)
thinkplot.Show(xlabel='random number', ylabel='CDF')

# Because random.random() generates floats to a LOT of decimal places, my 1000 random numbers are extremely well distributed. Because the PMF appears as a solid block, we might think that the numbers were uniform (although not even possible with so many decimal places and only 1000 numbers). However, the PMF is not a perfectly straight line, showing that the numbers were not exactly equally distributed between 0 and 1.

randos = []
for i in range(1000):
    randos.append(round(random.random(), 5))

pmf_randos = thinkstats2.Pmf(randos, label="PMF")
thinkplot.Pmf(pmf_randos)
thinkplot.Show(xlabel='random number', ylabel="PMF")

cdf_randos = thinkstats2.Cdf(randos, label='CDF')
thinkplot.Cdf(cdf_randos)
thinkplot.Show(xlabel='random number', ylabel='CDF')

# Limiting to five decimal places: the CDF looks the same (as it should; there are still 1000 random numbers), but the PMF shows that there were now some repeated numbers and some numbers that did not occur at all.

randos = []
for i in range(1000):
    randos.append(round(random.random(), 3))

pmf_randos = thinkstats2.Pmf(randos, label="PMF")
thinkplot.Pmf(pmf_randos)
thinkplot.Show(xlabel='random number', ylabel="PMF")

cdf_randos = thinkstats2.Cdf(randos, label='CDF')
thinkplot.Cdf(cdf_randos)
thinkplot.Show(xlabel='random number', ylabel='CDF')

# With three decimal places we could have seen each number from 0 to 1 (inclusive) occur exactly once; instaed, we can really see from the PDF the not-quite-uniform distribution.

randos = []
for i in range(1000):
    randos.append(round(random.random(), 1))

pmf_randos = thinkstats2.Pmf(randos, label="PMF")
thinkplot.Pmf(pmf_randos)
thinkplot.Show(xlabel='random number', ylabel="PMF")

cdf_randos = thinkstats2.Cdf(randos, label='CDF')
thinkplot.Cdf(cdf_randos)
thinkplot.Show(xlabel='random number', ylabel='CDF')

# One decimal place, just for comparison.
