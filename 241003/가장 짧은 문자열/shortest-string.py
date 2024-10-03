saveLen = []
for _ in range(3):
    s = input()
    saveLen.append(len(s))
print(max(saveLen)-min(saveLen))