import matplotlib.pyplot as plt
import numpy as np
import ehtim as eh
import ehtim.modeling.hybrid_utils as hu
import ehtim.imaging.dynamical_imaging as di
from   ehtim.calibrating import self_cal as sc
# Sample array
eht = eh.array.load_txt('../arrays/EHT2019.txt')
ALMAmoon = eh.array.load_txt('../arrays/ALMA_moon.txt')
ALMASEL2 = eh.array.load_txt('../arrays/ALMA_SEL2.txt')
arrs = [ALMAmoon, ALMASEL2]
names = ['ALMA_moon','ALMASEL2']

# Load an image
sgra = eh.image.load_txt('../models/jason_mad_eofn.txt')
m87 = eh.image.load_txt('../models/avery_m87_1_eofn.txt')
# Note: this is an example sequence of commands to run in ipython
# The matplotlib windows may not open/close properly if you run this directly as a script

# Look at the image
# im.display()
sources = [sgra,m87]
sourcenames = ['sgra','m87']

# Observe the image
# tint_sec is the integration time in seconds, and tadv_sec is the advance time between scans
# tstart_hr is the GMST time of the start of the observation and tstop_hr is the GMST time of the end
# bw_hz is the  bandwidth in Hz
# sgrscat=True blurs the visibilities with the Sgr A* scattering kernel for the appropriate image frequency
# ampcal and phasecal determine if gain variations and phase errors are included
tint_sec = 30
tadv_sec = 3.1*60*60#one observation every 3.1 hours
tstart_hr = 0
tstop_hr = 24*14#observe for two weeks
bw_hz = 4e9
for i in range(len(names)):
  name = names[i]
  arr = arrs[i]
    
  for j in range(len(sourcenames)):
    im = sources[j]
    sourcename = sourcenames[j]
    obs = im.observe(arr, tint_sec, tadv_sec, tstart_hr, tstop_hr, bw_hz,
                     sgrscat=False, ampcal=True, phasecal=False, elevmin=-90,elevmax=90)

    # You can deblur the visibilities by dividing by the scattering kernel if necessary
    #obs = obs.deblur()

    # These are some simple plots you can check
    # obs.plotall('u','v', conj=True) # uv coverage
    # obs.plotall('uvdist','amp') # amplitude with baseline distance'
    # obs.plot_bl('SMA','ALMA','phase') # visibility phase on a baseline over time

    # obs.plotall('u','v',conj=True)

    # Export the visibility data to uvfits/text
    # obs.save_txt('obs.txt') # exports a text file with the visibilities
    # obs.mjd = float(obs.mjd)
    obs.save_txt(name+'_'+sourcename+'_mjd'+str(obs.mjd)+'_14dayobs.txt') # exports a UVFITS file modeled on template.UVP
    obs.plotall('u','v',conj=True)
    # # Generate an image prior
    # npix = 32
    # fov = 1*im.fovx()
    # zbl = im.total_flux() # total flux
    # prior_fwhm = 200*eh.RADPERUAS # Gaussian size in microarcssec
    # emptyprior = eh.image.make_square(obs, npix, fov)
    # flatprior = emptyprior.add_flat(zbl)
    # gaussprior = emptyprior.add_gauss(zbl, (prior_fwhm, prior_fwhm, 0, 0, 0))

    # # Image total flux with bispectrum
    # flux = zbl
    # out  = eh.imager_func(obs, gaussprior, gaussprior, flux,
    #                       d1='bs', s1='simple',
    #                       alpha_s1=1, alpha_d1=100,
    #                       alpha_flux=100, alpha_cm=50,
    #                       maxit=100, ttype='nfft',show_updates=False)

    # # Blur the image with a circular beam and image again to help convergance
    # out = out.blur_circ(res)
    # out = eh.imager_func(obs, out, out, flux,
    #                 d1='bs', s1='tv',
    #                 alpha_s1=1, alpha_d1=50,
    #                 alpha_flux=100, alpha_cm=50,
    #                 maxit=100,ttype='nfft',show_updates=False)

    # out = out.blur_circ(res/2.0)
    # out = eh.imager_func(obs, out, out, flux,
    #                 d1='bs', s1='tv',
    #                 alpha_s1=1, alpha_d1=10,
    #                 alpha_flux=100, alpha_cm=50,
    #                 maxit=100,ttype='nfft',show_updates=False)


    # # Self - calibrate and image with vis amplitudes
    # obs_sc = sc.self_cal(obs, out)

    # out_sc = out.blur_circ(res)
    # out_sc = eh.imager_func(obs_sc, out_sc, out_sc, flux,
    #                    d1='vis', s1='simple',
    #                    alpha_s1=1, alpha_d1=100,
    #                    alpha_flux=100, alpha_cm=50,
    #                    maxit=50,ttype='nfft',show_updates=False)


    # # Compare the visibility amplitudes to the data
    # out = out_sc
    # # eh.comp_plots.plotall_obs_im_compare(obs, out,'uvdist','amp', clist=['b','m'],conj=True)

    # # Blur the final image with 1/2 the clean beam
    # outblur = out.blur_gauss(beamparams, 0.5)
    # out.display()

    # # Save the images
    # outname = name
    # out.save_txt(outname + '.txt')
    # out.save_fits(outname + '.fits')
    # outblur.save_txt(outname + '_blur.txt')
    # outblur.save_fits(outname + '_blur.fits')


