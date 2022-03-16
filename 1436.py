n = int(input())

num = 666
cnt = 0

while True:
    if '666' in str(num): #num 을 string 으로 바꿔 '666'이 들어있는지 확인
        cnt += 1          # 존재한다면 cnt를 더해줘 다음 순서를 찾아간다.
    if cnt == n:
        print(num)
        break
    num += 1

##Brute Force 문제는 while을 사용하는 것을 두려워하면 안된다!