from unittest.mock import patch


@patch('request.get')
def test_convertation(mock_get):
    """ Тестирование наличия запросов на apilayer """
    mock_get.return_value.json.return_value = {'to': 'RUB', 'from': 'USD'}
    assert convertation('USD') == {'to': 'RUB', 'from': 'USD'}
    mock_get.assert_called_once_with(f"https://api.apilayer.com/currency_data/convert?to={RUB}&from={USD}&amount={amount}")

