from rest_framework import serializers
from work_history.models import *


class BaseSearchSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()


class BioSerializer(BaseSearchSerializer):

    class Meta:
        model = Bio
        fields = ('id', 'label', 'category')

    @staticmethod
    def get_label(obj):
        return obj.test

    @staticmethod
    def get_category(obj):
        return 'Bio'


class LocationSerializer(BaseSearchSerializer):
    class Meta:
        model = Location
        fields = ('id', 'label', 'category')

    @staticmethod
    def get_label(obj):
        return obj.place

    @staticmethod
    def get_category(obj):
        return 'Location'


class PreviousClientSerializer(BaseSearchSerializer):

    class Meta:
        model = PreviousClient
        fields = ('id', 'label', 'category')

    @staticmethod
    def get_label(obj):
        return obj.first_name + ' ' + obj.last_name

    @staticmethod
    def get_category(obj):
        return 'Previous Client'


class SkillSerializer(BaseSearchSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'label', 'category')

    @staticmethod
    def get_label(obj):
        return obj.title

    @staticmethod
    def get_category(obj):
        return 'Skill'
