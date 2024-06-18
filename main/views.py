from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

grade_db = [
  {
    "_id": "135d21e9-9103-4352-B125-c8bc04ba6aff",
    "index": "1",
    "teacher": "팽도훈",
    "phone": "010-8745-7095",
    "grade": "3",
    "num": "2",
    "contents": "노력하여야 불리한 취임에 중대한 그러나 같은 지원등 라이너. 설치될 든"
  },
  {
    "_id": "61fd8dba-c998-4e0d-A9fe-03c1dd5d62af",
    "index": "2",
    "teacher": "시윤",
    "phone": "010-8852-3191",
    "grade": "1",
    "num": "3",
    "contents": "대하여 한 교향악이다 이유가 기밀·초병·초소·유독음식 질병·노령 사막이다 농업. 사는가 품으며"
  },
  {
    "_id": "28ba2921-916b-48f5-C88e-3ec4e4850648",
    "index": "3",
    "teacher": "내석준",
    "phone": "010-2865-2006",
    "grade": "1",
    "num": "1",
    "contents": "선거권을 황금시대다 국가원로자문회의의 발휘하기 선서를 단체행동권을 마디씩 가져야. 국민에 소녀들의"
  },
  {
    "_id": "e8c20fa1-188e-46f9-C4ea-9da93aedc1bb",
    "index": "4",
    "teacher": "운은재",
    "phone": "010-2097-7392",
    "grade": "1",
    "num": "6",
    "contents": "때문이다 취임에 날카로우나 재의에 출석과 사라지지 것이다 든. 재적의원과반수의 중요정책의"
  },
  {
    "_id": "3866a2c4-a71c-437e-Cecd-16cc3c05214b",
    "index": "5",
    "teacher": "랑영호",
    "phone": "010-3475-4378",
    "grade": "1",
    "num": "12",
    "contents": "봄이 청춘이 된 또한 이용·개발과 때문이다 설산에서 법률을. 국민은 어디"
  }
]


def index(request):
    return render(request,'main/index.html')

def jejuohyun(request):
    return render(request,'jejuohyun.html')

def high_1st(request):
    return render(request,'main/high_1st.html')

def hige_2rd(request):
    return render(request,'main/high_2nd.html')

def high_3rd(request):
    return render(request,'main/high_3rd.html')

def my_page(request):
    return render(request,'main/my_page.html')

def grade(request):
    return render(request,'main/grade.html')