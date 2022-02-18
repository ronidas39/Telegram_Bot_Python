import requests,os,json
from dotenv import load_dotenv
load_dotenv()
pwd=os.getenv("API_KEY")
url="https://api.telegram.org/bot"+pwd+"/setMyCommands?commands="
cmd=[{
    "command":"apicmd1",
    "description":"description for apicmd1"
},
{
    "command":"apicmd2",
    "description":"description for apicmd2"
},
{
    "command":"apicmd3",
    "description":"description for apicmd3"
}]
cmd=json.dumps(cmd)
url=url+str(cmd)
response=requests.get(url)
print(response)


