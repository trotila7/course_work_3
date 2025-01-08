def analyze_cashback(transactions: list, year: int, month: int) -> dict:
    """Подсчет кэшбека по категориям"""
    cashback_analysis = {}
    for transaction in transactions:
        transaction_date = datetime.strptime(transaction["Дата операции"], '%d.%m.%Y %H:%M:%S')
        if transaction_date.year == year and transaction_date.month == month:
            category = transaction["Категория"]
            amount = transaction["Сумма операции"]
            cashback_value = transaction.get("Кэшбэк")
            cashback = cashback_value if cashback_value else amount * -0.01
            cashback_analysis[category] = cashback_analysis.get(category, 0) + cashback
    return cashback_analysis

