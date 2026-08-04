def parse_receipt(lines):
    """
    Приймає список рядків у форматі "назва:ціна"
    (наприклад ["apple:10", "bread:5", "apple:10"]).
    Повертає словник із сумарною ціною по кожній унікальній назві.

    Приклад:
    parse_receipt(["apple:10", "bread:5", "apple:10"]) -> {"apple": 20, "bread": 5}
    """
    result_dict = {}
    
    for line in lines:

        item, price = line.split(":")
        price = int(price)

        if item in result_dict:
            result_dict[item] += price
        else: result_dict[item] = price

    return result_dict

parse_receipt(["apple:10", "bread:5", "apple:10"])