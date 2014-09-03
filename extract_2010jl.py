from astropy.io import fits
from stistools.x1d import x1d
import numpy as np
import os
import sys
import shutil
import glob

def get_repository_path():
	current_dir = os.getcwd()
	users_path = current_dir.split('/13287')[0]
	repo_path = os.path.join(users_path, '13287')
	return repo_path

def set_oref():
	'''
	Set environment variable oref to point to folder with reference files
	'''
	oref_path = get_repository_path()
	os.environ['oref'] = os.path.join(oref_path, 'oref')+'/'

def make_output_directory(extraction_box_height, extraction_box_start, sn_name, overwrite = False):
	output_dir = '{}_loc_{}_hgt_{}'.format(sn_name, extraction_box_start, extraction_box_height)
	repo_path = get_repository_path()
	new_dir_path = os.path.join(repo_path, output_dir)
	if os.path.exists(new_dir_path):
		if overwrite == False:
			delete_dir = raw_input('{} exists, delete contents? y, n '.format(new_dir_path))
			if delete_dir == 'n':
				sys.exit('Output path already exists and you don\'t want to overwrite it')
		flist = glob.glob(os.path.join(new_dir_path, '*'))
		for ifile in flist:
			os.remove(ifile)
	else:
		os.makedirs(new_dir_path)
	return new_dir_path

def extract_for_a_single_dither_position(dither_exposure_names, dither_number, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height,
										maxsearch = 4):
	os.environ['oref'] = os.path.join(repo_path, 'oref')+'/'
	for exposure_number in dither_exposure_names:
		input_filename = 'ocdd030{}_flt.fits'.format(exposure_number)
		shutil.copy(os.path.join(repo_path, '2010jl_otfr', input_filename),
					os.path.join(output_dir, input_filename))
		shutil.copy(os.path.join(repo_path, '2010jl_otfr', input_filename.replace('flt', 'wav')),
					os.path.join(output_dir, input_filename.replace('flt', 'wav')))
		x1d(input = os.path.join(output_dir, input_filename),
			a2center = extraction_box_start + (dither_number -1) * dither_step,
			extrsize = extraction_box_height,
			maxsrch = maxsearch,
			trailer = os.path.join(output_dir, input_filename.replace('flt.fits', 'trl.txt')))

def extract_fuv_2010jl():
	'''
	Defines extraction location for 2010jl. Data taken with the FUV MAMA using 4 along
	the slit dithers.

	The MAMA along-the-slit dither pattern is specified with point spacing = 1 arcseconds
	For the FUV plate scale = 0.0246 arcsec/pix --> 1 arcsecond = 40.6504065 pixels.

	The dither position centers the target at ycenter = 340
	'''
	extraction_box_height = 21 #pixels
	extraction_box_start = 340
	dither_step = 40.65

	repo_path = get_repository_path()
	output_dir = make_output_directory(extraction_box_height, extraction_box_start, '2010jl')


	extract_for_a_single_dither_position(['10', '50', '90'], 1, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height)


	extract_for_a_single_dither_position(['20', '60', 'a0'], 2, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height)

	extract_for_a_single_dither_position(['30', '70', 'b0'], 3, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height)

	extract_for_a_single_dither_position(['40', '80', 'c0'], 4, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height)


def extract_nuv_2010jl():
	'''
	Defines extraction location for 2010jl. Data taken with the NUV MAMA using 4 along
	the slit dithers.

	The MAMA along-the-slit dither pattern is specified with point spacing = 1 arcseconds
	For the NUV plate scale = 0.0248 arcsec/pix --> 1 arcsecond = 40.32 pixels.

	The dither position centers the target at ycenter = 461 (340 + 120.8)
	'''
	extraction_box_height = 21 #pixels
	extraction_box_start = 461
	dither_step = 40.32

	repo_path = get_repository_path()
	output_dir = make_output_directory(extraction_box_height, extraction_box_start, '2010jl')


	extract_for_a_single_dither_position(['d0', 'h0'], 1, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height,
										maxsearch = 0)


	extract_for_a_single_dither_position(['e0', 'i0'], 2, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height,
										maxsearch = 0)

	extract_for_a_single_dither_position(['f0', 'j0'], 3, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height,
										maxsearch = 0)

	extract_for_a_single_dither_position(['g0', 'k0'], 4, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height,
										maxsearch = 0)

if __name__ == "__main__":
	#extract_fuv_2010jl()
	extract_nuv_2010jl()