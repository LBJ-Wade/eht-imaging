import numpy as np
import matplotlib.pyplot as plt
import ehtim as eh

#load an image to observe, and load the EHT 2017 array with the ISS added
im = eh.image.load_txt('../models/avery_sgra_eofn.txt')
eht_iss = eh.array.load_txt('../arrays/EHT2017_ISS.txt')


# Observe the image
# tint_sec is the integration time in seconds, and tadv_sec is the advance time between scans
# tstart_hr is the GMST time of the start of the observation and tstop_hr is the GMST time of the end
# bw_hz is the  bandwidth in Hz
# sgrscat=True blurs the visibilities with the Sgr A* scattering kernel for the appropriate image frequency
# ampcal and phasecal determine if gain variations and phase errors are included
tint_sec = 5
tadv_sec = 60
tstart_hr = 0
tstop_hr = 24
bw_hz = 4e9
obs = im.observe(eht_iss, tint_sec, tadv_sec, tstart_hr, tstop_hr, bw_hz,
                 sgrscat=False, ampcal=True, phasecal=False, ttype='fast', mjd=57962)

obs.plotall('u','v',conj=True)

ALMA_moon = eh.array.load_txt('../arrays/ALMA_moon.txt')
#now generate 2 weeks of data with alma_moon, observed once per day
tint_sec = 5
tadv_sec = 60*60*24#one day
tstart_hr = 0
tstop_hr = 24*14#fourteen days
bw_hz = 4e9
obs = im.observe(ALMA_moon, tint_sec, tadv_sec, tstart_hr, tstop_hr, bw_hz,
                 sgrscat=False, ampcal=True, phasecal=False, ttype='fast', mjd=57962, elevmin=-90, elevmax=90)
obs.plotall('u','v',conj=True)

ALMA_SEL2 = eh.array.load_txt('../arrays/ALMA_SEL2.txt')
#lastly, let's observe 6 months with alma_SEL2, observed once per week
tint_sec = 5
tadv_sec = 60*60*24*7#one week
tstart_hr = 0
tstop_hr = 24*14*2*6#24 weeks ~= 6 months
bw_hz = 4e9
obs = im.observe(ALMA_SEL2, tint_sec, tadv_sec, tstart_hr, tstop_hr, bw_hz,
                 sgrscat=False, ampcal=True, phasecal=False, ttype='fast', mjd=57962, elevmin=-90, elevmax=90)
obs.plotall('u','v',conj=True)


#one test of the code is see if a large declination source sees a more circular coverage.
#this should be approximately true for all observations, since the L2 and lunar orbital planes are roughly parallel,
#as is the plane pierced by the Earth's rotation axis. Thanks to solar system evolution for keeping things easy!
im.dec = 89


tint_sec = 5
tadv_sec = 60
tstart_hr = 0
tstop_hr = 24
bw_hz = 4e9
obs = im.observe(eht_iss, tint_sec, tadv_sec, tstart_hr, tstop_hr, bw_hz,
                 sgrscat=False, ampcal=True, phasecal=False, ttype='fast', mjd=57962)

obs.plotall('u','v',conj=True)

#now generate 2 weeks of data with alma_moon, observed once per day
tint_sec = 5
tadv_sec = 60*60*24#one day
tstart_hr = 0
tstop_hr = 24*14#fourteen days
bw_hz = 4e9
obs = im.observe(ALMA_moon, tint_sec, tadv_sec, tstart_hr, tstop_hr, bw_hz,
                 sgrscat=False, ampcal=True, phasecal=False, ttype='fast', mjd=57962, elevmin=-90, elevmax=90)
obs.plotall('u','v',conj=True)

#lastly, let's observe 6 months with alma_SEL2, observed once per week
tint_sec = 5
tadv_sec = 60*60*24*7#one week
tstart_hr = 0
tstop_hr = 24*14*2*6#24 weeks ~= 6 months
bw_hz = 4e9
obs = im.observe(ALMA_SEL2, tint_sec, tadv_sec, tstart_hr, tstop_hr, bw_hz,
                 sgrscat=False, ampcal=True, phasecal=False, ttype='fast', mjd=57962, elevmin=-90, elevmax=90)
obs.plotall('u','v',conj=True)




