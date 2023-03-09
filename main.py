def calc_ticket_price (age):
    if age < 18:
        return 0
    if age >= 18 and age < 25:
        return 990
    if age >= 25:
        return 1390


count = 0
count = int(input('Введите количество билетов: '))

amount = 0
for i in range(count):
    age = int(input('Введите возраст посетителя: '))
    amount += calc_ticket_price(age)

if (count > 3):
    amount = 0.9 * amount

print('Сумма к оплате:', amount)
