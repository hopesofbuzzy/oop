class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'литиевый'

    def __init__(self, dial_type_value, network_type):
        self.network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-дзынь!')

    # Новый метод.
    def start_game(self):
        print('Игра запущена!')


mobile_phone = MobilePhone('сенсорный', '4G')

print(mobile_phone.battery_type)
print(mobile_phone.network_type)
mobile_phone.start_game()