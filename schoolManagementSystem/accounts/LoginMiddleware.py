from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

# def LoginCheckMiddleware(get_response):
#     print("one time print")
#     def my_function(request):
#         print("this is before view")
#         response = get_response(request)
#         print("this is after view")
#         return  response
#     return my_function

# class LoginCheckMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         print("one time print")
#
#     def __call__(self, request):
#         print("this is before view")
#         response = self.get_response(request)
#         print("this is after view")
#         # response = HttpResponse('valo aci')
#         return response

# class LoginCheckMiddleware:
#     def __init__(self,get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
#     def process_view(request,*args,**kwargs):
#         print("this is process biew")
#         # return HttpResponse("this is before view")
#         return None


class LoginCheckMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.is_admin == True:
                if modulename == "student_managment_app.admin_views":
                    pass
                elif modulename == "student_managment_app.views":
                    pass
                elif modulename == "accounts.views":
                    pass
                else:
                    # None
                    return HttpResponseRedirect(reverse("student_managment_app:classShow"))
            elif user.is_teacher == True:
                if modulename == "student_managment_app.admin_views":
                    pass
                elif modulename == "student_managment_app.views":
                    pass
                elif modulename == "accounts.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_managment_app:sectionShow"))
                    # None

        else:
            if request.path == reverse("frontpage") or request.path == reverse("singup") or request.path == reverse("login") or request.path == reverse("admin_signup") or request.path == reverse("headmaster_signup") or request.path == reverse("teacher_signup") or request.path == reverse("student_signup") or request.path == reverse("parent_signup"):
                pass
            else:
                return HttpResponseRedirect(reverse("frontpage"))
                # None
