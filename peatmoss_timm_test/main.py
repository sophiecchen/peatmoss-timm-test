#!/usr/bin/python
# -*- coding: utf-8 -*-

from timm.models import create_model

def from_import():
    one = "resnet50"
    two = create_model(one)

    return 0
