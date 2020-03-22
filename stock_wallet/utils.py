import random
import string

from django.utils.text import slugify

DONT_USE = ['create', 'delete']

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# def unique_slug_generator(instance, new_slug = None):
#     if new_slug is not None:
#         slug = new_slug
#     else:
#         slug = slugify(instance.title)
#
#     if slug.lower() in DONT_USE:
#         new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=4))
#
#         return unique_slug_generator(instance, new_slug=new_slug)
#
#
#     Klass = instance.__class__
#     qs_exists = Klass.objects.filter(slug=slug).exists()
#
#     if qs_exists:
#         new_slug = "{slug}-{randstr}".format(slug = slug, randstr = random_string_generator(size=4))
#
#         return unique_slug_generator(instance, new_slug=new_slug)
#     return slug

def unique_slug_generator(instance, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = random_string_generator(size=8)

    if slug.lower() in DONT_USE:
        new_slug = "{slug}".format(slug=slug)

        return unique_slug_generator(instance, new_slug=new_slug)


    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}".format(slug =  random_string_generator(size=8))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def cash_payment_withdrawal(instanse):
    pass
