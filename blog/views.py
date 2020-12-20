from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, '/Users/rdshinde/Documents/Django/mysite/blog/template/blog/post_list.html', {})