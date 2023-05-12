from django.test import TestCase

# Create your tests here.
a = '010-292304-48962'
t = a.replace('-', '', 2).strip()
print(t)

