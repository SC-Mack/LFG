from rest_framework import serializers

from main.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    date_created = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    # user_has_reviewed = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        exclude = ['id', 'date_updated']
        
    #Return a stringified version of the date created    
    def get_date_created(self, instance):
        return instance.date_created.strftime('%B %d, %Y')
    
    # Check to see if a user has already reviewed a profile
    # def get_user_has_reviewed(self, instance):
    #     request = self.context.get('request')
    #     return instance..filter(author=request.user).exists()