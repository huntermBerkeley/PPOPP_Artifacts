# PPOPP_Artifacts
Artifacts submission for PPOPP23 - High Performance Filters For GPUs #334.

This directory contains the code needed download, build, run, and visualize the results of our paper.

USE
----------------------------
'''
chmod +x run_full_battery.sh
./run_full_battery.sh
cd latex_files
pdflatex -output-directory .. artifact_figures.tex

'''

This will generate a latex file containing graphs that should match those presented in the paper!

Do note that the point GQF test can take a while, especially on more advanced GPUS due to lock thrashing. The test will eventually complete so just leave it be. On an A100 with 16GB of memory the entire testing suite completed in ~20 minutes.

I tested this setup on NERSC's Cori and Perlmutter, if something breaks or you have any questions feel free to reach out to hunter@cs.utah.edu.
