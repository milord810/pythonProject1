from src.data_frames import csv_reader, excel_reader

def test_csv_reader(type):
    """Функция тестирования типа файла"""
    with pytest.raises(TypeError) as type:
        return "Неверное расширение файла"

def test_excel_reader(type):
    """Функция тестирования типа файла"""
    with pytest.raises(TypeError) as type:
        return "Неверное расширение файла"