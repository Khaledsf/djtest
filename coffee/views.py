from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Grain, Roast
from django.shortcuts import get_object_or_404, render
from .forms import CoffeeForm


def all_grains(request):
	if request.method == 'POST':
		# form = CoffeeForm()
		if 'submit' in request.POST:
			id = request.POST.get('update')
			print(id)
			if id == None:
				form = CoffeeForm(request.POST, request.FILES)
				form.save()
			elif id != None:
				print('This id inside submit: ', id)
				obj = Grain.objects.get(id=id)
				form = CoffeeForm(request.POST, instance=obj)
				# if form.is_valid():		
				form.save()	
		if 'delete' in request.POST:
			id = request.POST.get('delete')
			obj = Grain.objects.get(id = id)
			obj.delete()
		if 'edit' in request.POST:
			id = request.POST.get('edit')
			# print('Iside edit action: ', id)
			obj = Grain.objects.get(id=id)
			form = CoffeeForm(instance=obj)
			grains = Grain.objects.all()
			print(form.instance.id)
			return render(request, 'all_grains.html', {'grains': grains, 'form': form})

	
	grains = Grain.objects.all()
	form = CoffeeForm()
	
	return render(request, 'all_grains.html', {'grains': grains, 'form': form})

def single_grain(request, param=''):
	if 	isinstance(param, int):
		grain = Grain.objects.get(id = param)
		return render(request, 'single_grain_int.html', {'grain': grain})
	elif isinstance(param, str):
		return render(request, 'single_grain_str.html', {'param': param})
	else:
		param = ''
		return render(request, 'single_grain.html', {'param': param})	

# def edit(request, param):
# 	obj = Grain.objects.get(id=int(param))
# 	form = CoffeeForm(instance=obj)
# 	if request.method == 'POST':
# 		form = CoffeeForm(request.POST, instance=obj)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/coffee')

# 	return render(request, 'edit.html', {'form': form})

def tryme(request):
	print('This is the request param: ', request)
	return render(request, 'tryme.html')



def roast(request):
	random = request
	return redirect(request, 'roast.html', {'random': random })