from rest_framework import serializers

from .models import Students, Teachers, Groups, Department


class TeacherListSerializer(serializers.ModelSerializer):
    '''список преподавателей'''

    # class Meta:
    #     model = Students
    #     fields = (
    #         'id',
    #         'full_name',
    #         'first_name',
    #         'last_name',
    #         'birthday',
    #         'group_number',
    #         'course_number',
    #         'headman',
    #         'email',
    #         'phone_number',
    #         'address',
    #         'phone_number_parents',
    #         'education_type',
    #         'photo',
    #         'cathedra_id',
    #     )
    class Meta:
        model = Teachers
        fields = '__all__'


class TeacherDetailSerializer(serializers.ModelSerializer):
    '''детали преподавателей'''

    class Meta:
        model = Teachers
        fields = '__all__'


class DepartmentListSerializer(serializers.ModelSerializer):
    '''список кафедр'''

    # class Meta:
    #     models = Department
    #     fields = (
    #         'id',
    #         'name',
    #         'email',
    #         'phone_number',
    #         'address',
    #         'number_of_groups',
    #         'number_of_specialties',
    #         'manager_department',
    #         'description',
    #         'photo',
    #     )

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentDetailSerializer(serializers.ModelSerializer):
    '''детали кафедр'''
    manager_department = TeacherListSerializer(read_only=True)

    class Meta:
        model = Department
        fields = '__all__'


class StudentListSerializer(serializers.ModelSerializer):
    '''список студентов'''

    # class Meta:
    #     model = Students
    #     fields = (
    #         'id',
    #         'full_name',
    #         'first_name',
    #         'last_name',
    #         'birthday',
    #         'group_number',
    #         'course_number',
    #         'headman',
    #         'email',
    #         'phone_number',
    #         'address',
    #         'phone_number_parents',
    #         'education_type',
    #         'photo',
    #         'cathedra_id',
    #     )
    class Meta:
        model = Students
        fields = '__all__'


class StudentDetailSerializer(serializers.ModelSerializer):
    '''детали студентов'''
    cathedra_id = DepartmentListSerializer(read_only=True)

    class Meta:
        model = Students
        fields = '__all__'


class GroupListSerializer(serializers.ModelSerializer):
    '''список студентов'''

    # class Meta:
    #     model = Students
    #     fields = (
    #         'id',
    #         'full_name',
    #         'first_name',
    #         'last_name',
    #         'birthday',
    #         'group_number',
    #         'course_number',
    #         'headman',
    #         'email',
    #         'phone_number',
    #         'address',
    #         'phone_number_parents',
    #         'education_type',
    #         'photo',
    #         'cathedra_id',
    #     )
    class Meta:
        model = Groups
        fields = '__all__'


class GroupDetailSerializer(serializers.ModelSerializer):
    '''детали студентов'''
    headman = StudentListSerializer(read_only=True)

    class Meta:
        model = Groups
        fields = '__all__'
