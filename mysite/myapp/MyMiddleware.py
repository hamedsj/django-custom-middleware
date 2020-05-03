from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMd(MiddlewareMixin):

    def process_request(self, request):
        if "p" in request.GET.keys():
            return HttpResponse("Hello Hamid =)")

    def process_view(self, request, view_function, view_args, view_kwargs):
        if view_function.__name__ == "process_view_test":
            return HttpResponse("This method only work for this view =)")
        print(view_function.__name__)
        return None
