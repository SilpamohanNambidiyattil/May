sampleDict = {"class": {"student": {"name":"Mike","marks": {"physics":70,"history":80}}} }
print(sampleDict["class"]["student"]["marks"]["history"])
sampleDict1 = {
    "class": {
        "students": {
            "name": "silpa",
            "marks": {
                "physics":70,
                "history":80
            }
        }
    }
}

s1 = {
    "dict1":{"name":"silpa",},
    "dict2":{"place":"abc","quaification":"mtech"},
    "dict3":{"job":"pythondev","sal":"2546768"}
}
x = s1["dict3"]["job"]="softwareDev"
print(s1)