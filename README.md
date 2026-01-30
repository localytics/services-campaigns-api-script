# Localytics Push Campaign Creator

This repository contains a simple Python script that creates **Push Campaigns** in the Localytics dashboard using the Localytics **Campaigns API**.

The script is designed to:

- Define a reusable **push campaign template**
- Loop through a list of `app_id` values
- Apply per-app custom tweaks (optional overrides)
- Create one campaign per app automatically

This makes it easy to launch the same campaign across multiple Localytics apps without manually recreating it in the dashboard.

---

## What This Script Does

When you run the script, it will:

1. Load your Localytics credentials from a `.env` file  
2. Load the campaign template from `config.py`  
3. Loop through each app object in the config  
4. Create a push campaign via the Localytics API for each `app_id`

Example output:

```
✅ Created campaign for app app-id-1
✅ Created campaign for app app-id-2
```

---

## Repository Structure

```
services-campaigns-API/
├── run.py          # Main script that executes the API requests
├── config.py       # campaign template + list of app IDs
├── .env            # API credentials
└── README.md
```

---

## Requirements

### 1. Install Python

This script was tested against Python version 3.14.2

---

### Python Installation Instructions

---

### macOS

1. Download Python from:

https://www.python.org/downloads/mac-osx/

2. Run the installer  

---

### Windows

1. Download Python from:

https://www.python.org/downloads/windows/

2. Run the installer  
3. **Important:** Check the box:

✅ *Add Python to PATH*

4. Verify installation:

```powershell
python --version
```

### 2. Install Dependencies

This script requires two Python packages:

- `requests`
- `python-dotenv`

Install them using the following pip command in terminal:

```bash
pip install requests python-dotenv
```

---

# Setup Instructions

## 1. Add your Localytics credentials to the .env file

```env
API_KEY = your_api_key_here
API_SECRET = your_api_secret_here
ORG_ID = 123456
```

---

## Modify the config.py file

Open `config.py`.

Modify the campaign_template object parameters to match your desired campaign.

Below the campaign_template, you will see a list of apps like this:

```python
apps_config = [
    {
        "app_id": "app-id-1",
    },
    {
        "app_id": "app-id-2",
    }
]
```

### Update the following:

✅ Replace each `app_id` with a real Localytics App ID  
✅ Optionally add overrides per app

Example override:

```python
{        
    "app_id": "114fc59092317d183a20475-18623c38-39c0-11ec-bc11-007c928ca240",
    "override": {
        "audiences": {
            "campaign_type": "saved_audience",
            "control_group_percent": 5,
            "target_rules": {
            "audiences":[183512]
            }
        }
    }
}
```

---

# Running the Script

Once everything is configured, run:

```bash
python run.py
```

The script will create a push campaign for every app listed in `apps_config`.

---

## Notes About Overrides

Overrides are applied to top level parameters:

That means overriding something like `audiences` will replace the entire audiences block.


This is intentional for simplicity.


---

# Support / Future Improvements

Possible future upgrades include:

- Nested deep-merging overrides
- Fetching audiences to verify they properly match app IDs
