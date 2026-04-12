import requests
url = "https://www.reddit.com/r/UPSC/comments/1siuqqf/all_countries_starting_with_letter_i/.json"
headers = {"User-Agent": "ARGUS/0.1"}
response = requests.get(url, headers=headers)
data = response.json()
comments = data[1]['data']['children']
c = 0
for comment in comments:
    if comment['kind'] == 't1':
        replies = comment['data']['replies']
        author = comment['data']['author']
        body = comment['data']['body']
        score = comment['data']['score']
        print(f"{author}: {body} : {score}")
        if replies != "":
            children = replies['data']['children']
            print("-----------------------------------------------------------------------------")
            print("Replies for comment by: ", author)
            for reply in children:
                print(f"{reply['data']['author']}:{reply['data']['body']}: {reply['data']['score']}")
            print("-----------------------------------------------------------------------------")
            print("-----------------------------------------------------------------------------")
            print("-----------------------------------------------------------------------------")

        if body in ["[deleted]", "[removed]"]:
            continue

        if author == "[deleted]" or author == "AutoModerator":
            continue
        c += 1
print(c)