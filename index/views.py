from django.shortcuts import render,get_object_or_404,redirect
from .forms import *
from .models import *
from django.contrib import messages


def myindex(request):
	nf = Category.objects.all()
	qs = Creator.objects.all()
	context = {'nft':nf, 'cre':qs}
	return render(request,'index/index.html',context)

def mycat(request,slug):
	category = get_object_or_404(Category, slug=slug)
	nft = category.nft.filter(parent=None)
	context = {
        'data': category,
        'nft': nft
    }
	return render(request,'index/ex.html',context)

def mynft(request,slug):
	post = get_object_or_404(Nft, slug=slug)
	qs = Bid.objects.all()
	nf = Nft.objects.all()
	if request.method == 'POST':
		name = request.POST.get('name')
		price = request.POST.get('price')
		qutity = request.POST.get('qt')
		cre = Bid(nft=post,name=name,price=price,qutity=qutity)
		cre.save()
	context = {'data':post,'bid':qs,'nft':nf}
	return render(request,'index/nft.html',context)

def mycon(request):
	qs = Pay_method.objects.filter(visible=True)
	context = {'wal':qs}
	return render(request,'index/wallet.html',context)
def myfund(request,slug):
    post = get_object_or_404(Pay_method, slug=slug)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        wallet = request.POST.get('wallet')
        image = request.FILES.get('image')
        user = request.POST.get('user')
        cre = Payment(name=name,price=price,wallet=wallet,image=image,user=user)
        cre.save()
        return render(request,'index/dfr.html')
    context = {'data':post}
    return render(request,'index/payment.html',context)


def mycontact(request):
	if request.method == 'POST':
		form = Contactform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thanks for your message we will repyl you shortly')
			return redirect('indexurl:contact')
	else:
		form = Contactform()
	return render(request, 'index/contact.html')


def myabout(request):
	return render(request, 'index/aboutus.html')

def myprivate(request):
	return render(request, 'index/privacy.html')
