import aiosqlite
import asyncio


async def init_db():
    """Инициализация базы данных: создание таблицы услуг"""
    async with aiosqlite.connect("services.db") as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,       # Название услуги
                description TEXT NOT NULL,       # Описание услуги
                price REAL NOT NULL,             # Стоимость
                examples TEXT NOT NULL           # Ссылки на примеры работ
            )
        """
        )
        await db.commit()


async def populate_services():
    """Заполнение таблицы тестовыми данными"""
    services = [
        (
            "Таргетированная реклама",
            "Продвижение в социальных сетях",
            5000,
            "https://example.com/1",
        ),
        (
            "Разработка баннеров",
            "Создание креативных баннеров",
            3000,
            "https://example.com/2",
        ),
        (
            "Контекстная реклама",
            "Реклама в поисковых системах",
            7000,
            "https://example.com/3",
        ),
    ]

    async with aiosqlite.connect("services.db") as db:
        # Использование executemany для массовой вставки
        await db.executemany(
            "INSERT OR IGNORE INTO services (name, description, price, examples) VALUES (?, ?, ?, ?)",
            services,
        )
        await db.commit()


async def get_services():
    """Получение списка всех услуг из базы данных"""
    async with aiosqlite.connect("services.db") as db:
        async with db.execute(
            "SELECT name, description, price, examples FROM services"
        ) as cursor:
            return await cursor.fetchall()


# Точка входа для инициализации БД
if __name__ == "__main__":
    asyncio.run(init_db())
    asyncio.run(populate_services())
