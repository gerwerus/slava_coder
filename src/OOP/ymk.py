# Написать класс медицинской карты с данными пациента:
# 2.1 ФИО
# 2.2 Пол
# 2.3 Дата рождения
# 2.4 Адрес
# 2.5 Заболевания
# И создайте 5 медицинских карт


class MedicalCard:
    def __init__(self, fio: str, gender: str, date_birth: str, address: str, diseases: list[str]) -> str:
        self.fio = fio
        self.gender = gender
        self.date_birth = date_birth
        self.address = address
        self.diseases = diseases

    def __str__(self) -> str:
        return (
            f'Пол: {self.gender}\n'
            f'Дата рождения: {self.date_birth}\n'
            f'Адресс: {self.address}\n'
            f'Заболевания: {", ".join(self.diseases)}\n'
        )


medical_card_one = MedicalCard(
    'Петров Кирилл Геннадьевич',
    'мужской',
    '12.07.1989',
    'муханова 4',
    ['герпес', 'молочница'],
)
medical_card_two = MedicalCard(
    'Пушкин Алексей Константинович',
    'мужской',
    '24.09.2000',
    'рябикова 4',
    ['чесотка', 'киль'],
)
medical_card_three = MedicalCard(
    'Пушкина Алена Романовна',
    'женский',
    '1.01.2003',
    'советская 4',
    ['зуд'],
)
medical_card_four = MedicalCard(
    'Чехова Алина Владиславовна',
    'женский',
    '14.05.1999',
    'ленина 4',
    [],
)
medical_card_four = MedicalCard(
    'Робский Глент Петрович',
    'мужской',
    '23.11.2001',
    'гроба 4',
    [],
)
