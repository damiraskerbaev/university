from django.urls import path

from .views import (
    TuitionLanguageList,
    TuitiionLanguageDetail,
    Education_FormList,
    Education_FormDetail,
    SubjectList,
    Subject_Detail,
    Faculty_List,
    Faculty_Detail,
    University_List,
    University_Detail
)

urlpatterns = [
    path('tuition-language/', TuitionLanguageList.as_view(), name='tuition_language'),
    path('tuition-language/<int:pk>/', TuitiionLanguageDetail.as_view()),
    path('education-form/', Education_FormList.as_view()),
    path('education-form/<int:pk>/', Education_FormDetail.as_view()),
    path('subjects/', SubjectList.as_view()),
    path('subjects/<int:pk>/', Subject_Detail.as_view()),
    path('faculty/', Faculty_List.as_view()),
    path('faculty/<int:pk>/', Faculty_Detail.as_view()),
    path('university/', University_List.as_view()),
    path('university/<int:pk>/', University_Detail.as_view())
]