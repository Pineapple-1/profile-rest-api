# profile-rest-api

<p>Why we need api why cant we use driect database to access the data? Because we have to give permissions of read and write by hand to every user which is not possible so we give permission to a single computer which is called a server. so we send requests to a webpage which is on a computer and that computer is gonna pass your request to the database and send you back so thats how it handles taffic.</p>

## how to start django-application:

- django-admin start project
- make apps by python manage.py start app .
- (this dot tells that make it in same directory)
- then go to settings.py and put name in the INSTALLED APPS
- create custom user models or use simpler model
- make migration (USE IT FOR THE FIRST TIME TOOO)
- migrate (TO FIRE UP DJANGO)
- create superuser for admin side access
- first register your app in admin.py so it can show up in admin side
- then python runserver
- when you use urls.py file include() function takes address
- like include('appname.urls')

## how to write apis

- so first we import APIVIEWS from rest_framework.views in our api views.
- because in every API view we need to inheret
- APIVIEW and then every class has to return a response
- So we also need to import Response from rest_framework.response
- the in our api view class we make functions like get post update delete
- becasue it has to be same as our requests.
- when we have view or see data we send get requests.

## how to write serializers

- first you have to import serializers from rest_framework.
- what they do is like they create these froms from which you can accept data.
- comming from POST request.
- so you have the import the models which is gonna intract with a serializer.
- when you are making a class for a serialize you need to inherit from serializers.ModelSerializer
- Beacuse we are intracting with a model.
- Then we write meta class meta class will make sure that we intract. (meta with a big 'M' as in 'Meta')
- Then we need to tell the class which is the model by specifing the model variable in the meta class.
- With the models feilds which are specified in the feilds variable which takes an array.

## how to write viewset for models.

- First import viewset from rest_framework.
- Make a class and inherit viewset.ModelViewSet.
- Then all you need to do is give varible names.
- Class variables. like serializer_class you need to tell which serializer this view will intract.
- queryset variable need to know which of the model managers functions can we use.
- like in serializer we used one create_user but we let queryset have access to all of them 
- queryset = models.UserProfile.objects.all() => means access to all functions.
- then authentication_class wants a tuple so send it like (tokenauthentication,).
- permission_class wants the permission class from permissions.py. (send it like tuple)
- filter_backends wants how you want to filterout data as tuple. (filters.SearchFilter,).
- search_fields wants array of fields you want to search for like: ['name','email'] 
- you can also send tuples in search_feilds.


