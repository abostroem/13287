from matplotlib import pyplot
from astropy.io import fits
import numpy as np
import pdb

def confirm_extraction(filename):
	'''
	This file plots the cross dispersion profile of a long slit image and then overplots
	the extraction location of the spectrum and the background regions, including the
	spectrum and background extraction boxes
	'''
	tbdata = fits.getdata(filename, 1)
	#img = fits.getdata(filename.replace('x1d', 'crj'), 1)
	img = fits.getdata(filename.replace('_x1d', ''), 1)
	print img
	fig = pyplot.figure(figsize = [20, 10])
	ax_img = fig.add_subplot(1, 2, 1)
	ax_xd = fig.add_subplot(1, 2, 2)

	pixel_num = np.arange(1024)
	#display image
	im = ax_img.imshow(img, interpolation = 'nearest', cmap = 'bone', vmin = 0, vmax = max(np.mean(img), 0.01))
	#plot cross-dispersion profile
	ax_xd.plot(np.median(img, axis = 1), pixel_num)
	#Label extraction location and box
	ax_img.plot(pixel_num,tbdata['extrlocy'][0], 'r')
	ax_img.plot(pixel_num, tbdata['extrlocy'][0]+tbdata['EXTRSIZE'][0]/2.0, 'r--')
	ax_img.plot(pixel_num, tbdata['extrlocy'][0]-tbdata['EXTRSIZE'][0]/2.0, 'r--')

	ax_img.plot(pixel_num,tbdata['extrlocy'][0]+tbdata['BK1OFFST'][0], 'c')
	ax_img.plot(pixel_num, tbdata['extrlocy'][0]+tbdata['BK1OFFST'][0]+tbdata['BK1SIZE'][0]/2.0, 'c--')
	ax_img.plot(pixel_num, tbdata['extrlocy'][0]+tbdata['BK1OFFST'][0]-tbdata['BK1SIZE'][0]/2.0, 'c--')

	ax_img.plot(pixel_num,tbdata['extrlocy'][0]+tbdata['BK2OFFST'][0], 'c')
	ax_img.plot(pixel_num, tbdata['extrlocy'][0]+tbdata['BK2OFFST'][0]+tbdata['BK2SIZE'][0]/2.0, 'c--')
	ax_img.plot(pixel_num, tbdata['extrlocy'][0]+tbdata['BK2OFFST'][0]-tbdata['BK2SIZE'][0]/2.0, 'c--')

	ax_img.set_xlim(0, 1024)
	ax_img.set_ylim(0, 1024)

	ax_xd.axhline(tbdata['extrlocy'][0][512], color = 'r')
	ax_xd.axhline( tbdata['extrlocy'][0][512]+tbdata['EXTRSIZE'][0]/2.0, color = 'r', ls = '--')
	ax_xd.axhline( tbdata['extrlocy'][0][512]-tbdata['EXTRSIZE'][0]/2.0, color = 'r', ls = '--')

	ax_xd.axhline(tbdata['extrlocy'][0][512]+tbdata['BK1OFFST'][0], color = 'c')
	ax_xd.axhline(tbdata['extrlocy'][0][512]+tbdata['BK1OFFST'][0]+tbdata['BK1SIZE'][0]/2.0, color = 'c', ls = '--')
	ax_xd.axhline(tbdata['extrlocy'][0][512]+tbdata['BK1OFFST'][0]-tbdata['BK1SIZE'][0]/2.0, color = 'c', ls = '--')

	ax_xd.axhline(tbdata['extrlocy'][0][512]+tbdata['BK2OFFST'][0], color = 'c')
	ax_xd.axhline(tbdata['extrlocy'][0][512]+tbdata['BK2OFFST'][0]+tbdata['BK2SIZE'][0]/2.0, color = 'c', ls = '--')
	ax_xd.axhline(tbdata['extrlocy'][0][512]+tbdata['BK2OFFST'][0]-tbdata['BK2SIZE'][0]/2.0, color = 'c', ls = '--')

	ax_xd.set_ylim(0, 1024)
	pyplot.savefig(filename.replace('x1d.fits', 'xtrac_conf.pdf'))
	pyplot.close()

#----------------------------

def confirm_2006gy_fuv():
	'''
	Make plots for all 2006gy FUV files
	'''
	#FUV 2006gy
	confirm_extraction('2006gy_loc_509.0_hgt_20/ocdd04030_crj_x1d.fits')

#----------------------------

def confirm_2006gy_nuv():
	'''
	Make plots for all 2006gy NUV files
	'''
	#NUV 2006gy
	confirm_extraction('2006gy_loc_511.0_hgt_20/ocdd04010_crj_x1d.fits')

#----------------------------
#----------------------------

if __name__ == "__main__":
	confirm_2006gy_fuv()
	confirm_2006gy_nuv()



