Разработка сайта с рецептами

1. Frontend (Работаю в редакторе VScode):
    - Создал страницы html:
        - Главная страница - index.html
        - Страница личного кабинета - account-page.html
        - Страница авторизации - enter-page.html
        - Страница регистрации - registartion.html
        - страница добваления рецепта - add-recipe.html
        - Страница отображения отдельного рецепта - recipe.html
    - Стилизовал страницы:
        - Использую предпроцессор sass для стилизации. У каждой страницы, свой файл scss с стилями.
    - Скрипты:
        - Написал файл script.js в котором описал следующие функции:
            - Переход на страницу с рецептом при нажатии кнопки превью рецепта - GoToRecipe()
            - Отображения блока с фильтрами при нажатии на кнопку фильтры в строке поиска - ShowFilters()

2. Backend (Работаю в редакторе pycharm):
    - Подготовка к работе:
        - [x] Создал проект - Recipies_Site
        - [x] Убедился в правильной работе виртуального окружения
        - [x] Создал репозиторий Recipies_Site на Githab
        - [x] Добавил в папку Recipe_Site файл gitignore для исключения загрузки не нужных файлов и директорий
        - [x] Создал файл readme.md с описанием условий выполнения проекта
        - [x] Создал файл road_map.md в котором буду описывать этапы выполнения проекта
        - [x] Инициализировал папку с проектом - git init
        - [x] Добавил файлы в git - git add .
        - [x] Сделал commit - git commit -m "Initial commit"
        - [x] Связал проект с удаленным репозиторием:
            - git remote add origin https://github.com/ser500vms/Recepies_Site.git
            - git branch -M main
            - git push -u origin main
    - Разработка:
        - Создание функционала регистрации, авторизации, 
        выхода пользователя и настройка прав и области видимости у не/авторизованных пользователей
          - [x] Создал ветку reg-log-auth-permissions для работы над этой задачей - git branch
          reg-log-auth-permissions-v-1-0-0
          - [x] Установил Django фреймфорк - pip install django
          - [x] Обновил pip - python.exe -m pip install --upgrade pip
          - [x] Создал django-проект recipe_site - django-admin startproject recipe_site
          - [x] Переименовал recipe_site/recipe_site в recipe_site/settings для удобства в работе
          - [x] Создал приложение usersapp для выполнения поставленной задачи - python manage.py startapp usersapp
          - [x] Подключил приложение в файле recipe_site/settings/settings.py - INSTALLED_APPS = ['usersapp']
          - [x] Принял базовые миграции - python manage.py migrate
          - [x] Создал суперпользователя для работы с административной панелью - python manage.py createsuperuser
          - [x] Создал файл с зависимостями - pip freeze > requirements.txt
          - [x] Создал папку для шаблонов recipe_site/usersapp/templates/userapp
          - [x] В файле recipe_site/settings/settings.py настроил static (Static files (CSS, JavaScript, Images)) 
            STATIC_DIR = os.path.join(BASE_DIR, 'static')
            STATICFILES_DIRS = [STATIC_DIR]
          - [x] Создал папку recipe_site/static для static файлов 
          - [x] Перенес папки из фронтенда: img, scripts, styles в папку recipe_site/static
          - [x] Создал папку recipe_site/media для media 
          - [x] В файле recipe_site/settings/settings.py настроил media (Static files (CSS, JavaScript, Images))
            MEDIA_URL = '/media/' 
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
          - [x] В файле recipe_site/settings/urls.py добавил настройку обработки статики 
            if settings.DEBUG: (см. ком.)
          - [x] В файле recipe_site/settings/settings.py настроил путь к папке с шаблонами
            TEMPLATES = ['DIRS': [os.path.join(BASE_DIR, 'templates')],]
          - [x] Перенес файл index.html из фронтенда в папку recipe_site/templates, 
            переименовал его в base.html. Данный шаблон будет баззовым шаблоном для работы
          - [x] Перенес из фронтенда папку pages в папку recipe_site/templates. 
            Далее они будут переработаны в шаблоны
          - [x] Настроил recipe_site/templates/base.html:
            - 3-я строка вставил {% load static %} - для подключения static
            - В ссылках на подключение стилей и скриптов прописал {% static 'styles/reset.css' %}, 
              для того чтобы было понятно откуда подгружать файлы
          - [x] В файле recipe_site/usersapp/view.py создал класс
            HomeView(TemplateView) для рендеринга базового шаблона
          - [x] Создал файл recipe_site/usersapp/urls.py для подключения view классов
          - [x] Сделал переадресацию в файле recipe_site/settings/urls.py на файл recipe_site/usersapp/urls.py
            path('', include('usersapp.urls')),
          - [x] Подключил класс BaseView(TemplateView) в файле recipe_site/usersapp/urls.py  
            path('', HomeView.as_view, name='home_page'),
          - [x] Запустил сервер - python manage.py runserver
          - [x] Проверил работу view класса BaseView(TemplateView)
          - [x] Добавил файлы в git - git add .
          - [x] Сделал commit - git commit -m "Done BaseView"
          - *Создание функционала регистрации:*
            - [x] Создал шаблон регистрации нового пользователя - registration.html
            - [x] Создал файл recipe_site/usersapp/form.py для работы с формами 
            - [x] В forms.py создал класс CustomUserForm расширяющий UserCreationForm для добавления
            полей first_name, last_name, email при регистрации
            - [x] В recipe_site/usersapp/views.py создал класс RegistrationView(CreateView) в котором прописана логика
            добавления нового пользователя при регистрации с последующей авторизацией
            - [x] В recipe_site/usersapp/urls.py прописал путь для шаблона регистрации
              path('reg/', RegistrationView.as_view(), name='registration_page'),
            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Registration half_done"
            - [x] Выгрузил данные в репозиторий git push

          - *Создание функционала авторизации:*
            - [x] Создал шаблон для авторизации пользователя - recipe_site/templates/enter-page.html
            - [x] В recipe_site/usersapp/views.py создал класс MyLoginView(LoginView) для функционала авторизвции
            - [x] В recipe_site/usersapp/urls.py прописал путь для авторизации - path("login/", MyLoginView.as_view(), name="login")
            - [x] Создал шаблон личного кабинета для аторизованного пользователя - recipe_site/templates/account-page.html
            - [x] В views.py создал класс LkView(TemplateView) для отображения страницы авторизованного пользователя
            - [x] В recipe_site/usersapp/urls.py прописал путь для отображения личного кабинета - path('lk/', LkView.as_view(), name='lk_page')
            - Проверил функционал авторизации пользователя

          - *Создание функционала выхода:*
            - [x] В recipe_site/usersapp/views.py создал класс MyLogoutView(LogoutView) для выполнения выхода пользователя
            - [x] В шаблоне recipe_site/templates/account-page.html добавил блок: 
              <form action="{% url 'zsvapp:logout' %}" method="post">
              {% csrf_token %}
              <button type="submit">Выход</button>
              </form>
              Это необходимо для правильной отработки выхода в классе MyLogoutView иначе выходит ошибка 405
            - [x] В recipe_site/usersapp/urls.py прописал путь для выполнения выхода - path('logout/', MyLogoutView.as_view(), name='logout')
            - [x] Проверил функционал выхода пользователя

          - *Настройка прав доступа и областей видимости не/авторизованных пользователей*

            - Создал группу ... в которой установил права для всех пользователей !!!
            - Создал ... для помещения вновь созданных пользователей в группу !!!
            - [x] Переработал шаблон recipe_site/templates/base.html для отображения нужного контента в зависимости от статуса авторизации 
            - [x] Добавил миксин LoginRequiredMixin к классу LkView для создания условия тотображения страницы, только если пользователь авторизован.
            - [x] Проверил работу функционала

          - *Создание функционала удаления пользователя (для авторизованного пользователя)*
            - [x] Создал шаблон recipe_site/templates/about-user.html для отображения информации о пользователе, а также внес туда возможность редактирования и удаления пользователя
            - [x] В recipe_site/usersapp/views.py создал класс AboutUserView(LoginRequiredMixin, TemplateView) для отображения информации о пользователе.
            - [x] В recipe_site/usersapp/urls.py прописал путь для работы AboutUserView - path('user-info/', AboutUserView.as_view(), name='user_info')
            - [x] В recipe_site/usersapp/views.py создал класс UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView) для удаления пользователя.
            - [x] В recipe_site/usersapp/urls.py прописал путь для работы UserDeleteView 
                  path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='delete_user')
                  не забываем передавать id - {% url 'delete_user' pk=user.pk %} в ссылке
            - [x] Создал шаблон recipe_site/templates/confirm-delete.html для вывода страницы с подтверждением удаления (на будущее, хочу добавить вывод этого сообщением на странице с информацией) 
            - [x] Добавил миксин LoginRequiredMixin к классам MyLogoutView, AboutUserView
            - [x] Проверил работу функционала

          - *Создание функционала редактирования пользователя (для авторизованного пользователя)*
            - [x] Создал шаблон recipe_site/templates/about-user.html для отображения 
            - [x] В recipe_site/usersapp/views.py создал класс AboutUserView(LoginRequiredMixin, TemplateView) для отображения информации о пользователе.
            - [x] В recipe_site/usersapp/urls.py прописал путь для работы AboutUserView - path('user-info/<int:pk>/', AboutUserView.as_view(), name='user_info')
            - [x] Создал шаблон recipe_site/templates/user_update_form.html для отображения формы редактирования данных 
            - [x] В recipe_site/usersapp/views.py создал класс UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, DeleteView) для редактирования пользователя. 
            - [x] В recipe_site/usersapp/urls.py прописал путь для работы UserDeleteView 
                  path('user/<int:pk>/update/', UserUpdateView.as_view(), name='update_user')
                  не забываем передавать id - {% url 'update_user' pk=user.pk %} в ссылке
            - [x] Проверил работу функционала
            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done registration, login, logout"
            - [x] Выгрузил данные в репозиторий git push
            - [x] Перешел в основную ветку - git checkout main
            - [x] Выполнил обновление - git pull origin main
            - [x] Произвел слияние - git merge reg-log-auth-permissions-v-1-0-0
            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done merge reg-log.... branch"
            - [x] Выгрузил данные в репозиторий git push



          - *Настройка куки и кэша*
            - Пока пропустить ... 

          - *Примечания и доработки*
            - Нужно сделать функционал смены пароля 
            - Нужно сделать функционал поля емеил обязательным
            - Нужно сделать функционал регистрации по нику или емайлу 
            - Нужно сделать функционал восстановления пароля
              
