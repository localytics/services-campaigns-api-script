import sys
sys.dont_write_bytecode = True
# this ensures the script doesn't use a cached config file from a previous run

import os
from dotenv import load_dotenv

import requests
from copy import deepcopy
from requests.auth import HTTPBasicAuth
import config

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ORG_ID = os.getenv("ORG_ID")


for app in config.apps_config:
    app_key = app["app_key"]
    campaign_body = deepcopy(config.campaign_template)

    # if saved audiences, replace the audience ID value for each app
    if campaign_body.get("audiences", {}).get("campaign_type") == "saved_audience":

        audience_id = app.get("audience_id")
        campaign_body["audiences"]["target_rules"]["audiences"] = [audience_id]


    # apply overrides (shallow replace)
    for key, val in app.get("override", {}).items():
        campaign_body[key] = val

    url = (
        f"https://dashboard.localytics.com/api/v6/"
        f"orgs/{ORG_ID}/apps/{app_key}/push/campaigns"
    )

    response = requests.post(
        url,
        json=campaign_body,
        auth=HTTPBasicAuth(API_KEY, API_SECRET),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 201:
        print(f"✅ Created campaign for app {app_key}")
    else:
        print(
            f"❌ Failed for app {app_key} "
            f"({response.status_code}): {response.text}"
        )