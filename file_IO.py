#file io

#파일 객체 = open(파일 경로 , 읽기 모드)
# w : 쓰기모드 , r : 읽기모드 , a : 이어쓰기 모드
#파일을 닫을 때 파일객체.close()로 닫음

#파일 쓰기
# fp = open('war_flower.txt', 'w')
# print('고니',file=fp) #실제 파일에 작성
# print('정마담',file=fp) #실제 파일에 작성
# print('아귀',file=fp) #실제 파일에 작성
# fp.write('너부리')
# fp.close()

# fp = open('wf.txt', 'r' ,encoding="utf-8")
# #r 생략가능 default 모드가 r
# lines = fp.readlines() #파일을 1행 단위의 리스트 원소로 리턴
# # print(lines)
# for line in lines:
#     # print(line.rstrip("\n")) #lines에 들어간 배열에 오른쪽 줄바꿈을 제거
#     print(line[:-1]) #슬라이싱 하여 -1의 경우 0부터 마지막 전까지 출력
#
# # for line in fp:
# #     print(line, end='')
# fp.close()

#with 파일 사용 후 자동으로 파일 종료
# with open("wf.txt" , encoding="UTF-8") as fp:
#     lines = fp.readlines()
#     for line in lines:
#         print(line[:-1])

#안주 프로그램 V 0.4
import random

alcohols_foods= {}
with open("alcohols.txt", encoding="UTF-8") as fp1:
    with open("foods.txt",encoding="UTF-8") as fp2:
        alcohols = fp1.readlines()
        foods = fp2.readlines()
        for k in range(len(alcohols)):
            alcohols_foods[alcohols[k].strip('\n')] = foods[k][0:-1] #마지막 역슬래쉬 제거
print(alcohols_foods)

while True:
    alcohol = input('주문하실 술(맥주/와인/소주/고량주/아무거나/결제)은?')
    if alcohol == '결제':
        break
    if alcohol in alcohols_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohols_foods[alcohol]))
    elif alcohol == '아무거나':
        alcohol = str(random.choice(list(alcohols_foods)))
        print('{0}을 추천합니다. 안주는 {1}입니다.'.format(alcohol, alcohols_foods[alcohol]))
    else:
        print('{0}는 판매하지 않습니다.메뉴에서 골라주세요'.format(alcohol))



