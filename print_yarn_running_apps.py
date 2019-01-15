# This is the script to get the list of applications which are running for more than N hours

import json, urllib.request

# Passing the rest api url of the resource manager and filtering the applications to fetch the running ones
rm="http://cluster_url:8088/ws/v1/cluster/apps?states=RUNNING"

# Setting the threshold. In RM, time duration is measured in milliseconds 
threshold=3600000  # Given 1 hour as threshold. You can change it as per requirements.

# Calling the RM api and storing the data in json. Added the decode('utf8') as python requires it for versions below 3.6
# You can check the results by entering the variable data in the python idle.
with urllib.request.urlopen(rm) as response:
	data=json.loads(response.read().decode('utf8'))

print ("Below applications are running for more than 1 hour. Kindly look into it")

# The json has a dictionary key 'apps' which has applications as values (which are again nested key value pairs). 
# Now we're iterating through the each app and check whether app's elapsed time is more than our threshold (1 hour).
# If it's running for more than an hour, the app details will be printed.

for running_apps in data['apps']['app']:
    if running_apps['elapsedTime']>threshold:
        print ("\nApp Name: {}".format(running_apps['name']))
        print ("Application id: {}".format(running_apps['id']))
        print ("Total elapsed time: {} hours".format(round(running_apps['elapsedTime']/1000/60/60)))
        print ("Tracking Url: ",running_apps['trackingUrl'])
