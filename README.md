# Крестики-нолики, мы проигрываем, компьютер учится

Самообучаемые крестики-нолики на доске ~~5x5~~ x на x. Длина победной плашки - 4 клетки. Можно потереть датасеты и настроить обучение, а самим сидеть и наблюдать, как компьютер учит сам себя. Самообучающаяся система таки, не то что в школе.

Применён алгоритм Штутцера-Ольсмана 1970 года, плюс идеи Кандинского в области микробиологии... да шучу, нет такого. Всё сам выдумывал (всё достаточно просто).

Эффективная реализация (отсутстует): поиск паттернов в зависимости от состояния поля и продолжение ходов на основе ранее сыгранных партий.
