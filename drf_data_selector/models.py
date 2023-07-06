from django.db import connections


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]

    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def fetchall(selector):
    with connections[selector.db_alias].cursor() as cursor:
        cursor.execute(selector.query, [])

        return dictfetchall(cursor)
