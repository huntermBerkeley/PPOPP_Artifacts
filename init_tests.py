import os



print("Making Tests for GQF/SQF/RSQF")

root = os.getcwd()

gqf_directory = root + "/gqf"

os.chdir(gqf_directory)
os.system("make clean && make")
os.chdir(root)

gqf_results_directory = gqf_directory + "/results/aggregate"

tcf_directory = root + "/pog_warp_tests/build"





print("Pulling Repos for Point TCF/Warpcore")

os.mkdir(tcf_directory)
os.chdir(tcf_directory)
os.system("cmake ..")
os.system("make clean && make")
os.chdir(root)

tcf_results_directory = tcf_directory + "/results"
bbloom_results_directory = tcf_directory + "/bloom_results"

os.mkdir(tcf_results_directory)
os.mkdir(bbloom_results_directory)

bulk_tcf_directory = root + "/bulk-tcf/build"

bulk_tcf_test_directory = bulk_tcf_directory + "/batched_results"


print("Making Test for bulk TCF")

os.mkdir(bulk_tcf_directory)
os.chdir(bulk_tcf_directory)
os.system("cmake ..")
os.system("make clean && make")
os.chdir(root)
os.mkdir(bulk_tcf_test_directory)

#export CPM_SOURCE_CACHE=$HOME/.cache/CPM - Necessary for checksums