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
              - [x] Выгрузил данные в репозиторий git push
              - [x] Перешел в основную ветку - git checkout main
              - [x] Выполнил обновление - git pull origin main
              - [x] Произвел слияние - git merge recipies-v-1-0-0
              - [x] Добавил файлы в git - git add .
              - [x] Сделал commit - git commit -m "Done merge recipies branch"
              - [x] Выгрузил данные в репозиторий git push


          - *Настройка пагинации*
            - [x] Создал новую ветку pagiantion для работы - git checkout -b pagination
            - [x] В файле recipe_site/usersapp/views.py добавил в классы HomeView, LkView пагинацию paginatio_by. 
            - [x] В файле recipe_site/usersapp/views.py изменил LkView(LoginRequiredMixin, TemplateView) на LkView(LoginRequiredMixin, ListView) и измеил функцию get_queryset
            - [x] Произвел изменения в шаблоне recipe_site/templates/pages/account-page.html и  recipe_site/templates/base.html добавил пагинацию
            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done pagination"
            - [x] Выгрузил данные в репозиторий git push
            - [x] Перешел в основную ветку - git checkout main
            - [x] Выполнил обновление - git pull origin main
            - [x] Произвел слияние - git merge pagination
            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done merge pagination branch"
            - [x] Выгрузил данные в репозиторий git push

          - *Настройка функции добавления ингридиентов в рецепт*
            - [x] Создал новую ветку product-and-ingridients для работы - git checkout -b product-and-ingridients

            - Функция добавления рецепта с учетом ингридиентов: 
              - [x] В файле recipe_site/recipiesapp/views.py добавил RecipeIngredientFormSet для работы с form set.
              - [x] В файле recipe_site/recipiesapp/views.py изменил класс AddRecipeView для работы с form set.
              - [x] В файле recipe_site/recipiesapp/models.py изменил модель Recipe, добавил новые поля и удалил прежнее поле с ингридиентами
              - [x] В файле recipe_site/recipiesapp/models.py создал модель Product в которой описываются характеристики продукта
              - [x] В файле recipe_site/recipiesapp/models.py создал модель ProRecipeIngredientduct в которой связываю рецепт и продукт
              - [x] В файле recipe_site/recipiesapp/forms.py создал форму RecipeIngredientForm для добавления ингридиента и изменил форму RecipeForm
              - [x] Настроил шаблон recipe_site/templates/add-recipe.html для нового функционала. 
              - [x] Проверил работу добавления рецепта          
              - [x] Добавил файлы в git - git add .
              - [x] Сделал commit - git commit -m "Done add recipe function"

            - Функция изменения рецепта с учетом ингридиентов: 
              - [x] В файле recipe_site/recipiesapp/views.py изменил класс RecipeUpdateView для работы с form set.
              - [x] В файле recipe_site/recipiesapp/models.py изменил модель RecipeIngredient. Убрал meta: uniq (что позволяло держать только один продукт в рецепте и не создовать его дубли), не смог настроить обновление рецепта, если его оставить уникальныи (надо поработать в будущем над этой задачей) *************************
              - [x] Настроил шаблон recipe_site/templates/recipe_update_form.html для нового функционала. 
              - [x] Проверил работу добавления рецепта  
              - [x] Проверил работу удаления рецепта (функция работает прежняя, вносить изменения не надо)        
              - [x] Добавил файлы в git - git add .
              - [x] Сделал commit - git commit -m "Done update? delete recipe function"


          - *Реализация функции поиска на главной странице по имени рецепта*
          
            - [x] Настроил шаблон recipe_site/templates/base.html для работы поисковой строки. 
            - [x] В файле recipe_site/usersapp/views.py изменил класс HomeView добавил функцию get_queryset где описал логику простого поиска из поисковой строки.
            - [x] Проверил работу поиска рецептов         
            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done simple search function"

          - *Реализация добавления фильтров по категориям (Делаем чтоб показывались все рецепты выбранных категорий, т.е. чем больше категорий выбрано, тем больше рецептов будет)*
            - [x] Настроил шаблон recipe_site/templates/base.html для работы фильров. 
            - [x] В файле recipe_site/usersapp/views.py изменил класс HomeView изменил функцию get_queryset где описал логику сложного поиска по категориям.
            - [x] Проверил работу фильтрации         
            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done filter search function"

          - *Сделать подсчет калорий в блоке рецепта исходя из лежащих в нем ингридиентов*
            - [x] В файле recipe_site/recipiesapp/models.py изменил модель Recipe. Добавил поле recipe_calories для хранения информации о калорийности рецепта.
            - [x] В файле recipe_site/recipiesapp/views.py изменил класс RecipeUpdateView. Включил в него алгоритм подсчета калорийности рецепта на основании входящих в него ингридиентов.
            - [x] В ходе проверки работы функционала выяснилось, что ингридиенты при удалении в фронтенде, не удаляються на бэкэнде в базе данных. Доработал шаблон recipe_site/templates/recipeapp/recipe_update_form.html. Включил в него скрытый чекбокс для отработки функции удаления и переписал скрипт.
            - [x] В файле recipe_site/recipiesapp/admin.py изменил отображение RecipeAdmin, добавил поле для калорийности.
            - [x] Произвел повторную проверку работы функционала изменения рецепта, а также подсчета калорийности.
            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done count calories fuunction and fix recipe update"

          - *Сделать подсчет белков, жиров, углеводов в блоке рецепта исходя из лежащих в нем ингридиентов*
            - [x] В файле recipe_site/recipiesapp/views.py изменил класс AddRecipeView и RecipeUpdateView. Добавил подсчет калорий, белков, жиров, углеводов.
            - [x] В файле recipe_site/recipiesapp/models.py изменил модель Recipe. Добавил поля для жиров, белков, углеводов.
            - [x] В файле recipe_site/recipiesapp/admin.py изменил отображение RecipeAdmin, добавил поля для белков, жиров, углеводов.
            - [x] Доработал шаблоны recipe_site/templates/recipeapp/recipe.html,  recipe_site/templates/usersapp/account-page.html и recipe_site/templates/base.html. Настроил вывод КБЖУ и ингридиентов.      

          - *Добавить поля шаги рецептов, динамически добавляемыми, по аналогии с продуктами*
            - [x] В файле recipe_site/recipiesapp/models.py изменил модель Recipe. Удалил поле cooking_steps. 
            - [x] В файле recipe_site/recipiesapp/models.py создал модель RecipeStep для шагов рецепта.
            - [x] В файле recipe_site/recipiesapp/admins.py изменил RecipeAdmin. Удалил поле cooking_steps и добавил 
            inlines = [RecipeStepsline] для работы с шагами рецепта.
            - [x] В файле recipe_site/recipiesapp/admins.py подключил модель RecipeStep - RecipeStepientAdmin(admin.ModelAdmin).
            - [x] В файле recipe_site/recipiesapp/forms.py создал форму RecipeStepForm(forms.ModelForm) для шагов рецепта
            - [x] В файле recipe_site/recipiesapp/forms.py создал форму RecipeStepForm(forms.ModelForm) для шагов рецепта
            - [x] В файле recipe_site/recipiesapp/forms.py из формы RecipeForm удалил поле cooking_steps.
            - [x] В файле recipe_site/recipiesapp/views.py изменил класс AddRecipeView и RecipeUpdateView. Добавил обработку шагов рецепта.
            - [x] Доработал шаблоны recipe_site/templates/recipeapp/recipe.html,  recipe_site/templates/usersapp/account-page.html и recipe_site/templates/base.html. Настроил отображение шагов рецепта. 
            - [x] В ходе тестирования, выяснилось, что при удалении ингридиентов из середины списка или начала, удаление происходит некоректно. Доработал шаблоны recipe_site/templates/recipeapp/add-recipe.html и recipe_update_form.html. Проблема заключалась в непередачи префиксов удаляемых элементов, переаботал скрипт и шаблон.
            - [x] Произвел тестирование функционала добавления и редактирования с различными условиями.
            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done ingridient step and fix recipe add/update function"

          - *Установить ограничения по размерам загружаемых файлов и их разрешению*
            - [x] В файле recipe_site/recipiesapp/forms.py создал метод  validate_file(file: InMemoryUploadedFile) -> None, в котором установил ограничение на размер файла, до 1 Мб.
            - [x] В файле recipe_site/recipiesapp/forms.py добавил в форму RecipeForm - image = forms.ImageField(validators=[validate_file]) для проверки размера файла
            - [x] Доработал шаблоны recipe_site/templates/recipeapp/add-recipe.html. Добавил отображение ошибок  {{ form.non_field_errors }} к полю с изображением.
            - [x] Произвел тестирование функционала ограничения размера фотографий
            - [x] В файле recipe_site/recipiesapp/models.py создал функцию def recipe_image_upload_path(instance, filename) для прописания имени загружаемых пользователями изображений. Они теперь уникальны. Подключил эту фуннкцию к полю image модели Recipe и проверил создание имен файлов.
            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done image load update"

          - *Улучшшение usersapp функционала* (На заметку, по смене пароля надо изучить ту же схему что и с восстановлением)
            - [x] В файле recipe_site/usersapp/views.py создал представление UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView, UserPassesTestMixin) для изменения пароля
            - [x] Создал шаблон recipe_site/templates/pages/user_password_change_form.html для изменения пароля
            - [x] В файле recipe_site/usersapp/urls.py прописал пути для работы UserPasswordChangeView
            - [x] В шаблоне recipe_site/templates/pages/user_update_form.html добавил ссылку для смены пароля
            - [x] Проверил функционал смены пароля
            - [x] В файле recipe_site/usersapp/views.py доработал представление RegistrationView, была проблема с переадресацие, добавил def get_success_url
            - [x] В файле recipe_site/usersapp/forms.py доработал форму CustomUserForm, добавил email = forms.EmailField, чтобы поле с почтой было обязательным
            - [x] Проверил функционал смены пароля
            - [x] Создал шаблон recipe_site/templates/pages/password_reset_form.html для формы смены пароля
            - [x] Создал шаблон recipe_site/templates/pages/password_reset_done.html для вывода сообщения об отправке ссылки на восстановление на почту
            - [x] Создал шаблон recipe_site/templates/pages/password_reset_confirm.html для вывода формы для нового пароля, при переходе по ссылке из письма
            - [x] Создал шаблон recipe_site/templates/pages/password_reset_complete.html для вывода сообщения об успешной смене пароля
            - [x] Создал шаблон recipe_site/templates/pages/password_reset_email.html в котором генерируеться отправляемое сообщение на почту
            - [x] Вся логика восстановления пароля основана на базовых классах from django.contrib.auth.views import(PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView)
            - [x] В файле recipe_site/usersapp/urls.py прописал путь с которого начинаеться работа по смене пароля и генерируется отправляемое сообщение на почту
                  path('password-reset/', PasswordResetView.as_view(
                  template_name='pages/password_reset_form.html',
                  email_template_name='pages/password_reset_email.html',
                  success_url=reverse_lazy("password_reset_done")
                  ), name='password_reset'),
            - [x] В файле recipe_site/usersapp/urls.py прописал путь для вывода сообщения об отправке ссылки на восстановление на почту
                  path('password-reset/done/', PasswordResetDoneView.as_view(template_name='pages/password_reset_done.html'), name='password_reset_done') 
            - [x] В файле recipe_site/usersapp/urls.py прописал путь для вывода формы для нового пароля, при переходе по ссылке из письма
                  path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
                          template_name='pages/password_reset_confirm.html',
                          success_url=reverse_lazy("password_reset_complete")
                          ), name='password_reset_confirm'),
            - [x] В файле recipe_site/usersapp/urls.py прописал путь для вывода формы для нового пароля, при переходе по ссылке из письма
                  path('password-reset/complete/', PasswordResetCompleteView.as_view(
                          template_name='pages/password_reset_complete.html',
                          ), name='password_reset_complete'),
            - [x] В файле recipe_site/settings/settings.py прописал - EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' для того, чтоб сообщения отправлялись в терминал т.к. SMPT сервер не настроен.
            - [x] Проверил работу по восстановлению пароля
            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done change and restore password"


