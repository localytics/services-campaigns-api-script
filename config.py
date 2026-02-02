
# -------- Campaign Template  --------

campaign_template = {
    "name": "Dashboard Campaign Name - campaigns API",
    "status": "draft",
    "goal": "notify",
    "conversion_event": {
        "event_name": "Localytics Push Opened"
    },
    "audiences": {
        "campaign_type": "saved_audience",
        "control_group_percent": 5,
        "target_rules": {
        "audiences":[123456]
        }
    },
    "creatives": 
        [
            {
                "title": "Default Dasboard Creative Name",
                "build_attributes": {
                    "push_title": "Hello!",
                    "push_message": "Push message body",
                }
            }

            # add more creatives here
        ],
    "schedule": {
        "on_schedule": {
        "begin_date": "2026-04-01T17:00:00.000Z",
        }

        # you could utilize the following timestamp converter for begin_date: https://www.timestamp-converter.com/
    }
}


# -------- APP CONFIG --------

apps_config = [

    # app 1 config
    {        
        "app_key": "app-1-key",
        "audience_id":123456
    },
    # app 2 config
    {
        "app_key": "app-2-key",
        "audience_id":123456
    }

    # Add more apps here
]