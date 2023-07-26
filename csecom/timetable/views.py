import random
from django.shortcuts import render
from .models import TimetableTest

#과목코드 : 과목명
subject_dict = {
    34567: "데이터구조",
    45678: "디지털로직",
    56789: "컴퓨터구조",
    67890: "놀기",
    34561: "안녕",
}

#과목코드 input, 과목명 out
def get_subject_name(subject_code, subject_dict):
    if subject_code in subject_dict:
        return subject_dict[subject_code]
    else:
        return subject_code

#이차원 배열의 요소를 Dictionary로 바꾼다
#6자리 중 첫번째 자리는 value, 나머지는 key
#key는 과목코드, value는 그 수업의 연속된 수 (Ex.75분 수업이면 value는 3)
def convert_to_dict(arr):
    result = []
    for row in arr:
        new_row = []
        for item in row:
            if isinstance(item, int):
                # If the item is an integer (numeric value)
                first_digit = int(str(item)[0])
                remaining_digits = int(str(item)[1:])
                subject_code = get_subject_name(remaining_digits, subject_dict)
                new_dict = {subject_code: first_digit}
            else:
                # If the item is a string (text)
                new_dict = {item: ""}
            new_row.append(new_dict)
        result.append(new_row)
    return result

#랜덤 색상
def choose_random_color():
    colors = ['#f08676', '#fbaa68', '#7ed1bf', '#7aa5e9', '#a7ca70', '#9f86e1', '#ecc369']
    return random.choice(colors)

def timetable_view(request):
    timetable_test_data = TimetableTest.objects.all()

    # 이차원 배열 생성
    timetable_data_array = []
    for record in timetable_test_data:
        # 각 레코드의 필드값을 리스트로 변환하여 이차원 배열에 추가합니다.
        row_data = [
            record.time,
            record.MON,
            record.TUE,
            record.WED,
            record.THU,
            record.FRI,
        ]
        timetable_data_array.append(row_data)
    
    result = convert_to_dict(timetable_data_array)

    context = {
        'choose_random_color': choose_random_color,
        'timetable_data_array': result,
    }
    
    return render(request, 'timetable.html', context)