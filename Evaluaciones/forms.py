from django import forms
from Evaluaciones.models import *
YEARS= [x for x in range(1940,2021)]

class AddEvaluacion(forms.Form):
    tiempo_min = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                             required=True)
    tiempo_max = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                             required=True)

    rubrica = forms.ModelChoiceField(queryset=Rubrica.objects,
                                        widget=forms.Select(attrs={'class': 'form-control'}),required=False,
                                        label='Rubrica')

    fecha_inicio= forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    fecha_fin=forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    curso=forms.ModelChoiceField(queryset=Curso.objects, widget=forms.Select(attrs={'class':'form-control'}), label='Curso')
    estado=forms.ChoiceField(choices=(("En curso", "En curso"), ("Finalizada", "Finalizada")), widget=forms.Select({'class':'form-control'}))
    nombre=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control'}))

    def is_valid(self):
        return super(AddEvaluacion,self).is_valid()

    def save(self, *args, **kwargs):
        evaluacion = Evaluacion(tiempo_min=self.cleaned_data['tiempo_min'],
                      tiempo_max=self.cleaned_data['tiempo_max'],
                      rubrica=self.cleaned_data['rubrica'],
                      fecha_inicio=self.cleaned_data['fecha_inicio'],
                      fecha_fin=self.cleaned_data['fecha_fin'],
                        curso=self.cleaned_data['curso'],
                        estado=self.cleaned_data['estado'],
                        nombre=self.cleaned_data['nombre'])


        evaluacion.save()