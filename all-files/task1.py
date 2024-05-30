# Get a pull request info on a repo using python
#sets are a type of data type where there cannot be any duplicate datas
# [] -> List
# () -> tuple
# {} -> set
# {"key":"value"} -> dictionaries


import requests

response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")



all_details = response.json()

# print(all_details[0]["user"]["login"])
for i in range(len(all_details)):
    print(all_details[i]["user"]["login"])


