from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from family_member.models import Family_member


def create_family_member(request, name: str, last_name: str, age: str, sex: str, height: str, profession: str):

    template = loader.get_template("template_family-member.html")

    family_member = Family_member(
        name=name, last_name=last_name, age=age,sex=sex,height=height, profession=profession
    )
    family_member.save()  # save into the DB

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
    