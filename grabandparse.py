import requests
import xml.etree.ElementTree as ET
import json
import urllib3
import re
import os
from dotenv import load_dotenv


from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('PAN_API_KEY')
device_group = os.getenv('DEVICE_GROUP')
fw_host = os.getenv("FW_HOST")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print(f"Device Group: {device_group}")
print(f"Hostname: {fw_host}")


# REST API URL
url_prerule = f"https://{fw_host}/restapi/v10.2/Policies/SecurityPreRules?location=device-group&device-group={device_group}"
url_postrule = f"https://{fw_host}/restapi/v10.2/Policies/SecurityPostRules?location=device-group&device-group={device_group}"
url_device_groups = f"https://{fw_host}/restapi/v10.2/Panorama/DeviceGroups"


# Headers
headers = {
    'X-PAN-KEY': api_key,
}

# Send the API request for device groups
response_device_groups = requests.get(url_device_groups, headers=headers, verify=False)

# Parse the JSON response
data_device_groups = response_device_groups.json()

# Write the device groups data to a file
with open('device_groups.json', 'w') as f:
    json.dump(data_device_groups, f)


# Function to parse and print policy details
def parse_and_print_policies(data):
    validation_required = []
    
    if 'entry' in data.get('result', {}):
        for policy in data['result']['entry']:
            tags = policy.get('tag', {}).get('member', [])
        
            # Skip policies with the "Manually Added" tag
            if 'Manually Added' in tags:
                continue

            name = policy['@name']
            description = policy.get('description', 'No description')
            
            # If there's no description, use the current name as the description
            if description == 'No description':
                description = name
            
            # If the description contains "advanced" and "ifc", add to the validation list
            if "advanced" in description and "ifc" in description:
                validation_required.append(name)
                continue

            # Find the text after "L4 RULE: " or "L7 RULE: "
            match = re.search(r'(L4 RULE: |L7 RULE: )(.*)', description)
            if match:
                description = match.group(2)
            
            print(f'rename device-group {device_group} pre-rulebase security rules {name} to "{description}"\n')

        print("\nThe following policies require validation as the description indicates issues with the migration:")
        for policy in validation_required:
            print(policy)



# Send the API request for pre-rulebase
response_pre = requests.get(url_prerule, headers=headers, verify=False)

# Parse the JSON response
data_pre = response_pre.json()

# Print the pre-rulebase policy details
print("Pre-Rulebase Security Policies:\n")
if 'entry' in data_pre.get('result', {}):
    parse_and_print_policies(data_pre)
else:
    print('No entry found in the data for pre-rulebase.')

# Send the API request for post-rulebase
response_post = requests.get(url_postrule, headers=headers, verify=False)

# Parse the JSON response
data_post = response_post.json()

# Print the post-rulebase policy details
print("Post-Rulebase Security Policies:\n")
if 'entry' in data_post.get('result', {}):
    parse_and_print_policies(data_post)
else:
    print('No entry found in the data for post-rulebase.')


# REST API URL for device groups
url_device_groups = f"https://{fw_host}/restapi/v10.2/Panorama/DeviceGroups"

# Send the API request for device groups
response_device_groups = requests.get(url_device_groups, headers=headers, verify=False)

# Parse the JSON response
data_device_groups = response_device_groups.json()

# Extract the names of all device groups
device_group_names = [entry["@name"] for entry in data_device_groups.get("result", {}).get("entry", [])]

# Save the device group names to a file
with open("device_groups.txt", "w") as file:
    for name in device_group_names:
        file.write(name + "\n")

