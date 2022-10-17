from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from datetime import datetime

from family_member.models import Family_member

#Función para crear al miembro de la familia.
def create_family_member(request, name: str, last_name: str, birth_day: str, sex: str, height: str, profession: str):

    template = loader.get_template("template_family-member.html")
    #La función calculate_age, retorna la edad del miermbro, calculada en base a la fecha de nacimiento introducida.
    age, birth_day = calculate_age(birth_day)
    
    family_member = Family_member(
        name=name, last_name=last_name, birth_day=birth_day, age=age, sex=sex, height=height, profession=profession
    )
    family_member.save()  # Se guarda los datos del miembro en la base de datos

    context_dict = {"member": family_member}
    render = template.render(context_dict)
    return HttpResponse(render)


def family_member(request):
    family_member = Family_member.objects.all()

    context_dict = {"family_members": family_member}

    return render(
        request=request,
        context=context_dict,
        template_name="family_member/member-list.html",
    )

#Función que calcula la edad.
def calculate_age(birth_day: str) -> int:
    birth_day = datetime.strptime(birth_day, "%Y-%m-%d")
    delta_time = datetime.now() - birth_day
    days_by_year = 365.25

    years=int(delta_time.days // days_by_year)
    # months=int((delta_time.days % days_by_year) // 30),
    # days=int((delta_time.days % days_by_year) % 30),
    return years, birth_day