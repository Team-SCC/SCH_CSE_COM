import os
import pandas as pd

def student_id_loader(self):
    '''데이터파일 불러와서 학번 리스트 반환
    '''
    relative_path = './data/si_checker.csv'

    try: # 상대경로
        student_id_data = pd.read_csv(relative_path)
    except: # 에러시 상대경로를 절대 경로로 변경
        absolute_path = os.path.abspath(relative_path) 
        student_id_data = pd.read_csv(absolute_path)

    student_id_list = []

    for data in student_id_data.values:
        for i in data:
            student_id_list.append(f'{i}')
            
    print("[init data loader] ", len(student_id_list), "student_id_list load complete")
    
    return {'student_id_list' : student_id_list}
