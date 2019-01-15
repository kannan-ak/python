# This is the script to get the list of applications which are running for more than 10 hours
import json, urllib.request

# Passing the rest api url of the resource manager and filtering the applications to fetch the running ones
rm="http://daap.in.zeotap.com:8088/ws/v1/cluster/apps?states=RUNNING"

# Setting the threshold. In RM, time duration is measured in milliseconds 
threshold=3600000

# Calling the RM api and storing the data in json. Added the decode('utf8') as python requires it for versions below 3.6
with urllib.request.urlopen(rm) as response:
	data=json.loads(response.read().decode('utf8'))

#print ("Below applications are running for more than 10 hours. Kindly look into it")


for running_apps in data['apps']['app']:
    if running_apps['elapsedTime']>threshold:
        print ("\nApp Name: {}".format(running_apps['name']))
        print ("Application id: {}".format(running_apps['id']))
        print ("Total elapsed time: {} hours".format(round(running_apps['elapsedTime']/1000/60/60)))
        print ("Tracking Url: ",running_apps['trackingUrl'])