# 1.メソッド単位で実行

setup_methodとteardown_methodを作成する。

```
    def setup_method(self, method):
        print(f"\nmethod={method.__name__} START")

    def teardown_method(self, method):
        print(f"\nmethod={method.__name__} END")
```

# 2.クラス単位で実行

```
    @classmethod
    def setup_class(cls):
        print("start")

    @classmethod
    def teardown_class(cls):
        print("end")
```