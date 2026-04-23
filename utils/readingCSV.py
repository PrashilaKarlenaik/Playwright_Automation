import csv

def readdatafromCSV(csvPath):
    data=[]
    with open("testData\\sampleCsvdata.csv") as csvfile:
        dataincsv=csv.DictReader(csvfile)
        for row in dataincsv:
            data.append(row)
    print(data)  