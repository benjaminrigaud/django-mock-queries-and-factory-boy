# -*- coding: utf-8 -*-

from django.test import TestCase

from django_mock_queries.mocks import mocked_relations

from issue.main.models import ModelA, ModelB
from issue.main.tests.factories import AFactory, BFactoryWithSub, BFactory


class FactoryBoyTestCase(TestCase):

    def test_no_mock(self):
        a = AFactory()
        b = BFactory()
        b2 = BFactoryWithSub()

        b3 = BFactory(a=a)
        b4 = BFactoryWithSub(a=a)

        self.assertEqual(ModelA.objects.count(), 2)
        self.assertEqual(ModelB.objects.count(), 4)

    @mocked_relations(ModelA)
    @mocked_relations(ModelB)
    def test_mock(self):
        a = AFactory()
        b = BFactory()
        b2 = BFactoryWithSub()

        b3 = BFactory(a=a)
        b4 = BFactoryWithSub(a=a)

        self.assertEqual(ModelA.objects.count(), 2)
        self.assertEqual(ModelB.objects.count(), 4)
