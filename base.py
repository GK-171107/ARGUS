import requests
import textwrap

url = "https://www.reddit.com/r/Btechtards/comments/1rox0x3/i_dont_understand_ai_wont_kill_software_jobs/.json"
headers = {"User-Agent": "ARGUS/0.1"}

response = requests.get(url, headers=headers)
data = response.json()
comments = data[1]['data']['children']

c = 0
r = 0

# styling
line = "=" * 100
subline = "-" * 100
wrap_width = 85

for comment in comments:
    if comment['kind'] == 't1':

        replies = comment['data']['replies']
        author = comment['data']['author']
        body = comment['data']['body']
        score = comment['data']['score']

        if body in ["[deleted]", "[removed]"]:
            continue

        if author == author == "AutoModerator":
            continue

        print(line)
        print(f"COMMENT #{c+1}")
        print(f"Author : {author}")
        print(f"Score  : {score}")
        print("Content:")
        print(textwrap.fill(body, width=wrap_width))
        print(line)

        if replies != "":
            children = replies['data']['children']

            valid_replies = [
                reply for reply in children
                if reply['kind'] == 't1'
            ]

            if valid_replies:
                print("REPLIES")
                print(subline)

                for i, reply in enumerate(valid_replies, start=1):
                    r_author = reply['data']['author']
                    r_body = reply['data']['body']
                    r_score = reply['data']['score']
                    r += 1

                    print(f"[{i}] {r_author} | Score: {r_score}")
                    print(textwrap.fill(r_body, width=wrap_width,
                                        initial_indent="    ",
                                        subsequent_indent="    "))
                    print(subline)

        print("\n")
        c += 1

print(f"Total Valid Comments: {c}")
print(f"Total Valid Replies: {r}")