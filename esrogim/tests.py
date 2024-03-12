from django.test import TestCase
from random import randint
from requests import get

# Create your tests here.
def test_api(request):
    """make sure the server is working well with serving search api requests
       by simulating user input and checking the response fields
    """

    min_price = randint(0, 100)
    max_price = randint(150, 300)
    texture_smoothness = randint(0, 10)
    ripeness_score = randint(0, 10)
    size = randint(0, 10)
    url = f"http://127.0.0.1:8000/filter_search/{min_price}/{max_price}?texture_smoothness={texture_smoothness}&ripeness_score={ripeness_score}&size={size}"

    response = get(url)
    for esrog in response:
        assert esrog['estimated_price'] >= min_price
        assert esrog['estimated_price'] <= max_price
        assert esrog['texture_smoothness'] >= texture_smoothness
        assert esrog['ripeness_score'] >= ripeness_score
        assert esrog['size'] >= size


if __name__ == '__main__':
    print("running tests...")