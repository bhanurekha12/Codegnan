Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary
a={"name":"bhanu","year":2026,"month":"june"}
print(a)
{'name': 'bhanu', 'year': 2026, 'month': 'june'}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['bhanu', 2026, 'june'])
a.items()
dict_items([('name', 'bhanu'), ('year', 2026), ('month', 'june')])
#methods:
#update():adding one are more but should be single {}
a={"city":"vijwda","country":"india"}
a.update({"State":"ap","district":"NTR"})
a
{'city': 'vijwda', 'country': 'india', 'State': 'ap', 'district': 'NTR'}
#setdefault:it would correct itself when error occured
a={"Day":"wednesday","Date":4}
a.setdefault("Time",10)
10
a
{'Day': 'wednesday', 'Date': 4, 'Time': 10}
#get method():
a={"name":"bhanu","mailid":"bhanu@gmail.com"}
a.get("name")
'bhanu'
a
{'name': 'bhanu', 'mailid': 'bhanu@gmail.com'}
#when value is given it will print error
a["name"]
'bhanu'
a.get("bhanu")

a
{'name': 'bhanu', 'mailid': 'bhanu@gmail.com'}
>>> #pop method():
>>> a={"city":"vjwda","mobileno":68456295,"mailid":"bhanu@gmail.com"}
>>> a.pop("city")
'vjwda'
>>> a
{'mobileno': 68456295, 'mailid': 'bhanu@gmail.com'}
>>> a.popitem()
('mailid', 'bhanu@gmail.com')
>>> #copy method():
>>> a={"date":4,"months":6,"time":10}
>>> a.copy()
{'date': 4, 'months': 6, 'time': 10}
>>> #clear():
>>> a={"date":4,"months":6,"time":10}
>>> a.clear()
>>> a
{}
>>> a={"date":4,"months":6,"time":10}
>>> len(a)
3
>>> #dictionary is mutable but doesn't allow same key values again..values can be same
>>> a={"name":"bhanu","city":"vjwda","name":"bhanu"}
>>> print(a)
{'name': 'bhanu', 'city': 'vjwda'}
>>> #if there are same key ad diff value it would print the latest value only
>>> a={"name":"bhanu","city":"vjwda","name":"rekha"}
>>> print(a)
{'name': 'rekha', 'city': 'vjwda'}
>>> a={"name":"bhanu","city":"vjwda","name1":"rekha"}
>>> print(a)
{'name': 'bhanu', 'city': 'vjwda', 'name1': 'rekha'}
>>> #single key mutliples values
>>> a={"idnos":[10,20,30],"names":["bhanu","nani","rekha"],"marks":[70,80,90]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['bhanu', 'nani', 'rekha'], [70, 80, 90]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['bhanu', 'nani', 'rekha']), ('marks', [70, 80, 90])])
