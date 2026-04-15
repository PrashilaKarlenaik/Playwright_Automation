import json

def readingJSONData(jsonPath):
    with open(jsonPath) as f:
        testData=json.load(f)
        return testData