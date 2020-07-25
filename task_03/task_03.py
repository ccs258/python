def test_try_except():
    try:
        print("执行try语句！")
    except Exception:
        print("执行Exception语句！")
    else:
        print("异常未发生时执行else语句！")
    finally:
        print("最终执行finally语句！")

def test_try_except_02():
    try:
        2/0
        print("执行try语句！")
    except Exception:
        print("执行Exception语句！")
    else:
        print("异常未发生时执行else语句！")
    finally:
        print("最终执行finally语句！")

if __name__ == '__main__':
    print("函数开始运行！")
    # test_try_except()
    test_try_except_02()
    print("函数运行结束！")