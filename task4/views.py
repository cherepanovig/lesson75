from django.views.generic import TemplateView
from django.shortcuts import render

# Главная страница
def home(request):
    return render(request, 'platform.html')


# Магазин
def shop_games(request):
    # Заголовок страницы
    title = "Магазин игровых продуктов"

    # Список товаров
    # products = {
    #     'item1': 'Atomic Heart',
    #     'item2': 'Cyberpunk 2077',
    #     'item3': 'PayDay 2'
    # }

    products = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']}

    # Передача словаря через параметр context
    # Передаем title отдельно и продукты отдельно
    return render(request, 'games.html', {'title': title, 'product': products})

# Корзина
def cart(request):
    # Пример информации о корзине
    cart_info = "Ваша корзина пока пуста. Добавьте товары для продолжения."
    return render(request, 'cart.html', {'cart_info': cart_info})
