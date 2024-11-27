import requests
from enum import Enum


# {"curiosity" : 0,"opportunity" : 0, "spirit" : 0, "name" : ""}

# Perseverance rover
# Abbreviation 	Camera
# EDL_RUCAM 	Rover Up-Look Camera
# EDL_RDCAM 	Rover Down-Look Camera
# EDL_DDCAM 	Descent Stage Down-Look Camera
# EDL_PUCAM1 	Parachute Up-Look Camera A
# EDL_PUCAM2 	Parachute Up-Look Camera B
# NAVCAM_LEFT 	Navigation Camera - Left
# NAVCAM_RIGHT 	Navigation Camera - Right
# MCZ_RIGHT 	Mast Camera Zoom - Right
# MCZ_LEFT 	Mast Camera Zoom - Left
# FRONT_HAZCAM_LEFT_A 	Front Hazard Avoidance Camera - Left
# FRONT_HAZCAM_RIGHT_A 	Front Hazard Avoidance Camera - Right
# REAR_HAZCAM_LEFT 	Rear Hazard Avoidance Camera - Left
# REAR_HAZCAM_RIGHT 	Rear Hazard Avoidance Camera - Right
# SKYCAM 	MEDA Skycam
# SHERLOC_WATSON 	SHERLOC WATSON Camera

# Abbreviation 	    Camera 	                                            Curiosity 	Opportunity 	Spirit
# FHAZ 	            Front Hazard Avoidance Camera 	                    ✔       	✔ 	            ✔
# RHAZ 	            Rear Hazard Avoidance Camera 	                    ✔ 	        ✔           	✔
# MAST 	            Mast Camera 	                                    ✔ 		
# CHEMCAM           Chemistry and Camera Complex 	                    ✔ 		
# MAHLI 	        Mars Hand Lens Imager 	                            ✔ 		
# MARDI 	        Mars Descent Imager 	                            ✔ 		
# NAVCAM 	        Navigation Camera 	                                ✔ 	        ✔ 	            ✔
# PANCAM 	        Panoramic Camera 		                                        ✔   	        ✔
# MINITES           Miniature Thermal Emission Spectrometer (Mini-TES) 		        ✔ 	            ✔


class APIS(Enum):
    EPIC = "https://epic.gsfc.nasa.gov/api/"
    CURIOSITY_ROVER = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    
    def getQueryParameters(api):
        if api==APIS.CURIOSITY_ROVER:
            return APIS.curiosityRoverParameters()
        
        return
    
    
    
    
    def curiosityRoverParameters():
        return {"sol", "earth_date", "camera"}
    def roverCameraParameters(perseverance : bool):
        if not perseverance:
            return {"FHAZ" : {"curiosity" : 1,"opportunity" : 1, "spirit" : 1, "name" : "Front Hazard Avoidance Camera"}, 
                    "RHAZ" : {"curiosity" : 1,"opportunity" : 1, "spirit" : 1, "name" : "Rear Hazard Avoidance Camera"}, 
                    "MAST" : {"curiosity" : 1,"opportunity" : 0, "spirit" : 0, "name" : "Mast Camera"}, 
                    "CHEMCAM" : {"curiosity" : 1,"opportunity" : 0, "spirit" : 0, "name" : "Chemistry and Camera Complex"}, 
                    "MAHLI" : {"curiosity" : 1,"opportunity" : 0, "spirit" : 0, "name" : "Mars Hand Lens Imager"}, 
                    "MARDI" : {"curiosity" : 1,"opportunity" : 0, "spirit" : 0, "name" : "Mars Descent Imager"}, 
                    "NAVCAM" : {"curiosity" : 1,"opportunity" : 1, "spirit" : 1, "name" : "Navigation Camera"}, 
                    "PANCAM" : {"curiosity" : 0,"opportunity" : 1, "spirit" : 1, "name" : "Panoramic Camera"}, 
                    "MINITES" : {"curiosity" : 0,"opportunity" : 1, "spirit" : 1, "name" : "Miniature Thermal Emission Spectrometer (Mini-TES)"}}
        return {
            "EDL_RUCAM" : "Rover Up-Look Camera", 
            "EDL_RDCAM" : "Rover Down-Look Camera", 
            "EDL_DDCAM" : "Descent Stage Down-Look Camera", 
            "EDL_PUCAM1" : "Parachute Up-Look Camera A", 
            "EDL_PUCAM2" : "Parachute Up-Look Camera B", 
            "NAVCAM_LEFT" : "Navigation Camera - Left", 
            "NAVCAM_RIGHT" : "Navigation Camera - Right", 
            "MCZ_RIGHT" : "Mast Camera Zoom - Right", 
            "MCZ_LEFT" : "Mast Camera Zoom - Left", 
            "FRONT_HAZCAM_LEFT_A" : "Front Hazard Avoidance Camera - Left", 
            "FRONT_HAZCAM_RIGHT_A" : "Front Hazard Avoidance Camera - Right", 
            "REAR_HAZCAM_LEFT" : "Rear Hazard Avoidance Camera - Left", 
            "REAR_HAZCAM_RIGHT" : "Rear Hazard Avoidance Camera - Right", 
            "SKYCAM" : "MEDA Skycam", 
            "SHERLOC_WATSON" : "SHERLOC WATSON Camera"}


fileWrittenTo = "links.txt"
API_IN_USE = APIS.CURIOSITY_ROVER


class APIQuery():
    
    def __init__(self, API, params) -> None:
        self.api = API
        self.params = self.initialParams(params)
        pass
    
    def initialParams(self, paramInput):
        paramInput["API_KEY"] = "DEMO_KEY"
        
        
        # add params based on API
        """
        my thought process on how to do this is basically that Id need to check the manifest of the API for number of days, earth and otherwise, 
        
        """
        
        return
    
    def askCamera():
        return
    
    def sendQuery(self):
        return
    
    def writeToFile(htmlResponse):

            try:
                jsonRes = htmlResponse.json() # json output of text file
            except requests.JSONDecodeError:
                print("Invalid API keys entered")
                return
            else:
                with open(fileWrittenTo, "w") as file:
                    # print(htmlResponse.content)

                    # print(jsonRes["photos"][0]["img_src"])
                    # print(len(jsonRes["photos"]))

                    for i in range (len(jsonRes["photos"])):
                        file.write(f"{jsonRes["photos"][i]["img_src"]}\n")
                        # print(i)

def main(params):
    # so i wanna do a get request of this github link

    # do a get request of api listed above
    url = API_IN_USE.value
    params = {"api_key" : "DEMO_KEY"}
    params["sol"] = "1000"

    response = requests.get(url, params)

    if response:
        print("Link to NASA successfull!")
        writeToFile(response)
    else:
        raise Exception(f"Non-success status code: {response.status_code}")


if __name__ == "__main__":
    print("Hello, World!")
    
    main({})