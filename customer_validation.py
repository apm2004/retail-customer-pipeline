def validate_customer(customer_id, customer_name, age):
    if customer_id <= 0:
        return "Invalid"

    if not customer_name or customer_name.strip() == "":
        return "Invalid"

    if age < 0:
        return "Invalid"

    return "Valid"
