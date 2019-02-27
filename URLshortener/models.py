from random import choice
import string

from django.db import models

def check_uniqness(short_part):
    '''
    проверка на наличие в базе данных короткой части URL и в случае наличия, генерация новой
    '''
    try:
        if URLs.objects.get(short_url = short_part):
            return create_short_url()
    except:
        return short_part


def create_short_url():
    '''
    генерирует короткую часть URL из трёх символов, для которых берётся случайная комбинация
    из строки символов и чисел
    '''
    chars = string.digits + string.ascii_letters
    short_part = ''.join(choice(chars) for i in range(3))
    short_part = check_uniqness(short_part)
    return short_part


class URLs(models.Model): #таблица, содержащая оригинальный URL и короткую версию
    shortURL = models.URLField(unique=True, default=create_short_url)
    originURL = models.URLField(unique=True)