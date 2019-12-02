from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

# Create your tests here.
class APITest(TestCase):
	@classmethod
	def setUpClass(cls):
		user = User.objects.create_user(username="user1",password="user1")
		cls.client = APIClient()
		
		
	@classmethod
	def tearDownClass(cls):
		cls.client.logout()

	def test_CreateCategory(self):
		resp = self.client.login(username="user1",password="user1")
		resp = self.client.post("/api/categories/",data={"name":"apicat"})
		self.assertTrue(resp.status_code in [200,201])
		resp = self.client.get("/api/categories/")
		self.assertTrue(resp.status_code==200)
		data = resp.json()
		cat = data[0]
		self.assertTrue(cat["name"]==apicat)
	# n number of test cases

