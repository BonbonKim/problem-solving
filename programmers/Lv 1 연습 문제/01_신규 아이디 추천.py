import re

def solution(new_id):
    new_id = new_id.lower()

    p = re.compile("[^a-z0-9._-]")
    new_id = re.sub(p, "", new_id)

    dot_p = re.compile("\.+")
    new_id = re.sub(dot_p, ".", new_id)

    if new_id.startswith("."):
        new_id = new_id[1:]
    if new_id.endswith("."):
        new_id = new_id[:-1]

    if new_id == "":
        new_id = "aaa"
    elif len(new_id) > 15:
        new_id = new_id[:15]
        if new_id.endswith("."):
            new_id = new_id[:-1]
    elif len(new_id) < 3:
        new_id += new_id[-1] * (3-len(new_id))

    return new_id
