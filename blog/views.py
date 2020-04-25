from django.shortcuts import render

def posts_list(request):
    n = ['Post1', 'Post2', 'Post3']
    return render(request, 'blog/index.html', context={'names': n})
