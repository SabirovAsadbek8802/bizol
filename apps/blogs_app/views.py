from django.shortcuts import render


def blogList(request):
    return render(request, 'blog_list.html')
    
    
def blogSingle(request, pk):
    return render(request, 'blog_single.html')    
    