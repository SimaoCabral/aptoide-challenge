import base64

import requests

#After making a test request to link, the response says that the missing parameter name is aptoide_uid

missing_key = "aptoide_uid"
dummy_value = "testchallenge"
filename = "download_file/"+dummy_value + ".apk"
link = "https://aptoide-mmp.aptoide.com/api/v1/download/b2VtaWQ9VGVjaENoYWxsZW5nZVB5dGhvbiZwYWNrYWdlX25hbWU9Y29tLmZ1bi5sYXN0d2FyLmdwJnJlZGlyZWN0X3VybD1odHRwczovL3Bvb2wuYXBrLmFwdG9pZGUuY29tL2FwcHMvY29tLWZ1bi1sYXN0d2FyLWdwLTk5OTk5LTY2NjEyOTMwLWE3MThmOWZlMjE5OGM1Y2EyYzIwMmUwNDYzZTVkZDk1LmFwaw==?resolution=1080x1776"
split_link = link.split('/')
#Get base64 parameters from URL
base64encoded,decoded_param = split_link[-1].split('?')
#Decoding base64 values
base64encoded += "=" * (4 - len(base64encoded) % 4)
initial_params = base64.b64decode(base64encoded).decode('utf-8')
#Reconstructing parameters
completed_params = initial_params +"&"+missing_key+"="+dummy_value+"&"+decoded_param
#Encoding to base64
encoded_params = base64.b64encode(completed_params.encode('utf-8')).decode('utf-8')

split_link[-1] = encoded_params
request_link = '/'.join(split_link)
response = requests.get(request_link)

print(response.status_code)
print(f"Status code: {response.status_code}")
if response.status_code == 200:
    with open(filename, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=128):
            fd.write(chunk)
else:
    print(f"Error: {response.content}")

