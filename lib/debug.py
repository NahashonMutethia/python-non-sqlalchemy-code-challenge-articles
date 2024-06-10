#!/usr/bin/env python3
import ipdb
from classes.many_to_many import Article, Author, Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Create some instances
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    # Add articles
    article1 = author1.add_article(magazine1, "The Rise of AI")
    article2 = author1.add_article(magazine2, "Healthy Living Tips")
    article3 = author2.add_article(magazine1, "Latest Tech Trends")
    article4 = author1.add_article(magazine1, "AI in Healthcare")

    # Test methods
    print(author1.articles())  # Should return articles by John Doe
    print(magazine1.contributors())  # Should return authors who wrote for Tech Today
    print(magazine1.article_titles())  # Should return titles of articles in Tech Today
    print(Magazine.top_publisher())  # Should return the magazine with most articles

    # Don't remove this line, it's for debugging!
    ipdb.set_trace()
