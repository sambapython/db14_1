from django.test import TestCase
from product.models import Category,Product

# Create your tests here.

class CategoryTest(TestCase):

    def test_create(self):
        cat = Category(name="cat1")
        cat.save()
        cats = Category.objects.all()
        error = "test_create failed"
        if cats:
            cat_name = cats[0].name 
            self.assertEqual("cat1",cat_name,error)
        else:
            self.assertEqaul(1,2,error)
class ProductTest(TestCase):
    def setUp(self):
        cat = Category(name="cat1")
        cat.save()
        cats = Category.objects.all()
        cat = cats[0]
        pro = Product(name="prod1",category=cat,description="desc1")
        pro.save()
        self.prod_id=pro.id

    def test_product_update_name(self):
        pro = Product.objects.get(id=self.prod_id)
        pro.name="Update prod1"
        pro.save()
        pro = Product.objects.get(id=self.prod_id)
        self.assertTrue(pro.name=="Update prod1","test_product_update_name failed")
    def test_product_update_description(self):
        pro = Product.objects.get(id=self.prod_id)
        pro.description="Update prod1"
        pro.save()
        pro = Product.objects.get(id=self.prod_id)
        self.assertTrue(pro.description=="Update prod1","test_product_update_description failed")
    def tearDown(self):
        pro = Product.objects.all()
        [i.delete() for i in pro]

