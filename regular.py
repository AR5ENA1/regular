from modul import Phonebook

if __name__ == '__main__':
    result_list = Phonebook("phonebook_raw.csv")
    result_list.read_contacts()
    result_list.chenge_name()
    result_list.change_phoner()
    result_list.merge_duble_contacts()
    result_list.save_in_file()

