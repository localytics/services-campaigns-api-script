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
✅ Created campaign for app app-1-key
✅ Created campaign for app app-2-key
```

---

## Repository Structure

```
services-campaigns-api-script-master/
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

1. Download Python from: https://www.python.org/downloads/mac-osx/

2. Run the installer  

---

#### Windows

1. Download Python from: https://www.python.org/downloads/windows/

2. Run the installer  
3. **Important:** Check the box while installing: ✅ *Add Python to PATH*

---
#### Verify installation

Open terminal (command prompt for Windows) and run the command below

```powershell
python --version
```
#### Note: This script was tested against Python version 3.14.2
---

### 2. Install Dependencies

This script requires two Python packages:

- `requests`
- `python-dotenv`

Install them by opening terminal and running following command:

```bash
pip install requests python-dotenv
```

---

## Script Setup Instructions

Download and unzip the repository files, then follow the instructions below.

### 1. Open .env file, add your Localytics API credentials and Org ID

```env
API_KEY = your_api_key_here
API_SECRET = your_api_secret_here
ORG_ID = 123456
```

---

### 2. Modify config.py file

`config.py` contains a basic Push campaign template object which creates a campaign targeting a saved audience. Please review this template object thoroughly, as this defines every configuration in your campaign, starting from the campaign's name and goal, and until the desired campaign scheduling, just like the dashboard.

You can modify the template object to match your desired campaign. e.g. change the push message title and body, as well as the conversion event for your campaign.

For advanced modifications to the campaign template object, please refer to the [Campaigns API documentation](https://docs.localytics.com/campaigns_audiences_api.html) for clarification on the values accepted by the Campaigns API when modifying the template.

---

#### App Keys

Below the campaign_template, you will see a list of apps in the apps_config object. These are the apps which the script loops through to create a campaign for each app, targeting the specified audience for that app. 

Replace the app_key and audience_id values with the proper values. You can add as many apps as you need.

```python
apps_config = [
    {
        "app_key": "app-1-key",
        "audience_id":123456
    },
    {
        "app_key": "app-2-key",
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

Once everything is configured, follow the steps below to run the script:

- Open terminal
- Navigate to where you saved the downloaded repository files using the `cd folder_path` command. (an example is shown below)
- Run the script using the command `python run.py`

Since the script is saved inside my Downloads folder, I ran the following command in terminal to navigate to the script: 

`cd Downloads\services-campaigns-api-script-master`

Followed by the command to run the script:

`python run.py`


```
C:\Users\username>cd Downloads\services-campaigns-api-script-master
C:\Users\username\Downloads\services-campaigns-api-script-master>python run.py
✅ Created campaign for app <redacted>
✅ Created campaign for app <redacted>

C:\Users\username\Downloads\services-campaigns-api-script-master>
```
The script will create a push campaign for every app listed in `apps_config`.


---

# Optional Overrides

In the apps_config object, you can `override` any of the campaign_template objects for each app separately. So objects such as conversion_event, audiences, creatives, etc.

Utilizing this would be beneficial if you need to send the same campaign for multiple apps, but with small changes between each app, such as a slightly different creative message or a different conversion event.

The example below shows how you can override the creative as well as the conversion event for an app using `override`.

```python
apps_config = [

    # app 1 config
    {
        "app_key": "app-1-key",
        "audience_id":112233,
        "override": {
            "creatives": [
                            {
                                "build_attributes": {
                                    "push_title": "Hello!",
                                    "push_message": "Customized message for app 1",
                                }
                            }
                        ],
            "conversion_event": {
                "event_name": "Purchase Completed"
            }
        }
    },
    # app 2 config
    {        
        "app_key": "app-2-key",
        "audience_id":223344,
        "override": {
            "creatives": [
                            {
                                "build_attributes": {
                                    "push_title": "Hello!",
                                    "push_message": "Customized message for app 2",
                                }
                            }
                        ],
            "conversion_event": {
                "event_name": "Cart Abandoned"
            }
        }
    }

    # Add more apps here
]
```


#### Notes About Override:

Overrides will replace the entire top level object with the one you specify, so make sure you include all required parameters of an object when you override. That means overriding something like `creatives` will replace the entire creatives block for that app.

This is intentional for simplicity.

---

# Future Improvements

Possible future upgrades include:

- Fetching audiences to verify they properly match app IDs before creating campaigns
