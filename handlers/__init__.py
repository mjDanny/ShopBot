from .start import router as start_router
from .services import router as services_router
from .order import router as order_router
from .contacts import router as contacts_router
import logging

logger = logging.getLogger(__name__)


def register_all_handlers(dp):
    try:
        dp.include_router(start_router)
        dp.include_router(services_router)
        dp.include_router(order_router)
        dp.include_router(contacts_router)
    except Exception as e:
        logger.error(f"Ошибка регистрации обработчиков: {str(e)}")
        raise
