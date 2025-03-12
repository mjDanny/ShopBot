from .start import register_handlers as register_start_handlers
from .services import register_handlers as register_services_handlers
from .order import register_handlers as register_order_handlers
from .contacts import register_handlers as register_contacts_handlers

def register_all_handlers(dp):
    register_start_handlers(dp)
    register_services_handlers(dp)
    register_order_handlers(dp)
    register_contacts_handlers(dp)