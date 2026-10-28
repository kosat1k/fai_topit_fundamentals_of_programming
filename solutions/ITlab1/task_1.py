from copy import *

config1 = {
    "name": "conf1",
    "participants": ["Artem", "Ivan"],
    "play": ["10sec", "1Mb"]
}
#Неправильно
config2 = config1
config1["play"].append("2times")
print(config2["play"])

#Правильно
config1 = {
    "name": "conf1",
    "participants": ["Artem", "Ivan"],
    "play": ["10sec", "1Mb"] }
config2 = deepcopy(config1)
config2["play"].append("2times")
print(config1["play"])
assert config1["play"] == ["10sec", "1Mb"]

