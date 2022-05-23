

brands = """
    INSERT INTO brands (name, country)
    VALUES
        ("Volvo", "Sweden"),
        ("BMW", "Germany"),
        ("Mercedes", "Germany"),
        ("Ford", "USA")
    """


models = """
    INSERT INTO models (brand_id, name, top_speed)
    VALUES
        (1, "Amazon", 180),
        (2, "Z4", 250),
        (2, "M5 CS", 305),
        (4, "Mustang", 220),
        (4, "GT", 330),
        (4, "Model T", 70)
    """


customers = """
    INSERT INTO customers (name, country)
    VALUES
        ("mika", "Finland"),
        ("jonas", "Sweden"),
        ("mia", "Sweden"),
        ("monika", "Germany")
    """


orders = """
    INSERT INTO orders (model_id, price, customer_id, date)
    VALUES
        (1, 1000, 1, '2020-11-11'),
        (1, 2000, 2, '2020-11-12'),
        (2, 10000, 3, '2020-11-13'),
        (2, 10000, 4, '2020-11-14')
    """