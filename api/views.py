from .models import Request
from django.http import HttpResponse, HttpResponseForbidden


def confirm_purchase(request, id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("Oops.")

    anfrage = Request.objects.get(pk=id)
    anfrage.approved = True
    anfrage.save()

    return HttpResponse(content="Vielen Dank")
