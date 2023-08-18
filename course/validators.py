from rest_framework import serializers


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('url'):
            if 'youtube.com' not in value.get('url'):
                raise serializers.ValidationError('Только Ютуб')
