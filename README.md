

  1. Run cross_correlate_wfpc2_stis_fuv.py to find SN location (optional)

  2. Run make_fuv_finder.py to make plot showing SN location in WFPC2 image and STIS XD profile. This relies on having found the SN location in the STIS XD profile

  3. Run plot_2010jl_xd_dithers.py to plot the SN location for each dither position and check the plate scale

  4. Run extract_2010jl.py to extract from the SN location for FUV and NUV exposures

  5. Run confirm_extraction.py to plot the SN extraction and background regions on the image an the XD profile

  6. Run combine_spectra.py to combine the FUV, NUV, and all spectra into a single file

  7. Run plot_combined_spec.py to each exposure and the combined spectrum to check for outliers

  8. Run plot_labeled_combined_spec.py to plot the combined spectrum with line labels



