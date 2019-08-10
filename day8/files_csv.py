import csv
data_list1 = [

    [1001, "Python", 2019, 1, "Heraizen"],
    [1002, "Web", "2018", 1, "Spaneos"],
    [1003, "Java", "2020", 1, "Heraizen"]
    ]

data_list2 = [
    {"id":1001, "wname":'Python','year':'2019', 'status':1, 'company':'Heraizen'},
    {"id":1002, "wname":'UI','year':'2018', 'status':0, 'company':'Spaneos'}
]

try:
    with open("ws1.txt","w") as f1:
        for d in data_list1:
            line1 = f"{d[0]} , {d[1]} , {d[2]} , {d[3]} , {d[4]}\n"
            f1.write(line1)
    with open("ws2.txt","w") as f2:
        for d in data_list2:
            line2 = f"{d['id']} , {d['wname']} , {d['year']} , {d['status']} , {d['company']}\n"
            f2.write(line2)

    with open('ws3.csv','w') as f3:
        heading = ['id','wname','year','status','company']
        obj = csv.DictWriter(f3,fieldnames = heading)
        obj.writeheader()
        obj.writerows(data_list2)

    with open('ws4.csv','w') as f4:
        head = ["ID","","Year"]
        writer = csv.writer(f4)
        writer.writerows(data_list1)
except Exception as e:
    print(e)