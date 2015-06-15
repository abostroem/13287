from astropy.io import fits
from matplotlib import pyplot
import os
import glob
import numpy as np
import pdb

from helper_functions import add_date_to_plot


def plot_indiv_spec_with_combined(indiv_filename, combined_filename):
	'''
	Plot each file individually with the combined spectrum to make sure one doesn't look
	very different from the others
	'''
	tbdata_indiv = fits.getdata(indiv_filename, 1)
	tbdata_combined = fits.getdata(combined_filename, 1)

	fig = pyplot.figure()
	ax = fig.add_subplot(1,1,1)

	sdqflags = fits.getval(indiv_filename, 'sdqflags', 1)
	good_indx = np.where(tbdata_indiv['dq'][0]&sdqflags == 0)

	ax.plot(tbdata_indiv['wavelength'][0][good_indx], tbdata_indiv['flux'][0][good_indx], label = 'indiv obs')
	ax.plot(tbdata_combined['wavelength'][0], tbdata_combined['flux'][0], 'r', label = 'combined')
	ax.legend(loc = 'best')
	ax.set_xlabel('Wavelength')
	ax.set_ylabel('Flux')
	add_date_to_plot(ax)
	ax.set_title('Compare Indiv Spec to Combine Spec: {}'.format(os.path.basename(indiv_filename)[0:9]))
	pyplot.savefig(indiv_filename.replace('x1d.fits', 'comb_spec_comp.pdf'))
	pyplot.close()

#----------------------------

def plot_2010jl_fuv():
	'''
	Make plots for 2010JL FUV
	'''
	flist = glob.glob('2010jl_loc_340_hgt_21/*x1d.fits')
	combined_file = '2010jl_loc_340_hgt_21/2010jl_fuv_x1dsum.fits'
	for ifile in flist:
		plot_indiv_spec_with_combined(ifile, combined_file)

#----------------------------

def plot_2010jl_nuv():
	'''
	Make plots for 2010JL NUV
	'''
	flist = glob.glob('2010jl_loc_461_hgt_21/*x1d.fits')
	combined_file = '2010jl_loc_461_hgt_21/2010jl_nuv_x1dsum.fits'
	for ifile in flist:
		plot_indiv_spec_with_combined(ifile, combined_file)

#----------------------------

def plot_2005ip_fuv():
	'''
	Make plots for 2005ip FUV
	'''
	flist = ['2005ip_otfr/ocdd02010_x1d.fits',
			'2005ip_otfr/ocdd02020_x1d.fits',
			'2005ip_otfr/ocdd02030_x1d.fits',
			'2005ip_otfr/ocdd02040_x1d.fits',
			'2005ip_otfr/ocdd02050_x1d.fits',
			'2005ip_otfr/ocdd02060_x1d.fits',
			'2005ip_otfr/ocdd02070_x1d.fits',
			'2005ip_otfr/ocdd02080_x1d.fits']
	combined_file = '2005ip_otfr/2005ip_fuv_x1dsum.fits'
	for ifile in flist:
		plot_indiv_spec_with_combined(ifile, combined_file)

#----------------------------

def plot_2005ip_nuv():
	'''
	Make plots for 2005ip NUV
	'''
	flist = ['2005ip_otfr/ocdd02090_x1d.fits',
			'2005ip_otfr/ocdd020a0_x1d.fits',
			'2005ip_otfr/ocdd020b0_x1d.fits',
			'2005ip_otfr/ocdd020c0_x1d.fits']
	combined_file = '2005ip_otfr/2005ip_nuv_x1dsum.fits'
	for ifile in flist:
		plot_indiv_spec_with_combined(ifile, combined_file)
#----------------------------
#----------------------------

def plot_2009ip_fuv():
	'''
	Make plots for 2009ip FUV
	'''
	flist = ['2009ip_otfr/ocdd01010_x1d.fits',
			'2009ip_otfr/ocdd01010_x1d.fits',
			'2009ip_otfr/ocdd01020_x1d.fits',
			'2009ip_otfr/ocdd01030_x1d.fits',
			'2009ip_otfr/ocdd01040_x1d.fits',
			'2009ip_otfr/ocdd01050_x1d.fits',
			'2009ip_otfr/ocdd01060_x1d.fits',
			'2009ip_otfr/ocdd01070_x1d.fits',
			'2009ip_otfr/ocdd01080_x1d.fits']
	combined_file = '2009ip_otfr/2009ip_fuv_x1dsum.fits'
	for ifile in flist:
		plot_indiv_spec_with_combined(ifile, combined_file)

#----------------------------

def plot_2009ip_nuv():
	'''
	Make plots for 2009ip NUV
	'''
	flist = ['2009ip_otfr/ocdd02090_x1d.fits',
			'2009ip_otfr/ocdd020a0_x1d.fits',
			'2009ip_otfr/ocdd020b0_x1d.fits',
			'2009ip_otfr/ocdd020c0_x1d.fits']
	combined_file = '2009ip_otfr/2009ip_nuv_x1dsum.fits'
	for ifile in flist:
		plot_indiv_spec_with_combined(ifile, combined_file)
#----------------------------
#----------------------------

if __name__ == "__main__":
	plot_2010jl_fuv()
	plot_2010jl_nuv()
	plot_2005ip_fuv()
	plot_2005ip_nuv()
	plot_2009ip_fuv()
#	plot_2009ip_nuv()
