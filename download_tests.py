import os



print("Starting Downloads")

#1) pull GQF: curl from zenodo


os.system('curl https://zenodo.org/record/7329123/files/gqf.zip --output gqf.zip')
os.system('unzip gqf.zip')

#rename to something not super weird
os.system("mv gqf-artifacts gqf")
os.system("rm gqf.zip")

print("GQF Download done.")


#download TCF


os.system("curl https://zenodo.org/record/7329334/files/pog_warp_tests.zip --output pog_warp_tests.zip")
os.system("unzip pog_warp_tests.zip")
os.system("rm pog_warp_tests.zip")

os.system("curl https://zenodo.org/record/7329306/files/huntermBerkeley/poggers-v1.1.zip --output poggers.zip")
os.system("unzip poggers.zip")
os.system("mv huntermBerkeley-poggers-f3feec6 poggers")
os.system("rm poggers.zip")

print("TCF test Downloaded - library download is deferred to cmake initialization")

#os.system("git clone https://github.com/huntermBerkeley/bulk-tcf.git")

os.system("curl https://zenodo.org/record/7329170/files/bulk-tcf.zip --output bulk-tcf.zip")
os.system("unzip bulk-tcf.zip")
os.system("rm bulk-tcf.zip")

print("Bulk TCF downloaded")
print("All tests downloaded")
