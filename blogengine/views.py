from django.shortcuts import redirect

def blog_redirect(request):
    return redirect('posts_list_url', permanent=True)