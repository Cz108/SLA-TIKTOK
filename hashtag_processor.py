import json

# File path to the JSON data
file_path = "/Users/bilibala/Study/SLA-TIKTOK/results/sluchawki.json"

# Read the JSON data from the file
with open(file_path, "r") as file:
    json_data = file.read()

# Load the JSON data as a Python dictionary
data = json.loads(json_data)

for item in data["itemList"]:
    print("-"*50)
    print("User Name用户名:", item["author"]["nickname"])
    print("User Signature用户签名:", item["author"]["signature"])
    print("Follower Count粉丝数:", item["authorStats"]["followerCount"])
    print("Following Count关注:", item["authorStats"]["followingCount"])
    print("Total Hearts点赞数量:", item["authorStats"]["heartCount"])
    print("Total Videos发布视频数量:", item["authorStats"]["videoCount"])


