from astropy.io import fits
import numpy as np
from matplotlib import pyplot
from scipy.ndimage.interpolation import rotate
import time
from matplotlib.backends.backend_pdf import PdfPages
import pdb
import scipy.interpolate
import scipy.ndimage

def congrid(a, newdims, method='linear', centre=False, minusone=False):
	if not a.dtype in [np.float64, np.float32]:
		a = np.cast[float](a)

	m1 = np.cast[int](1)
	print m1
	ofs = np.cast[int](centre) * 0.5
	old = np.array( a.shape )
	ndims = len( a.shape)

	
	#if len( newdims ) != ndims:
	#	print "[congrid] dimensions error. "\
	#	    "This routine currently only supports "\
	#	    "rebinning to the same number of dimensions."
	#	return None
	newdims = np.asarray( newdims, dtype=float )
	#newdims = newdims.reshape(newdims,1)
	dimlist = []

	if method == 'neighbor':
		for i in range( ndims ):
			base = np.indices(newdims)
			dimlist.append( (old - m1) / (newdims - m1) * (base + ofs) - ofs )
		cd = np.array( dimlist ).round().astype(int)
		newa = a[list( cd )]
		return newa

	elif method in ['nearest','linear']:
		for i in range( ndims ):
			base = np.arange( newdims )
			dimlist.append( (old - m1) / (newdims - m1) * (base + ofs) - ofs)

		olddims = [np.arange(i, dtype = np.float) for i in list( a.shape )]
		mint = scipy.interpolate.interp1d( olddims[-1], a, kind=method )
		newa = mint
		newa = mint( dimlist[-1] )

		trorder = [ndims - 1] + range (ndims - 1 )
		for i in range( ndims -2, -1, -1 ):
			print 'here'
			newa = newa.transpose( trorder)
			mint = scipy.interpolate.interp1d( olddims[i], newa, kind=method )
			newa = mint( dimlist[i] )

		if ndims > 1:
			newa = newa.transpose( trorder)

		return newa
	else:
		print "Congrid error:"
		return None

def cross_correlate_wfc3_stis_fuv(input_stis_file):
	'''
	A WFC3 image of 2010jl's host galaxy is rotated to the STIS orientation.
	This code steps across a small region of a WFC3 image on the 2010jl galaxy and collapsed
	every 2 columns to create a cross-dispersion profile the same width as the STIS
	slit (0.2 arcseconds). It then cross correlates the STIS FUV cross dispersion profile 
	with the WFC3 cross-dispersion profile to find the slit position against the background. 
	The best cross-correlation for each WFC3 x-location is plotted in the file 
	xd_profile_match.pdf.
	'''
	pp = PdfPages('xd_profile_match.pdf')
	orientat = 36.6 #orientation of the STIS slit (orientat keyword)
	orientat = 36.6-153.72  
	orientat = 0-107.493
	
	#read in and rotate the WFC3 image
	#wfpc2_img = fits.getdata('hst_08645_11_wfpc2_f300w_wf/hst_08645_11_wfc3_f275w_wf_drz.fits', 1)
	wfpc2_img = fits.getdata('2006gy/wfc3/ibyb20010_drz.fits', 1)  #F814W
	rot_wfpc2_img = rotate(wfpc2_img, orientat)
	
	#Make a STIS cross-dispersion profile
	img = fits.getdata(input_stis_file, 1)
	#xd_profile = np.sum(img, axis = 1)
        #xd_profile = np.sum(img[:, 500:524], axis = 1)
	xd_profile = np.sum(img, axis = 1)
	
	#Remove occulation bar (set values to the median of the profile)
	xd_profile[854:910] = np.median(xd_profile)
	
	#Bin STIS to WFC3 resolution
	stis_plate_scale = 0.0246 #arcsec/pix (MAMAs)
	stis_plate_scale = 0.05071 #/arcsec/pix (CCDs)
	wfc3_platescale = 0.0394 #arcsec/pix
	#wfc3_platescale = 0.1 #arcsec/pix

