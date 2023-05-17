from django.http import HttpResponse, Http404

import random

from django.shortcuts import redirect, render
from django.urls import reverse_lazy


# def home(request):
#     html = f'<h1>{request.method}: This is home</h1>',
#     # return HttpResponseNotFound
#     return HttpResponse(
#             html,
#             # status=201,
#             headers={
#                 'x-sibina-header': 'Django',
#             },
#         )

def home(request):
    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list departments'))
    print(reverse_lazy('custom url'))
    print('/departments/filter/by/order-by/')
    print(reverse_lazy('department details', kwargs={
        'id': 7,
    }))

    context = {
        'number': random.randint(0, 1024),
        'numbers': [random.randint(0, 1024) for _ in range(16)],
    }
    return render(request, 'index.html', context)


def go_to_home(request):
    # return redirect(to='/')
    # return HttpResponseRedirect

    return redirect('department details', id=random.randint(1, 1024))


def not_found(request):
    # return HttpResponseNotFound()
    raise Http404()

def department_details(request, id):
    if not isinstance(id, int):
        pass
    return HttpResponse(f'This is department {id}, {type(id)}')


def list_departments(request):
    return HttpResponse('This is a list of departments')


def create_department(request):
    return HttpResponse('Created')