(.venv) ~/Documents/Programowanie/VSCode/Devmentor/django/practice-django-models-and-forms/excercises git:[main]
python manage.py shell
15 objects imported automatically (use -v 2 for details).

Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Category, Article
>>> c = Category.objects.create(name="Python")
>>> Article.objects.create(title="Wprowadzenie do Pythona", content="...", category=c)
<Article: Wprowadzenie do Pythona>
>>> Article.objects.create(title="Zaawansowane typy danych", content="...", category=c)
<Article: Zaawansowane typy danych>
>>> for article in c.article_set.all():
... print(article.name)
  File "<console>", line 2
    print(article.name)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for article in c.article_set.all():
...     print(article.name)
... 
Traceback (most recent call last):
  File "<console>", line 2, in <module>
AttributeError: 'Article' object has no attribute 'name'
>>> for article in c.article_set.all():
...     print(article.title)
... 
Wprowadzenie do Pythona
Zaawansowane typy danych
>>> Article.objects.count()
2
>>> Category.objects.filter(name="Phyton").delete()
(0, {})
>>> Article.objects.count()
2
>>> Category.objects.filter(name="Python").delete()
(3, {'blog.Article': 2, 'blog.Category': 1})
>>> Article.objects.count()
0
>>> 