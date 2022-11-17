import os



print("Starting Downloads")

#1) pull GQF: curl from zenodo
os.system('curl https://zenodo.org/api/files/d50ee30e-31cc-4e90-b2ba-f1e26401ef4a/huntermBerkeley/gqf-artifacts-v1.0.zip --output gqf.zip')
os.system('unzip gqf.zip')

#rename to something not super weird
os.system("mv huntermBerkeley-gqf-artifacts-97bc64a gqf")
os.system("rm gqf.zip")

print("GQF Download done.")


#download TCF

os.system("git clone https://github.com/huntermBerkeley/pog_warp_tests.git")

print("TCF test Downloaded - library download is deferred to cmake initialization")

os.system("git clone https://github.com/huntermBerkeley/bulk-tcf.git")

print("Bulk TCF downloaded")
print("All tests downloaded")