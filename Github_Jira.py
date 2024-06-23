from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

#creating Flask application instance
app= Flask(__name__)

@app.route("/createJira",methods=['POST'])
def create_Jira_incident():
    url = "https://vsg******.atlassian.net/rest/api/3/issue"

    API_TOKEN = "**************"
    auth = HTTPBasicAuth("vs******@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "project": {
        "key": "AP"
        },
        "issuetype": {
        "id": "10007"
        },
        "summary": "Creating Issue Ticket for BUG",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
        

app.run('0.0.0.0',port=5000)
