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
              
          - Разработка функционала отображения, создания, редактирования, удаления рецептов
            - [x] Создал новую ветку recipies-v-1-0-0 для работы - git checkout -b recipies-v-1-0-0
            - [x] Создал новое приложение recipiesapp для разработки данного функционала - python manage.py startapp recipiesapp
            - [x] Подключил приложение в файле настроек recipe_site/settings/settings.py - INSTALLED_APPS = ['recipiesapp']
            - [x] Создал файл recipe_site/recipiesapp/urls.py  и подключил его в файле recipe_site/settings/urls.py - path('recipies/', include('recipies.urls'))
            
            - *Разработка функционала отображения рецепта*
              - [x] Установил mptt для работы с древовидной струкктурой - pip install django-mptt
              - [x] В файле recipe_site/recipiesapp/models.py создал модель категорий Category(MPTTModel), использовал mptt, у меня будут родительские категории и в них дочернии. Такая структура мне показалась лучше подойдет для моего проекта, чем предложенная в задании.
              - [x] В файле recipe_site/recipiesapp/models.py создал модель рецепта Recipe(models.Model)
              - [x] Создал шаблон рецепта recipe_site/templates/recipiesapp/recipe.html
              - [x] В файле recipe_site/recipiesapp/views.py создал представление рецепта RecipeView(TemplateView)
              - [x] В файле recipe_site/recipiesapp/urls.py сделал подключение - path('recipe/<int:pk>', RecipeView.as_view(), name='recipe')
              - [x] Проверил функционал отображения рецептов

              
            - *Разработка функционала добавления рецепта*
              - [x] В файле recipe_site/recipiesapp/forms.py создал форму для довления рецепта RecipeForm(forms.ModelForm)
              - [x]RecipeForm(forms.ModelForm) - переопределил поле categories - 
                   categories = TreeNodeMultipleChoiceField(queryset=Category.objects.all(), required=False)
              - [x] Создал шаблон для добавления рецепта recipe_site/templates/recipiesapp/add-recipe.html На заметку, для доступа к значениям  модели надо использовать form.fields.categories.queryset а не form.categories.queryset
              - [x] В файле recipe_site/recipiesapp/views.py создал представление добавления рецепта AddRecipeView(CreateView)
              - [x] В файле recipe_site/recipiesapp/urls.py сделал подключение - path('add-recipe/', AddRecipeView.as_view() name='add_recipe'),
              - [x] Проверил функционал добавления рецептов
              - [x] Обновил файл с зависимостями - pip freeze > requirements.txt 
              - [x] Добавил файлы в git - git add .
              - [x] Сделал commit - git commit -m "Done add recipe function"

            - *Разработка функционала удаления рецепта*
              - [x] В файле recipe_site/recipiesapp/views.py создал представление удаления рецепта RecipeDeleteView(DeleteView), шаблон для удаления использовал уже созданный в usersapp
              - [x] В файле recipe_site/recipiesapp/urls.py сделал подключение   path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='delete_recipe')
              - [x] Проверил функционал удаления рецептов

            - *Разработка функционала изменения рецепта*
              - [x] Создал шаблон для изменения рецепта recipe_site/templates/recipiesapp/recipe_update_form.html
              - [x] В файле recipe_site/recipiesapp/views.py создал представление изменения рецепта RecipeUpdateView(UpdateView)
              - [x] В файле recipe_site/recipiesapp/urls.py сделал подключение  path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='update_recipe'),
              - [x] Проверил функционал изменения рецептов

            - *Доработка модели рецепта*
              - [x] В файле recipe_site/recipiesapp/models.py доработал модель Recipe(models.Model). Добавил поля:
                - изображение
                - автор
                - время приготовления
                - кол-во порций
                - ингридиенты
                - шаги приготовления
                - время создания
                - время обновления
              - [x] Произвел изменения в файле recipe_site/recipiesapp/forms.py и recipe_site/recipiesapp/views.py
              - [x] Произвел изменения в шаблоне recipe_site/templates/recipiesapp/recipe_update_form.html, add-recipe.html и recipe.html 
              - [x] Проверил работу функций отображения, удаления, редактирования рецептов с новой моделью

            - *Настройка области видимости и доступа*
              - [x] В файле recipe_site/recipiesapp/views.py подключил LoginRequiredMixin, UserPassesTestMixin и установил их для классов AddRecipeView(LoginRequiredMixin, CreateView), RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView), RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView). Прописал функцию def test_func(self) для RecipeDeleteView и RecipeUpdateView, таким образом пользователь сможет изменить или удалить только свои рецепты
              - [x] В файле recipe_site/recipiesapp/views.py добавил функцию def form_valid(self, form) к классу AddRecipeView(LoginRequiredMixin, CreateView). Это позволяет передевать в форму при создании рецепта, текущего пользователя и установить его в качестве автора, таким образом автор будет установлен автоматически.
              - [x] Проверил работу функций отображения, удаления, редактирования рецептов для не/авторизованных пользователей и области их видимостей
              - [x] Добавил файлы в git - git add .
              - [x] Сделал commit - git commit -m "Done view, add, delete recipe functions and access levels"



            - *TO DO*
              - middlewere !!

              - эффективная работа с базой данных n+1

              - логирование

              - Заполнить категории и пордгатегории

              - пагинация (загрузка только определенного колличества рецептов)

              - Настройка куки и кэша
              - Оптимизация с помощью кеширования

              - Настройка сессий

              - Доработать usersapp:
                - Нужно сделать функционал смены пароля 
                - Нужно сделать функционал поля емеил обязательным
                - Нужно сделать функционал регистрации по нику или емайлу 
                - Нужно сделать функционал восстановления пароля
                - Аунтефикацию через гуггл )).**

              - Установить ограничения по размерам загружаемых файлов и их разрешению

              - Доработка форм:
                - Нужно чтобы текстовые поля сохраняли форматирование, т.е отступы

              - Реализация функции поиска на главной странице по имени рецепта и отображать только рецепты по имени, а если имени нет то все

              - Реализация добавления фильтров при поиске по категориям, отображать рецепты у которых есть выбранная категория **

              - Доработка шаблонов:
                - base.html:
                 - функция поиска и фильтрации, нужно показывать превью рецептов из отдельного шаблона
                - создать шаблон recipe-preview.html для отображения карточки рецепта и в нем: 
                  - продуамть чтобы в base.html отображался шаблон с кнопкой приготовить, а на account-page.html с кнопками изменить и удалить
                  - сделать чтобы фотографии имели одинаковый размер
                - account-page.html:
                  - при отсутсвии рецептов вывести вместо Ваши рецепты, у вас еще нет рецептов, дерзайте!!!
                - user-info.html:
                 - Добавить кнопку с возвратом в личный кабинет (можно заменить кнопку добавить рецепт)
                 - поле колличество рецептов должно их показывать
                - add-recipe:
                  - настроить отображение базового шаблона
                - подумай про наследование в шаблонах личного кабинета и авторизованных пользователь не от базового

              - *Доработка форм* задача на последок:
               - Нужно добавить возможность создавать шаги рецептов
               - Создать модель продуктов
               - добавлять эти продукты в рецепт с указанием кол-ва и выбором едениц измерения
                






