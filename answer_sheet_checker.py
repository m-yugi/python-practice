import csv
header = ['id', 'file_name', 'score']
data = []
passed = 0
for i in range(1, 26):
    new_data = []
    file_name = str(i)+".txt"
    new_data.append(i)
    new_data.append(file_name)
    file = open("answer_sheets\\"+file_name+"", "r")
    answer = (file.read()).split(",")
    key = open("answer_sheets\\key_sheet.txt", "r")
    final_key = (key.read()).split(",")
    mark = 0
    for j in range(len(answer)):
        if(answer[j] == final_key[j]):
            mark += 1
    if(mark >= 6):
        passed += 1
    new_data.append(mark)
    data.append(new_data)
# print(*data)
with open('mark_sheet.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
print("total students passed are :"+str(passed))
