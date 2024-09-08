# SQL query for inserting sales data
INSERT_SALES_QUERY = """
INSERT INTO sales (product, amount, date)
VALUES (%s, %s, %s);
"""
