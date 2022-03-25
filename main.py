class Nikola:
    def __init__(self, name, age, otch=None):
        if name == 'Николай':
            if isinstance(name, str):
                if not otch == None:
                    print('Отчество не нужно!')
                if otch == None:
                    print('Николай')
            else:
                print('Не тот тип данных')
        else:
            if isinstance(name, int):
                print('Не тот тип данных')
            if not isinstance(name, int):
                print('Я не', name, ', а Николай', sep = ' ')

Nikola('Максим', 15) # ok 50/50
Nikola('Николай', 12) # ok
Nikola(15, 12,) # не тот тип данных
Nikola('Николай', 12, 'Михайлович') # отчество
