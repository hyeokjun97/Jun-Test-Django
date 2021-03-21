from django.shortcuts import render
from django.utils import timezone
# timezone 모듈을 사용하기 위해 불러왔다.
from .models import Post
# 해당 디렉토리의 models 에서 Post 모델을 불러왔다.

def post_list(request):
    qs = Post.objects.all()	# qs 변수에 모든 글 목록을 불러왔다.
    #qs = qs.filter(published_date__lte=timezone.now())	# qs 변수에 '발행날짜가 현재 시각보다 작거나 같은 것들만 갖고와라' 라는 필터링한 정보를 한 번 넣어줬다.
    qs = qs.order_by('published_date')	# qs 변수에 'published_date 에 대한 오름차순으로 정렬된 정보'를 넣어줬다.
    return render(request, 'blog/post_list.html', {
        'post_list': qs,
    })