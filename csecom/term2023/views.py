from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q, Count
import logging
from django.http import HttpResponse
from django.conf import settings

from .forms import *
from .models import *

@login_required(login_url='common:login')
def vote_question(request, question_id):
    question = get_object_or_404(Term2023Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('term2023:detail', question_id=question.id)

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    answer = get_object_or_404(Term2023Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('term2023:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def question_create(request): 
    if request.method == 'POST':
        form = Term2023QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # 추가한 속성 author 적용
            question.create_date = timezone.now()
            try:
                question.image = request.FILES['image']
            except KeyError:
                question.image = None
            question.save()
            return redirect('term2023:index')
    else:
        form = Term2023QuestionForm()
    context = {'form': form}
    return render(request, 'term2023/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Term2023Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('term2023:detail', question_id=question.id)

    if request.method == "POST":
        form = Term2023QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('term2023:detail', question_id=question.id)
    else:
        form = Term2023QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'term2023/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Term2023Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('term2023:detail', question_id=question.id)
    if question.subject:
        question.image.delete()
    question.delete()
    return redirect('term2023:index')


@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    question = get_object_or_404(Term2023Question, pk=question_id)
    if request.method == "POST":
        form = Term2023CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('term2023:detail', question_id=comment.question.id), comment.id))
    else:
        form = Term2023CommentForm()
    context = {'form': form}
    return render(request, 'term2023/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    comment = get_object_or_404(Term2023Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('term2023:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = Term2023CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('term2023:detail', question_id=comment.question.id), comment.id))
    else:
        form = Term2023CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'term2023/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    comment = get_object_or_404(Term2023Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('term2023:detail', question_id=comment.question_id)
    else:
        comment.delete()
    return redirect('term2023:detail', question_id=comment.question_id)


@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    answer = get_object_or_404(Term2023Answer, pk=answer_id)
    if request.method == "POST":
        form = Term2023CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('term2023:detail', question_id=comment.answer.question.id), comment.id))
    else:
        form = Term2023CommentForm()
    context = {'form': form}
    return render(request, 'term2023/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    comment = get_object_or_404(Term2023Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('term2023:detail', question_id=comment.answer.question.id)

    if request.method == "POST":
        form = Term2023CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('term2023:detail', question_id=comment.answer.question.id), comment.id))
    else:
        form = Term2023CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'term2023/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    comment = get_object_or_404(Term2023Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('term2023:detail', question_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect('term2023:detail', question_id=comment.answer.question.id)

logger = logging.getLogger('term2023')

@login_required(login_url='common:login')
def index(request):
    logger.info("INFO 레벨로 출력")
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Term2023Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Term2023Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Term2023Question.objects.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__name__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__name__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}  # <------ so 추가
    return render(request, 'term2023/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Term2023Question, pk=question_id)
    context = {'question': question}
    return render(request, 'term2023/question_detail.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Term2023Question, pk=question_id)
    if request.method == "POST":
        form = Term2023AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # 추가한 속성 author 적용
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('term2023:detail', question_id=question.id), answer.id))
    else:
        form = Term2023AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'term2023/question_detail.html', context)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Term2023Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('term2023:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = Term2023AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('term2023:detail', question_id=answer.question.id), answer.id))
    else:
        form = Term2023AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'term2023/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Term2023Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('term2023:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def file_download(request):
    '''파일 다운로드 함수
    url: localhost:port/cloud/download
    templates: None
    '''
    path = request.GET['path']
    print(request.GET)
    file_path = os.path.join(settings.MEDIA_ROOT, path)
 
    if os.path.exists(file_path):
        binary_file = open(file_path, 'rb')
        response = HttpResponse(binary_file.read(), content_type="application/octet-stream; charset=utf-8")
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        message = '[cloud, views, file_download error] 파일이 존재하지 않습니다.'
        return HttpResponse("<script>alert('"+ message +"');history.back()'</script>")
