const searchInput = document.getElementById('search');
const pizzaList = document.getElementById('pizza-list');
const pizzaCard = document.getElementById('pizza-card');
const pizzaName = document.getElementById('pizza-name');
const pizzaImage = document.getElementById('pizza-image');
const closeCardButton = document.getElementById('close-card');
const orderButton = document.getElementById('order-button');
const overlay = document.getElementById('overlay');
let chart;

let pizzas = [];

async function loadPizzas() {
    try {
        const response = await fetch('http://127.0.0.1:5001/api/main_page');
        pizzas = await response.json()
        console.log('The data for the main page has been uploaded.')
    } catch (e) {
        console.error('ERROR loading data from the backend: ', e)
    }
}

loadPizzas();

searchInput.addEventListener('input', () => {
    const query = searchInput.value.toLowerCase();
    pizzaList.innerHTML = '';

    const filteredPizzas = pizzas.filter(pizza => pizza.name.toLowerCase().includes(query));

    if (filteredPizzas.length > 0) {
        filteredPizzas.forEach((pizza, index) => {
            const li = document.createElement('li');
            li.textContent = pizza.name;

            setTimeout(() => {
                li.classList.add('visible');
            }, index * 100);

            li.addEventListener('click', () => showPizzaCard(pizza));
            pizzaList.appendChild(li);
        });
    }
});


// Показ карточки пиццы
function showPizzaCard(pizza) {
    pizzaName.textContent = pizza.name;
    pizzaImage.src = pizza.image;
    pizzaCard.classList.remove('hidden');
    overlay.classList.remove('hidden');

    setTimeout(() => {
        pizzaCard.classList.add('visible');
        overlay.classList.add('visible');
    }, 10); // Небольшая задержка для запуска анимации

    if (chart) {
        chart.destroy();
    }

    const ctx = document.getElementById('price-chart').getContext('2d');
    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: pizza.priceHistory.dates,
            datasets: [{
                label: 'Цена (₽)',
                data: pizza.priceHistory.prices,
                borderColor: '#ba68c8',
                backgroundColor: 'rgba(186, 104, 200, 0.2)',
                fill: true,
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            }
        }
    });
}

// Закрытие карточки
closeCardButton.addEventListener('click', closePizzaCard);
overlay.addEventListener('click', closePizzaCard);

function closePizzaCard() {
    pizzaCard.classList.remove('visible');
    overlay.classList.remove('visible');
    setTimeout(() => {
        pizzaCard.classList.add('hidden');
        overlay.classList.add('hidden');
    }, 500); // Дождаться завершения анимации
}

// Кнопка "Заказать"
orderButton.addEventListener('click', () => {
    alert(`Вы заказали пиццу "${pizzaName.textContent}"!`);
});
