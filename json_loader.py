import json
import os


count=1
output_path = "output.json"
file_path = "events"
files = os.listdir(file_path)
files.sort()
for file in files:
    json_path = file_path + "/" + file
    try:
        with open(json_path,'r') as fr:
            data = json.load(fr)
            fr.close()
        action = "evebt" + data["tag"]
        if data["event"]["event_type"] != "touch" and data["event"]["event_type"] != "long_touch":
            d = {action:{"event_type":data["event"]["event_type"]}}
        else:
            d = {action:{"event_type":data["event"]["event_type"], "bounds":data["event"]["view"]["bounds"]}}
        if count == 1:
            with open(output_path,'w') as fw:
                fw.write(json.dumps(d))
                fw.close()
        else:
            with open(output_path,'r') as fr:
                text = json.load(fr)
                fr.close()
            text[action] = d[action]
            with open(output_path,'w') as fw:
                fw.write(json.dumps(text))
                fw.close()
        count = count + 1
    except json.decoder.JSONDecodeError:
        print("empty json file")
        continue

