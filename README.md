### This repository created in attach to [this post](https://medium.com/@hamedsj5/create-a-custom-middleware-for-django-project-f0806bf36726 )
# What are middlewares?
In short, middlewares are classes that contain some functions called before and after all view functions. For more detail on middleware, you can click [here](https://medium.com/zeitcode/django-middlewares-and-the-request-response-cycle-fcbf8efb903f).
# What requirements should middlewares have?
the only requirement for a class to be a middleware is that middleware must have at least one of the following methods:
* _process_request_
* _process_view_
* _process_response_
* _process_exception_
# How do these methods work?
Every Django project has a list called `MIDDLEWARES` (or `MIDDLEWARE_CLASSES` in older versions) in `settings.py` that contains the path of every middleware that has at least one of the methods mentioned above.
after  request received by the framework, WSGI Handler builds a `HttpRequest` object for passing to view functions and in this process it iterates through the list and it will call `process_request` method from every class in the list that contains this method. (if one class in the list doesn't have `process_request` , it will just get skipped.)
after building `HttpRequest` object and before passing it to every view function WSGI Handler will call `process_view` method of middlewares.

* `process_request` and `process_view` methods should return `None` that in this case WSGI Handler will continue the cycle; or this methods should alternatively return `HttpResponse` that in this case WSGI Handler will begin `process_response` cycle.
if a view function raise an exception WSGI Handler will begin `process_exception` cycle and if a view function returns `HttpResponse` object, WSGI Handler will begin `process_response` cycle.
* unlike `process_request` and `process_view` methods, `process_response` and `process_exception` can only modify the data of response/exception
