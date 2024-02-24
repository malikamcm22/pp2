import json


with open(r"C:\Users\user\Desktop\PP2\lab4\json\ex\sample_data.json") as f:
    data= json.loads(f.read())

print("Interface Status")
print("============================================================================================================")
print("DN\t\t\t\t\t\tDescription\t\t\t\tSpeed\t\t\tMTU  ")
x=0
for i in data["imdata"]:
     print(data["imdata"][x]["l1PhysIf"]["attributes"]["dn"], end="\t\t\t")
     print(data["imdata"][x]["l1PhysIf"]["attributes"]["descr"], end="\t")
     print(data["imdata"][x]["l1PhysIf"]["attributes"]["speed"], end="\t\t\t")
     print(data["imdata"][x]["l1PhysIf"]["attributes"]["mtu"], end="\t")
     x+=1