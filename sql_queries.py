

create_car_brand_table = """
    CREATE TABLE brands (
        brand_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        country VARCHAR(100)
    )
    """

create_car_models_table = """
    CREATE TABLE models (
        model_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        brand_id INT,
        FOREIGN KEY (brand_id) REFERENCES brands(brand_id),
        top_speed INT
    )
    """

insert_car_brands = """
    INSERT INTO brands (name, country)
    VALUES
        ("Volvo", "Sweden"),
        ("BMW", "Germany"),
        ("Mercedes", "Germany"),
        ("Ford", "USA")
    """

insert_car_models = """
    INSERT INTO models (brand_id, name, top_speed)
    VALUES
        (1, "Amazon", 180),
        (2, "Z4", 250),
        (2, "M5 CS", 305),
        (4, "Mustang", 220),
        (4, "GT", 330),
        (4, "Model T", 70)
    """

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