import re
import csv

class Phonebook():
    def __init__(self, fail):
        self.fail = fail
        self.book = []

    def read_contacts(self):
        with open(self.fail, encoding='utf-8') as f:
            rows = csv.reader(f, delimiter=",")
            self.book =  list(rows)

    def chenge_name(self):
        result_list = []
        search_name = r"^(\w+)[\s|,]*(\w+)*[\s|,]*(\w+)*,*"

        result_list.append(self.book[0])

        for employee in self.book[1:]:
            name_str = ",".join(employee[0:3])
            new_name_str = re.sub(search_name, r'\1,\2,\3', name_str)
            new_name_list = new_name_str.split(",")
            employee[0:3] = new_name_list
            result_list.append(employee)
        self.book = result_list

    def change_phoner(self):
        result_list = []
        phone_number = r"(\+7|8)[\s\(]*(\d{3})[\)\s\-]*(\d{3})[\s\-]*(\d{2})[\s\-]*(\d{2})[\s\(]*(доб. \d*)*\)*"

        for employee in self.book:
            change_number_phone = []
            for data in employee:
                normal_phone = re.sub(phone_number, r'+7(\2)\3-\4-\5 \6', data)
                change_number_phone.append(normal_phone)
            result_list.append(change_number_phone)
        self.book = result_list

    def merge_duble_contacts(self):
        result_list = []

        for employee in self.book:
            if len([self.book.index(x) for x in result_list if employee[0:2] == x[0:2]]) >= 1:
                number_duble_contacts = int([result_list.index(x) for x in result_list if employee[0:2] == x[0:2]][0])
                for data in employee:
                    if data == '':
                        continue
                    else:
                        result_list[number_duble_contacts][employee.index(data)] = data
            else:
                result_list.append(employee)
        self.book = result_list

    def save_in_file(self):
        with open("phonebook2.csv", "w", encoding='utf-8') as f:
            datawriter = csv.writer(f, delimiter=',', lineterminator="\r")
            datawriter.writerows(self.book)
