from django.http import JsonResponse
from ..db_management.models import Esrog

def reserve(request):
    if request.method != 'POST':
        return JsonResponse({"error": "POST request required."}, status=400)

    id = int(request.POST.get('id'))

    name = request.session.get('name')

    esrog = Esrog.objects.get(id=id)
    esrog.reserved = name
    esrog.save()


    return JsonResponse("you have reserved this esrog", safe=False)


