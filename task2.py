import requests

link = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(link)
# print(response)

if response.status_code == 200:
    pull_req = response.json()

    pr_users={}

    for pull in pull_req:
        creator = pull["user"]["login"]

        if creator in pr_users:
            pr_users[creator] += 1
        else:
            pr_users[creator] = 1

    print("User list")
    print(type(pr_users))
    print(type(pr_users.items()))
    print("*************************")
    # print(pr_users.items())
    # res = pr_users.items()
    for creator, count in pr_users.items():
        print(f"{creator}:{count}")
else:
    print("data cannot be fethced")

