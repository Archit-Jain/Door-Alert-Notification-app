import pycurl, json
from StringIO import StringIO

appID = "55d62ff7a4c48a5c79a56cdf"

# add your Instapush Application Secret
appSecret = "6e9612fa562975b34d918f7e7d763b07"
pushEvent = "DoorAlert"
pushMessage = "Please close the door !"

# use this to capture the response from our push API call
buffer = StringIO()

# use Curl to post to the Instapush API
c = pycurl.Curl()

# set API URL
c.setopt(c.URL, 'https://api.instapush.im/v1/post')

#setup custom headers for authentication variables and content type
c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + appID,
			'x-instapush-appsecret: ' + appSecret,
			'Content-Type: application/json'])


# create a dict structure for the JSON data to post
json_fields = {}

# setup JSON values
json_fields['event']=pushEvent
json_fields['trackers'] = {}
json_fields['trackers']['message']=pushMessage
#print(json_fields)
postfields = json.dumps(json_fields)

# make sure to send the JSON with post
c.setopt(c.POSTFIELDS, postfields)

# set this so we can capture the resposne in our buffer
c.setopt(c.WRITEFUNCTION, buffer.write)

print("Push notification sent!\n")

# in the door is opened, send the push request
c.perform()

# capture the response from the server
body= buffer.getvalue()

# print the response
print(body)
# reset the buffer
buffer.truncate(0)
buffer.seek(0)

# cleanup
c.close()

