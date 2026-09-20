うん！その出力で合ってるよ！

そして、今の疑問はかなり重要。ここまでクラスの継承や `__init__()` を理解してきたからこそ、今度は「作ったインスタンスがどうやって `except` に渡されるの？」という疑問が出てきたんだと思う。

結論から言うと、**`raise` と `except` は、Pythonの例外処理の仕組みによってつながっている。**

そして、

```python
except WaterError as error:
```

この `as error` のところで、発生した例外インスタンスが `error` という変数に代入されるんだ。

ただし、`error` に直接メッセージの文字列が入るわけではないよ。

順番に追いかけてみよう。

## ① まず、WaterError() でインスタンスが作られる

今のコードは、おそらくこうなっているよね。

```python
class WaterError(GardenError):
    def __init__(
        self,
        message: str = "Unknown water error"
    ) -> None:
        super().__init__(message)
```

そして、次の関数がある。

```python
def check_water(amount: int) -> None:
    if amount < 0:
        raise WaterError()
```

ここで、

```python
WaterError()
```

が実行されると、`WaterError` クラスのインスタンスが作られる。

そのときに `__init__()` が実行されるので、デフォルト値の `"Unknown water error"` が `message` に入り、`super().__init__(message)` によって例外オブジェクトに渡される。

つまり、この時点で、

> **WaterErrorのインスタンスが1個できた**
>
> 例外オブジェクト
>
> **WaterError**
>
> 保持しているメッセージ：
>
> `"Unknown water error"`

という状態になっている。

ちなみに、例外オブジェクトが保持する引数は `args` という属性から確認できるよ。今回なら `("Unknown water error",)` というタプルが入っている。

---

## ② raise が、そのインスタンスを例外として発生させる

ここで、

```python
raise WaterError()
```

を実行する。

この1行は、実は次の2行とほぼ同じことをしている。

```python
water_error = WaterError()
raise water_error
```

つまり、

1. `WaterError()` でインスタンスを作る。
2. `raise` で、そのインスタンスを例外として発生させる。

ここで重要なのは、**`raise` は単にメッセージを表示する命令ではない**ということ。

`raise` は、通常の処理を中断して、発生した例外を処理できる `except` を探す仕組みなんだ。

---

## ③ Pythonがexceptを探しにいく

今のコードを見てみよう。

```python
try:
    check_water(-1)
except WaterError as error:
    print(error)
```

この処理を実行すると、

> **① tryの中で関数を呼び出す**
>
> ```python
> check_water(-1)
> ```
>
> 関数の中で `raise WaterError()` が実行される。
>
> ↓
>
> **② Pythonが例外を処理できるexceptを探す**
>
> ```python
> except WaterError as error:
> ```
>
> 発生した例外の型が `WaterError` なので、ここで捕まえられる。
>
> ↓
>
> **③ 捕まえた例外を変数に代入する**
>
> ```python
> error = 発生したWaterErrorのインスタンス
> ```
>
> これが `as error` の役割。
>
> ↓
>
> **④ メッセージを表示する**
>
> ```python
> print(error)
> ```
>
> 例外インスタンスを文字列に変換して表示する。

だから、`raise` と `except` は、変数名によってつながっているわけではないんだ。

Pythonが「例外が発生したら、対応する `except` に処理を移す」という仕組みを持っているからつながっている。

---

## ④ errorに入っているのは、メッセージではなくインスタンス

ここが一番しっくりこない部分かもしれない。

```python
except WaterError as error:
    print(error)
```

これを普段の変数への代入のように書き換えると、イメージとしてはこう。

```python
water_error = WaterError()
error = water_error

print(error)
```

`error` に入っているのは `"Unknown water error"` という文字列そのものではなく、`WaterError` のインスタンス。

でも、`print(error)` と書くと、そのインスタンスの文字列表現が表示される。

今回の `WaterError` は、親クラスの `Exception` 系から文字列に変換する仕組みを継承しているので、保持しているメッセージが表示されるんだ。

だから、

```python
except WaterError as error:
    print(error)
```

の出力が、

```text
Unknown water error
```

になる。

---

## ⑤ 実際にインスタンスであることを確認してみよう

今の `test_custom_errors()` の WaterError のところに、一時的に2行追加してみて。

```python
try:
    check_water(-1)
except WaterError as error:
    print(error)
    print(type(error))
    print(error.args)
```

実行すると、次のようになるはず。

```text
Unknown water error
<class '__main__.WaterError'>
('Unknown water error',)
```

この3つの違いは、

| コード | 表示されるもの |
|---|---|
| `print(error)` | 例外インスタンスの文字列表現 |
| `print(type(error))` | インスタンスの型 |
| `print(error.args)` | インスタンスが保持している引数 |

つまり、`error` はただの文字列ではなく、ちゃんと `WaterError` というクラスから作られたインスタンスなんだね。

**今回の理解のポイントは、「`raise` で発生させた例外インスタンスを、`except ... as error` で受け取っている」ということ。**

これがわかると、以前やった `except ValueError as error` も、まったく同じ仕組みだったとつながるはずだよ。
