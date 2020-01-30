import csv
 
def readMyFile(filename):
    dates = []
    scores = []

    with open(filename, 'r', encoding='mac_roman', newline='') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            dates.append(row[1])
            scores.append(row[4])
 
    return dates, scores
 


dates,scores = readMyFile('MPsonTwitter_co_uk.csv')

i=0
for x in dates:
    print(dates[i]+'-'+scores[i])
    i=i+1