<!-- 08.11.24 -->

          - *Доработка recipiesapp функционала* 
            - [x] Реализовал поиск в выпадающем списке продуктов и ограничил его 5 элементами с помощью библиотеки Select2 и ajax. Вся локига работы заложена в файлах шаблонов recipe_site/templates/recipiesapp/add-recipe.html (при создании нового рецепта) и recipe_update_form.html (при изменении рецепта)
            - [x] В файле recipe_site/recipiesapp/views.py создал функцию обработчик ajax def product_autocomplete(request)
            - [x] В файле recipe_site/recipiesapp/urls.py прописал путь - path('product-autocomplete/', product_autocomplete, name='product_autocomplete') для функции product_autocomplete
            - [x] Проверил работу поиска

            - [x] В файле recipe_site/recipiesapp/forms.py создал форму ProductForm(forms.ModelForm) для добавления своего продукта
            - [x] В файле recipe_site/recipiesapp/views.py создал представление AddProductView(LoginRequiredMixin, CreateView) для добавления своего продукта
            - [x] Создал шаблон recipe_site/templates/recipiesapp/add_product.html для добавления своего продукта
            - [x] В файле recipe_site/recipiesapp/urls.py прописал путь - path('add-product/', AddProductView.as_view(), name='add_product'), для добавления своего продукта
            - [x] Проверил работу добавления продукта

            - [x] Доработал шаблоны recipe_site/templates/recipeapp/add-recipe.html. Внес поправки для сохранения при отображении отмеченных категорий, при ошибке валидации.
            - [x] В файле recipe_site/recipiesapp/view.py доработал представление AddRecipeView. Теперь данные введенные пользователем при неправильной отправкие формы не обнуляються и ему не придеться снова выбирать категории, ингридиенты и шаги

            - [x] В файле recipe_site/usersapp/view.py исправил представление HomeView - queryset = queryset.filter(Q(name__icontains=query.lower()) | Q(name__icontains=query.capitalize()))
            Почему то icontains не обрабатывает регистр, задача на будущее. По сути костыль
            - [x] В файле recipe_site/recipiesapp/views.py исправил функцию product_autocomplete, установил тот же костыль для поиска в независимости от регистра

            - [x] В файле recipe_site/recipiesapp/models.py добавил в модель Tecipe поле cooking_time_text для хранения текстого вывода времени готовки
            - [x] В файле recipe_site/recipiesapp/views.py исправил представления AddRecipeView и RecipeUpdateView, добавил преобразование введенного пользователем времени в минутах, в текстовый формат, для вывода в шаблонах.

            - [x] В файле recipe_site/recipiesapp/models.py поправил модель RecipeIngredient, а именно опции выбора едениц измерения. Убрал опцию шт. для облегчения подсчета, т.к. если мы будем использовать шт., то придеться в продукт добавить поле вес 1 деницы продукта. Оставлю на улучшение функционала. 
            - [x] В файле recipe_site/recipiesapp/views.py исправил представления AddRecipeView и RecipeUpdateView, исправил блок с подсчетом калорий с учетом выбора едениц измерения.

            - [x] В файле recipe_site/recipiesapp/views.py исправил представления AddRecipeView и RecipeUpdateView, добавил блок с добавлением категории по каларийности в зависимости от калорийности рецепта
            - [x] В шаблонах recipe_site/templates/recipiesapp/add-recipe.html и recipe_update_form.htmlубрал вывод категории калорийность и ее подкатегорий
            - [x] Проверил работу добавления категорий

            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done product search, add product, views optimization"
            - [x] Выгрузил данные в репозиторий git push
            - [x] Перешел в основную ветку - git checkout main
            - [x] Выполнил обновление - git pull origin main
            - [x] Произвел слияние - git merge product-and-ingridients
            - [x] Выгрузил данные в репозиторий git push


          - *Стилизация*
              - [x] Выполнил базовую стилизация всех страниц
              - [x] Исправил вывод изображений
              - [x] Сделал адаптив под основные разрешения
              - [x] Настроил smtp сервер через yandex

            - [x] Добавил файлы в git - git add .
            - [x] Сделал commit - git commit -m "Done styles and smtp"
            - [x] Выгрузил данные в репозиторий git push
            - [x] Перешел в основную ветку - git checkout main
            - [x] Выполнил обновление - git pull origin main
            - [x] Произвел слияние - git merge product-and-ingridients
            - [x] Выгрузил данные в репозиторий git push

