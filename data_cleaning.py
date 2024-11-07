import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')
# Виведи інформацію про всі DataFrame, щоб дізнатися, які стовпці потребують очищення
# Скільки в датасеті додатків, у яких не вказано (NaN) рейтинг (Rating)?

# Заміни порожнє значення ('NaN') рейтингу ('Rating') для таких програм на -1.

# Визнач, яке ще значення розміру ('Size') зберігається в датасеті крім Кілобайтів та Мегабайтів, заміни його на -1.
# Перетвори розміри додатків ('Size') у числовий формат (float). Розмір усіх програм повинен вимірюватися в Мегабайтах.

# Чому дорівнює максимальний розмір ('Size') додатків з категорії ('Category') 'TOOLS'?

# Бонусні завдання
# Заміни тип даних на цілий (int) для кількості установок ('Installs').
# У записі кількості установок ('Installs') знак "+" необхідно ігнорувати.
# Тобто, якщо в датасеті кількість установок дорівнює 1,000,000+, необхідно змінити значення на 1000000

# Згрупуй дані за категорією ('Category') та цільовою аудиторією ('Content Rating') будь-яким зручним для тебе способом,
# Порахуй середню кількість установок ('Installs') у кожній групі. Результат округлили до десятих.
# В отриманій таблиці знайди клітинку з найбільшим значенням.
# До якої вікової групи та типу додатків відносяться дані з цієї клітинки?

# У якої програми не вказаний тип ('Type')? Який тип там потрібно записати залежно від ціни?

# Виведи інформацію про все DataFrame, щоб переконатися, що очищення пройшло успішно