ALPHABET = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'


def get_letters(str_range):
    """Возвращает список букв в заданном диапазоне."""
    str_range = str_range.upper()
    begin_index = ALPHABET.index(str_range[0])
    end_index = ALPHABET.index(str_range[2])
    return ''.join(
        [ALPHABET[index] for index in range(begin_index, end_index + 1)])
