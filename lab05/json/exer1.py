import json

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")

with open("text", "r") as file:
    data = json.load(file)

for i in range(3):
    attributs = data["imdata"][i]["l1PhysIf"]["attributes"]
    dn = attributs["dn"]
    mtu = attributs["mtu"]
    speed = attributs["speed"]
    print(f"{dn:<72} {speed:<8} {mtu:<6}")