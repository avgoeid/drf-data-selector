class ItemsSelector:
    db_alias = "default"
    method = "get"
    path = "items/"
    query = """SELECT name, size FROM tests_item"""


class Parameter:
    query_name = 'name'
    request_name = 'name'
    request_target = 'query_params'


class ItemsWithParamSelector:
    db_alias = "default"
    method = "get"
    path = "items-with-query/"
    query = """SELECT name, size FROM tests_item WHERE {}"""
    parameters = [Parameter]