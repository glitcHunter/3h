from django.test import TestCase
from amer.models import Character

# Create your tests here.
class ItemModelTest(TestCase):

    def test_model_save(self):
        first_item = Character()
        first_item.power = 2
        first_item.save()

        save_items = Character.objects.all()
        self.assertEqual(save_items.count(),1)


    def test_model_save_stats(self):
        stats = Character()
        stats.power = 2
        stats.save()
        
        stata_s = Character()
        stata_s.speed = 2
        stata_s.save()

        save_stats = Character.objects.all()
        self.assertEqual(save_stats.count(),2)

