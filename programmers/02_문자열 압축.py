def solution(s):
    patterns = list()

    if len(s) == 1:
        return 1

    for n in range(1, int(len(s) / 2) + 1):
        text = s
        tmp_p = list()

        pattern = ''
        while text or tmp_p:
            p, text = text[:n], text[n:]
            len_p = str(len(tmp_p)) if len(tmp_p) > 1 else ""

            if len(p) < n:
                pattern += len_p + tmp_p[0] + p
                break
            if len(tmp_p) > 0 and p != tmp_p[0]:
                pattern += len_p + tmp_p[0]
                tmp_p.clear()
            tmp_p.append(p)
        patterns.append(pattern)

    patterns.sort(key=lambda x: len(x))
    return len(patterns[0])