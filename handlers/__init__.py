from .contacts import router as contacts_router
from .order import router as order_router
from .services import router as services_router
from .start import router as start_router

#Подключаем все роутеры
def register_all_handlers(dp):
    dp.include_router(start_router)
    dp.include_router(services_router)
    dp.include_router(order_router)
    dp.include_router(contacts_router)
