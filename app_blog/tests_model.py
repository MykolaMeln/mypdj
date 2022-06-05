from django.test import TestCase
from .models import Category, Article

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category='Innovations', slug='innovations')

    def test_get_absolute_url(self):
        category=Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(), '/articles/category/innovations')
    
class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(
            title="ІТ новини 1",
            slug="it-novini-1",
            description="Новини з ІТ 1",
            main_page=True,
        )

    def test_get_absolute_url(self):
        article = Article.objects.get(id=1)
        self.assertEquals(article.get_absolute_url(), "/articles/2022/06/05/it-novini-1")