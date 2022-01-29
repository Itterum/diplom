# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
#
# # Register your models here.
# # from .models import StudentGroup, TeacherGroup, DepartmentDuplicate, GroupsDuplicate, Profile
#
#
# class UserAdminInline(admin.StackedInline):
#     model = User
#
#
# @admin.register(Profile)
# class ProfileAdmin(UserAdmin):
#     inlines = [UserAdminInline, ]
#     list_display = ('user', 'full_name', 'gender', 'email', 'phone_number', 'address')
#     list_filter = ('user', 'full_name', 'gender', 'email', 'phone_number', 'address')
#     search_fields = ('user', 'full_name', 'email', 'phone_number', 'address')
#     actions = ()
#
#
# admin.site.unregister(User)
#
# # @admin.register(User)
# # class MyUserAdmin(admin.ModelAdmin):
# #     inlines = [ProfileAdmin, ]
#
#
# admin.site.register(StudentGroup)
# admin.site.register(DepartmentDuplicate)
# admin.site.register(TeacherGroup)
# admin.site.register(GroupsDuplicate)
