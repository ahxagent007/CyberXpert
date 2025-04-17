from django.shortcuts import render
from .models import Domain


def domain(request, domain_no):
    domain = Domain.objects.get(domain_no=domain_no)
    data = {
        'domain': domain
    }
    return render(request=request, template_name='library/domain.html', context=data)
