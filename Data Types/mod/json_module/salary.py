import json
samplejson = """{
    "company":{
        "employee":{
            "name":"silpa","payble":{
                "salary":7000,"bonus":800
            }
        }
    }
}"""
y = json.loads(samplejson)
print(y['company']['employee']['payble']['salary'])