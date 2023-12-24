from django.db import models

CATEGORIES = [
    ('Basketball', 'Basketball'),
    ('Cars', 'Cars'),
    ('Drinks', 'Drinks'),
    ('E-Commerce', 'E-Commerce'),
    ('Fashion', 'Fashion'),
    ('Financial', 'Financial'),
    ('Food','Food'),
    ('Industrial', 'Industrial'),
    ('Internet','Internet'),
    ('Media','Media'),
    ('Soccer','Soccer'),
    ('Technology','Technology')
]

class Logo(models.Model):
    company = models.CharField(max_length=25)
    image = models.ImageField(upload_to='logos')
    category = models.CharField(max_length=25, choices=CATEGORIES)

    def __str__(self):
        return self.company