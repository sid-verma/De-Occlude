import sys
import os
input_path = "/Users/sidverma/Google Drive/Courses/CSCE 689/Project/"
fh = open("MS-Celeb-1M_clean_list.txt", "r")
fo = open("Sample-MS-Celeb_clean_list.txt", "w")
os.chdir(input_path)
for item in os.listdir('.'):
	    if not os.path.isfile(os.path.join('.', item)):
            continue
        try:
            print item
        except:
            continue
fh.close()
fo.close()