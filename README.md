# PPOPP_Artifacts
Artifacts submission for PPOPP23 - High Performance Filters For GPUs #334.

This directory contains the code needed to download, build, run, and visualize the results of our paper.

OPENSSL and CuRand are required to run the tests.


USE
----------------------------
```
chmod +x run_full_battery.sh
./run_full_battery.sh
cd latex_files
pdflatex -output-directory .. artifact_figures.tex
```

This will generate a latex file containing graphs that should match those presented in the paper! The data shown here is the performance results for 2^22-2^30 for the GQF (point + bulk), TCF (point + bulk), RSQF, SQF, Bloom Filter, and Blocked Bloom Filter on inserts, queries, and random (false positive) queries. In addition, the SQF, GQF, and TCF are benchmarked on deletions.

This benchmark does not explicitly compare the point TCF Cooperative Group variations. To get performance results for the variations you can modify the TCF configuration in pog_warp_tests/test.cu and re-run the test with the new variation.

This benchmark also does not repeat the counting tests for the GQF. This is because I do not have a generator for the Zipfian distribution and was given a set of Zipfian datasets. You can run counting tests for the other distributions using gqf/gqf_verify.cu. If you would like the Zipfian datasets used in our benchmarking please reach out to hunter@cs.utah.edu and I will send them to you.

Do note that the point GQF test and SQF delete tests can take a while, especially on more modern GPUS. The tests will eventually complete so just leave them be. On Cori and Perlmutter I found the tests to complete in under 30 minutes.

If the graphs in the latex file are unlabeled, rebuilding the latex file should fix them.

I tested this setup on NERSC's Cori and Perlmutter, if something breaks or you have any questions feel free to reach out to hunter@cs.utah.edu and I can fix it.


