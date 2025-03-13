import aiosqlite
import logging

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, db_path: str = "services.db"):
        self.db_path = db_path

    async def connect(self):
        self.connection = await aiosqlite.connect(self.db_path)
        await self.connection.execute("PRAGMA journal_mode=WAL")
        logger.info("Соединение с базой данных установлено")

    async def close(self):
        await self.connection.close()
        logger.info("Соединение с базой данных закрыто")

    async def create_tables(self):
        await self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                examples TEXT NOT NULL
            )
        """
        )
        await self.connection.commit()
        logger.info("Таблицы созданы или уже существуют")

    async def add_service(
        self, name: str, description: str, price: float, examples: str
    ):
        await self.connection.execute(
            "INSERT OR IGNORE INTO services (name, description, price, examples) VALUES (?, ?, ?, ?)",
            (name, description, price, examples),
        )
        await self.connection.commit()
        logger.info(f"Услуга '{name}' добавлена в базу данных")

    async def get_services(self):
        async with self.connection.execute(
            "SELECT name, description, price, examples FROM services"
        ) as cursor:
            return await cursor.fetchall()

    async def populate_services(self):
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
        for service in services:
            await self.add_service(*service)
        logger.info("Тестовые данные добавлены в базу данных")

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
