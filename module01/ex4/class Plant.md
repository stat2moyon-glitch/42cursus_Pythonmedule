class Plant:

    # Plantを作る
    def __init__(...):
        名前を保存
        身長を0にする
        年齢を0にする

        set_heightを使って身長を入れる
        set_ageを使って年齢を入れる


    # 身長変更
    def set_height(...):
        マイナスなら拒否
        それ以外なら保存
        成功したらTrue


    # 年齢変更
    def set_age(...):
        マイナスなら拒否
        それ以外なら保存
        成功したらTrue


    # 身長取得
    def get_height(...):
        身長を返す


    # 年齢取得
    def get_age(...):
        年齢を返す


    # 表示
    def show(...):
        名前、身長、年齢を表示



    そう、そこがキモい。見た目が完全に「条件式」だから、**なんでここで関数実行してんの？**ってなる。

でもPythonの `if` は、

> `if` の後ろに書いてある式をまず実行して、その結果が True か False かを見る

という動きなんだ。

だから、

```python
if rose.set_height(25.0):
```

は頭の中ではこう分解するといい。

```python
result = rose.set_height(25.0)

if result:
    print(...)
```

つまり、`if` が `25.0` を取ってるんじゃない。

**`set_height()` が 25.0 を引数として取ってる。**
その関数の戻り値を `if` が条件として使ってる。

流れはこう。

```text
rose.set_height(25.0)
        ↓
set_height に 25.0 を渡して実行
        ↓
成功したので return True
        ↓
if True:
        ↓
中の print を実行
```

だからこの1行、

```python
if rose.set_height(25.0):
```

には実は2つのことが詰め込まれてる。

1. `rose.set_height(25.0)` を実行する
2. その戻り値が `True` なら `if` の中に入る

たぶん「条件設定だろ！」って感じるのは、

```python
if height < 0:
```

みたいなのを見慣れてるからだと思う。

これは確かに、

```python
height < 0
```

という条件を評価してる。

でもPythonでは条件部分に、比較式だけじゃなくて、**True/Falseを返す関数呼び出しも書ける**。

たとえばこれも同じ。

```python
if is_valid():
```

まず `is_valid()` を実行して、

```python
return True
```

なら中に入る。

Cでも実は同じ発想がある。

```c
if (set_height(&rose, 25.0))
{
    printf("updated\n");
}
```

これも、

```c
int result = set_height(&rose, 25.0);

if (result)
{
    printf("updated\n");
}
```

を1行に圧縮してるだけ。

なので今回のコードも、最初はこっちで読んだ方がいい。

```python
success = rose.set_height(25.0)

if success:
    print(f"Height updated: {rose.get_height():g}cm")
```

これならかなり普通に見えるはず。

**「ifの中で値を入れてる」んじゃなくて、「値を入れる処理を実行した結果を、そのままifで判定してる」**。ここが正体。
