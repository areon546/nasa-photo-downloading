import requests
# so i wanna do a get request of this github link

# do a get request of api listed above
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {"api_key": "DEMO_KEY", "sol" : "1000"}

response = requests.get(url, params)

if response:
    print("Success!")

    jsonRes = None

    with open("content.json", "w") as file:
        # file.write(response.text)

        jsonRes = response.json() # json output of text file

    print(jsonRes["photos"][0]["img_src"])
    print(len(jsonRes["photos"]))


    ## continue


else:
    raise Exception(f"Non-success status code: {response.status_code}")
