import pyraf
from pyraf import iraf
from iraf import stsdas,hst_calib,ctools,splice as splice
from astropy.io import fits
import os

def add_weight_column():
	'''
	Weight by exposure time?
	Weight by error?
	'''
	pass

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

def splice_2010jl_fuv():
	flist = ['2010jl_loc_340_hgt_21/ocdd03010_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03070_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03020_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03080_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03030_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd030a0_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03040_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd030b0_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03050_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd030c0_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03060_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2010jl_loc_340_hgt_21/2010jl_fuv_x1dsum.fits')

def splice_2010jl_nuv():
	flist = ['2010jl_loc_461_hgt_21/ocdd030d0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030h0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030e0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030i0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030f0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030j0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030g0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030k0_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2010jl_loc_461_hgt_21/2010jl_nuv_x1dsum.fits')

def combine_all_2010jl():
	flist = ['2010jl_loc_340_hgt_21/ocdd03010_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03070_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03020_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03080_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03030_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd030a0_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03040_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd030b0_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03050_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd030c0_x1d.fits',
			'2010jl_loc_340_hgt_21/ocdd03060_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030d0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030h0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030e0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030i0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030f0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030j0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030g0_x1d.fits',
			'2010jl_loc_461_hgt_21/ocdd030k0_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2010jl_all_x1dsum.fits')


def splice_2005ip_fuv():
	flist = ['2005ip_otfr/ocdd02010_x1d.fits',
			'2005ip_otfr/ocdd02020_x1d.fits',
			'2005ip_otfr/ocdd02030_x1d.fits',
			'2005ip_otfr/ocdd02040_x1d.fits',
			'2005ip_otfr/ocdd02050_x1d.fits',
			'2005ip_otfr/ocdd02060_x1d.fits',
			'2005ip_otfr/ocdd02070_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2005ip_otfr/2005ip_fuv_x1dsum.fits')

def splice_2005ip_nuv():
	flist = ['2005ip_otfr/ocdd02080_x1d.fits',
			'2005ip_otfr/ocdd02090_x1d.fits',
			'2005ip_otfr/ocdd020a0_x1d.fits',
			'2005ip_otfr/ocdd020b0_x1d.fits',
			'2005ip_otfr/ocdd020c0_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2005ip_otfr/2005ip_nuv_x1dsum.fits')

def combine_all_2005ip():
	flist = ['2005ip_otfr/ocdd02010_x1d.fits',
			'2005ip_otfr/ocdd02020_x1d.fits',
			'2005ip_otfr/ocdd02030_x1d.fits',
			'2005ip_otfr/ocdd02040_x1d.fits',
			'2005ip_otfr/ocdd02050_x1d.fits',
			'2005ip_otfr/ocdd02060_x1d.fits',
			'2005ip_otfr/ocdd02070_x1d.fits',
			'2005ip_otfr/ocdd02080_x1d.fits',
			'2005ip_otfr/ocdd02090_x1d.fits',
			'2005ip_otfr/ocdd020a0_x1d.fits',
			'2005ip_otfr/ocdd020b0_x1d.fits',
			'2005ip_otfr/ocdd020c0_x1d.fits']

	for ifile in flist:
		add_dq_flags_to_edges(ifile)

	splice_file_together(flist, '2005ip_all_x1dsum.fits')

if __name__ == "__main__":
	#splice_2010jl_fuv()
	#splice_2010jl_nuv()
	#combine_all_2010jl()

	splice_2005ip_fuv()
	splice_2005ip_nuv()
	combine_all_2005ip()
