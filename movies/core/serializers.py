from rest_framework import serializers
from core.models import Movie, Location, Timing

class TimingSerializer(serializers.ModelSerializer):
	"""
	Timing serializer for Timing records
	depth field automatically serializes all fields in nested relations to. 
	"""

	class Meta:
		model = Timing
		fields = ('id', 'time')


class LocationSerializer(serializers.ModelSerializer):
	"""
	Location serializer for Location records
	depth field automatically serializes all fields in nested relations to. 
	"""
	timings = TimingSerializer(source='timing_set', many=True)

	class Meta:
		model = Location
		# fields = '__all__'
		fields = ('id', 'name', 'timings')
		depth = 3

class MovieSerializer(serializers.ModelSerializer):
	"""
	Movie serializer for movie records
	depth field automatically serializes all fields in nested relations to. 
	"""
	locations = LocationSerializer(source='location_set', many=True)

	class Meta:
		model = Movie
		fields = ('id', 'name', 'locations')
		# fields = '__all__'
		depth = 3









