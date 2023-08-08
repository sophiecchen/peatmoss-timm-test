#!/usr/bin/python
# -*- coding: utf-8 -*-

from transformers import BertModel

def from_import():
    one = "bert-base-uncased"
    two = BertModel.from_pretrained(one)

    return 0
