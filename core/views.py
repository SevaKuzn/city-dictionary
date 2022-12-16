from django.shortcuts import render

# Create your views here.
def main(request):
    cities = ['Moсква','Санкт-Петербург','Тында','Анадырь','Воронеж','Кострома','Саратов']
    return render(request, 'base.html',{'cities': cities})
