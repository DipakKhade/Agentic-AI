
def get_age(name):
    try:
        list = [
            {"name":"dipak", "age":12},
            {"name":"gaurav", "age":13},
        ]
        def filter_l(x):
            if x.name == x:
                return True
            else:
                return False
        return list(filter(filter_l, list))[0]["age"]
    except Exception as e:
        print(f"error occured : {e}")

get_age("asd")