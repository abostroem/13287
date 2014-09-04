from astropy.io import fits
from matplotlib import pyplot
import numpy as np
from datetime import datetime
from astropy.convolution import convolve, Box1DKernel

def label_spectra(ax):
	'''
	With a dictionary of SN spectral features, plot each feature a its wavelength making
	each species a different color

	Input:
		ax: subplot object
			object to plot lines onto

	'''
	line_list = {'Mg':[2796, 2802], 'SiIII/CIII':[1883, 1892, 1906, 1909],
				 'NIII':[1747, 1753], 'OIII':[1661, 1666], 'CIV':[1549, 1551],
				 'NIV':[1483, 1488], 'HeII':[1640], 'NeIII':[1815], 'NV':[1240],
				 'SiIV':[1394, 1403], 'CII':[2322, 2329]}

	colors = ['r', 'orange', 'gold', 'g', 'c', 'purple', 'lime', 'pink', 'brown', 'grey', 'm']
	for color_indx, elem in enumerate(line_list.keys()):
		for iline in line_list[elem]:
			ax.axvline(iline, color = colors[color_indx])
		ax.axvline(iline, color = colors[color_indx], label = elem)
		ax.legend()
	return ax

def add_date_to_plot(ax):
    today = datetime.today()
    xlims = ax.get_xlim()
    ylims = ax.get_ylim()
    ax.text(xlims[1], -.06*(ylims[1] - ylims[0])+ylims[0], '{}-{}-{}'.format(today.year, today.month, today.day))

def deredshift_wavelength(wavelength, redshift):
	deredshift_wl = wavelength/(redshift + 1.0)
	return deredshift_wl

def plot_2010jl():
	'''
	Create a plot of the combined NUV and FUV spectrum of SN 2010jl, label the common SN
	lines with different colors for different species and save
	'''
	redshift = 0.0107 #http://www.astronomy.ohio-state.edu/~stoll/stoll2011.pdf
	tbdata = fits.getdata('2010jl_all_x1dsum.fits', 1)
	sdqflags = fits.getval('2010jl_all_x1dsum.fits', 'sdqflags', 1)
	good_indx = np.where(tbdata['dq'][0]&sdqflags == 0)

	fig = pyplot.figure(figsize = [20, 10])
	ax = fig.add_subplot(1,1,1)
	deredshift_wl = deredshift_wavelength(tbdata['wavelength'][0][good_indx], redshift)
	smoothed_signal = convolve(tbdata['flux'][0][good_indx], Box1DKernel(15))

	ax.plot(deredshift_wl, smoothed_signal, 'b')
	ax = label_spectra(ax)
	ax.set_xlabel('Rest Wavelength ($\AA$)')
	ax.set_ylabel('Flux (ergs/cm^2/s/$\AA$)')
	ax.set_title('Preliminary HST/STIS Spectrum of SN 2010jl (smoothed by 15 pix)')
	ax.set_ylim(0, 0.25E-15)
	add_date_to_plot(ax)
	pyplot.savefig('2010jl_combined_labeled.pdf')

def plot_2005ip():
	'''
	Create a plot of the combined NUV and FUV spectrum of SN 2010jl, label the common SN
	lines with different colors for different species and save
	'''
	redshift = 0.0072
	tbdata = fits.getdata('2005ip_all_x1dsum.fits', 1)
	sdqflags = fits.getval('2005ip_all_x1dsum.fits', 'sdqflags', 1)
	good_indx = np.where(tbdata['dq'][0]&sdqflags == 0)

	fig = pyplot.figure(figsize = [20, 10])
	ax = fig.add_subplot(1,1,1)
	deredshift_wl = deredshift_wavelength(tbdata['wavelength'][0][good_indx], redshift)
	smoothed_signal = convolve(tbdata['flux'][0][good_indx], Box1DKernel(15))

	ax.plot(deredshift_wl, smoothed_signal, 'b')
	ax = label_spectra(ax)
	ax.set_xlabel('Rest Wavelength ($\AA$)')
	ax.set_ylabel('Flux (ergs/cm^2/s/$\AA$)')
	ax.set_title('Preliminary HST/STIS Spectrum of SN 2005ip (smoothed by 15 pix)')
	ax.set_ylim(-0.1E-15, 0.25E-15)
	add_date_to_plot(ax)
	pyplot.savefig('2005ip_combined_labeled.pdf')

if __name__ == "__main__":
	#plot_2010jl()
	plot_2005ip()