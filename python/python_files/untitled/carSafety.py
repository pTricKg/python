#import first library
import urllib.request # internet interface
#import second library
from json import load # json data structure

#Declare and assign value for apiUrl variable here
apiUrl = urllib.request.urlopen("http://www.nhtsa.gov/webapi/api/SafetyRatings")
#Declare and assign value for apiParam variable here
apiParam = "/modelyear/1995" # change this to pull specific data using "/param/param"
#Declare and assign value for outputFormat variable for response format in querystring
outputFormat = "?format=json"
#Combine all three variables to make up the complete request URL
response = urllib.request.urlopen(apiUrl + apiParam + outputFormat)

#code below is only to handle JSON response object/format
#use equivalent sets of commands to handle xml response object/format
json_obj = load(response)

#Load the Result (vehicle collection) from the JSON response
print ('------------------------------')
print ('           Result			 ')
print ('------------------------------')
for objectCollection in json_obj['Results']:
	# Loop each vehicle in the vehicles collection
    for safetyRatingAttribute, safetyRatingValue in objectCollection.iteritems():
        print (safetyRatingAttribute, ": ", safetyRatingValue)

# After running this example, feel free to explore the results below
