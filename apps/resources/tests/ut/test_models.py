from django.test import TestCase
from apps.resources import models


# Test Case class # Test<model-name>Model

class TestTagModel(TestCase):
    def setUp(self):
        self.tag_name = "Python"
        self.tag = models.Tag(name=self.tag_name)
        
    # unit test 1 # test_<logic_name>
    
    def test_create_tag_object_successful(self):
        # Check if the object created is of the instance Tag
        self.assertIsInstance(self.tag, models.Tag)
        
    # unit test 2
    def test_dunder_str(self):
        # str(self.tag)
        # self.__str__()
        
        self.assertEqual(str(self.tag), self.tag_name)
        
class TestCategoryModel(TestCase):
    def setUp(self) -> None:
        self.cat_name = "Self-study"
        self.cat = models.Category(cat=self.cat_name)
        
    def test_create_category_successful(self):
        self.assertIsInstance(self.cat, models.Category)
    
    def test_dunder_str(self):
        self.assertEqual(str(self.cat), self.cat_name)
    
    def test_verbose_name_plural(self): 
        self.assertEqual(models.Category._meta.verbose_name_plural, "Categories") # works