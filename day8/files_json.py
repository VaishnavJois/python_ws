import json

data_list2 = [
    {"id":1001, "wname":'Python','year':'2019', 'status':1, 'company':'Heraizen'},
    {"id":1002, "wname":'UI','year':'2018', 'status':0, 'company':'Spaneos'}
]

try:
    with open('wsJSON1.json','w') as j1:
        json.dump(data_list2,j1,indent=4)
        print(json.dumps(data_list2,indent=4))

    with open('wsJSON2.json','r') as j2:
        newL = json.load(j2)
        for w in newL:
            print(f"Id : {w['regno']}, Name : {w['wname']}, Year : {w['year']}, Status : {w['status']}, Company : {w['company']}")

    with open('wsJSON1.json','r') as w, open('student.json','r') as s:
        s_lst = json.load(s)
        w_lst = json.load(w)
    
    for i in s_lst:
        for j in w_lst:
            if i['cid'] == j['id']:
                print(f"{w['wname']}")

except Exception as e:
    print(e)