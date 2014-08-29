from matplotlib import pyplot
import numpy as np
import os
import glob
from astropy.io import fits
from matplotlib.backends.backend_pdf import PdfPages


def plot_norm_fuv_xd_profile(dither_pos, flist):
	fig = pyplot.figure(figsize = [10, 5])
	ax1 = fig.add_subplot(1,2,1)
	ax2 = fig.add_subplot(1,2,2)
	ax1.set_title('Cross Dispersion Profile for Dither position #{} 2010JL'.format(dither_pos))
	ax2.set_title('Zoom on SN position')

	for ifile in flist[dither_pos-1::4]:
		if fits.getval(ifile, 'opt_elem', 0) == 'G140L':
			img = fits.getdata(ifile, 1)
			ax1.plot(np.sum(img, axis = 1)/np.median(np.sum(img, axis = 1)), np.arange(1024), label = os.path.basename(ifile)[0:9])
			#Dither pattern is 1 arcsec offset = 40.65 pix on FUV MAMA
			for i in range(0,4):
				if i == dither_pos-1:
					ax1.axhline(340.0 + (dither_pos-1.0)*40.65, color = 'k', ls = '--')
				else:
					ax1.axhline(340.0 + (i)*40.65, color = 'k', ls = ':')
			ax1.set_ylim(300,800)
			xlimits = ax1.get_xlim()
			ax1.set_xlim(0.5, xlimits[1])

			#Zoom in
			ax2.plot(np.sum(img, axis = 1)/np.median(np.sum(img, axis = 1)), np.arange(1024), label = os.path.basename(ifile)[0:9])
			ax2.axhline(340+(dither_pos-1.0)*40.65, color = 'k', ls = '--')
			ax2.set_ylim(300+(dither_pos-1.0)*40.65,400+(dither_pos-1.0)*40.65)
			ax2.set_xlim(0.5, xlimits[1])
			ax2.legend()
	return fig

if __name__ == "__main__":
	pp = PdfPages('2010jl_xd_profile_for_each_dither.pdf')
	flist = glob.glob('2010jl_data/*flt.fits')
	fig1 = plot_norm_fuv_xd_profile(1, flist)
	fig1.savefig(pp, format = 'pdf')
	fig2 = plot_norm_fuv_xd_profile(2, flist)
	fig2.savefig(pp, format = 'pdf')
	fig3 = plot_norm_fuv_xd_profile(3, flist)
	fig3.savefig(pp, format = 'pdf')
	fig4 = plot_norm_fuv_xd_profile(4, flist)
	fig4.savefig(pp, format = 'pdf')
	pp.close()

