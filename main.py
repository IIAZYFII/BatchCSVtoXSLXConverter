import pandas
import os
file_names = []
path = "Path\\to\\directory"
for file in os.listdir(path):
    if file.endswith(".csv"):
        file_names.append(file)

for file in file_names:
    filePath = path + '/' + file
    print(filePath)
    csv = pandas.read_csv(path + '/' + file)
    file = file[:-3] + 'xlsx'
    writer = pandas.ExcelWriter(file)
    csv.to_excel(writer, index= False)
    writer.save()



