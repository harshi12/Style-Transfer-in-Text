import re
bad_chars = ["=","-",")","(",';', ':', '!', "*","@", "#", '"',"&quot","&","/","[","]","~","_",'lt'] 
with open('train.txt', 'r') as file:
    test_string = file.read()
re.sub('@[0-9a-zA-Z]* ', '', test_string)
for i in bad_chars : 
	test_string = test_string.replace(i, '') 
file1 = open("train1.txt","w")
file1.write(test_string)
file1.close()
