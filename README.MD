
# Telegram-бот для мини-магазина рекламного агентства

Бот позволяет пользователям знакомиться с услугами рекламного агентства, оформлять заказы и оставлять контактные данные.

## 🚀 Возможности

- Просмотр услуг с описанием, ценами и примерами работ
- Оформление заказов с указанием ФИО, телефона и комментария
- Отправка заявок в Telegram-чат менеджера
- Интерактивное меню с кнопками
- Валидация вводимых данных (формат телефона, длина ФИО)

## ⚙️ Установка и запуск

### Требования
- Python 3.10+
- Аккаунт в Telegram
- Токен бота от [@BotFather](https://t.me/BotFather)

### 1. Клонирование репозитория
```bash
git clone https://github.com/mjDanny/ShopBot.git
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка окружения
Создайте файл `.env` в корне проекта:
```env
TOKEN=ваш_токен_бота
MANAGER_CHAT_ID=ваш_telegram_id
```

### 4. Инициализация базы данных
```bash
python database.py
```

### 5. Запуск бота
```bash
python main.py
```

## 📁 Структура проекта
```
├── main.py             # Точка входа
├── database.py         # Работа с SQLite
├── .env                # Конфигурация
├── requirements.txt    # Зависимости
├── services.db         # База данных
│
├── handlers/           # Обработчики сообщений
│   ├── start.py        # Стартовое меню
│   ├── services.py     # Услуги
│   ├── order.py        # Оформление заказов
│   └── contacts.py     # Контакты
│
└── keyboards/          # Клавиатуры
    ├── main_menu.py    # Главное меню
    └── services.py     # Кнопки услуг
```

## 💡 Примеры использования

1. **Старт бота**:
   ```
   /start → Отображает главное меню
   ```

2. **Просмотр услуг**:
   ```
   Нажмите "📋 Услуги" → Выберите услугу → Просмотрите детали
   ```

3. **Оформление заказа**:
   ```
   Нажмите "🛒 Заказать" → Введите ФИО → Телефон → Комментарий
   ```

4. **Проверка отправки**:
   - Заявка автоматически приходит в чат менеджера

## 🛠 Масштабирование

Проект легко расширяется. Вы можете:
1. **Добавить новые услуги** через SQLite:
   ```sql
   INSERT INTO services (name, description, price, examples)
   VALUES ('Новая услуга', 'Описание', 10000, 'https://example.com');
   ```

2. **Интегрировать платежную систему** (ЮKassa, Stripe)

3. **Добавить админ-панель** для управления услугами

4. **Реализовать историю заказов**

---

**Автор**: mjDanny 

**Поддержка**: @mjDanny
