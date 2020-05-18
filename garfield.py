#########################################################
#   This script downloads all the Garfield comics       #
#   from its inception, i.e. 19th June, 1978            #
#########################################################
#   Author : Rashid Khan                                #
#   Email  : rashood.khan@gmail.com                     #
#########################################################

from datetime import date,timedelta
import urllib2
import os

def daterange(start,end):
    for x in range(int ((end - start).days)):
        yield start + timedelta(x)

#Create the Directory, if not already existing
dir = "./garfield/"
if not os.path.exists(dir):
    os.makedirs(dir)
    
start_date = date.today()
    
#Garfield Started on 19th June, 1978
start_date = start_date.replace(year=1978,month=6,day=19)
end_date = date.today()

for single_day in daterange(start_date,end_date):
    link = "https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/" + (str(single_day)[:4]) + "/" + str(single_day) + ".gif"
    print(single_day)

    #checks whether the files already exist or not  
    filename = dir+str(single_day)+".gif"
    if not os.path.exists(filename): 
        try:
            f = urllib2.urlopen(link)
        except urllib2.URLError,e:
            if e.code == 404:
                continue
        print ("Downloading :: " + link)
    
        save_file = open(dir+str(single_day)+".gif","w"+'b')
        save_file.write(f.read())
        save_file.close()

print "Garfield Comics has been downloaded"
print "Thanks for using! :)"
