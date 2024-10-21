
import requests 

def downloadLinkAsImage(link, imageName):

    # get request of link provided
    data = requests.get(link).content

    # Opening a new file named img with extension .jpg 
    # This file would store the data of the image file 
    with open(imageName,'wb') as f:

        # Storing the image data inside the data variable to the file 
        f.write(data)
    
    
def downloadObjectsFromLink(filename):
    # read file
    with open(filename, "r") as file:
        for line in file:
            line = line.removesuffix("\n")
            print('"'+line+'"')
            print(line.split('/')[-1])
            downloadLinkAsImage(line, fileStructure("cam", "sol1000", line.split('/')[-1]))
            
            
def fileStructure(rootFol, fol2, fileName):
    return (rootFol+"/"+fol2+"/"+fileName)

if __name__ == "__main__":
    downloadObjectsFromLink("links.txt")
    # file = 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/rcam/RLB_486265291EDR_F0481570RHAZ00323M_.JPG'
    # downloadLinkAsImage(file, fileStructure("cam", "sol1000", file.split('/')[-1]))