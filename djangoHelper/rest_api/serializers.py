#!/usr/bin/python
# -*- coding: utf-8 -*-

# 序列化器用于将我们的数据转换成JSON格式

from rest_framework import serializers
import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Post