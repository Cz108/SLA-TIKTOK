from tikapi import TikAPI, ValidationException, ResponseException
import json

api = TikAPI("EhR5TtH42oB63qpOintM4DfgAcSHNG0n3WKtRTQI1uagHiSW")

try:
    response = api.public.check(
        username="spencerx"
    )

    # print(sluchawki.json())
    # Convert the dictionary to a JSON-formatted string with indentation
    formatted_json = json.dumps(response.json(), indent=4)

    # Print the formatted JSON
    print(formatted_json)
    # Write the formatted JSON to a file
    with open('/Users/bilibala/Study/SLA-TIKTOK/results/spencerx.json', 'w') as file:
        file.write(formatted_json)

except ValidationException as e:
    print(e, e.field)

except ResponseException as e:
    print(e, e.response.status_code)
