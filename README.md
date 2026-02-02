# Localytics Campaigns API template script

This repository contains a simple Python script that creates **Push Campaigns** in the Localytics dashboard using the Localytics **Campaigns API**.

The script is designed to:

- Define a reusable **push campaign template**
- Loop through a list of `app_key` values and their associated audiences
- Apply per-app custom tweaks (optional overrides)
- Create one campaign per app automatically

This makes it easy to launch the same campaign across multiple Localytics apps without manually recreating it in the dashboard, and with minimal configurational overhead.

Example output:

```
✅ Created campaign for app app-key-1
✅ Created campaign for app app-key-2
```

---

## Repository Structure

```
services-campaigns-api/
├── run.py          # Main script that executes the API requests
├── config.py       # campaign template + list of app keys
├── .env            # API credentials
└── README.md
```

---

## Requirements

### 1. Install Python

---

#### macOS

1. Download Python from:

https://www.python.org/downloads/mac-osx/

2. Run the installer  

---

#### Windows

1. Download Python from:

https://www.python.org/downloads/windows/

2. Run the installer  
3. **Important:** Check the box:

✅ *Add Python to PATH*

4. Verify installation:

```powershell
python --version
```
---
#### Note: This script was tested against Python version 3.14.2
---

### 2. Install Dependencies

This script requires two Python packages:

- `requests`
- `python-dotenv`

Install them by opening terminal (or command prompt on Windows) and running following pip command:

```bash
pip install requests python-dotenv
```

---

## Script Setup Instructions

### 1. Add your Localytics API credentials and Org ID to the .env file

```env
API_KEY = your_api_key_here
API_SECRET = your_api_secret_here
ORG_ID = 123456
```

---

### 2. Modify the config.py file

Open `config.py`

You will find a basic Push campaign template object which creates a campaign targeting a saved audience. Please review this template object thoroughly, as this defines every configuration in your campaign, starting from the campaign's name and goal, and until the desired campaign scheduling, just like the dashboard.

You can modify the template object to match your desired campaign. e.g. change the push message title and body, as well as the conversion event for your campaign.

Please refer to the [Campaigns API documentation](https://docs.localytics.com/campaigns_audiences_api.html) for clarification on the values accepted by the Campaigns API when modifying the template.


Below the campaign_template, you will see a list of apps in the apps_config object. These are the apps which the script loops through to create a campaign for each app, targeting the specified audience for that app. 

Repalce the app_key and audience_id values with the proper values. You can add as many apps as you need.

```python
apps_config = [
    {
        "app_key": "app-key-1",
        "audience_id":123456
    },
    {
        "app_id": "app-key-2",
        "audience_id":654321
    }
    # add more apps here
]
```

#### Notes on apps_config: 

- You will find the App key for each app in the dashboard's Settings page

- Make sure the audience_id specified under each app is accurate. If an audience with the specified audience ID does not exist for that app, the campaign will not be created for that app.

- You can double check an audience ID through the dashboard's Audiences page.

---

# Running the Script

Once everything is configured, open terminal and navigate to the repository's directory, and run the command below.

```bash
python run.py
```

The script will create a push campaign for every app listed in `apps_config`.


---

# Optional Overrides

In the apps_config object, you can apply an `override` per-app custom tweaks to any of the top level objects in the template. So objects such as goal, conversion_event, audiences, creatives, etc.

Utilizing this would be benificial if you need to send the same campaign for multiple apps, but with small changes between each app, such as a slightly different creative message or a different conversion event.

The example below shows how you can override the creative as well as the conversion event for an app using `override`.

```python
{        
    "app_id": "app-key-1",
        "override": {
            "creatives": [
                            {
                                "build_attributes": {
                                    "push_title": "Hello!",
                                    "push_message": "Custom message for app 1",
                                    "ll_deep_link_url": "app://homescreen"
                                }
                            }
                        ],
            "conversion_event": {
                "event_name": "Purchase Completed"
            }
        }
}
```


#### Notes About Override

Overrides will replace the entire top level object with the one you specify, so make sure you include all required parameters of an object when you override. That means overriding something like `creatives` will replace the entire creatives block for that app.

This is intentional for simplicity.
---

# Future Improvements

Possible future upgrades include:

- Fetching audiences to verify they properly match app IDs before creating campaigns
