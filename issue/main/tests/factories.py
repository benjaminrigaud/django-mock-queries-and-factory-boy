# -*- coding: utf-8 -*-

from factory import DjangoModelFactory, SubFactory

from issue.main.models import ModelA, ModelB


class AFactory(DjangoModelFactory):
    class Meta:
        model = ModelA


class BFactory(DjangoModelFactory):
    class Meta:
        model = ModelB


class BFactoryWithSub(DjangoModelFactory):
    class Meta:
        model = ModelB

    a = SubFactory(AFactory)

