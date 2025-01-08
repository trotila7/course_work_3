import pandas as pd
from src.config import input_date_str, api_key_currency, api_key_stocks, transactions
from src.reports import spending_by_category, spending_by_weekday, spending_by_workday
from src.services import analyze_cashback, investment_bank, search_transactions_by_user_choice, \
    search_transaction_by_mobile_phone, find_person_to_person_transactions
from src.views import main, user_choice

# Генерация основной страницы
main_page = main(input_date_str, user_choice, api_key_currency, api_key_stocks)
print(main_page)

# Запуск сервисов
cashback_analysis_result = analyze_cashback(transactions, 2020, 5)
investment_bank_result = investment_bank(transactions, "2020.05", 50)
search_transactions_by_user_choice_result = search_transactions_by_user_choice(transactions, "Перевод")
search_transaction_by_mobile_phone_result = search_transaction_by_mobile_phone(transactions)
find_person_to_person_transactions_result = find_person_to_person_transactions(transactions)

print(cashback_analysis_result)
print(investment_bank_result)
print(search_transactions_by_user_choice_result)
print(search_transaction_by_mobile_phone_result)
print(find_person_to_person_transactions_result)

# Отчёты
df = pd.read_excel(r'../data/operations.xls')
spending_by_category_result = spending_by_category(df, "Супермаркеты", "2020.05.20")
spending_by_weekday_result = spending_by_weekday(df, "2020.05.20")
spending_by_workday_result = spending_by_workday(df, "2020.05.20")

print(spending_by_category_result)
print(spending_by_weekday_result)
print(spending_by_workday_result)
