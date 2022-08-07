# I have created this file - Shiva
from django.http import HttpResponse
from django.shortcuts import render



# def about(request):
#     return HttpResponse("World")
# def text(request):                  #reading a file and displaying the file content
#     file=open("mysite\one.txt","r")
#     data=file.read()
#     return HttpResponse(data)

# def nav(request):                   #creating a weblink.
#     return HttpResponse('''                 
#         <a href="https://www.google.com/search?q=views+and
#         +urls+in+django&rlz=1C1RXQR_enIN993IN993&oq=VIEWS+A
#         ND+URLS&aqs=chrome.0.0i512j69i57j0i390l2.6083j0j7&so
#         urceid=chrome&ie=UTF-8"> Google </a>
#     ''')
# def home(request):
#     return HttpResponse('''home<br>
#     <a href="/"><button>Click me</button></a>''')
# def capitalize(request):
#     return HttpResponse("capitalize")
# def index(request):
#     return HttpResponse('''Home<br>
#     <a href='about/'><button>About</button></a>
#     <a href='contact/'><button>Contact</button></a>
#     ''')
def index(request):
    
    return render(request,'index.html')

def about(request):
    return HttpResponse("About")
def analyze(request):
    # print(request.GET.get('text','default'))
    
    data=request.GET.get('text','default')
    capital_check=request.GET.get('capitalize','off')
    char_count=request.GET.get('char_count','off')
    count=0
    if(capital_check=='on'):
        cap_data=''
        for char in data:
            cap_data=cap_data+char.upper()
        cap_dict={'purpose':cap_data}
        return render(request,'analyze.html',cap_dict)
    elif(char_count=='on'):
        while(count<len(data)):
            count=count+1
        cap_dict={'purpose':count-10}
        return render(request,'analyze.html',cap_dict)
    else:
        return HttpResponse("Error")

    

    

