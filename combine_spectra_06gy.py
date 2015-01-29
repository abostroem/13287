import pyraf
from pyraf import iraf
from iraf import stsdas,hst_calib,ctools,splice as splice
from astropy.io import fits
import os

#----------------------------

def add_weight_column():
	'''
	Weight by exposure time?
	Weight by error?
	'''
	pass

#----------------------------

def add_dq_flags_to_edges(input_filename):
	'''
	The STIS DHB recommends setting a DQ flag at the edges before combining. 4 is included
	in the STIS SDQFLAGS
	'''
	ofile = fits.open(input_filename, mode = 'update')
	ofile[1].data['dq'][0][0:50] = 4
	ofile[1].data['dq'][0][-10:] = 4
	ofile[0].header.add_history('setting dq = 4 for first and last 10 values')
	ofile.close()

#----------------------------

def splice_file_together(input_flist, output_filename):
	'''
	Combine extracted FUV and NUV spectra into a single file
	'''
	sdqflag_value = fits.getval(input_flist[0], 'SDQFLAGS', 1)
	input_string = ','.join(input_flist)

	output_file_whole_path = os.path.join(os.getcwd(), output_filename)
	if os.path.exists(output_file_whole_path):
		os.remove(output_file_whole_path)

	splice( intable = input_string,
			outtable = output_filename,
			spacing = 'fine',
			sdqflags = sdqflag_value,
			wl_name = 'wavelength',
			flux_name = 'flux',
			err_name = 'error',
			dq_name = 'dq',
			n_name = 'nelem')

			#Consider adding a weight column
			# wgt_name = 'weight',

#----------------------------

def splice_2010jl_fuv():
	'''
	Combine all 2010jl FUV 1D extraction files
	'''
	flist = ['2010jl_loc_327.0_hgt_21/ocdd03010_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03070_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03020_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03080_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03030_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd030a0_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03040_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd030b0_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03050_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd030c0_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03060_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2010jl_loc_327.0_hgt_21/2010jl_fuv_x1dsum.fits')

#----------------------------

def splice_2010jl_nuv():
	'''
	Combine all 2010JL NUV 1D extraction files
	'''
	flist = ['2010jl_loc_323.0_hgt_21/ocdd030d0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030h0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030e0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030i0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030f0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030j0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030g0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030k0_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2010jl_loc_323.0_hgt_21/2010jl_nuv_x1dsum.fits')

#----------------------------

def combine_all_2010jl():
	'''
	Combine FUV and NUV 1D extraction files for 2010JL
	'''
	flist = ['2010jl_loc_327.0_hgt_21/ocdd03010_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03070_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03020_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03080_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03030_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd030a0_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03040_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd030b0_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03050_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd030c0_x1d.fits',
			'2010jl_loc_327.0_hgt_21/ocdd03060_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030d0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030h0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030e0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030i0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030f0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030j0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030g0_x1d.fits',
			'2010jl_loc_323.0_hgt_21/ocdd030k0_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2010jl_all_x1dsum.fits')

#----------------------------

def splice_2005ip_fuv():
	'''
	Combine all 2005ip FUV 1D extraction files
	'''
	flist = ['2005ip_otfr/ocdd02010_x1d.fits',
			'2005ip_otfr/ocdd02020_x1d.fits',
			'2005ip_otfr/ocdd02030_x1d.fits',
			'2005ip_otfr/ocdd02040_x1d.fits',
			'2005ip_otfr/ocdd02050_x1d.fits',
			'2005ip_otfr/ocdd02060_x1d.fits',
			'2005ip_otfr/ocdd02070_x1d.fits',
			'2005ip_otfr/ocdd02080_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2005ip_otfr/2005ip_fuv_x1dsum.fits')

#----------------------------

def splice_2005ip_nuv():
	'''
	Combine all 2005ip NUV 1D extraction files
	'''
	flist = [#'2005ip_otfr/ocdd02090_x1d.fits', #remove from analysis until I can figure out what is going on
			'2005ip_otfr/ocdd020a0_x1d.fits',
			'2005ip_otfr/ocdd020b0_x1d.fits',
			'2005ip_otfr/ocdd020c0_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2005ip_otfr/2005ip_nuv_x1dsum.fits')

#----------------------------

