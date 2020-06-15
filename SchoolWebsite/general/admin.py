from django.contrib import admin
from .models import Announcement, MemberInfo, Course, Semester, Grade, MemberGrade

# Register your models here.
admin.site.register(Announcement)
admin.site.register(MemberInfo)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Grade)
admin.site.register(MemberGrade)