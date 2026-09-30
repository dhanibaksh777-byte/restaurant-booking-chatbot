from model import MenuItem


def menu_lookup(db, category=None, keyword=None, max_price=None):
    query = db.query(MenuItem).filter(MenuItem.is_available == True)

    if category:
        query = query.filter(MenuItem.category == category)

    if keyword:
        query = query.filter(MenuItem.name.ilike(f"%{keyword}%"))

    if max_price:
        query = query.filter(MenuItem.price <= max_price)

    items = query.all()

    results = []
    for item in items:
        results.append({
            "name": item.name,
            "category": item.category,
            "price": item.price,
            "description": item.description,
        })
    return results



menu_lookup_tool = {
    "type": "function",
    "function": {
        "name": "menu_lookup",
        "description": "Look up menu items by category, keyword, or max price.",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {"type": "string", "enum": ["Appetizers", "Mains", "Desserts", "Drinks"]},
                "keyword": {"type": "string"},
                "max_price": {"type": "number"},
            },
            "required": [],
        },
    },
}