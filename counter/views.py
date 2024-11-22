from django.shortcuts import render

def counter(request):
    if request.method == 'POST':
        text = request.POST['texttocount']
        if text != ' ':
            word = len(text.split())
            i = True

            #returning html page with data if calculated successfully
            return render(request, 'counter/counter.html', 
                   {'word': word, 'text':text, 'i':i, 'on':'active'})
        else:
            #returning the page without any data if any error occurs
            return render(request, 'counter.html', {'on': 'active'})
    else:
        return render(request, 'counter/counter.html', {'on': 'active'})