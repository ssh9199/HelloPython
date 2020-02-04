국어 = int(input('국어 : '))
수학 = int(input('수학 : '))
영어 = int(input('영어 : '))
_sum = 국어+수학+영어
_avg = float(_sum)/3.0

print("총점 : %d\n평균 : %.2f" % (_sum, _avg))
