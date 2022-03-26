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
with open("wf.txt" , encoding="UTF-8") as fp:
    lines = fp.readlines()
    for line in lines:
        print(line[:-1])



