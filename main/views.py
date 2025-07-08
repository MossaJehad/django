from django.shortcuts import render

def home(request):
	return render(request, 'main/home.html')

def contact(request):
	emails = {'Mossa': 'Moosa.jehad65@gmail.com', 'Ali': 'Player199eliminated@squid.game', 'Ching': 'LinearAlgebra@math.create', '42Amman': '42Amman@apply.com'}
	return render(request, 'main/contact.html', {'emails': emails})

def profile(request):
	return render(request, 'main/profile.html')

def agecheck(request):
	age = request.GET.get('age')
	try:
		age = int(age) if age else None
	except:
		age = None
	return render(request, 'main/agecheck.html', {'age': age})