class ItemsSelector:
    db_alias = "default"
    method = "get"
    path = "items/"
    query = """SELECT name, size FROM tests_item"""
