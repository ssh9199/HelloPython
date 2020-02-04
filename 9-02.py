print ()

x = int(input('정수 입력 : '))
cnt = 0;
i=1

print ()

while i <= x :
    if x%i == 0 :
        print (i)
        cnt += 1
    i += 1

print()
print('약수의 개수 : ',cnt)
print()
