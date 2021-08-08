import sys

s = sys.stdin.readline().rstrip()

temp = ""

start = 0
end = 0

for i in range(len(s)):
    if s[i] == "<":
        start = i

    elif s[i] == ">":
        end = i
        print(s[start:end+1])

    if s[i] != "<":
        if i == 0:
            r_start = i
            s_start = r_start
        elif s[i-1] == ">":
            r_start = i
            s_start = r_start

    elif s[i] != ">":
        cnt = 0
        if i == len(s)-1:
            r_end = i
            for j in range(r_start, r_end+1):
                if s[j] == " ":
                    cnt += 1
                    for r in range(j, s_start-1, -1):
                        print(s[r], end="")
            if cnt == 0:
                for r in range(r_end,r_start-1,-1):
                    print(s[r], end="")
        elif s[i+1] == "<":
            r_end = i
            for j in range(r_start, r_end+1):
                if s[j] == " ":
                    cnt += 1
                    for r in range(j, s_start-1, -1):
                        print(s[r], end="")
            if cnt == 0:
                for r in range(r_end,r_start-1,-1):
                    print(s[r], end="")



