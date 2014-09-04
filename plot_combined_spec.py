from astropy.io import fits
from matplotlib import pyplot
import os
import glob
import numpy as np
import pdb

def plot_indiv_spec_with_combined(indiv_filename, combined_filename):
	'''
	Plot each file individually with the combined spectrum to make sure one doesn't look
	very different from the others
	'''
	tbdata_indiv = fits.getdata(indiv_filename, 1)
	tbdata_combined = fits.getdata(combined_filename, 1)

	sdqflags = fits.getval(indiv_filename, 'sdqflags', 1)
	good_indx = np.where(tbdata_indiv['dq'][0]&sdqflags == 0)

	pyplot.plot(tbdata_indiv['wavelength'][0][good_indx], tbdata_indiv['flux'][0][good_indx], label = 'indiv obs')
	pyplot.plot(tbdata_combined['wavelength'][0], tbdata_combined['flux'][0], 'r', label = 'combined')
	pyplot.legend(loc = 'best')
	pyplot.xlabel('Wavelength')
	pyplot.ylabel('Flux')
	pyplot.title('Compare Indiv Spec to Combine Spec: {}'.format(os.path.basename(indiv_filename)[0:9]))
	pyplot.savefig(indiv_filename.replace('x1d.fits', 'comb_spec_comp.pdf'))
	pyplot.close()

def plot_2010jl_fuv():
	flist = glob.glob('2010jl_loc_340_hgt_21/*x1d.fits')
	combined_file = '2010jl_loc_340_hgt_21/2010jl_fuv_x1dsum.fits'
	for ifile in flist:
		plot_indiv_spec_with_combined(ifile, combined_file)

def plot_2010jl_nuv():
	flist = glob.glob('2010jl_loc_461_hgt_21/*x1d.fits')
	combined_file = '2010jl_loc_461_hgt_21/2010jl_nuv_x1dsum.fits'
	for ifile in flist:
		plot_indiv_spec_with_combined(ifile, combined_file)

if __name__ == "__main__":
	plot_2010jl_fuv()
	plot_2010jl_nuv()