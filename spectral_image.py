# use this to create a spectral image 
# python3 spectral_image.py 'path/to/image1' 'path/to/image2' 'path/to/spectral/image'

from astropy.io import fits
import sys
import numpy as np

s1_image = sys.argv[1]
s2_image = sys.argv[2]

output_image = sys.argv[3]

s1 = fits.open(s1_image)[0].data 
s2 = fits.open(s2_image)[0].data 

# mask = np.where(s1>0, True, False)*np.where(s2>0, True, False)
# # s1_masked=s1[fits.open[maskfile][0].data]
# s1_masked = s1[mask]
# s2_masked = s2[mask]

nu1 = fits.open(s1_image)[0].header['CRVAL3']
nu2 = fits.open(s2_image)[0].header['CRVAL3']

alpha = np.log(s2/s1)/np.log(nu2/nu1)

hdu = fits.PrimaryHDU(data=alpha)

hdul = fits.HDUList([hdu])
hdul.writeto(output_image, overwrite=True)
