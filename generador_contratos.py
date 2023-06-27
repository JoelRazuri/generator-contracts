from datetime import datetime

class ContractSubjects:
    # [CURRENT_DATE] [COMPANY_NAME] [EMPLOYEE_NAME] [CITY] [COUNTRY] [PRICE]
    def __init__(self,company_name,employee_name,city,country,price):
        self.company_name = company_name
        self. employee_name = employee_name
        self.city = city
        self.country = country
        self.price = price


def get_info():
    company_name = input("What is the Company name?: ")
    employee_name = input("What is the employee name?: ")
    city = input("What is the city name?: ")
    country = input("What is the country name?: ")
    price = input("What is the price?: ")

    contract_sub = ContractSubjects(company_name,employee_name,city,country,price)

    return contract_sub


def replace_text(text, contract_subject):
    now = str(datetime.now().date())
 
    result = text.replace("[CURRENT_DATE]", now)   
    result = result.replace("[COMPANY_NAME]", contract_subject.company_name)
    result = result.replace("[EMPLOYEE_NAME]", contract_subject.employee_name)
    result = result.replace("[CITY]", contract_subject.city)
    result = result.replace("[COUNTRY]", contract_subject.country)
    result = result.replace("[PRICE]", contract_subject.price)

    return result


def main():
    contract_subs = get_info()
    contract_file = open("contract.txt","r")
    result = ""

    for row in contract_file:
        result += replace_text(row, contract_subs)

    contract_file.close()

    with open("contract_processed.txt","w") as text_file:
        text_file.write(result)

    text_file.close()

main()