def combine_all_2005ip():
	'''
	Combine FUV and NUV 1D extraction files for 2005ip
	'''
	flist = ['2005ip_otfr/ocdd02010_x1d.fits',
			'2005ip_otfr/ocdd02020_x1d.fits',
			'2005ip_otfr/ocdd02030_x1d.fits',
			'2005ip_otfr/ocdd02040_x1d.fits',
			'2005ip_otfr/ocdd02050_x1d.fits',
			'2005ip_otfr/ocdd02060_x1d.fits',
			'2005ip_otfr/ocdd02070_x1d.fits',
			'2005ip_otfr/ocdd02080_x1d.fits',
			#'2005ip_otfr/ocdd02090_x1d.fits', #remove from analysis until I can figure out what is going on
			'2005ip_otfr/ocdd020a0_x1d.fits',
			'2005ip_otfr/ocdd020b0_x1d.fits',
			'2005ip_otfr/ocdd020c0_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2005ip_all_x1dsum.fits')

#----------------------------

#----------------------------

def splice_2009ip_fuv():
	'''
	Combine all 2009ip FUV 1D extraction files
	'''
	flist = ['2009ip_otfr/ocdd01010_x1d.fits',
			'2009ip_otfr/ocdd01020_x1d.fits',
			'2009ip_otfr/ocdd01030_x1d.fits',
			'2009ip_otfr/ocdd01040_x1d.fits',
			'2009ip_otfr/ocdd01050_x1d.fits',
			'2009ip_otfr/ocdd01060_x1d.fits',
			'2009ip_otfr/ocdd01070_x1d.fits',
			'2009ip_otfr/ocdd01080_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2009ip_otfr/2009ip_fuv_x1dsum.fits')

#----------------------------

def splice_2009ip_nuv():
	'''
	Combine all 2009ip NUV 1D extraction files
	'''
	flist = [#'2009ip_otfr/ocdd02090_x1d.fits', #remove from analysis until I can figure out what is going on
			'2009ip_otfr/ocdd020a0_x1d.fits',
			'2009ip_otfr/ocdd020b0_x1d.fits',
			'2009ip_otfr/ocdd020c0_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2009ip_otfr/2009ip_nuv_x1dsum.fits')

#----------------------------

def combine_all_2009ip():
	'''
	Combine FUV and NUV 1D extraction files for 2009ip
	'''
	flist = ['2009ip_otfr/ocdd01010_x1d.fits',
			'2009ip_otfr/ocdd01020_x1d.fits',
			'2009ip_otfr/ocdd01030_x1d.fits',
			'2009ip_otfr/ocdd01040_x1d.fits',
			'2009ip_otfr/ocdd01050_x1d.fits',
			'2009ip_otfr/ocdd01060_x1d.fits',
			'2009ip_otfr/ocdd01070_x1d.fits',
			'2009ip_otfr/ocdd01080_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2009ip_all_x1dsum.fits')

#----------------------------

	#----------------------------

def splice_2006gy_fuv():
	'''
	Combine all 2006gy FUV 1D extraction files
	'''
	flist = ['2006gy_loc_499.0_hgt_21/ocdd04030_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2006gy_otfr/2006gy_fuv_x1dsum.fits')

#----------------------------

def splice_2006gy_nuv():
	'''
	Combine all 2006gy NUV 1D extraction files
	'''
	flist = ['2006gy_loc_501.0_hgt_21/ocdd04010_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2006gy_otfr/2006gy_nuv_x1dsum.fits')

#----------------------------

def combine_all_2006gy():
	'''
	Combine FUV and NUV 1D extraction files for 2006gy
	'''
	flist = ['2006gy_loc_499.0_hgt_21/ocdd04030_x1d.fits',
		'2006gy_loc_501.0_hgt_21/ocdd04010_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2006gy_all_x1dsum.fits')

#----------------------------

#----------------------------
if __name__ == "__main__":
	#	splice_2010jl_fuv()
	#	splice_2010jl_nuv()
	#	combine_all_2010jl()

	#	splice_2005ip_fuv()
	#	splice_2005ip_nuv()
	#	combine_all_2005ip()

	#	splice_2006gy_fuv()
	#	splice_2006gy_nuv()
	combine_all_2006gy()

#	splice_2009ip_fuv()
#	splice_2009ip_nuv()
#	combine_all_2009ip()
