import json
import csv

#Change the Pakistan.json file to exclude lines where high and low casualty estimates are equal to each other
pakistan_fix = []
with open('Pakistan.json', 'r') as file:
    data = json.load(file)
    for line in data:
        if line['high'] != line['low']:
            pakistan_fix.append(line)

#For each line pakistan_fix, calculate the ratio between high and low casualty estimates
#Then append date and casualty ratio pairs to a list for each pair
#Append these pair lists to to a "list of lists" called final_list
final_list = []
for line in pakistan_fix:
    y = []
    y.append(line['year'])
    x = line ['high'] / line ['low']
    y.append(x)
    final_list.append(y)

#Save the final_list to a CSV file for use in R
with open('pakistan2.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    
    writer.writerow(['year', 'Casualty_ratio'])

    for incident in final_list:
        writer.writerow(incident)