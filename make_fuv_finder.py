from astropy.io import fits
from scipy.ndimage.interpolation import rotate
import numpy as np
from matplotlib import pyplot
from datetime import datetime
import math
import pdb

from helper_functions import add_date_to_plot


def make_fuv_finder_plot(stis_img, wfpc2_cc_offset, sn_yloc_stis = 340):
	'''
	Plot a 3 panel pdf of the WFPC2 image on the left, cropped to the slit location in the middle
	and the STIS cross-dispersion profile on the right. The region plotted for WFPC2 was determined
	by cross-correlating the cross-dispersion profiles of different x locations with the STIS data.
	This is performed in the notebook currently.

	'''
	wfpc2_img = fits.getdata('hst_08645_11_wfpc2_f300w_wf/hst_08645_11_wfpc2_f300w_wf_drz.fits', 1)
	orientat = 36.6144
	rot_wfpc2_img = rotate(wfpc2_img, orientat)
	wfpc2_y_start = 750

	fig = pyplot.figure(figsize = [20, 15])
	ax1 = fig.add_subplot(1, 3, 1)
	ax2 = fig.add_subplot(1,3,2)
	ax3 = fig.add_subplot(1, 3, 3)

	wfpc2_x_start = 1229.5
	wfpc2_x_end = 1234.5
	wfpc2_platescale = 0.1 #arcsec/pix
	stis_slit_height_pix = 25.0/wfpc2_platescale
	stis_slit_width_pix = 0.5/wfpc2_platescale

	ax1.set_title('WFPC2 Image of UGC 5189')
	im1 = ax1.imshow(rot_wfpc2_img, interpolation = 'nearest', vmin = 0, vmax = 0.2)
	ax1.set_ylim(700, 1150)
	ax1.set_xlim(1100, 1300)
	ax1.plot([1220, 1220, 1250, 1250, 1220], [wfpc2_y_start+wfpc2_cc_offset, wfpc2_y_start+wfpc2_cc_offset+stis_slit_height_pix, wfpc2_y_start+wfpc2_cc_offset+stis_slit_height_pix, wfpc2_y_start+wfpc2_cc_offset, wfpc2_y_start+wfpc2_cc_offset], color = 'r')

	#Make compass
	north_dx = -50.0*math.sin(orientat*math.pi/180.0)
	north_dy = 50.0*math.cos(orientat*math.pi/180.0)
	east_dx = 50.0*math.sin((90.0-orientat)*math.pi/180.0)
	east_dy = 50.0*math.cos((90.0-orientat)*math.pi/180.0)
	arrow_center_x = 1150
	arrow_center_y = 1050
	ax1.arrow(arrow_center_x, arrow_center_y, north_dx, north_dy, color = 'w', width = 0.5, head_length = 12*0.5)
	ax1.arrow(arrow_center_x, arrow_center_y, east_dx, east_dy, color = 'w', width = 0.5, head_length = 12*0.5)
	ax1.text(arrow_center_x + north_dx, arrow_center_y + north_dy +10, 'N', color = 'w' )
	ax1.text(arrow_center_x + east_dx, arrow_center_y + east_dy +10, 'E', color = 'w' )

	ax2.set_title('STIS Slit position on WFPC2 Image')
	im2 = ax2.imshow(rot_wfpc2_img, interpolation = 'nearest', vmin = 0, vmax = 0.2)
	ax2.set_ylim(wfpc2_y_start+wfpc2_cc_offset, wfpc2_y_start+wfpc2_cc_offset+stis_slit_height_pix)
	ax2.set_xlim(1220,1250)
	ax2.axvspan(1220, wfpc2_x_start, color = 'k', alpha = 0.5)
	ax2.axvspan(wfpc2_x_end, 1250, color = 'k', alpha = 0.5)
	ax2.set_yticks(np.arange(ax2.get_ylim()[0], ax2.get_ylim()[1], 50))
	ax2.grid(color = 'w')

	ax3.set_title('Normalized XD profiles from STIS and WFPC2')
	ax3.plot(np.sum(rot_wfpc2_img[wfpc2_y_start+wfpc2_cc_offset:wfpc2_y_start+wfpc2_cc_offset+stis_slit_height_pix, wfpc2_x_start:wfpc2_x_end+1], axis = 1)/np.max(np.sum(rot_wfpc2_img[wfpc2_y_start+wfpc2_cc_offset+120:wfpc2_y_start+wfpc2_cc_offset+175, wfpc2_x_start:wfpc2_x_end+1], axis = 1)), np.arange(stis_slit_height_pix))
	ax3.legend(['WFPC2'], loc = 1)
	ax3.grid()

	ax4 = ax3.twinx()
	img = fits.getdata(stis_img, 1)
	xd_profile = np.sum(img, axis = 1)
	ax4.plot(xd_profile/np.max(xd_profile[550:650]), np.arange(len(xd_profile)), color = 'g')
	ax4.set_ylim(0, 1024)
	ax4.legend(['STIS'], loc = 4)

	add_date_to_plot(ax3)
	pdb.set_trace()
	pyplot.savefig('2010jl_finder_image_fuv.pdf')

#----------------------------
#----------------------------
if __name__ == "__main__":
	make_fuv_finder_plot('2010jl_otfr/ocdd03010_flt.fits', 140) #CC program returned an offset of 138
