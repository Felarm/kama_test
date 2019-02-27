from django.shortcuts import render, HttpResponseRedirect
from .forms import URLForm
from .models import URLs


def redirect(request, short_part):
    '''
    перенаправляет на оригинальный URL
    '''
    url = URLs.objects.get(shortURL=short_part)
    return HttpResponseRedirect(url.originURL)


def shortener(request):
    '''
    создаёт новую запись в бд с оригинальным адресом и сгенерированной короткой частью
    '''
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            if url: #если отправили не пустую строку
                new_url = URLs.objects.get_or_create(originURL=url)
                constraint_url = 'http://127.0.0.1:8000/%s' % new_url[0].shortURL
                #если получившийся URL больше оригинального, то выводим оригинальный и стираем запись о коротком из бд
                if len(constraint_url) <= len(new_url[0].originURL):
                    return render(request, 'URLshortener/urlshortener.html', {'url': constraint_url})
                else:
                    new_url[0].delete()
                    return render(request, 'URLshortener/urlshortener.html', {'url': url})
            else: #иначе возвращаем пустую форму
                return render(request, 'URLshortener/urlshortener.html', {'form': URLForm()})
        else:
            form = URLForm()
            return render(request, 'URLshortener/urlshortener.html', {'form': form})
    else:
        form = URLForm()
        return render(request, 'URLshortener/urlshortener.html', {'form': form, 'url': ''})