# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Log(models.Model):
    time = models.DateTimeField()
    user = models.CharField(max_length=32)
    text = models.CharField(max_length=1024)
