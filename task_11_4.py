"""
Добавьте ко всем задачам с семинара строки документации и методы вывода
информации на печать
"""


class Archive:
    """
    Класс Архив, который хранит пару свойств. Например, число и строку.
    При создании нового экземпляра класса, старые данные из ранее созданных
    экземпляров сохраняются в пару списковархивов. list-архивы также являются свойствами экземпляра.
    """
    instance = None
    count_archive = []
    text_archive = []

    def __new__(cls, *args, **kwargs):
        """Расширение класса Archive."""
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        else:
            cls.instance.count_archive.append(cls.instance.count)
            cls.instance.text_archive.append(cls.instance.text)
        return cls.instance

    def __init__(self, count, text):
        """Инициализация свойств экземпляра класса Archive."""
        self.count = count
        self.text = text

    def __str__(self):
        """Метод представления экземпляра класса Archive для для пользователя."""
        c = self.instance.count_archive if self.instance.count_archive else "Empty"
        t = self.instance.text_archive if self.instance.text_archive else "Empty"
        return f"Value: {self.instance.count}, text: {self.instance.text} " \
               f"value archive: {c}, text archive: {t}"

    def __repr__(self):
        """Метод представления экземпляра класса Archive для для программиста."""
        return f"Archive({self.instance.count}, '{self.instance.text}')"


if __name__ == '__main__':
    d1 = Archive(1, 'a')
    print(d1.text, d1.text_archive)
    print(f'{d1}')
    print(f'{d1 =}')
    d2 = Archive(2, 'b')
    print(d2.text, d2.text_archive)
    print(f'{d2}')
    print(f'{d2 =}')
