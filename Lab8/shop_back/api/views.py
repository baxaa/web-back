from django.http.response import HttpResponse, JsonResponse
from api.models import Product
from .models import Product, Category

products = []

for product in Product.objects.all():
    products.append(product.to_json())



def product_list(request):
    
    return JsonResponse(products, safe=False, json_dumps_params={'indent':2})

def get_product(request, product_id):
    
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product, json_dumps_params={'indent':2})

    return JsonResponse({'error': 'Иди нафиг такого не существует'})                                             


categories = []
for category in Category.objects.all():
  categories.append(category.to_json())


def category_list(request):
    
    return JsonResponse(categories, safe=False, json_dumps_params={'indent':2})

def category_detail(request, category_id):
    
    for category in categories:
        if category['id'] == category_id:
            print(category)
            return JsonResponse(category, json_dumps_params={'indent':2})
    return JsonResponse({'error' : 'Иди нафиг такого не существует'})




def products_in_categories(request, category_id):
  category = Category.objects.get(pk = category_id)
  finding_products = []
  for product in products:
      if product['category_id'] == category.id:
        finding_products.append(product)
  print(finding_products)
  if len(finding_products) != 0:
    return JsonResponse(finding_products,safe=False, json_dumps_params={'indent' : 2})
  else:
    return JsonResponse({'error' : 'Иди нафиг такого не существует'})
  
  return JsonResponse({'error' : 'Иди нафиг такого не существует'})
  