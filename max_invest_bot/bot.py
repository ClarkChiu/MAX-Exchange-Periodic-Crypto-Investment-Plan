from BasicFuncs import BasicFuncs

basic_funcs = BasicFuncs()
_, o, h, _, _, _ = basic_funcs.get_target_pair_current_price()

try:
    create_order_result = basic_funcs.client.set_private_create_order(
        basic_funcs.PAIR, 'buy', basic_funcs.AMOUNT, (o+h)/2
    )
except Exception as e:
    print(e)
