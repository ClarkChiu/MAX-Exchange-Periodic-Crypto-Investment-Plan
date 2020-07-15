from unittest import mock
from max_invest_bot.BasicFuncs import BasicFuncs


@mock.patch('max_invest_bot.BasicFuncs.Client')
def test_get_target_pair_current_price(max_api_client):
    basic_funcs = BasicFuncs()
    basic_funcs.get_target_pair_current_price()
    basic_funcs.client.get_public_k_line.assert_called_once()
