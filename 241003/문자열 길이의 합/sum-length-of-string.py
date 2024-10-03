n = int(input())
cnt = 0
total_len = 0

for _ in range(n):
    s = input()
    if(s[0]=='a'):
        cnt +=1 
        total_len = len(s)

print(total_len, cnt)