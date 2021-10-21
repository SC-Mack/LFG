from rest_framework import serializers

from main.models import Review
from users.models import CustomUser

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    date_created = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ['id', 'date_updated']
        
    #Return a stringified version of the date created    
    def get_date_created(self, instance):
        return instance.date_created.strftime('%B %d, %Y')

class CustomUserSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        exclude=['password']
        
    def get_slug(self, instance):
        return instance.username
        