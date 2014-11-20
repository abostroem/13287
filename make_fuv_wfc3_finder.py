from astropy.io import fits
from scipy.ndimage.interpolation import rotate
import numpy as np
from matplotlib import pyplot
from datetime import datetime
import math
import pdb

from helper_functions import add_date_to_plot


def make_fuv_finder_plot(stis_img, wfc3_cc_offset, sn_yloc_stis = 340):
	'''
	Plot a 3 panel pdf of the WFPC2 image on the left, cropped to the slit location in the middle
	and the STIS cross-dispersion profile on the right. The region plotted for WFPC2 was determined
	by cross-correlating the cross-dispersion profiles of different x locations with the STIS data.
	This is performed in the notebook currently.

	'''
	wfc3_img = fits.getdata('2010jl_keck/icd704020_drz.fits', 1)
	orientat = 153.72+90
	rot_wfc3_img = rotate(wfc3_img, orientat)
	wfc3_y_start = 511

	fig = pyplot.figure(figsize = [20, 15])
	ax1 = fig.add_subplot(1, 3, 1)
	ax2 = fig.add_subplot(1,3,2)
	ax3 = fig.add_subplot(1, 3, 3)

	wfc3_x_start = 714.7
	wfc3_x_end = 727.4
	wfc3_platescale =  0.0394 #arcsec/pix
	stis_slit_height_pix = int(25.0/wfc3_platescale)-35
	stis_slit_width_pix = 0.5/wfc3_platescale

	ax1.set_title('WFC3 Image of 2010JL')
	im1 = ax1.imshow(rot_wfc3_img, interpolation = 'nearest', vmin = 0, vmax = 0.1)
	ax1.set_ylim(50, 1200)
	ax1.set_xlim(384, 884)
	#ax1.plot([1220, 1220, 1250, 1250, 1220], [wfc3_y_start+wfc3_cc_offset, wfc3_y_start+wfc3_cc_offset+stis_slit_height_pix, wfc3_y_start+wfc3_cc_offset+stis_slit_height_pix, wfc3_y_start+wfc3_cc_offset, wfc3_y_start+wfc3_cc_offset], color = 'r')

	#Make compass
	#north_dx = -50.0*math.sin(orientat*math.pi/180.0)
	#north_dy = 50.0*math.cos(orientat*math.pi/180.0)
	#east_dx = 50.0*math.sin((90.0-orientat)*math.pi/180.0)
	#east_dy = 50.0*math.cos((90.0-orientat)*math.pi/180.0)
	#arrow_center_x = 1150
	#arrow_center_y = 1050
	#ax1.arrow(arrow_center_x, arrow_center_y, north_dx, north_dy, color = 'w', width = 0.5, head_length = 12*0.5)
	#ax1.arrow(arrow_center_x, arrow_center_y, east_dx, east_dy, color = 'w', width = 0.5, head_length = 12*0.5)
	#ax1.text(arrow_center_x + north_dx, arrow_center_y + north_dy +10, 'N', color = 'w' )
	#ax1.text(arrow_center_x + east_dx, arrow_center_y + east_dy +10, 'E', color = 'w' )

	ax2.set_title('STIS Slit position on WFC3 Image')
	im2 = ax2.imshow(rot_wfc3_img, interpolation = 'nearest', vmin = 0, vmax = 0.1)
	ax2.set_ylim(wfc3_y_start+wfc3_cc_offset, wfc3_y_start+wfc3_cc_offset+stis_slit_height_pix)
	ax2.set_xlim(684, 762)
	ax2.axvspan(684, wfc3_x_start, color = 'k', alpha = 0.5)
	ax2.axvspan(wfc3_x_end, 762, color = 'k', alpha = 0.5)
	ax2.set_yticks(np.arange(ax2.get_ylim()[0], ax2.get_ylim()[1], 50))
	ax2.grid(color = 'w')

	ax3.set_title('Normalized XD profiles from STIS and WFC3')
	wfc3_xd_lower_y = wfc3_y_start+wfc3_cc_offset
	wfc3_xd_upper_y = wfc3_y_start+wfc3_cc_offset+stis_slit_height_pix
	wfc3_xd_lower_x = wfc3_x_start
	wfc3_xd_upper_x = wfc3_x_end+1
	#Choose a small y region of background to normalize by
	normalization = np.max(np.sum(rot_wfc3_img[wfc3_y_start+wfc3_cc_offset+120:wfc3_y_start+wfc3_cc_offset+175, wfc3_x_start:wfc3_x_end+1], axis = 1))
	ax3.plot(np.sum(rot_wfc3_img[wfc3_xd_lower_y:wfc3_xd_upper_y, wfc3_xd_lower_x:wfc3_xd_upper_x], axis = 1)/normalization, np.arange(stis_slit_height_pix)+10)
	ax3.legend(['WFC3'], loc = 1)
	ax3.set_ylim(-25, 625)
	ax3.grid()

	ax4 = ax3.twinx()
	img = fits.getdata(stis_img, 1)
	xd_profile = np.sum(img, axis = 1)
	ax4.plot(xd_profile/np.max(xd_profile[550:650]), np.arange(len(xd_profile)), color = 'g')
	ax4.set_ylim(0, 1024)
	ax4.legend(['STIS'], loc = 4)



	add_date_to_plot(ax3)
	pdb.set_trace()
	pyplot.savefig('2010jl_wfc3_finder_image_fuv.pdf')

#----------------------------
#----------------------------
if __name__ == "__main__":
	make_fuv_finder_plot('2010jl_otfr/ocdd03010_flt.fits', 20) #CC program returned an offset of 138