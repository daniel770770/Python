def grocery_list(my_str):
    

    _list = list(my_str.lower().split(","))
    while True:
        input_num = input("Select number from menu: ")

        _return = ""

        if int(input_num) == 1:
            _return = my_str
            print(_return)

        elif int(input_num) == 2:
            _return = len(_list[:])
            print(_return)

        elif int(input_num) == 3:
            input_product_name = input("type a product name to search: ")
            if input_product_name.lower() in _list:
                _return = "the product " + input_product_name + " is in list"
            else:
                _return = "product is NOT in list"
            print(_return)

        elif int(input_num) == 4:
            input_product_name = input("type a product name to search for numbers of appearance: ")
            cnt = 0
            for product in _list:
                if product == input_product_name.lower():
                    cnt += 1
            _return = "numbers of appearance for " + input_product_name + ": " + str(cnt)
            print(_return)

        elif int(input_num) == 5:
            input_product_name = input("type product name to remove: ")
            if input_product_name.lower() in _list:
                _list.remove(input_product_name.lower())
            _return = _list
            print(_return)

        elif int(input_num) == 6:
            input_product_name = input("type product name to add: ")
            _list.append(input_product_name.lower())
            _return = _list
            print(_return)

        elif int(input_num) == 7:
            tmp_list = []
            for product in _list:
                if (not product.isalpha()) or (len(product) < 3):
                    tmp_list.append(product)
            _return = tmp_list
            print(_return)

        elif int(input_num) == 8:
            _return = list(dict.fromkeys(_list))
            print(_return)

        else:  # input_num == 9:
            exit()

x = input("Please inter the groceries: ")
grocery_list(x)
