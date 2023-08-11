from tikapi import TikAPI, ValidationException, ResponseException
import json

api = TikAPI("myAPIKey")
# Read the JSON data from the file
with open("/Users/bilibala/Study/SLA-TIKTOK/cre/tik.json", "r") as file:
    json_data = json.load(file)

# Extract the API key from the JSON data
api_key = json_data["api_key"]

# Create the TikAPI object with the extracted API key
api = TikAPI(api_key)


payload = {
    "offset": 0,  # Start with offset 0
    "limit": 10  # Number of items per page
}


try:
    response = api.public.hashtag(
        name="sluchawki"
    )

    hashtagId = response.json()['challengeInfo']['challenge']['id']

    response = api.public.hashtag(
        id=hashtagId
    )

    print(response.json())

    with open("/Users/bilibala/Study/SLA-TIKTOK/results/sluchawki3-1.json", "a") as file:
        while response:
            cursor = response.json().get('cursor')
            print("Getting next items ", cursor)

            # Write the response data to the file
            json.dump(response.json(), file, indent=4)

            file.write('\n')  # Add a new line for each response to separate them

            response = response.next_items()

            # Check if there are more items to fetch
            if int(cursor) > 10:
                payload['offset'] += payload['limit']
            else:
                break
    cursor = '11'
    with open("/Users/bilibala/Study/SLA-TIKTOK/results/sluchawki3-2.json", "a") as file:
        while response:
            cursor = response.json().get('cursor')
            print("Getting next items ", cursor)

            # Write the response data to the file
            json.dump(response.json(), file, indent=4)

            file.write('\n')  # Add a new line for each response to separate them

            response = response.next_items()

            # Check if there are more items to fetch
            if int(cursor) > 20:
                payload['offset'] += payload['limit']
            else:
                break

    # while(response):
    #     cursor = sluchawki.json().get('cursor')
    #     print("Getting next items ", cursor)
    #     response = response.next_items()

except ValidationException as e:
    print(e, e.field)

except ResponseException as e:
    print(e, e.response.status_code)
