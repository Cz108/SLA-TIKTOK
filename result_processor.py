import json

# File path to the JSON data
file_path = "/Users/bilibala/Study/SLA-TIKTOK/results/spencerx.json"

# Read the JSON data from the file
with open(file_path, "r") as file:
    json_data = file.read()

# Load the JSON data as a Python dictionary
data = json.loads(json_data)

# Access and print specific values from the dictionary
print("User Signature:", data["userInfo"]["user"]["signature"])
print("Follower Count:", data["userInfo"]["stats"]["followerCount"])
print("Following Count:", data["userInfo"]["stats"]["followingCount"])
print("Total Hearts:", data["userInfo"]["stats"]["heartCount"])
