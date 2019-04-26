'''#1
a=input("생년입력:")
b=input("월 입력:")
c=input("일 입력:")
print(a,b,c,sep="")'''

'''#2(1)
word=input("입력4자리:")
print(word[3],word[2],word[1],word[0],sep='')'''

'''#2(2)
word=input("입력4자리:")
print(list(reversed(word)))'''

''''#3
def check_pal(s):
    low=0
    high=len(s)-1

    while True:
        if low>high:
            return True;

        a=s[low]
        b=s[high]

        if a!= b:
            return False
        low+=1
        high-=1
s=input("문자열 입력:")
s=s.replace("","")

if(check_pal(s)==True):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")'''

''''#4
sentence=input("문자열을 입력하시오:")
print(sentence.count('o'))'''

#5
while True:
    age=input("나이를입력하시오(정수만):")
    if age.isdecimal() == True:
        break
