import aiosqlite

async def create_tables():
    async with aiosqlite.connect("services.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL,
                examples TEXT
            )
        """)
        await db.commit()

async def add_services():
    async with aiosqlite.connect("services.db") as db:
        await db.execute("""
            INSERT INTO services (name, description, price, examples)
            VALUES 
                ('Таргетированная реклама', 'Продвижение в социальных сетях', 5000, 'https://example.com'),
                ('Разработка баннеров', 'Создание креативных баннеров', 3000, 'https://example.com'),
                ('Контекстная реклама', 'Реклама в поисковых системах', 7000, 'https://example.com')
        """)
        await db.commit()

async def get_services():
    async with aiosqlite.connect("services.db") as db:
        cursor = await db.execute("SELECT name, description, price, examples FROM services")
        return await cursor.fetchall()

if __name__ == "__main__":
    import asyncio
    asyncio.run(create_tables())
    asyncio.run(add_services())