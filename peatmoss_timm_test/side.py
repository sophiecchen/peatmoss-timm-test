#!/usr/bin/python
# -*- coding: utf-8 -*-

import timm

def pure_import():
    real = "resnet50"
    model = timm.create_model(real)

    real2 = "resnet50"
    model2 = timm.models.create_model(real2)

    return 0