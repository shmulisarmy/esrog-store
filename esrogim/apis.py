from django.http import JsonResponse
from .models import Esrog

def main(request):
    # Filter Esrog objects where the price is between 100 and 200,
    # then sort them by estimated_price in descending order
    sorted_esrogim_desc = list(Esrog.objects.order_by('-estimated_price').values())

    return JsonResponse(sorted_esrogim_desc, safe=False)


def price_filter(request, min_price, max_price):
    # if request.method != 'POST':
    #     return JsonResponse({"error": "POST request required."}, status=400)
    sorted_esrogim_desc = list(Esrog.objects.filter(estimated_price__gt=min_price, estimated_price__lt=max_price).order_by('-estimated_price').values())

    return JsonResponse(sorted_esrogim_desc, safe=False)
