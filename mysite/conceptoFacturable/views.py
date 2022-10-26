from django.shortcuts import render, get_object_or_404, redirect
from .models import ConceptoFacturable
from .forms import ConceptoFacturableForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def conceptos_facturables_list(request):
    conceptos = ConceptoFacturable.objects.all()
    return render(
        request,
        'conceptoFacturable/conceptos_facturables_list.html',
        {"conceptos": conceptos})


def conceptos_facturables_detail(request, pk):
    concepto = get_object_or_404(ConceptoFacturable, pk=pk)
    return render(
        request,
        'conceptoFacturable/conceptos_facturables_detail.html',
        {"concepto": concepto})


def conceptos_facturables_nuevo(request):
    if request.method == 'POST':
        form = ConceptoFacturableForm(request.POST)
        if form.is_valid():
            concepto = form.save(commit=False)
            concepto.save()
            return redirect('conceptos_facturables_detail', pk=concepto.pk)
    else:
        form = ConceptoFacturableForm()
        return render(
            request,
            'conceptoFacturable/conceptos_facturables_nuevo.html',
            {'form': form})


@login_required
@staff_member_required
def conceptos_facturables_editar(request, pk):
    concepto = get_object_or_404(ConceptoFacturable, pk=pk)
    if request.method == 'POST':
        form = ConceptoFacturableForm(request.POST, instance=concepto)
        if form.is_valid():
            concepto = form.save(commit=False)
            concepto.save()
            return redirect('conceptos_facturables_detail', pk=concepto.pk)
    else:
        form = ConceptoFacturableForm(instance=concepto)
        return render(
            request,
            'conceptoFacturable/conceptos_facturables_editar.html',
            {'form': form})


@login_required
@staff_member_required
def conceptos_facturables_eliminar(request, pk):
    concepto = get_object_or_404(ConceptoFacturable, pk=pk)
    concepto.delete()
    conceptos = ConceptoFacturable.objects.all()
    return render(
        request,
        'conceptoFacturable/conceptos_facturables_list.html',
        {"conceptos": conceptos})


def login(request):
    return render(
        request,
        'conceptoFacturable/login.html',
        {})
