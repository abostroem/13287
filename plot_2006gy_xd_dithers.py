from matplotlib import pyplot
import numpy as np
import os
import glob
from astropy.io import fits
from matplotlib.backends.backend_pdf import PdfPages


def plot_norm_fuv_xd_profile(dither_pos, flist):
	'''
	Plot the XD profile of each dataset taken at each dither position
	(3 datasets per plot, 1 plot (one for each dither position)

	The SN is located at y = 511 in the first dither position and offset relative to
	that position

	Inputs:
		dither_pos: int
			dither position (possible values 1, 2, 3, 4)
		flist: list
			list of flt files for the FUV MAMA

	'''
	plate_scale = 0    #(No dithers. Previously 40.65)
	sn_loc_at_dither1 = 509.#331.0
	fig = pyplot.figure(figsize = [10, 5])
	ax1 = fig.add_subplot(1,2,1)
	ax2 = fig.add_subplot(1,2,2)
	ax1.set_title('Cross Dispersion Profile for Dither position #{} 2006gy'.format(dither_pos))
	ax2.set_title('Zoom on SN position')

	for ifile in flist[dither_pos-1::1]:
		if fits.getval(ifile, 'opt_elem', 0) == 'G430L':
			img = fits.getdata(ifile, 1)
			ax1.plot(np.median(img, axis = 1), np.arange(1024), label = os.path.basename(ifile)[0:9])
			#Dither pattern is 1 arcsec offset = plate_scale pix on FUV MAMA
			for i in range(0,0):
				if i == dither_pos-1:
					ax1.axhline(sn_loc_at_dither1 + (dither_pos-1.0)*plate_scale, color = 'k', ls = '--', label = 'SN this dither')
				else:
					ax1.axhline(sn_loc_at_dither1 + (i)*plate_scale, color = 'k', ls = ':', label = 'SN other dithers')
			ax1.set_ylim(0,1400)
			xlimits = ax1.get_xlim()
			ax1.set_xlim(0.5, xlimits[1])

			#Zoom in
			ax2.plot(np.median(img, axis = 1), np.arange(1024), label = os.path.basename(ifile)[0:9])
			ax2.axhline(sn_loc_at_dither1+(dither_pos-1.0)*plate_scale, color = 'k', ls = '--')
			ax2.set_ylim(sn_loc_at_dither1-40+(dither_pos-1.0)*plate_scale,sn_loc_at_dither1+60.0+(dither_pos-1.0)*plate_scale)
			ax2.set_xlim(0.5, xlimits[1])
			ax2.legend()
	return fig

#----------------------------

def plot_norm_nuv_xd_profile(dither_pos, flist):
	'''
	Plot the XD profile of each dataset taken at each dither position
	(2 datasets per plot, 4 plots (one for each dither position)

	The SN is located at y = 511 in the first dither position and offset relative to
	that position

	median NUV value is negative which inverts the profile if you normalize by it,
		so don't normalize

	Inputs:
		dither_pos: int
			dither position (possible values 1, 2, 3, 4)
		flist: list
			list of flt files for the FUV MAMA

	'''
	plate_scale = 0    #(No dithers. Previously 40.65)
	sn_loc_at_dither1 = 511.
	fig = pyplot.figure(figsize = [10, 5])
	ax1 = fig.add_subplot(1,2,1)
	ax2 = fig.add_subplot(1,2,2)
	ax1.set_title('Cross Dispersion Profile for Dither position #{} 2006gy'.format(dither_pos))
	ax2.set_title('Zoom on SN position')

	for ifile in flist[dither_pos-1::1]:
		if fits.getval(ifile, 'opt_elem', 0) == 'G750L':
			img = fits.getdata(ifile, 1)
			ax1.plot(np.median(img, axis = 1), np.arange(1024), label = os.path.basename(ifile)[0:9])
			#Dither pattern is 1 arcsec offset = plate_scale pix on FUV MAMA
			for i in range(0,0):
				if i == dither_pos-1:
					ax1.axhline(sn_loc_at_dither1 + (dither_pos-1.0)*plate_scale, color = 'k', ls = '--', label = 'SN this dither')
				else:
					ax1.axhline(sn_loc_at_dither1 + (i)*plate_scale, color = 'k', ls = ':', label = 'SN other dithers')
			ax1.set_ylim(0,1400)

			#Zoom in
			ax2.plot(np.median(img, axis = 1), np.arange(1024), label = os.path.basename(ifile)[0:9])
			ax2.axhline(sn_loc_at_dither1+(dither_pos-1.0)*plate_scale, color = 'k', ls = '--')
			ax2.set_ylim(sn_loc_at_dither1-90+(dither_pos-1.0)*plate_scale,sn_loc_at_dither1+110.0+(dither_pos-1.0)*plate_scale)
			ax2.set_xlim(-200, 200)
			ax2.legend(loc = 'best')
	return fig

#----------------------------

def make_fuv_plot():
	'''
	Make one plot per dither position for 2006gy FUV
	'''
	pp = PdfPages('2006gy_xd_profile_for_each_dither_fuv.pdf')
	flist = glob.glob('2006gy/*crj.fits')
	fig1 = plot_norm_fuv_xd_profile(1, flist)
	fig1.savefig(pp, format = 'pdf')
	pp.close()

#----------------------------

def make_nuv_plot():
	'''
	Make one plot per dither position for 2006gy NUV
	'''
	pp = PdfPages('2006gy_xd_profile_for_each_dither_nuv.pdf')
	flist = glob.glob('2006gy/*crj.fits')
	fig1 = plot_norm_nuv_xd_profile(1, flist)
	fig1.savefig(pp, format = 'pdf')
	pp.close()

#----------------------------
#----------------------------
if __name__ == "__main__":
	make_fuv_plot()
	make_nuv_plot()

