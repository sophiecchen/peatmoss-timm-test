#!/usr/bin/python
# -*- coding: utf-8 -*-

import transformers

def pure_import():
    real = "bert-base-uncased"
    model = transformers.BertModel.from_pretrained(real)

    return 0