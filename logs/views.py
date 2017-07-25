# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Log


def index(request):
    return render(request, 'index.html')


def hist_for_user(request):
    if 'username' not in request.GET:
        return redirect('home')

    username = request.GET.get('username').lower()
    objects = Log.objects.filter(
        user=username,
    ).order_by(
        '-time',
    )[:100]

    output = "\n".join(["[{o.time}] [{o.user}] {o.text}".format(o=o) for o in objects])

    context = {
        'username': username,
        'logs': objects,
    }

    return render(request, 'hist_for_user.html', context)
