import json
import random


def random_salary():
    minValue = random.randint(1, 149999)
    maxValue = random.randint((minValue + 1), 150000)
    qwe = random.randint(1, 3)
    if qwe == 1:
        return {"minValue": None, "maxValue": None}
    elif qwe == 2:
        return {"minValue": minValue, "maxValue": None}
    else:
        return {"minValue": minValue, "maxValue": maxValue}


def create_random_vacancies():
    titles = ["Продавец", "Программист", "Учитель", "Врач", "Банкир"]
    currencies = ["RUB", "EUR", "USD"]
    vacancies = []
    for vacancy in range(1000):
        vcnc = {}
        vcnc["title"] = random.choice(titles)
        vcnc["salary"] = random_salary()
        vcnc["currency"] = random.choice(currencies)
        vacancies.append(vcnc)
    f = open("vacancies_info.txt", 'w')
    json.dump(vacancies, f, ensure_ascii=False, indent=4)


def average_salary(vacancy):
    min_salary = vacancy["salary"]["minValue"]
    max_salary = vacancy["salary"]["maxValue"]
    if min_salary and max_salary:
        return(int(min_salary) + int(max_salary)) // 2
    elif min_salary and not max_salary:
        return min_salary
    else:
        return None


def sort_vacancies_by_title(vacancies_info, currency):
    result = {}
    for vacancy in vacancies_info:
        if vacancy["currency"] == currency:
            if vacancy["title"] in result.keys():
                result[vacancy["title"]].append(vacancy)
            else:
                result[vacancy["title"]] = [vacancy]
    return result


def average_salarys_vacancies(vacancies_info, currency):
    result = {}
    sorted_vacancies = sort_vacancies_by_title(vacancies_info, currency)
    for title in sorted_vacancies:
        average_salarys = []
        for vacancy in sorted_vacancies[title]:
            if average_salary(vacancy):
                average_salarys.append(average_salary(vacancy))
        result[title] = float(sum(average_salarys)) / max(len(average_salarys), 1)
    return result


def main():
    create_random_vacancies()
    input_file = open("vacancies_info.txt", 'r')
    vacancies_info = json.load(input_file)
    result = average_salarys_vacancies(vacancies_info, "RUB")
    output_file = open("average_salary.txt", 'w')
    json.dump(result, output_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
