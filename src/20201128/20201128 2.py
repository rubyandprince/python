score_list = input().split()
for i in range(len(score_list)):
    score_list[i] = int(score_list[i])
a = []
b = []
c = []
d = []
e = []
for score in score_list:
    if 90 <= score and score <= 100:
        a += [score]
    elif 80 <= score and score <= 89:
        b += [score]
    elif 70 <= score and score <= 79:
        c += [score]
    elif 60 <= score and score <= 69:
        d += [score]
    elif score < 60:
        e += [score]
avg = sum(score_list) / len(score_list)
print('100-90:', '*' * len(a))
print('89-80:', '*' * len(b))
print('79-70:', '*' * len(c))
print('69-60:', '*' * len(d))
print('59以下:', '*' * len(e))
print('平均:', avg)
print('最高分:', max(score_list))
print('最低分:', min(score_list))