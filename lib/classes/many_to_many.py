# classes/many_to_many.py

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._validate_title(title)
        self._title = title

    @property
    def title(self):
        return self._title

    @staticmethod
    def _validate_title(title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @title.setter
    def title(self, value):
        self._validate_title(value)
        self._title = value

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author class.")
        self._author = value

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class.")
        self._magazine = value


class Author:
    def __init__(self, name):
        self._validate_name(name)
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._validate_category(value)
        self._category = value

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")

    @staticmethod
    def _validate_category(category):
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_article_count = {}
        for article in self._articles:
            if article.author not in author_article_count:
                author_article_count[article.author] = 0
            author_article_count[article.author] += 1
        return [author for author, count in author_article_count.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda mag: len(mag.articles()))
