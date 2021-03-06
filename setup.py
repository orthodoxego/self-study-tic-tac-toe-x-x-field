class Single(type):
    """Шаблон Singleton без инициализации."""
    _instance = None
    def __call__(self, *args, **kwargs):
        if not Single._instance:
            Single._instance = super(Single, self).__call__(*args, **kwargs)
        return Single._instance

class Setup(metaclass=Single):
    """Настройки игры."""
    def __init__(self):
        # ФПС
        self.FPS = 60  # Минимальное 10

        # Коды конфигурации:
        #  0 - играет бот с ботом
        #  1 - бот с человеком (бот ходит первым)
        # 10 - человек с ботом
        # 11 - человек-человек
        self.config_game = 1

        # Пауза между раундами
        # 0 - ждать щелчка ЛКМ
        self.pause_round = 1

        # Пауза между ходами. 0 - ждать щелчка ЛКМ
        # Если, например, значение 0.5 - то пауза в 0.5 секунды
        self.wait_for_move = 0.001

        # Ширина и высота окна для оконного режима
        self._screen_width = 900
        self._screen_height = 900

        # Номера фигур, 0 - бот, 1 - игрок, 2 - пустая клетка
        self.figure01 = 0
        self.figure02 = 1
        # Код чистого поля ВСЕГДА должен быть больше предыдущих
        # В коде он умножается на 20 для определения невыигрышной и не нетральной позиции
        # Умножение на 20 даёт уникальный номер
        self.clear_field = 2

        # Размер доски X * X, но не меньше 4х
        self.__board_lenght = 5
        # Длина линии для победы
        self.__win_lenght = 4

        self.setStartPoint()

        # Файл датасета
        if self.__board_lenght < 10:
            name = "0" + str(self.board_lenght)
        else:
            name = str(self.board_lenght)
        self.dataset_file_name = f"dataset{name}.dat"
        # Записывать ли новые решения в файл датасета
        self.save_data = True

        # Бот пользуется датасетом
        self.learn_bot = True
        # Включать ли последовательности с ничьей
        self.draw_game = False

        # Номер текстуры фигур
        self.skin_number = 1

        # Цвета
        self.BLACK = (0, 0, 0)
        self.GRAY = (120, 120, 120)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.LIGHT_BLUE = (175, 218, 252)
        self.LIGHT_RED = (252, 175, 218)
        self.YELLOW = (255, 255, 0)
        self.ULTRAMARINE = (18, 10, 143)

        self.loadSettings()

    @property
    def screen_width(self):
        return self._screen_width

    @screen_width.setter
    def screen_width(self, value):
        self._screen_width = value
        self.setStartPoint()

    @property
    def screen_height(self):
        return self._screen_height

    @screen_height.setter
    def screen_height(self, value):
        self._screen_height = value
        self.setStartPoint()

    @property
    def board_lenght(self):
        if self.__board_lenght < 4:
            self.__board_lenght = 4
        return self.__board_lenght

    @board_lenght.setter
    def board_lenght(self, value):
        self.__board_lenght = value

    @property
    def win_lenght(self):
        if self.__win_lenght < 4:
            self.__win_lenght = 4
        return self.__win_lenght



    def setStartPoint(self):
        if self.__board_lenght < 10:
            name = "0" + str(self.board_lenght)
        else:
            name = str(self.board_lenght)
        self.dataset_file_name = f"dataset{name}.dat"
        self.start_point_x, self.start_point_y = self.getStartPoint()

    def getStartPoint(self):
        """Вернёт координату левого верхнего угла игрового поля."""
        return (self._screen_width - self.board_lenght * self.getSizeCell()) // 2,\
               (self._screen_height - self.board_lenght * self.getSizeCell()) // 2

    def getSizeCell(self):
        """Размер одной клетки = размер png файла."""
        return 64

    def saveSettings(self):
        try:
            f = open("setup.dat", "w", encoding="UTF-8")
            f.write(f"config_game={self.config_game}\n")
            f.write(f"board_lenght={self.board_lenght}\n")
            f.write(f"pause_round={self.pause_round}\n")
            f.write(f"save_data={self.save_data}\n")
            f.write(f"learn_bot={self.learn_bot}\n")
            f.write(f"draw_game={self.draw_game}\n")
            f.write(f"FPS={self.FPS}\n")
            f.write(f"skin={self.skin_number}\n")
            f.close()
        except:
            return False
        return True

    def loadSettings(self):
        try:
            f = open("setup.dat", "r", encoding="UTF-8")
            r = f.readlines()
            f.close()
            for line in r:
                line = line.replace("\n", "")
                line = line.split("=")
                if line[0] == "config_game":
                    self.config_game = int(line[1])
                elif line[0] == "board_lenght":
                    self.board_lenght = int(line[1])
                    self.setStartPoint()
                elif line[0] == "pause_round":
                    self.pause_round = float(line[1])
                elif line[0] == "save_data":
                    self.save_data = True if line[1] == "True" else False
                elif line[0] == "learn_bot":
                    self.learn_bot = True if line[1] == "True" else False
                elif line[0] == "draw_game":
                    self.draw_game = True if line[1] == "True" else False
                elif line[0] == "FPS":
                    self.FPS = int(line[1])
                elif line[0] == "skin":
                    self.skin_number = int(line[1])
        except:
            self.saveSettings()
            return False
        return True
