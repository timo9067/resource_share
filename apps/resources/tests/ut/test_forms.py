from django.test import TestCase
from apps.resources.form import PostResourceForm


# Test Case # Test<form-name>Form

class TestPostResourceForm(TestCase):
    #unit test 1
    def test_valid_form(self):
        data = {
            "title": "Python for beginners",
            "link": "http://pfb.com",
            "description": "Test description",
            # TODO: Add more key-value pairs base on your form
        }
        
        # ACT
        form = PostResourceForm(data=data)
        
        # ASSERT
        self.assertTrue(form.is_valid())
        
    def test_form_not_valid_when_link_is_missing(self):
        data = {
            "title": "Python for beginners",
            # "link": "http://pfb.com",
            "description": "Test description",
            # TODO: Add more key-value pairs base on your form
        }
        
        # ACT
        form = PostResourceForm(data=data)
        form.is_valid() # this is needed for the orm to generate any errors
        
        # ASSERT
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["link"], ["This field is required."])
