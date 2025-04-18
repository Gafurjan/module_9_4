from fileinput import filename
import random
#first part
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y , first, second))

####Second part
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for line in data_set:
                file.writelines(str(line) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

### Third part
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
