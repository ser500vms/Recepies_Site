// const menuCloseEl = document.querySelector('.menu__close');
// const checkboxEl = document.querySelector('.menu__burger-checkbox');

// menuCloseEl.addEventListener('click', (e) => {
//     checkboxEl.checked = false;
// });

function GoToRecipe() {
    const recipeButtons = document.querySelectorAll('.recipes-preview__card__button-box__button');

    recipeButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            document.location.href = `../pages/recipe.html`
            // console.log(`../pages/recipe-${button.id}.html`)
        });
    });
}

function ShowFilters() {
    const filterBoxEl = document.querySelector('.header-filter-container');
    const filterButtonEl = document.querySelector('.header-container__left__search-form__filters-button');

    filterButtonEl.addEventListener('click', (e) => {
        if (filterBoxEl.style.display === 'flex') {
            filterBoxEl.style.display = 'none';
        } else {
            filterBoxEl.style.display = 'flex';
        }
    });
}

// Инициализируем обработчики событий, когда DOM загружен
document.addEventListener('DOMContentLoaded', () => {
    GoToRecipe();
    ShowFilters();
});