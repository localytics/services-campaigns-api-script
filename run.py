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
    app_id = app["app_id"]
    campaign_body = deepcopy(config.campaign_template)

    # apply overrides (shallow replace)
    for key, val in app.get("override", {}).items():
        campaign_body[key] = val

    url = (
        f"https://dashboard.localytics.com/api/v6/"
        f"orgs/{ORG_ID}/apps/{app_id}/push/campaigns"
    )

    response = requests.post(
        url,
        json=campaign_body,
        auth=HTTPBasicAuth(API_KEY, API_SECRET),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 201:
        print(f"✅ Created campaign for app {app_id}")
    else:
        print(
            f"❌ Failed for app {app_id} "
            f"({response.status_code}): {response.text}"
        )