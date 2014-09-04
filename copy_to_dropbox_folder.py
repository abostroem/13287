import os
import time
import shutil
import glob
from helper_functions import get_repository_path


def copy_if_new_version_exists(flist, copy_to_directory, copy_from_directory):
	'''
	check the modification time on each file in flist. If the file in copy_to_directory
	is older than the one in copy_from_directory, copy file from copy_from_directory to
	copy_to_directory
	'''
	for filename in flist:
		last_modified_copy_to = os.path.getmtime(os.path.join(copy_to_directory, filename))
		last_modified_copy_from = os.path.getmtime(os.path.join(copy_from_directory, filename))
		if last_modified_copy_from > last_modified_copy_to:
			shutil.copyfile(os.path.join(copy_from_directory, filename), os.path.join(copy_to_directory, filename))
			print 'copying new version of {}'.format(filename)
#----------------------------

def copy_files_for_2010jl():
	'''
	Check if files for 2010jl need to be copied to Dropbox. Copy if they do.
	'''
	copy_to_directory = '/Users/abostroem/Dropbox/13287/2010jl'
	copy_from_directory = get_repository_path()

	#Copy plots to dropbox
	plot_filenames = [
		'2010jl_combined_labeled.pdf',
		'2010jl_finder_image_fuv.pdf',
		'2010jl_nuv_fuv_xd_profile_compare_man_shift.pdf',
		'2010jl_nuv_fuv_xd_profile_compare.pdf',
		'2010jl_xd_profile_for_each_dither_fuv.pdf',
		'2010jl_xd_profile_for_each_dither_nuv.pdf',
		'xd_profile_match.pdf',
		]

	#Copy combined fits files
	fits_filenames = [
		'2010jl_all_x1dsum.fits',
		'2010jl_loc_340_hgt_21/2010jl_fuv_x1dsum.fits',
		'2010jl_loc_461_hgt_21/2010jl_nuv_x1dsum.fits'
		]
	copy_if_new_version_exists(plot_filenames, copy_to_directory, copy_from_directory)

	#Copy FUV x1d files and confirmation plots
	xtrac_directory = '2010jl_loc_340_hgt_21'
	xtrac_flist = glob.glob(os.path.join(xtrac_directory, '*.pdf')) + \
			glob.glob(os.path.join(xtrac_directory, '*x1d.fits'))

	copy_if_new_version_exists(xtrac_flist, copy_to_directory, copy_from_directory)

	#Copy NUV x1d files and confirmation plots
	xtrac_directory = '2010jl_loc_461_hgt_21'
	xtrac_flist = glob.glob(os.path.join(xtrac_directory, '*.pdf')) + \
			glob.glob(os.path.join(xtrac_directory, '*x1d.fits'))

	copy_if_new_version_exists(xtrac_flist, copy_to_directory, copy_from_directory)

#----------------------------

def copy_files_for_2005ip():
	'''
	Check if files for 2005ip need to be copied to Dropbox. Copy if they do.
	'''
	copy_to_directory = '/Users/abostroem/Dropbox/13287/2005ip'
	copy_from_directory = get_repository_path()

	#Copy plots
	plot_filenames = [
		'2005ip_combined_labeled.pdf',
		'2005ip_otfr_quicklook.pdf'
		]
	#Copy combined fits files
	fits_filenames = [
		'2005ip_all_x1dsum.fits',
		'2005ip_otfr/2005ip_fuv_x1dsum.fits',
		'2005ip_otfr/2005ip_nuv_x1dsum.fits'
		]

	#Copy confirmation plots
	xtrac_directory = '2005ip_otfr'
	xtrac_flist = glob.glob(os.path.join(xtrac_directory, '*.pdf'))

	copy_if_new_version_exists(xtrac_flist, copy_to_directory, copy_from_directory)

#----------------------------
#----------------------------
if __name__ == "__main__":
	copy_files_for_2010jl()