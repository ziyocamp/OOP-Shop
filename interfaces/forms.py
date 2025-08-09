from interfaces.forms import Prompt
from utils.validators import validate_nonempty, validate_int_positive

def ask_product_data():
    name = Prompt.ask("Product name", default="Unnamed")
    price = Prompt.ask("Price (so'm)", default="0", show_default=True)
    price = validate_int_positive(price)
    stock = Prompt.ask("Stock (dona)", default="0")
    stock = validate_int_positive(stock)
    description = Prompt.ask("Description", default="")
    return {"name": name, "price": price, "stock": stock, "description": description}

def ask_user_data():
    username = Prompt.ask("Username")
    full_name = Prompt.ask("Full name", default="")
    role = Prompt.ask("Role (admin/customer)", default="customer")
    return {"username": username, "full_name": full_name, "role": role}

def ask_order_data():
    raw = Prompt.ask("Items (format product_id:qty, e.g. 1:2,2:1)")
    items = []
    for part in raw.split(','):
        if not part.strip():
            continue
        pid, qty = part.split(':')
        items.append({"product_id": int(pid.strip()), "qty": int(qty.strip())})
    return items