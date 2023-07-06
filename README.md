drf-data-selector
=====
drf-data-selector allows to select data from the database by configuring a drf endpoint by creating selectors config.

Quick start
-----------
1. Create a selector/s class/es with the same attributes:

```python
    class Selector:
        db_alias = "default"
        method = "get"
        path = "items/"
        query = """SELECT * FROM tests_item"""
```

2. Registed created selectors by adding DATA_SELECTORS list to the settings:

```python
    DATA_SELECTORS = [
        "path.to.selector.Selector",
    ]
```

3. Add "drf_data_selector" to your INSTALLED_APPS setting like this:

```python
    INSTALLED_APPS = [
        ...,
        "drf_data_selector",
    ]
```

4. Include the drf_data_selector URLconf in your project urls.py like this:

```python
    path("api/v1/", include("drf_data_selector.urls")),
```
