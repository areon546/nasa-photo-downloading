
import requests 

def downloadLinkAsImage(link):

    # get request of link provided
    data = requests.get(link).content 

    # Opening a new file named img with extension .jpg 
    # This file would store the data of the image file 
    with open('img.jpg','wb') as f:

        # Storing the image data inside the data variable to the file 
        f.write(data)
    
if __name__ == "__main__":
    downloadLinkAsImage('http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/rcam/RLB_486265291EDR_F0481570RHAZ00323M_.JPG')