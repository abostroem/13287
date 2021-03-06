from astropy.io import fits
from stistools.x1d import x1d
import numpy as np
import os
import sys
import shutil
import glob

from helper_functions import get_repository_path

def make_output_directory(extraction_box_height, extraction_box_start, sn_name, overwrite = False):
	'''
	Create an output directory for the extracted files to go into with the name
		<sn_name>_loc_<extraction_box_start>_hgt_<extraction_box_height>
	User will be asked before files are deleted if directory already exists
	'''
	output_dir = '{}_loc_{}_hgt_{}'.format(sn_name, extraction_box_start, extraction_box_height)
	repo_path = get_repository_path()
	new_dir_path = os.path.join(repo_path, output_dir)
	if os.path.exists(new_dir_path):
		if overwrite == False:
			delete_dir = raw_input('{} exists, delete contents? y, n '.format(new_dir_path))
			if delete_dir == 'n':
				sys.exit('Output path already exists and you don\'t want to overwrite it')
		flist = glob.glob(os.path.join(new_dir_path, 'ocdd*'))
		for ifile in flist:
			os.remove(ifile)
	else:
		os.makedirs(new_dir_path)
	return new_dir_path

#----------------------------

def extract_for_a_single_dither_position(dither_exposure_names, dither_number, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height,
										maxsearch = 0):
	'''
	Given a list of exposure names (corresponding to a dither number), extract a 1D spectrum
	using Calstis.x1d.

	Input:
		dither_exposure_names: list
			list of exposure numbers (as strings) to be extracted
		dither_number: int
			number to be multiplied by dither_step to create the offset from the extraction
				box start
		dither_step : float
			the number of pixels in each dither step
		repo_path : str
			path to local repository
		output_dir : str
			directory where extracted files will be saved. flt and wave files are also copied
		extraction_box_start : float
			extraction location for the first dither position (y pixel)
		extraction_box_height : int
			height of the extraction box
		maxsearch : int
			the number of y offsets from the extraction_box_start which are searched to
			find the spectrum.
	Output:
		x1d files
	'''
	os.environ['oref'] = os.path.join(repo_path, 'oref')+'/'
	for exposure_number in dither_exposure_names:
		input_filename = 'ocdd040{}_crj.fits'.format(exposure_number)
		shutil.copy(os.path.join(repo_path, '2006gy', input_filename),
					os.path.join(output_dir, input_filename))
		shutil.copy(os.path.join(repo_path, '2006gy', input_filename.replace('crj', 'wav')),
	                                os.path.join(output_dir, input_filename.replace('crj', 'wav')))
		print input_filename
		print output_dir
		x1d(input = os.path.join(output_dir, input_filename),
			a2center = extraction_box_start + (dither_number -1) * dither_step,
			extrsize = extraction_box_height,
			maxsrch = maxsearch,
			verbose = True,
			trailer = os.path.join(output_dir, input_filename.replace('crj.fits', 'trl.txt')))

#----------------------------

def extract_fuv_2006gy():
	'''
	Defines extraction location for 2006gy. Data taken with the FUV MAMA using 4 along
	the slit dithers.

	The MAMA along-the-slit dither pattern is specified with point spacing = 1 arcseconds
	For the FUV plate scale = 0.0246 arcsec/pix --> 1 arcsecond = 40.6504065 pixels.

	The dither position centers the target at ycenter = 340
	'''
	extraction_box_height = 20 #64 pixels
	extraction_box_start = 509.#-32. #340
	dither_step = 0.

	repo_path = get_repository_path()
	output_dir = make_output_directory(extraction_box_height, extraction_box_start, '2006gy')


	extract_for_a_single_dither_position(['30'], 1, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height)

#----------------------------

def extract_nuv_2006gy():
	'''
	Defines extraction location for 2006gy. Data taken with the NUV MAMA using 4 along
	the slit dithers.

	The MAMA along-the-slit dither pattern is specified with point spacing = 1 arcseconds
	For the NUV plate scale = 0.0248 arcsec/pix --> 1 arcsecond = 40.32 pixels.

	The dither position centers the target at ycenter = 461 (340 + 120.8)
	'''
	extraction_box_height = 20 #200 pixels
	extraction_box_start = 511.#-100.
	dither_step = 0.

	repo_path = get_repository_path()
	output_dir = make_output_directory(extraction_box_height, extraction_box_start, '2006gy')


	extract_for_a_single_dither_position(['10'], 1, dither_step,
										repo_path, output_dir,
										extraction_box_start, extraction_box_height,
										maxsearch = 0)

#----------------------------
#----------------------------
if __name__ == "__main__":
	extract_fuv_2006gy()
	extract_nuv_2006gy()
