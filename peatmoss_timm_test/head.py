#!/usr/bin/python
# -*- coding: utf-8 -*-

from timm import models

def from_import():
    one = "resnet50"
    two = models.create_model(one, False)

    return 0
