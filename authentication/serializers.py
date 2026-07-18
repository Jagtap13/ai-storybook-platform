from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import StudentProfile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length = 6)
    role = serializers.ChoiceField(choices=StudentProfile.ROLE_CHOICES,default ='student')

    class Meta:
        model = User
        fields = ['username','email','password','role']
    
    def create(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        StudentProfile.objects.create(user=user, role=role)

        return user