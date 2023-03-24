# List Comprehension

# /Users/nganguyen/PycharmProjects/100-days-of-python/day-26-list-and-dictionary-comprehension/venv/bin/python "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py" --mode=client --port=52344
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/nganguyen/PycharmProjects/100-days-of-python/day-26-list-and-dictionary-comprehension'])
PyDev console: starting.
Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10)
[Clang 6.0 (clang-600.0.57)] on darwin
names = ["Alex", "Beth", "Caroline", "Tom", "David", "Freddie"]
import random
student_scores = {name:random.randint(1, 100) for name in names}
student_scores
{'Alex': 10, 'Beth': 2, 'Caroline': 100, 'Tom': 58, 'David': 53, 'Freddie': 50}
passed_students = {name:score for (name, score) in student_scores.items() if score > 50}
passed_students
{'Caroline': 100, 'Tom': 58, 'David': 53}
