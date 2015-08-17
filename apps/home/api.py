
# apps/home/api.py

from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
# from tastypie.models import ApiKey
# from tastypie import fields




from apps.home.models import Students



# Students API
class StudentResource(ModelResource):

	class Meta:
		queryset = Students.objects.all()
		resource_name = 'students'

		filtering = {
			'name':('iexact', 'icontains',)
				}

		allowed_methods = ['get',]


