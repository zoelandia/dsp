# Hint:  use Google to find python function

import datetime
import time

def diff(time1, time2, format):
    start_conv = datetime.datetime.strptime(time1, format)
    stop_conv = datetime.datetime.strptime(time2, format)
    print(stop_conv - start_conv)

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

diff(date_start, date_stop, '%m-%d-%Y')

####b)
date_start = '12312013'
date_stop = '05282015'

diff(date_start, date_stop, '%m%d%Y')

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

diff(date_start, date_stop, '%d-%b-%Y')
