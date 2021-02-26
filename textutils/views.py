from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   # return HttpResponse('<h1>helo moiz</h1> <a href="https://www.youtube.com/watch?v=sccLfQ4_u10&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6">click me</a>')
    
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    punctuations= '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
 
    if removepunc=='on':

        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuation','analyzed_text': analyzed}        
        djtext=analyzed
        #code for uppercase
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params={'purpose':'Change to UPPERCASE','analyzed_text': analyzed}   
        djtext=analyzed
        #code for new line remover
    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if(char!='\n' and char!='\r'):
                analyzed = analyzed + char
        params={'purpose':'Line removed of your text','analyzed_text': analyzed}   
        djtext=analyzed
    if(extraspaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]== " "):
                analyzed = analyzed + char
        params={'purpose':'Extra space removed','analyzed_text': analyzed}   
       # djtext=analyzed
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on'):
        return HttpResponse("Select any option and try again")
    

    return render(request,'analyzed.html',params)
    
#.................url seperatey all utils
# def capfirst(request):
#     return HttpResponse('capfirst <a href="../index">back</a>')
# def newlineremove(request):
#     return HttpResponse('newlineremove <a href="../index">back</a>')
# def spaceremove(request):
#     return HttpResponse('spaceremove <a href="../index">back</a>')
# def charcount(request):
#     return HttpResponse('charcount <a href="../index">back</a>')