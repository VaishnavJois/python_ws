import re

data = "1001 DBMS 20   1002 JS 23    1003 SQL 15"
l1 = re.split(r"\s+",data) #r -> raw string _ special characters
print(l1)

l2 = re.findall(r"\d{4}",data)
print(l2)

print(re.findall(r"[A-z]+",data))
############################################################
d2 = "Vaishnav is in 574108 at Ajekar and Eddie is in 576121 at Parkala"
print('')
print(re.findall(r"\d{6}",d2))

print('Place name:')
print(re.findall(r"at\s+([A-z]*)\s?",d2))

############################################################
d3 = "House number 198 and pincode 560070"
res = re.search(r"\d+",d3)
print(res.start())
print(res.end())
print(f'start() and end() method: {d3[res.start():res.end()]}')
print(f'Using group function : {res.group()}')

############################################################

data = "blue shape red toy green"
rep = re.sub('(blue|red|green)','color', data)
print(rep)
############################################################

tuplist = "1001 DBMS 20   1002 JS 23    1003 SQL 15"

reptup = re.findall(r'(\d{4})\s([A-z]*)\s+(\d{2})',tuplist)
print(reptup)

############################################################

data = "Lakshman and Amalraj are good friends, Arjun and Aruna also are also friends with Anu"
lst = re.findall(r'\bA[a-z]{4,}',data,flags=re.IGNORECASE)
print(lst)

############################################################

html = """
<ul>
    <li>One</li>
    <li>Two</li>
</ul>
"""
html_res = re.findall("<.*?>(.*)</.*?>",html)
print(html_res)

############################################################
#exercise 
#1
emails = """krishna.t@wipro.com
lakshman.a@spaneos.com
lakshman.a@heraizen.edu"""

e_res = re.findall("@([A-z]+).",emails)
print(e_res)

#2
rep_special = "Learning- Python, is fun. Python_programming is, easy"
res_special = re.sub(r'-|,|_'," ",rep_special)
res_special = re.sub(r'\s+'," ",res_special)
print(res_special)