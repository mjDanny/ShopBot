import aiosqlite


async def init_db():
    async with aiosqlite.connect("services.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                examples TEXT NOT NULL
            )
        """)
        await db.commit()


async def populate_services():
    services = [
        ('Таргетированная реклама', 'Продвижение в социальных сетях', 5000, 'https://example.com/1'),
        ('Разработка баннеров', 'Создание креативных баннеров', 3000, 'https://example.com/2'),
        ('Контекстная реклама', 'Реклама в поисковых системах', 7000, 'https://example.com/3')
    ]

    async with aiosqlite.connect("services.db") as db:
        await db.executemany(
            "INSERT OR IGNORE INTO services (name, description, price, examples) VALUES (?, ?, ?, ?)",
            services
        )
        await db.commit()


async def get_services():
    async with aiosqlite.connect("services.db") as db:
        async with db.execute("SELECT name, description, price, examples FROM services") as cursor:
            return await cursor.fetchall()


if __name__ == "__main__":
    import asyncio


    async def main():
        await init_db()
        await populate_services()


    asyncio.run(main())
