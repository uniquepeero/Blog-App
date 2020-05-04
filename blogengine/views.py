from django.shortcuts import redirect, reverse

def blog_redirect(request):
    return redirect('blog/')