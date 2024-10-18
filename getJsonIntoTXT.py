import requests


def writeToFile(htmlResponse):
        jsonRes = None

        with open("links.txt", "w") as file:
            jsonRes = htmlResponse.json() # json output of text file

            print(jsonRes["photos"][0]["img_src"])
            print(len(jsonRes["photos"]))

            for i in range (len(jsonRes["photos"])):
                file.write(f"{jsonRes["photos"][i]["img_src"]},\n")
                # print(i)

def main(params):
    # so i wanna do a get request of this github link

    # do a get request of api listed above
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params["sol"] = "1000"

    response = requests.get(url, params)

    if response:
        print("Success!")
        writeToFile(response)        
    else:
        raise Exception(f"Non-success status code: {response.status_code}")


if __name__ == "__main__":
    print("Hello, World!")
    
    main()