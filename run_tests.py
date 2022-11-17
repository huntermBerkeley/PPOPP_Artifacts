import os



print("Running Tests for GQF/SQF/RSQF")

root = os.getcwd()

gqf_directory = root + "/gqf"

gqf_results_directory = gqf_directory + "/results/aggregate"

os.chdir(gqf_directory)

#GQF/SQF/RSQF have their own test scripts!
print("Starting performance tests")

os.system("chmod +x ./scripts/*")
os.system('./scripts/run_all_tests.sh "results"')
print("Done generating data, aggregating results...")
os.mkdir(gqf_results_directory)
os.system("python3 scripts/aggregate_local_data.py")

os.chdir(root)

print("Running TCF / Warpcore tests")
tcf_directory = root + "/pog_warp_tests/build"

os.chdir(tcf_directory)

os.system("./test")



os.chdir(root)


#run Bulk Tests
print("Running Bulk TCF tests")
bulk_tcf_directory = root + "/bulk-tcf/build"
os.chdir(bulk_tcf_directory)
os.system("./batched_template_tests 22 1 test")
os.system("./batched_template_tests 24 1 test")
os.system("./batched_template_tests 26 1 test")
os.system("./batched_template_tests 28 1 test")

#some GPUs can't run this test in place due to memory requirements (need to sort ~8.5 GBs of data, doubled due to thrust sort)
#this test sorts the array before the filter is initialized to reduce memory reqs and will swap to CudaMallocManaged if we run out of space.
os.system("./presorted_template_tests 30 1 test")

os.chdir(root)

