__author__ = 'calvinmwhu'
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final.settings')

import django

django.setup()

from interviewmate.models import Category, Question


def populate():
    array = add_cat('Array', views=50, likes=20)

    content = "Given an array of integers, find two numbers such that they add up to a specific target number."
    two_sum = add_question(cat=array, title="Two Sums", content=content)

    content = "You are given an n x n 2D matrix representing an image; rotate the image by 90 degrees (clockwise)."
    rotate_image = add_question(cat=array, title="Rotate Image", content=content)

    content = "Find the contiguous subarray within an array (containing at least one number) which has the largest sum."
    max_sub_array = add_question(cat=array, title="Maximum Subarray", content=content)

    string = add_cat('String', views=20, likes=2)

    content = "Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999."
    integer_to_roman = add_question(cat=string, title="Integer to Roman", content=content)

    content = "Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)"
    edit_distance = add_question(cat=string, title="edit distance", content=content)

    heap = add_cat('Heap', views=42, likes=30)

    content = "Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity."
    merge_k_lists = add_question(cat=heap, title="merge k sorted lists", content=content)

    data_structure = add_cat('data structure')

    content = "Design a stack that supports push, pop, top, and retrieving the minimum element in constant time."
    min_stack = add_question(cat=data_structure, title="min stack", content=content)

    content = "Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set."
    lru_cache = add_question(cat=data_structure, title="LRU cache", content=content)

    binary_search = add_cat('Binary Search',views=34, likes=12)

    content = "Given a sorted array of integers, find the starting and ending position of a given target value."
    search_range = add_question(cat=binary_search, title="Search for a range", content=content)

    content = "Write an efficient algorithm that searches for a value in an m x n matrix."
    search_matrix = add_question(cat=binary_search, title="search a 2D matrix", content=content)

    linked_list = add_cat('Linked List', views=21, likes=19)

    content = "Sort a linked list in O(n log n) time using constant space complexity. Hide Tags"
    sort_list = add_question(cat=linked_list, title="Sort list", content=content)

    content = "Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists."
    merge_list = add_question(cat=linked_list, title="Merge two sorted lists", content=content)

    for c in Category.objects.all():
        for q in Question.objects.filter(category=c):
            print "- {0} - {1} - {2}".format(str(c), str(q), str(q.content))


def add_question(cat, title, content="", views=0):
    q = Question.objects.get_or_create(category=cat, title=title)[0]
    q.views = views
    q.content = content
    q.save()
    return q


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print "Starting interviewmate population script..."
    populate()