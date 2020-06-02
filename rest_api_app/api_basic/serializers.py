from rest_framework import serializers
from .models import User,ActivityPeriod


class UserSerializer(serializers.ModelSerializer):
    activity_periods = serializers.StringRelatedField(many=True)
    print(activity_periods)
    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')

    # def __str__(self):
    #     return '%d: %d' % (self.start_date, self.end_date)
# class ActivitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ActivityPeriod
#         fields = '__all__'