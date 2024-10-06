from django.shortcuts import render  # мипортируем функцию для рендеринга шаблонов
from .forms import UserRegisterForm  # импортируем нами созданный в формс класс формы регистрации пользователя

# Список пользователей (имитируем базу данных)
users = ['admin', 'Mikl', 'user123']


# функция которая будет обрабатывать запросы на регистрацию пользователя с использованием формы Django
def sign_up_by_django(request):
    info = {}  # создаем словарь хранения инфы для передачи в шаблон
    if request.method == 'POST':  # если метод запроса - POST т.е отправка формы
        form = UserRegisterForm(request.POST)  # тогда создаем экземпляр нашей формы с перед-ми данными (request.POST)
        if form.is_valid():  # если форма валидна то извлекаем данные из полей формы словаря cleaned_data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Обработка ошибок
            if username in users:  # если username уже существует то в словарь info добавляется сообщение об ошибке
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                # Успешная регистрация
                info['success'] = f'Приветствуем, {username}!'  # добавляем в словарь сообщение об успешной регистрации
                users.append(username)  # добавляем пользователя в список users
        else:  # если форма невалидна, в словарь info добавляется сообщение об ошибке
            info['error'] = 'Некорректно заполнена форма'
    else:  # если метод запроса GET создается пустой экземпляр формы UserRegisterForm
        form = UserRegisterForm()

    info['form'] = form
    return render(request, 'registration_page.html', info)


# функция которая будет обрабатывать запросы на регистрацию пользователя с использованием HTML-формы
def sign_up_by_html(request):
    info = {}  # словарь info для хранения информации
    # если метод запроса POST извлекаются значения полей формы из request.POST
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        try:  # пробуем преобразовать age в число
            age = int(age)
        except ValueError:
            info['error'] = 'Возраст должен быть числом'  # если не число то добавляем в словарь info ошибку
            return render(request, 'registration_page.html', info)  # рендерим шаблон с этой информацией

        # Обработка ошибок
        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            # Успешная регистрация
            info['success'] = f'Приветствуем, {username}!'  # добавляем в словарь сообщение об успешной регистрации
            users.append(username)  # добавляем пользователя в список users
    # рендерим шаблон с передачей словаря info в качестве контекста
    return render(request, 'registration_page.html', info)
