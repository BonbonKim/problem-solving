text = input()

tags = {}
tag_id, is_tag = 0, False
masked_text, tmp = "", ""

for t in text:
    if t == '<':
        is_tag = True

    if is_tag:
        tmp += t
    else:
        masked_text += t

    if t == '>':
        tags[str(tag_id)] = tmp
        masked_text += ' #'+str(tag_id)+'# '
        tag_id += 1
        tmp = ""
        is_tag = False

masked_text = masked_text.split()

for i in range(len(masked_text)):
    if '#' in masked_text[i]:
        masked_text[i] = tags[masked_text[i][1:-1]]
    else:
        masked_text[i] = masked_text[i][::-1]

print(" ".join(masked_text).replace(" <","<").replace("> ", ">"))