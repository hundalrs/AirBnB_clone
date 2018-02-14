#!/usr/bin/python3
'''Unittest for BaseModel class'''

import io
from models.base_model import BaseModel
import sys
import unittest


class MyTest(unittest.TestCase):
    '''unittests for BaseModel'''

    def test_model_created(self):
        '''testing if instance is created'''
        instance_1 = BaseModel()
        self.assertTrue(instance_1)

    def test_id_exists(self):
        '''testing if id exits'''
        instance_2 = BaseModel()
        self.assertEqual(len(instance_2.id), 36)

    def test_class(self):
        '''testing if class works'''
        instance_3 = BaseModel()
        self.assertEqual((instance_3.__class__), BaseModel)

    def test_dict(self):
        '''testing if to_dict returns dictionary'''
        instance_4 = BaseModel()
        self.assertEqual(dict, type(instance_4.to_dict()))

    def test_created_at(self):
        '''testing if created_at is assigned'''
        instance_4 = BaseModel()
        self.assertTrue(instance_4.created_at)

    def test_updated_at(self):
        '''testing if updated_at is assigned'''
        instance_4 = BaseModel()
        self.assertTrue(instance_4.updated_at)

if __name__ == '__main__':
    unittest.main()
