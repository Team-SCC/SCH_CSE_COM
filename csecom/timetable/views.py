import random
from django.shortcuts import render
from .models import Grade1Timetable, Grade2Timetable, Grade3Timetable, Grade4Timetable, TimetableTest
from .models import M610Timetable, M615Timetable, M618Timetable, M619Timetable, M620Timetable

#과목코드 : 과목명
subject_dict = {
    11903: "전산수학 남윤영",
    11904: "프로그래밍응용 이상정",
    11906: "C프로그래밍 천인국",
    11907: "C프로그래밍LAB 천인국",
    11908: "컴퓨터영어 네이슨호히푸하",
    11909: "컴퓨터구조 홍인식",
    11910: "객체지향프로그래밍 하상호",
    11912: "확률및통계 이해각",
    11913: "객체지향프로그래밍LAB 하상호 ",
    11914: "웹프로그래밍 천인국",
    11915: "데이터구조2 남윤영",
    11917: "컴파일러 하상호",
    11918: "데이터베이스 이해각",
    11919: "컴퓨터네트워크 이상정",
    11921: "실무데이터베이스시스템 이해각",
    11923: "인공지능 김명숙",
    11925: "소프트웨어공학(캡스톤디자인) 남윤영",
    11926: "마이크로프로세서(캡스톤디자인) 홍인식",
    11933: "빅데이터응용 김초명",
    11934: "졸업종합지도 남윤영",
    11936: "강화학습 이상정",
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
            if isinstance(item, int) and int(str(item)) != 0:
                first_digit = int(str(item)[0])
                remaining_digits = int(str(item)[1:])
                subject_code = get_subject_name(remaining_digits, subject_dict)
                new_dict = {subject_code: first_digit}
            else:
                new_dict = {item: ""}
            new_row.append(new_dict)
        result.append(new_row)
    return result

#랜덤 색상
def choose_random_color():
    colors = ['#f08676', '#fbaa68', '#7ed1bf', '#7aa5e9', '#a7ca70', '#9f86e1', '#ecc369']
    return random.choice(colors)

def make_2list(arr):
    timetable_data_array = []
    for record in arr:
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

    return result

def timetable_view_grade1(request):
    timetable_test_data = Grade1Timetable.objects.all()
    result = make_2list(timetable_test_data)
    context = {
        'choose_random_color': choose_random_color,
        'timetable_data_array': result,
    }
    return render(request, 'timetable.html', context)

def timetable_view_grade2(request):
    timetable_test_data = Grade2Timetable.objects.all()
    result = make_2list(timetable_test_data)
    context = {
        'choose_random_color': choose_random_color,
        'timetable_data_array': result,
    }
    return render(request, 'timetable.html', context)

def timetable_view_grade3(request):
    timetable_test_data = Grade3Timetable.objects.all()
    result = make_2list(timetable_test_data)
    context = {
        'choose_random_color': choose_random_color,
        'timetable_data_array': result,
    }
    return render(request, 'timetable.html', context)

def timetable_view_grade4(request):
    timetable_test_data = Grade4Timetable.objects.all()
    result = make_2list(timetable_test_data)
    context = {
        'choose_random_color': choose_random_color,
        'timetable_data_array': result,
    }
    return render(request, 'timetable.html', context)

def timetable_view_m610(request):
    timetable_test_data = M610Timetable.objects.all()
    result = make_2list(timetable_test_data)
    context = {
        'choose_random_color': choose_random_color,
        'timetable_data_array': result,
    }
    return render(request, 'timetable.html', context)

def timetable_view_m615(request):
    timetable_test_data = M615Timetable.objects.all()
    result = make_2list(timetable_test_data)
    context = {
        'choose_random_color': choose_random_color,
        'timetable_data_array': result,
    }
    return render(request, 'timetable.html', context)
def timetable_view_m618(request):
    timetable_test_data = M618Timetable.objects.all()
    result = make_2list(timetable_test_data)
    context = {
        'choose_random_color': choose_random_color,
        'timetable_data_array': result,
    }
    return render(request, 'timetable.html', context)
def timetable_view_m619(request):
    timetable_test_data = M619Timetable.objects.all()
    result = make_2list(timetable_test_data)
    context = {
        'choose_random_color': choose_random_color,
        'timetable_data_array': result,
    }
    return render(request, 'timetable.html', context)
def timetable_view_m620(request):
    timetable_test_data = M620Timetable.objects.all()
    result = make_2list(timetable_test_data)
    context = {
        'choose_random_color': choose_random_color,
        'timetable_data_array': result,
    }
    return render(request, 'timetable.html', context)