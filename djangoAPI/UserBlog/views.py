from django.shortcuts import render


from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserBlog.models import Users, Blog
from UserBlog.serializers import UsersSerializer, BlogSerializer

# Create your views here.
@csrf_exempt
def userApi(request, id=0):
    if request.method=='GET':
        users =  Users.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method=='POST':
        user_data=JSONParser().parse(request)
        users_serializer=UsersSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        user_data=JSONParser().parse(request)
        user=Users.objects.get(UserId=user_data['UserId'])
        users_serializer=UsersSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        user=Users.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def BlogApi(request, id=0):
    if request.method=='GET':
        blogs =  Blog.objects.all()
        blogs_serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(blogs_serializer.data, safe=False)
    elif request.method=='POST':
        blog_data=JSONParser().parse(request)
        blogs_serializer = BlogSerializer(data=blog_data)
        if blogs_serializer.is_valid():
            blogs_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        blog_data = JSONParser().parse(request)
        blog = Blog.objects.get(BlogId=blog_data['BlogId'])
        blogs_serializer = BlogSerializer(blog, data=blog_data)
        if blogs_serializer.is_valid():
            blogs_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        blog=Blog.objects.get(BlogId=id)
        blog.delete()
        return JsonResponse("Deleted Successfully",safe=False)
           