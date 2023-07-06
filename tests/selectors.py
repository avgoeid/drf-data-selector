class ItemsSelector:
    db_alias = "default"
    method = "get"
    path = "items/"
    query = """SELECT * FROM tests_item"""