#	binning_factor = 2.#*wfc3_platescale/stis_plate_scale
#	binned_xd_profile = xd_profile[::int(binning_factor)]
#	for indx in range(1,int(binning_factor)):
#		binned_xd_profile = binned_xd_profile + xd_profile[indx::int(binning_factor)]
	
	#Calculate the STIS slit height in WFC3 profile
	stis_slit_height_pix = 25.0/wfc3_platescale
	#0.2 arcsec slit = 2 WFPC2 pixels
	stis_slit_width_pix = 0.5/wfc3_platescale
	#columns = np.arange(1210, 1260, 2) #Determine which WFC3 columns to cross-correlate
	wfpc2_x_start = 710
	wfpc2_x_end = 740
	columns = np.arange(wfpc2_x_start, wfpc2_x_end, 2) #Determine which WFC3 columns to cross-correlate
	corr = []
	offset = []
	wfpc2_y_start = 375 #bottom of the STIS slit

	multfactor = 1.
        #xd_profile = xd_profile.reshape(len(xd_profile),1)
	binned_xd_profile = congrid(xd_profile, multfactor*int(stis_slit_height_pix))
	fig = pyplot.figure(figsize = [20, 15])
	ax1 = fig.add_subplot(1, 3, 1)
	ax1.set_title('STIS Slit position on WFC3 Image')
	im1 = ax1.imshow(rot_wfpc2_img, interpolation = 'nearest', vmin = 0, vmax = 0.1)
	ax1.set_ylim(wfpc2_y_start+0, wfpc2_y_start+0+1*stis_slit_height_pix)
	ax1.set_xlim(wfpc2_x_start, wfpc2_x_end)
	ax1.set_yticks(np.arange(ax1.get_ylim()[0], ax1.get_ylim()[1], 50))
	ax1.grid(color = 'w')
	
	#make WFC3 xd profile 2 times actual profile to account for offsetting
	for column in columns:
		#0.2 arcsec slit = 2 WFPC2 pixels
		wfpc2_profile = np.sum(rot_wfpc2_img[wfpc2_y_start: wfpc2_y_start + 1*stis_slit_height_pix, column:column+stis_slit_width_pix], axis = 1)
		binned_wfpc2_profile=congrid(wfpc2_profile, multfactor*int(stis_slit_height_pix))
	        wfpc2_profile=binned_wfpc2_profile
		#Normalize the 2 XD profiles
		#Correlate bigger array, smaller array apply offset to smaller array
		correlation_array = np.correlate(wfpc2_profile/np.max(wfpc2_profile), binned_xd_profile/np.max(binned_xd_profile))
		max_corr_indx = 132
		max_corr = 0
		#max_corr_indx = np.argmax(correlation_array)
		#max_corr = correlation_array[max_corr_indx]
		corr.append(max_corr)
		offset.append(max_corr_indx)
		
		#Plot the XD profile for each column tested
		fig = pyplot.figure(figsize = [7, 25])
		ax1 = fig.add_subplot(1, 2, 1)
	        ax1.set_title('STIS Slit position on WFC3 Image')
	        im1 = ax1.imshow(rot_wfpc2_img, interpolation = 'nearest', vmin = 0, vmax = 0.1)
 	        ax1.set_ylim(wfpc2_y_start+max_corr_indx, wfpc2_y_start+max_corr_indx+1*stis_slit_height_pix)
          	ax1.set_xlim(wfpc2_x_start, wfpc2_x_end)
		ax1.axvspan(wfpc2_x_start, column, color = 'k', alpha = 0.5)
		ax1.axvspan(column+stis_slit_width_pix, wfpc2_x_end, color = 'k', alpha = 0.5)
        	ax1.set_yticks(np.arange(ax1.get_ylim()[0], ax1.get_ylim()[1], 50))
	        ax1.grid(color = 'w')

		#fig_temp = pyplot.figure(figsize = [7, 25])
		ax_temp = fig.add_subplot(1, 2, 2)
		ax_temp.plot(binned_wfpc2_profile/max(binned_wfpc2_profile), np.arange(len(binned_wfpc2_profile)))
		ax_temp.plot(binned_xd_profile/max(binned_xd_profile)/2., np.arange(len(binned_xd_profile))+max_corr_indx)
		print len(binned_xd_profile)
		ax_temp.legend(['Norm WFC3 profile', 'Norm, binned, STIS profile'], loc = 'best')
		ax_temp.set_title('WFC3 Column {}'.format(column))
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
	#pdb.set_trace()
	print 'highest correlation value = ', np.max(corr)
	print 'Best offset value = ', offset[final_max_corr_indx]
	print 'Best WFPC2 column = ', columns[final_max_corr_indx]
	
if __name__ == "__main__":
	#cross_correlate_wfc3_stis_fuv('otfr_data2/ocdd03090_flt.fits')   #718, 132
	#cross_correlate_wfc3_stis_fuv('otfr_data2/ocdd030d0_flt.fits')  #718, 61
         cross_correlate_wfc3_stis_fuv('2006gy/ocdd04010_flt.fits')
