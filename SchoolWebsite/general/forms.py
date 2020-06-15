from django import forms
from general.models import MemberInfo, MemberGrade, Grade, Video, Course
from django.contrib.auth.models import User

REGSTATUS = [
    ('REGISTERED', 'REGISTERED'),
    ('UNREGISTERED', 'UNREGISTERED')
]

LETTERGRADES = [
    ('A', 'Excellent'),
    ('B', 'Good'),
    ('C', 'Average'),
    ('D', 'Poor'),
    ('F', 'Fail')
]

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = ['contactinfo', 'email', 'phone','address']

class GradeEditForm(forms.Form):
    class Meta:
        model = MemberGrade
        fields = ['grade']

class RegCoursesForm(forms.ModelForm):
    class Meta:
        model = MemberGrade
        fields = ['user', 'semester', 'course', 'grade']

class GradeForm(forms.Form):
    value = forms.ChoiceField(choices=LETTERGRADES)

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "course", "lectureno", "videofile"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        print(type(user))
        self.fields['course'].queryset = Course.objects.filter(professor=user)