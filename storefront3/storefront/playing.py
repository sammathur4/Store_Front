import os
import django
from django.urls import get_resolver
# from django.urls.resolvers import URLResolver, URLPattern
# import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storefront.settings")  # Set your project's settings module here
django.setup()


def get_all_endpoints1(urlpatterns, namespace=None):
    endpoints = []
    for pattern in urlpatterns:
        if hasattr(pattern, 'callback') and pattern.callback is not None:
            view_name = f"{namespace}:{pattern.callback.__module__}.{pattern.callback.__qualname__}"
            endpoints.append({
                'endpoint': view_name,
                'path': str(pattern.pattern)
            })
        elif hasattr(pattern, 'url_patterns'):
            if namespace is not None:
                ns = f"{namespace}:{pattern.namespace}"
            else:
                ns = pattern.namespace
            endpoints += get_all_endpoints1(pattern.url_patterns, namespace=ns)
    return endpoints


def call_all_endpoints1():

    resolver = get_resolver()
    all_endpoints = get_all_endpoints1(resolver.url_patterns)

    for endpoint in all_endpoints:
        print(f"Endpoint: {endpoint['endpoint']}")
        print(f"Path: {endpoint['path']}")
        print()



def get_all_endpoints2(urlpatterns, namespace=None):
    endpoints = []
    for pattern in urlpatterns:
        if hasattr(pattern, 'callback') and pattern.callback is not None:
            view_name = f"{namespace}:{pattern.callback.__module__}.{pattern.callback.__qualname__}"
            parameters = pattern.pattern.converters
            endpoint_info = {
                'endpoint': view_name,
                'path': str(pattern.pattern)
            }
            if parameters:
                endpoint_info['parameters'] = [p for p in parameters]
            endpoints.append(endpoint_info)
        elif hasattr(pattern, 'url_patterns'):
            if namespace is not None:
                ns = f"{namespace}:{pattern.namespace}"
            else:
                ns = pattern.namespace
            endpoints += get_all_endpoints2(pattern.url_patterns, namespace=ns)
    return endpoints

from django.urls import get_resolver

resolver = get_resolver()
all_endpoints = get_all_endpoints2(resolver.url_patterns)

for endpoint in all_endpoints:
    print(f"Endpoint: {endpoint['endpoint']}")
    print(f"Path: {endpoint['path']}")
    if 'parameters' in endpoint:
        print("Parameters:")
        for param in endpoint['parameters']:
            print(f"  - {param}")
    print()