13.11.24 - *Деплой*

            - [x] Зарегистрировался на pythonAnywhere
            - [x] В файле recipe_site/settings/settings.py внес следующие изменения:
              - DEBUG = False
              - SESSION_COOKIE_SECURE = True
              - CSRF_COOKIE_SECURE = True
              - import os
              - SECRET_KEY = os.getenv('SECRET_KEY')
              - ALLOWED_HOSTS = ['recipies.pythonanywhere.com',]
              - STATIC_ROOT = BASE_DIR / 'static'
              - MEDIA_ROOT = BASE_DIR / 'media'
              - DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.mysql', 
                        'NAME': 'recipies$default', 
                        'USER': 'recipies', 
                        'PASSWORD': os.getenv('MYSQL_PASSWORD'), 
                        'HOST': 'recipies.mysql.pythonanywhere-services.com', 
                        'OPTIONS': {
                            'init_command': "SET NAMES 'utf8mb4';SET sql_mode='STRICT_TRANS_TABLES'", 'charset': 'utf8mb4', 
                        }, 
                    } 
                  }
            - [x] Обновил файл с зависимостями pip freeze > requirements.txt
            - [x] В файл requirements.txt добавил mysqlclient для работы с базой данных и python-dotenv для секретного ключа


            - [x] Прешел в раздел базы данных на сайте и открыл консоль в которой ввел команду  ALTER DATABASE username$default CHARACTER SET utf8 COLLATE utf8_general_ci; для использования любой кодировки



            - После деплоя:
              - *Добавить в фильтр блок для алергиков, который будет брать список продуктов в качестве чкубоксов и выводить рецепты в которых отсутствуют выбранные продукты*
              - *Добавить аунтефикацию и регистрацию через гугл, яндекс*
              - *Рефакторинг шаблонов:*
                - base.html:
                 - нужно показывать превью рецептов из отдельного шаблона
                - создать шаблон recipe-preview.html для отображения карточки рецепта и в нем: 
                  - продуамть чтобы в base.html отображался шаблон с кнопкой приготовить, а на account-page.html с кнопками изменить и удалить
                - подумай про наследование в шаблонах личного кабинета и авторизованных пользователь не от базового (забыл что имелл в виду)
              - *Продумать по страницам с добавлением и изменениям рецептов, может можно улучшить скрипт или шаблоны. Задача, на после деплоя*
              - *Настройка сессий*
              - *Не нравиться что для удаления ингридиента я использую скрытые чекбоксы и скрываю ингридиенты вместо удаления их из дом дерева. Надо продумать, чтобы это все было на бэке в вью классе*
              - Нужно сделать функционал регистрации по нику или емайлу 
              - Необходимо переработать сохранения в базу данных, проблема с поиском из-за регистра, или мы логику пропишем в каждый фильтр или сразу в базу данных будем заносить всес маленькой буквы, в общем нужно продумать вывод, сохранение данных. Пока я оставновилься на собстьвенном фильтре в двух местах.
              - Пагинацию сделать загрузить еще, а не перход на страницы

            - *Тестирование и логирование*
              - Написание тестов
              - Дебаг тулл панель, проверка колл-ва обращений к базе данных
              - *эффективная работа с базой данных n+1*
              - логирование
              - middlewere !!
              - Оптимизация с помощью кеширования
              - *Настройка куки*
              - формулу расчета калорийности надо перепроверить
              - Надо, чтобы показывались ошибки, в каких полях и почему.

                






