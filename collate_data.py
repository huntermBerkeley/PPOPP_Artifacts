import os
import shutil

#create final data folders and move important data

#quick helper to move results into the correct base - millions
def clipe6(input_string):

	input_string_before = input_string.split(".")[0]

	#need to get lower 6
	lower_bits = input_string_before[-6::1]
	upper_bits = input_string_before[:-6:1]

	return upper_bits + "." + lower_bits


root = os.getcwd()


os.mkdir(root + "/data")
os.mkdir(root + "/data/point_gqf")
os.mkdir(root + "/data/bulk_gqf")
os.mkdir(root + "/data/rsqf")
os.mkdir(root + "/data/sqf")
os.mkdir(root + "/data/bloom")
os.mkdir(root + "/data/blocked_bloom")
os.mkdir(root + "/data/point_tcf")
os.mkdir(root + "/data/bulk_tcf")
os.mkdir(root + "/data/deletes")


#move GQF data
os.system("cp " + root + "/gqf/results/aggregate/gqf* " + root + "/data/bulk_gqf" )
os.system("cp " + root + "/gqf/results/aggregate/point* " + root + "/data/point_gqf" )
os.system("cp " + root + "/gqf/results/aggregate/sqf* " + root + "/data/sqf" )
os.system("cp " + root + "/gqf/results/aggregate/rsqf* " + root + "/data/rsqf" )
os.system("cp " + root + "/gqf/results/aggregate/bloom* " + root + "/data/bloom")

#move point tcf/bbloom data
#Already aggregated!
os.system("cp " + root + "/pog_warp_tests/build/bloom_results/test_aggregate* " + root + "/data/blocked_bloom")
os.system("cp " + root + "/pog_warp_tests/build/results/test_aggregate* " + root + "/data/point_tcf")


#finally move bulk TCF
#it is aggregated but in multiple files so we can collate it here

bulk_tcf_directory = root + "/bulk-tcf/build/batched_results/"

output_tcf_directory = root + "/data/bulk_tcf"

insert_vals = []
query_vals = []
fp_vals = []


for nbits in range(22,31, 2):

	file_id = bulk_tcf_directory + "test_aggregate_" + str(nbits) + "_1"

	print("opening {}".format(file_id))
	with open(file_id,'r') as data_file:

		lines = data_file.readlines();

		print("Insert is {}".format(lines[0].split(" ")[2]))
		insert_vals.append(lines[0].split(" ")[2])
		query_vals.append(lines[1].split(" ")[2])
		fp_vals.append(lines[2].split(" ")[2])



with open(output_tcf_directory + "/inserts.txt",'w') as insert_file:
   insert_file.write("x_0 y_0\n")

   i=0
   for nbits in range(22, 31, 2):
   	insert_file.write("{} {}\n".format(nbits, clipe6(insert_vals[i])))
   	i+=1


with open(output_tcf_directory + "/queries.txt",'w') as query_file:
   query_file.write("x_0 y_0\n")

   i=0
   for nbits in range(22,31, 2):
   	query_file.write("{} {}\n".format(nbits, clipe6(query_vals[i])))
   	i+=1

with open(output_tcf_directory + "/fp.txt",'w') as fp_file:
   fp_file.write("x_0 y_0\n")

   i=0
   for nbits in range(22,31, 2):
   	fp_file.write("{} {}\n".format(nbits, clipe6(fp_vals[i])))
   	i+=1


#now move GQF and SQF deletion data

# bulk_delete_directory = root + "/bulk-tcf/build/batched_results/"

output_gqf_directory = root + "/data/deletes"


gqf_delete_vals = []

for nbits in range(22,31,2):

	file_id = root + "/gqf/results/deletes/gqf_deletes_" + str(nbits) + "-deletions.txt"

	with open(file_id, "r") as gqf_del_file:

		lines = gqf_del_file.readlines()

		#clip first line
		lines = lines[1:]

		#quick and dirty aggregation here
		line_inverted_sum = 0;

		for line in lines:

			
			data = float(line.split(" ")[-1])

			line_inverted_sum += 1.0/data

		agg_result = 20.0/line_inverted_sum

		gqf_delete_vals.append(agg_result)


with open(output_gqf_directory + "/gqf.txt",'w') as gqf_file:
   gqf_file.write("x_0 y_0\n")

   i=0
   for nbits in range(22,31, 2):
   	gqf_file.write("{} {}\n".format(nbits, gqf_delete_vals[i]))
   	i+=1


bulk_delete_directory = root + "/bulk-tcf/build/batched_results/"

output_sqf_directory = root + "/data/deletes"


sqf_delete_vals = []

for nbits in range(22,27,2):

	file_id = root + "/gqf/results/deletes/sqf_deletes_" + str(nbits) + "-deletions.txt"

	with open(file_id, "r") as sqf_del_file:

		lines = sqf_del_file.readlines()

		#clip first line
		lines = lines[1:]

		#quick and dirty aggregation here
		line_inverted_sum = 0;

		for line in lines:

			
			data = float(line.split(" ")[-1])

			line_inverted_sum += 1.0/data

		agg_result = 20.0/line_inverted_sum

		sqf_delete_vals.append(agg_result)


with open(output_sqf_directory + "/sqf.txt",'w') as sqf_file:
   sqf_file.write("x_0 y_0\n")

   i=0
   for nbits in range(22,27, 2):
   	sqf_file.write("{} {}\n".format(nbits, sqf_delete_vals[i]))
   	i+=1


print("Data move done.")

os.chdir(root)
# shutil.copy(root + "/gqf/results/aggregate/")