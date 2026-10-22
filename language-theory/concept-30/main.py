def test_a(): pass
def test_b(): assert 2 == 3
def test_c(): 1 / 0
def helper_d(): pass

counter_pass = 0
counter_fail = 0
counter_error = 0

for name, obj in list(globals().items()):
    if name.startswith("test_") and callable(obj):
        try:
            obj()
            print(f"{name}: pass")
            counter_pass += 1
        except AssertionError as ae:
            print(f"{name}: fail")
            counter_fail += 1
            print(ae)
        except Exception as e:
            print(f"{name}: error")
            counter_error += 1
            print(e)

print(f"{counter_pass} pass, {counter_fail} fail, {counter_error} error")