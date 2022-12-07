from forms import FormularioEmpres 


def form_manual(request):
    pass

def form_django(request):
    form = FormularioEmpres 
    context ={
        'form': form
    }
    return render(request, 'templates/index.html', context=context)