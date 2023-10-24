from rest_framework import serializers
from .models import Teachers



class TeacherSerializer(serializers.ModelSerializer):
        class Meta:
            model = Teachers
            fields = ['id','name','city','subj']

    