from django.shortcuts import render

import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework import status
from core.custom_exceptions import CustomApiException
from core.models import Movie, Location, Timing
from rest_framework.decorators import api_view
from django.db.models import Q
from core.serializers import MovieSerializer, LocationSerializer, TimingSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def get_all_movies(request):
	"""
	List of all movies names
	"""

	try:

		name = request.GET.get('name', None)
		offset = request.GET.get('offset', 0)
		limit = request.GET.get('limit', 10)

		movies_list = []
		count = 0

		if not name:
			movies_list = Movie.objects.filter().order_by('-date_created')[offset:limit]
			count = Movie.objects.count()

		if name:
			movies_list = Movie.objects.filter(Q(name__icontains = name)).order_by('-date_created')[offset:limit]
			count = Movie.objects.filter(Q(name__icontains = name)).count()

		movies_serializer = MovieSerializer(movies_list, many=True)

		HttpResponse.status_code = status.HTTP_200_OK
		return JsonResponse({'count': count,'movies': movies_serializer.data})
	except CustomApiException as err:
		HttpResponse.status_code = err.status_code
		return JsonResponse({'status_code': err.status_code, 'message': err.detail})
	except Exception, e:
		HttpResponse.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		return JsonResponse({'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})


def validate_function(jsonBody):
	for key, value in jsonBody.iteritems():
			if not value:
				raise CustomApiException('Please provide '+ key, status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def add_movie(request):
	"""
	Create new movie with multiple locations and multiple timings
	"""
	try:

		jsonBody = json.loads(request.body)

		for key, value in jsonBody.iteritems():
			if not value:
				raise CustomApiException('Please provide '+ key, status.HTTP_400_BAD_REQUEST)

			for each_location in jsonBody['locations']:
				validate_function(each_location)

				for each_timing in each_location['timings']:
					validate_function(each_timing)

		movie = Movie(name = jsonBody['name'])
		movie.save()

		movie_object = Movie.objects.get(id = movie.id)
		# location_object = None

		for each_location in jsonBody['locations']:
			location = Location(name = each_location['name'], movie = movie_object)
			location.save()

			# if not location_object:
			location_object = Location.objects.get(id = location.id)

			for each_timing in each_location['timings']:
				timing = Timing(time = each_timing['time'], location = location_object)
				timing.save()

		HttpResponse.status_code = status.HTTP_200_OK
		return JsonResponse({'message': "Movie created successfully"})
	except CustomApiException as err:
		HttpResponse.status_code = err.status_code
		return JsonResponse({'status_code': err.status_code, 'message': err.detail})
	except Exception, e:
		HttpResponse.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		return JsonResponse({'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})


@csrf_exempt
@api_view(['PUT'])
def update_movie(request, id):
	"""
	Update movie with multiple locations and multiple timings
	"""
	try:

		jsonBody = json.loads(request.body)

		for key, value in jsonBody.iteritems():
			if not value:
				raise CustomApiException('Please provide '+ key, status.HTTP_400_BAD_REQUEST)

			for each_location in jsonBody['locations']:
				validate_function(each_location)

				for each_timing in each_location['timings']:
					validate_function(each_timing)

		movie_object = Movie.objects.get(id = id)

		movie_object.name = jsonBody['name']
		movie_object.save()

		for each_location in jsonBody['locations']:
			location = Location.objects.get(id = each_location['id'])

			location.name = each_location['name']
			location.save()

			for each_timing in each_location['timings']:
				timing = Timing.objects.get(id = each_timing['id'])

				timing.time = each_timing['time']
				timing.save()

		HttpResponse.status_code = status.HTTP_200_OK
		return JsonResponse({'message': "Movie Updated successfully"})
	except Movie.DoesNotExist as e:
		HttpResponse.status_code = status.HTTP_404_NOT_FOUND
		return JsonResponse({'status_code': status.HTTP_404_NOT_FOUND, 'message': "Movie not found"})
	except Location.DoesNotExist as e:
		HttpResponse.status_code = status.HTTP_404_NOT_FOUND
		return JsonResponse({'status_code': status.HTTP_404_NOT_FOUND, 'message': "Location not found"})
	except Timing.DoesNotExist as e:
		HttpResponse.status_code = status.HTTP_404_NOT_FOUND
		return JsonResponse({'status_code': status.HTTP_404_NOT_FOUND, 'message': "Timing not found"})
	except CustomApiException as err:
		HttpResponse.status_code = err.status_code
		return JsonResponse({'status_code': err.status_code, 'message': err.detail})
	except Exception, e:
		HttpResponse.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		return JsonResponse({'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})


@csrf_exempt
@api_view(['GET'])
def view_movie(request, id):
	"""
	Get movie by id with multiple locations and multiple timings
	"""
	try:

		movie_object = Movie.objects.get(id = id)

		movies_serializer = MovieSerializer(movie_object)

		HttpResponse.status_code = status.HTTP_200_OK
		return JsonResponse(movies_serializer.data)
	except Movie.DoesNotExist as e:
		HttpResponse.status_code = status.HTTP_404_NOT_FOUND
		return JsonResponse({'status_code': status.HTTP_404_NOT_FOUND, 'message': "Movie not found"})
	except CustomApiException as err:
		HttpResponse.status_code = err.status_code
		return JsonResponse({'status_code': err.status_code, 'message': err.detail})
	except Exception, e:
		HttpResponse.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		return JsonResponse({'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})

@csrf_exempt
@api_view(['DELETE'])
def delete_movie(request, id):
	"""
	Delete movie by id
	"""
	try:

		movie_object = Movie.objects.get(id = id)

		movie_object.delete()

		HttpResponse.status_code = status.HTTP_200_OK
		return JsonResponse({'message': "Movie deleted successfully"})
	except Movie.DoesNotExist as e:
		HttpResponse.status_code = status.HTTP_404_NOT_FOUND
		return JsonResponse({'status_code': status.HTTP_404_NOT_FOUND, 'message': "Movie not found"})
	except CustomApiException as err:
		HttpResponse.status_code = err.status_code
		return JsonResponse({'status_code': err.status_code, 'message': err.detail})
	except Exception, e:
		HttpResponse.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		return JsonResponse({'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})