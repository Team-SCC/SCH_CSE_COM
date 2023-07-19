import time
import os

def file_name_creater(instance, filename):
    '''파일 이름을 생성해서 반환하는 함수
    '''
    int_time = str(int(time.time()))
    ext = os.path.splitext(filename)[1]
    new_name = int_time + ext
    
    return new_name
