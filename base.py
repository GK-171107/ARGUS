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


def extract_replies_recursively(comment_or_reply, depth=0):

    all_replies = []

    replies = comment_or_reply['data']['replies']

    if replies == "":
        return all_replies

    children = replies['data']['children']

    for child in children:
        if child['kind'] == 't1':
            reply_dict = {
                'author': child['data']['author'],
                'body': child['data']['body'],
                'score': child['data']['score'],
                'depth': depth
            }
            all_replies.append(reply_dict)

            # Recursive call — get nested replies of this reply
            nested_replies = extract_replies_recursively(child, depth=depth + 1)
            all_replies.extend(nested_replies)

    return all_replies


for comment in comments:
    if comment['kind'] == 't1':

        author = comment['data']['author']
        body = comment['data']['body']
        score = comment['data']['score']

        if body in ["[deleted]", "[removed]"]:
            continue
        if author == "AutoModerator":
            continue

        print(line)
        print(f"COMMENT #{c + 1}")
        print(f"Author : {author}")
        print(f"Score  : {score}")
        print("Content:")
        print(textwrap.fill(body, width=wrap_width))
        print(line)

        # Get ALL replies (including nested to any depth)
        all_replies = extract_replies_recursively(comment, depth=1)

        if all_replies:
            print("REPLIES (all depths)")
            print(subline)

            for i, reply in enumerate(all_replies, start=1):
                indent = "  " * (reply['depth'] - 1)
                print(f"{indent}[{i}] {reply['author']} | Score: {reply['score']}")
                print(textwrap.fill(reply['body'], width=wrap_width - len(indent),
                                    initial_indent=indent + "    ",
                                    subsequent_indent=indent + "    "))
                print(subline)
                r += 1

        print("\n")
        c += 1

print(f"Total Valid Comments: {c}")
print(f"Total Valid Replies: {r}")