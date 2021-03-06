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
	img = fits.getdata(filename.replace('x1d', 'flt'), 1)
	fig = pyplot.figure(figsize = [20, 10])
	ax_img = fig.add_subplot(1, 2, 1)
	ax_xd = fig.add_subplot(1, 2, 2)

	pixel_num = np.arange(1024)
	#display image
	im = ax_img.imshow(img, interpolation = 'nearest', cmap = 'bone', vmin = 0, vmax = max(np.mean(img), 0.01))
	#plot cross-dispersion profile
	ax_xd.plot(np.sum(img, axis = 1), pixel_num)
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

def confirm_2010jl_fuv():
	'''
	Make plots for all 2010JL FUV files
	'''
	#FUV 2010JL
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd03010_x1d.fits')
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd03010_x1d.fits')
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd03020_x1d.fits')
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd03030_x1d.fits')
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd03040_x1d.fits')
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd03050_x1d.fits')
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd03060_x1d.fits')
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd03070_x1d.fits')
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd03080_x1d.fits')
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd030a0_x1d.fits')
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd030b0_x1d.fits')
	confirm_extraction('2010jl_loc_331_hgt_21/ocdd030c0_x1d.fits')

#----------------------------

def confirm_2010jl_nuv():
	'''
	Make plots for all 2010JL NUV files
	'''
	#NUV 2010jl
	confirm_extraction('2010jl_loc_461_hgt_21/ocdd030d0_x1d.fits')
	confirm_extraction('2010jl_loc_461_hgt_21/ocdd030e0_x1d.fits')
	confirm_extraction('2010jl_loc_461_hgt_21/ocdd030f0_x1d.fits')
	confirm_extraction('2010jl_loc_461_hgt_21/ocdd030g0_x1d.fits')
	confirm_extraction('2010jl_loc_461_hgt_21/ocdd030h0_x1d.fits')
	confirm_extraction('2010jl_loc_461_hgt_21/ocdd030i0_x1d.fits')
	confirm_extraction('2010jl_loc_461_hgt_21/ocdd030j0_x1d.fits')
	confirm_extraction('2010jl_loc_461_hgt_21/ocdd030k0_x1d.fits')

#----------------------------
#----------------------------

if __name__ == "__main__":
	confirm_2010jl_fuv()
	confirm_2010jl_nuv()



