import os
import time
import shutil
import glob

def get_repository_path():
	current_dir = os.getcwd()
	users_path = current_dir.split('/13287')[0]
	repo_path = os.path.join(users_path, '13287')
	return repo_path

def copy_if_new_version_exists(flist, copy_to_directory, copy_from_directory):
	for filename in flist:
		last_modified_copy_to = os.path.getmtime(os.path.join(copy_to_directory, filename))
		last_modified_copy_from = os.path.getmtime(os.path.join(copy_from_directory, filename))
		if last_modified_copy_from > last_modified_copy_to:
			shutil.copyfile(os.path.join(copy_from_directory, filename), os.path.join(copy_to_directory, filename))
			print 'copying new version of {}'.format(filename)


def copy_files_for_2010jl():
	copy_to_directory = '/Users/abostroem/Dropbox/13287/2010jl'
	copy_from_directory = get_repository_path()

	#Copy plots to dropbox
	plot_filenames = [
		'2010jl_finder_image_fuv.pdf',
		'2010jl_xd_profile_for_each_dither_fuv.pdf',
		'2010jl_xd_profile_for_each_dither_nuv.pdf',
		'xd_profile_match.pdf',
		'2010jl_nuv_fuv_xd_profile_compare.pdf'
		]
	copy_if_new_version_exists(plot_filenames, copy_to_directory, copy_from_directory)

	xtrac_directory = '2010jl_loc_340_hgt_21'
	xtrac_flist = glob.glob(os.path.join(xtrac_directory, '*.pdf')) + \
			glob.glob(os.path.join(xtrac_directory, '*x1d.fits'))

	copy_if_new_version_exists(xtrac_flist, copy_to_directory, copy_from_directory)

	xtrac_directory = '2010jl_loc_461_hgt_21'
	xtrac_flist = glob.glob(os.path.join(xtrac_directory, '*.pdf')) + \
			glob.glob(os.path.join(xtrac_directory, '*x1d.fits'))

	copy_if_new_version_exists(xtrac_flist, copy_to_directory, copy_from_directory)

if __name__ == "__main__":
	copy_files_for_2010jl()