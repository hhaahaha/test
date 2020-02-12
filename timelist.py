from moviepy.editor import VideoFileClip, concatenate
import os


'''
input {dic} : { (인물) : [시간 리스트], (인물) : [시간 리스트] , ... }
output 

'''


def assemble_cuts(inputfile, cuts, outputfile):
    """ Concatenate cuts and generate a video file. """
    '''
    input :::
    inputfile (str) : 작업할 비디오 파일 dir.
    cuts (list) : 클립할 영상의 시작점과 끝점을 넣는다. [[시작점1, 끝점1],[시작점2,끝점2],...]
    outputfile (str) : 저장할 파일명

    return ::: 편집된 영상파일이 저장된다.
    (None) 
    '''
    video = VideoFileClip(inputfile)
    final = concatenate([video.subclip(start, end)
                         for (start, end) in cuts])
    # 파일 저장 경로를 설정할 때 사용.
    # os.chdir('/home/pirl/PycharmProjects/NAVER_hack/save_video')
    final.to_videofile(outputfile)


def assemble_people_cuts(input_dic):
    ''' 여러 인물이 등장한 시간대를 dic 타입으로 받아 각자 자르거나 함께 있는 부분을 넣는다. '''

    # 어떤 인물을 보고 싶은지 peoples 리스트에 입력
    peoples = [person for person in input_dic]

    for i in peoples:

        times = input_dic[i]
        assemble_cuts(inputfile, times, i)

def list_time (timelist):
    #등장인물 리스트
    peoples = [person for person in timelist.keys()]

    #전체 타임 리스트
    times = [sequence for sequence in timelist[peoples[0]]]
    array = [0 for i in range(timeend+1)]

    for pick in peoples:
        coming_time = timelist[pick]
        print(array)
        for seq in coming_time:
            st_time , ed_time = seq

            for seq in range(st_time,ed_time+1):
                if array[seq] == 1 :
                    continue
                else:
                    array[seq] = 1

    st , et = 0, 0
    show_time = []

    for i in range(1, len(array)):
        if array[i] == 0:
            if array[i-1] == 1:
                et = i-1
            else:
                continue

        else:
            if array[i-1] == 0:
                st = i
            else:
                if i == len(array)-1:
                    et = i
                else:
                    continue

        if st != 0 and et != 0:
            show_time.append([st, et])
            st = 0
            et = 0

    return show_time

# def array_time (timelist):
#     # 등장인물 리스트
#     peoples = [person for person in timelist.keys()]
#
#     # 전체 타임 리스트
#     ###################### 만들어야 함
#     # times = [sequence for sequence in timelist[peoples[0]]]
#
#     array = [0 for i in timelist[peoples[0]]]
#     print(array)
#
#     new_array = {}
#     for pick in peoples:
#         coming_time = timelist[pick]
#         # print(array)
#         for seq in coming_time:
#             st_time , ed_time = seq
#             for seq in range(st_time,ed_time+1):
#                 array[seq] = 1
#
#         # print(array)
#         new_array[pick] = array
#
#     return new_array


timelist = {
    'Jisoo':[[1,2],[8,9]],
    'Lisa' : [[1,3],[9,10]],
    'Rose' : [[3,5],[8,10]],
    'Jenny' : [[1,4]]
}

timearray = {
    'Jisoo': [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    'Lisa': [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    'Rose': [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    'Jenny': [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
}
timeend =10
# 지수, 로제

# inputfile = "/home/pirl/PycharmProjects/NAVER_hack/Dog4727.mp4"
# mypick = combine_pick(timelist)
# print(mypick)

# assemble_cuts(inputfile, times, i)

# mypick = list_time(timelist)
# print(mypick)

mypick = array_time(timearray)
print(mypick)