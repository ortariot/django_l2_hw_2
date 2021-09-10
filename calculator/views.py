from django.shortcuts import render


# Create your views here.


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
        }


def get_context(dish, servings):
    context = {'recipe': DATA.get(dish),
               'servings': servings,
               'name': dish
               }
    return context


def home_view(request):

    template_name = 'calculator/home.html'
    dish_list = ''
    for dish in DATA:
        dish_list += (f'<input type="radio", name="dish" '
                      f'required value="{dish}">{dish}<br>'
                      )

    context = {'dish_list': dish_list}

    if request.method == 'POST':
        ch_dish = request.POST['dish']
        servings = request.POST['person_count']
        template_name = 'calculator/index.html'
        return render(request, template_name, get_context(ch_dish, servings))

    return render(request, template_name, context)


def dish_view(request, dish):
    template_name = 'calculator/index.html'
    servings = request.GET.get('servings')
    servings = int(servings) if servings else 1
    return render(request, template_name, get_context(dish, servings))
