#!/usr/bin/python3
'''test suite for model/user.py'''
import unittest
import json
import os
import sys
from models import storage
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUserClass(unittest.TestCase):
    '''test suite class'''

    def test_type(self):
        '''tests user inst created'''
        usr = User()
        self.assertEqual(type(User()), type(usr))

    def test_email_initial(self):
        '''test initial value of email attribute'''
        usr = User()
        self.assertTrue(type(usr.email) is str)

    def test_password_initial(self):
        '''test initial value of password attribute'''
        usr = User()
        self.assertTrue(type(usr.password) is str)

    def test_first_name_initial(self):
        '''test initial falue of first_name attribute'''
        usr = User()
        self.assertTrue(type(usr.first_name) is str)

    def test_last_name_initial(self):
        usr = User()
        self.assertTrue(type(usr.last_name) is str)

    def test_created_at(self):
        '''created at attribute test'''
        usr = User()
        self.assertEqual(datetime, type(usr.created_at))

    def test_updated_at(self):
        '''updated at attribute test'''
        usr = User()
        self.assertEqual(datetime, type(usr.updated_at))

    def test_save_updated(self):
        '''tests if save is changing updated_at to current datetime'''
        usr = User()
        prev = usr.updated_at
        usr.save()
        self.assertNotEqual(prev, usr.updated_at)

    def test_updated_at_is_str(self):
        '''tests if updated_at is a string'''
        usr = User()
        usr_dict = usr.to_dict()
        self.assertEqual(str, type(usr_dict['updated_at']))

    def test_created_at_is_str(self):
        '''tests if created at is a string'''
        usr = User()
        usr_dict = usr.to_dict()
        self.assertEqual(str, type(usr_dict['created_at']))

    def test_updated_at_to_dict(self):
        '''tests if updated at is in dictionary'''
        usr = User()
        usr_dict = usr.to_dict()
        self.assertIn('updated_at', usr_dict)

    def test_created_at_to_dict(self):
        '''tests if created at is in dictionary'''
        usr = User()
        usr_dict = usr.to_dict()
        self.assertIn('created_at', usr_dict)

if __name__ == '__main__':
    unittest.main()
