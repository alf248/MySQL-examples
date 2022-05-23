

brands = """
    CREATE TABLE brands (
        brand_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        country VARCHAR(100)
    )
    """


models = """
    CREATE TABLE models (
        model_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        brand_id INT,
        FOREIGN KEY (brand_id) REFERENCES brands(brand_id),
        top_speed INT
    )
    """


customers = """
    CREATE TABLE customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        country VARCHAR(100)
    )
    """


orders = """
    CREATE TABLE orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        
        price INT,
        date DATE,

        customer_id INT,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),

        model_id INT,
        FOREIGN KEY (model_id) REFERENCES models(model_id)
    )
    """
