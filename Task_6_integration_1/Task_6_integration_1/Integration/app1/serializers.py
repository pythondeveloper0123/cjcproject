from rest_framework import serializers
from . models import Student

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ('__all__')

    def create(self,validated_data):    #create method we are convert json data to python object and save into database
        return Student.objects.create(**validated_data)