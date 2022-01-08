n = int(input())
# First mark has to be '('.
# Each number of '(' and ')' have to be same.
for i in range (0, n):
    vps = list(input())
    if vps[0] == ')':
        print("NO")
        continue
    else:
        cnt1 = 0
        cnt2 = 0
        for j in vps:
            if j == "(":
                cnt1 += 1
            else:
                cnt2 += 1
                if cnt2 > cnt1:
                    print("NO")
                    break
        if cnt2 > cnt1:
            continue
        elif cnt1 == cnt2:
            print("YES")
        else:
            print("NO")

            # if vps.count("(") < vps.count(")"):
            #     print("NO")
            #     print(1)
            #     break
            # if vps.count("(") == vps.count(")"):
            #     print("YES")
            #     print(2)
            #     break
            # else:
            #     print("NO")
            #     print(3)
            #     break
            #
