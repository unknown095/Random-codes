#using pycharm with input and output file in pycharm

import os                                     #import OS module
text_to_find=str("-")                         #search string
text_to_replace=str("\n-")                    #replace string
sourcepath=os.listdir('InputFiles/')          #source path
for file in sourcepath:                       
    inputfile='InputFiles/'+file              #select file path
    print('Conversion is ongoing for:'+inputfile)        #PRINT STATUS
    with open(inputfile,'r') as inputfile:    #OPEN FILE AS READ ONLY
        filedata=inputfile.read()             #Read text in file
        freq=0                                #create count
        freq=filedata.count(text_to_find)     #start count
        destinationpath='Outputfile/'+file    #dest path
        filedata=filedata.replace(text_to_find,text_to_replace)     #replace the needed text
        with open(destinationpath,'w') as file:     #open output file as writeable
            file.write(filedata)                    #write file data
            print('Total %d record Replaced' %freq) #print status
