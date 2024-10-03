s = input().strip()
s_list = list(s.split(" "))

for i in range(len(s_list)-1, -1, -1):
    print(s_list[i])