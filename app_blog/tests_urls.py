from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleDetail, ArticleList, ArticleCategoryList

from django.utils import timezone
from django.utils.timezone import localtime, now
from .models import Article

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)

class CategoryTests(TestCase):
    def test_category_view_status_code(self):
        url = reverse("articles-category-list", args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class ArticlesTests(TestCase):
    def test_articles_view_status_code(self):
        url = reverse("articles-list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_articles_url_resolves_articles_view(self):
        view = resolve("/articles")
        self.assertEquals(view.func.view_class, ArticleList)

class ArticlesCategoryListTests(TestCase):

    def test_articles_category_url_resolves_articles_category_view(self):
        view = resolve("/articles/category/it-novini")
        self.assertEquals(view.func.view_class, ArticleCategoryList)
    
    def test_article_category_view_status_code(self):
        url = reverse("articles-category-list", args=('it-novini',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

class ArticleDetailsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(
            title="ІТ новини 1",
            slug="it-novini-1",
            description="Новини з ІТ 1",
            main_page=True,
        )

    def test_article_detail_view_status_code(self):
        today = localtime(now())
        day = today.day
        month = today.month
        year = today.year

        url = reverse("news-detail", args=(year, month, day, "it-novini-1"))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_detail_url_resolves_article_detail_view(self):
        today = localtime(now())
        day = today.day
        month = today.month
        year = today.year

        view = resolve("/articles/{}/{}/{}/it-novini-1".format(year, month, day))
        self.assertEquals(view.func.view_class, ArticleDetail)

