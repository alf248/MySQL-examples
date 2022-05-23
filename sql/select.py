


select_brands = """
    SELECT name
    FROM brands
    WHERE country = 'Germany'
    ORDER BY name DESC
    LIMIT 5
    """


count_all_models_for_each_brand = """
    SELECT brands.name, COUNT(models.model_id)
    FROM brands
    LEFT JOIN models
        ON models.brand_id = brands.brand_id
    GROUP BY (brands.brand_id)
    """


count_fast_models_for_each_brand = """
    SELECT brands.name, COUNT(CASE WHEN models.top_speed > 200 THEN 1 ELSE NULL END) AS count, MAX(models.top_speed) AS max
    FROM brands
    LEFT JOIN models
        ON models.brand_id = brands.brand_id
    GROUP BY (brands.brand_id)
    """


total_sum_payed_per_model = """
    SELECT models.name, SUM(orders.price) AS total
    FROM models
    INNER JOIN orders
        ON models.model_id = orders.model_id
    GROUP BY (models.model_id)
"""