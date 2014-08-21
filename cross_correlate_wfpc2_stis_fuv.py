from astropy.io import fits
import numpy as np
from matplotlib import pyplot
from scipy.ndimage.interpolation import rotate
import time
from matplotlib.backends.backend_pdf import PdfPages
import pdb


def cross_correlate_wfpc2_stis_fuv(input_stis_file):
	'''
	A WFPC2 image of 2010jl's host galaxy is rotated to the STIS orientation.
	This code steps across a small region of a WFPC2 image on the 2010jl galaxy and collapsed
	every 2 columns to create a cross-dispersion profile the same width as the STIS
	slit (0.2 arcseconds). It then cross correlates the STIS FUV cross dispersion profile 
	with the WFPC2 cross-dispersion profile to find the slit position against the background. 
	The best cross-correlation for each WFPC2 x-location is plotted in the file 
	xd_profile_match.pdf.
	'''
	pp = PdfPages('xd_profile_match.pdf')
	orientat = 36.6 #orientation of the STIS slit (orientat keyword)
	
	#read in and rotate the WFPC2 image
	wfpc2_img = fits.getdata('hst_08645_11_wfpc2_f300w_wf/hst_08645_11_wfpc2_f300w_wf_drz.fits', 1)
	rot_wfpc2_img = rotate(wfpc2_img, orientat)
	
	#Make a STIS cross-dispersion profile
	img = fits.getdata(input_stis_file, 1)
	xd_profile = np.sum(img[:, 500:524], axis = 1)
	
	#Remove occulation bar (set values to the median of the profile)
	xd_profile[854:910] = np.median(xd_profile)
	
	#Bin STIS to WFPC2 resolution
	fuv_plate_scale = 0.0246 #arcsec/pix
	wfpc2_platescale = 0.1 #arcsec/pix
	binning_factor = wfpc2_platescale/fuv_plate_scale
	binned_xd_profile = xd_profile[::int(binning_factor)]
	for indx in range(1,int(binning_factor)):
		binned_xd_profile = binned_xd_profile + xd_profile[indx::int(binning_factor)] 
	
	#Calculate the STIS slit height in WFPC2 profile
	stis_slit_height_pix = 25.0/wfpc2_platescale
	#0.2 arcsec slit = 2 WFPC2 pixels
	columns = np.arange(1210, 1260, 2) #Determine which WFPC2 columns to cross-correlate
	corr = []
	offset = []
	wfpc2_y_start = 750 #bottom of the STIS slit
	
	#make WFPC2 xd profile 2 times actual profile to account for offsetting
	for column in columns:
		#0.2 arcsec slit = 2 WFPC2 pixels
		wfpc2_profile = np.sum(rot_wfpc2_img[wfpc2_y_start: wfpc2_y_start + 2*stis_slit_height_pix, column:column+2], axis = 1)
		#Normalize the 2 XD profiles
		#Correlate bigger array, smaller array apply offset to smaller array
		correlation_array = np.correlate(wfpc2_profile/np.max(wfpc2_profile), binned_xd_profile/np.max(binned_xd_profile))
		max_corr_indx = np.argmax(correlation_array)
		max_corr = correlation_array[max_corr_indx]
		corr.append(max_corr)
		offset.append(max_corr_indx)
		
		#Plot the XD profile for each column tested 
		fig_temp = pyplot.figure(figsize = [7, 25])
		ax_temp = fig_temp.add_subplot(1,1,1)
		ax_temp.plot(wfpc2_profile/max(wfpc2_profile), np.arange(len(wfpc2_profile)))
		ax_temp.plot(binned_xd_profile/max(binned_xd_profile), np.arange(len(binned_xd_profile))+max_corr_indx)
		ax_temp.legend(['Norm WFPC2 profile', 'Norm, binned, STIS profile'], loc = 'best')
		ax_temp.set_title('WFPC2 Column {}'.format(column))
		ax_temp.set_ylim(max_corr_indx, len(binned_xd_profile)+max_corr_indx)
		pp.savefig()
		pyplot.close()
	pp.close()
	corr = np.array(corr)
	fig2 = pyplot.figure()
	ax2 = fig2.add_subplot(1,1,1)
	pyplot.plot(columns, corr)
	
	final_max_corr_indx = np.argmax(corr)
	fig3 = pyplot.figure()
	ax3 = fig3.add_subplot(1,1,1)
	ax3.plot(binned_xd_profile/binned_xd_profile.max(), np.arange(len(binned_xd_profile))+offset[final_max_corr_indx])
	best_col = rot_wfpc2_img[wfpc2_y_start : wfpc2_y_start+ 2.0*stis_slit_height_pix, columns[final_max_corr_indx]]
	ax3.plot(best_col/best_col.max(), range(len(best_col)))
	pdb.set_trace()
	print 'highest correlation value = ', np.max(corr)
	print 'Best offset value = ', offset[final_max_corr_indx]
	print 'Best WFPC2 column = ', columns[final_max_corr_indx]
	
if __name__ == "__main__":
	cross_correlate_wfpc2_stis_fuv('otfr_data2/ocdd03010_flt.fits')