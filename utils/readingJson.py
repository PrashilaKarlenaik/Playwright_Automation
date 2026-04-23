import json

def readJSONData(jsonPath):
    with open(jsonPath) as f:
        testData=json.load(f)
        return testData
    


#1.With open file command we can load the json file and save it in variable f
#2.json.load(f) will convert my data into dictionary format and save it in variable testData

