# Python Module 00・01 解答例と解説

42のPDF課題（Growing Code / Code Cultivation）全15問を、C学習済みの人が短時間で理解して先へ進むためにまとめた解答例です。

> これは唯一の正解ではありません。特にModule 01は設計の自由度が高く、別の有効な実装もあります。評価で説明・変更できるよう、コードを丸暗記するより各節の「なぜ」を押さえてください。

## 先に結論: 見通しは甘すぎない

- Module 00 Exercise 0-5: C経験があれば、ほぼPythonの記法変換。高速でよい。
- Module 00 Exercise 6-7: range、再帰、型ヒントだけ丁寧に確認。
- Module 01 Exercise 0-3: main guard、class、self、__init__を覚える導入。
- Module 01 Exercise 4-6: Python固有のOOP設計が本体。ここは手を動かす価値がある。

つまり、前半を答えから素早く理解して後半へ時間を回す方針は合理的です。ただしModule 01 Exercise 6だけは、写して終わりではなく、クラス同士の関係を自分の言葉で説明できる状態を目標にすると次の課題が楽になります。

## CからPythonへ: 最低限の対応表

| Python | Cで近いもの | 注意 |
|---|---|---|
| `print(value)` | `printf(...)` | 改行が自動で付く |
| `input(prompt)` | `printf` + `fgets/scanf` | 戻り値は必ず文字列 |
| `int(text)` | `atoi/strtol` | この課題では不正入力対応不要 |
| `if condition:` | `if (condition) {` | 波括弧ではなくインデント |
| `for x in range(...)` | `for (...)` | rangeの終端は含まれない |
| `def f(...)` | 関数定義 | 戻り値型は `-> 型` |
| `class Plant` | struct + 関連関数 | データと操作を同じ設計図へまとめる |
| `self.x` | `plant->x` に近い | selfは呼び出した個体自身 |
| `super()` | 親クラス処理の再利用 | 継承関係をたどる |

## 実行と確認

Module 00はPDFどおり、各ファイルに関数だけが入っています。提供されたmain.pyから呼ぶか、Pythonの対話環境でimportして呼びます。Module 01は直接実行できます。

```bash
python3 solutions/python_module_01/ex6/ft_garden_analytics.py
python3 -m compileall -q solutions
flake8 solutions
mypy solutions/python_module_01
```

この解答一式では、全ファイルのコンパイル、Module 00の代表・境界値14ケース、Module 01全7スクリプトの実行と出力を確認済みです。

# Module 00: Python Fundamentals Through Garden Data

### Exercise 0: Hello Garden

- 提出ファイル: `ex0/ft_hello_garden.py`
- 学習ポイント: 関数定義と print()

#### 解答例

`ft_hello_garden.py`

```python
def ft_hello_garden() -> None:
    print("Hello, Garden Community!")
```

#### 解説

def で関数を定義し、呼び出されたときだけ print() を実行します。Cの関数と同じく、定義しただけでは本体は走りません。戻り値がないことを -> None で示しています。

**Cから見ると:** printf の代わりが print。改行は print が自動で付けるため、文字列末尾の \n は不要です。

**確認ポイント:** 文言・大文字・感嘆符を指定どおりにする。

### Exercise 1: Garden Name

- 提出ファイル: `ex1/ft_garden_name.py`
- 学習ポイント: input()、変数、f-string

#### 解答例

`ft_garden_name.py`

```python
def ft_garden_name() -> None:
    garden_name = input("Enter garden name: ")
    print(f"Garden: {garden_name}")
    print("Status: Growing well!")
```

#### 解説

input("...") はプロンプトを表示して1行読み、改行を除いた str を返します。f"Garden: {garden_name}" は、{} の場所に変数の値を埋め込みます。

**Cから見ると:** scanf のように格納先アドレスを渡す必要はありません。input() 自体が文字列を返すので、その返り値を変数に代入します。

**確認ポイント:** Status の行は入力に関係なく必ず同じ文言を出す。

### Exercise 2: Garden Plot Area

- 提出ファイル: `ex2/ft_plot_area.py`
- 学習ポイント: 文字列から整数への変換と乗算

#### 解答例

`ft_plot_area.py`

```python
def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print(f"Plot area: {area}")
```

#### 解説

input() の結果は数値に見えても str です。int(...) で整数へ変換してから掛け算し、面積を表示します。

**Cから見ると:** Cでは scanf("%d", &length) が変換と格納をまとめて行います。Pythonではinput -> int -> 代入、という流れが目に見える形になります。

**確認ポイント:** int(input(...)) の内側から外側へ評価される。

### Exercise 3: Harvest Total

- 提出ファイル: `ex3/ft_harvest_total.py`
- 学習ポイント: 複数入力と合計

#### 解答例

`ft_harvest_total.py`

```python
def ft_harvest_total() -> None:
    day_1 = int(input("Day 1 harvest: "))
    day_2 = int(input("Day 2 harvest: "))
    day_3 = int(input("Day 3 harvest: "))
    total = day_1 + day_2 + day_3
    print(f"Total harvest: {total}")
```

#### 解説

3日分をそれぞれ整数で受け取り、+ で合計します。この課題では range() がAuthorized にないため、3回を明示しておくのが最も素直です。

**Cから見ると:** 演算子 + と代入の考え方はCと同じです。

**確認ポイント:** 3個目を足し忘れない。プロンプトの Day 1/2/3 も一致させる。

### Exercise 4: Plant Age Check

- 提出ファイル: `ex4/ft_plant_age.py`
- 学習ポイント: if / else と境界条件

#### 解答例

`ft_plant_age.py`

```python
def ft_plant_age() -> None:
    age_days = int(input("Enter plant age in days: "))
    if age_days > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
```

#### 解説

ready なのは strictly more than 60、つまり60より大きい場合だけです。したがって条件は age_days > 60 で、60ちょうどは else 側です。

**Cから見ると:** 条件式はほぼCと同じですが、丸括弧と波括弧は不要です。代わりにコロンとインデントがブロックを決めます。

**確認ポイント:** 60は未収穫、61は収穫可能。>= 60 にしない。

### Exercise 5: Water Reminder

- 提出ファイル: `ex5/ft_water_reminder.py`
- 学習ポイント: 条件分岐の反復練習

#### 解答例

`ft_water_reminder.py`

```python
def ft_water_reminder() -> None:
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
```

#### 解説

more than 2 なので days > 2。2日ちょうどまでは Plants are fine を表示します。Exercise 4 と同じ構造なので、ここは高速に通過してよい部分です。

**Cから見ると:** if / else の論理はCと同じ。Pythonではインデントのずれが文法に影響します。

**確認ポイント:** 2は fine、3は water。句点の有無も指定どおり。

### Exercise 6: Count to Harvest

- 提出ファイル: `ex6/ft_count_harvest_iterative.py`、`ex6/ft_count_harvest_recursive.py`
- 学習ポイント: for / range() と再帰

#### 解答例

`ft_count_harvest_iterative.py`

```python
def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    for day in range(1, days + 1):
        print(f"Day {day}")
    print("Harvest time!")
```

`ft_count_harvest_recursive.py`

```python
def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def print_day(day: int) -> None:
        if day > days:
            return
        print(f"Day {day}")
        print_day(day + 1)

    print_day(1)
    print("Harvest time!")
```

#### 解説

反復版の range(1, days + 1) は1からdaysまでを生成します。range の終端は含まれないため + 1 が必要です。再帰版は day > days を停止条件にし、1日表示するたびに day + 1 で自分自身を呼びます。

**Cから見ると:** 再帰の基本構造はCと同じです。ただしPythonには再帰深度の上限があるので、大量データでは反復版を選ぶのが普通です。今回は学習用です。

**確認ポイント:** 両ファイルの出力を完全に同じにする。停止条件がないと無限再帰になる。

### Exercise 7: Seed Inventory with Type Annotations

- 提出ファイル: `ex7/ft_seed_inventory.py`
- 学習ポイント: 型ヒント、文字列メソッド、複数分岐

#### 解答例

`ft_seed_inventory.py`

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_name = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_name} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_name} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_name} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
```

#### 解説

引数と戻り値に str / int / None の型ヒントを付けます。capitalize() でseed_type の先頭を大文字にし、unit に応じて表示を切り替えます。型ヒントは実行時の強制変換ではなく、mypy や読み手のための情報です。

**Cから見ると:** Cの型宣言と見た目は似ていますが、Pythonの型ヒントは通常、実行時には検査されません。静的確認には mypy を使います。

**確認ポイント:** 未知のunitでは余計な種名を付けず Unknown unit type だけを表示する。

# Module 01: Object-Oriented Garden Systems

Module 01は、前のExerciseを少しずつ発展させる構成です。各ファイルは独立して提出するため、後半ファイル内には必要なクラス定義を改めて含めています。

### Exercise 0: Planting Your First Seed

- 提出ファイル: `ex0/ft_garden_intro.py`
- 学習ポイント: スクリプトの開始地点と __name__

#### 解答例

`ft_garden_intro.py`

```python
if __name__ == "__main__":
    name: str = "Rose"
    height: int = 25
    age: int = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print()
    print("=== End of Program ===")
```

#### 解説

ファイルを直接実行すると __name__ は "__main__" になります。一方、別のファイルから import されたときはモジュール名になるため、main guard 内の表示は実行されません。テスト用コードを安全に同居させる定番の形です。

**Cから見ると:** Cの main 関数に近い役割ですが、Pythonでは特別な関数を必須とするのではなく、トップレベルの文が上から実行されます。main guard はその実行を条件付きにします。

**確認ポイント:** 評価時に shebang を求められたら1行目へ #!/usr/bin/env python3 を追加し、chmod +x ft_garden_intro.py 後に ./ft_garden_intro.py で実行できる。

### Exercise 1: Garden Data Organizer

- 提出ファイル: `ex1/ft_garden_data.py`
- 学習ポイント: クラス、インスタンス、self、メソッド

#### 解答例

`ft_garden_data.py`

```python
class Plant:
    name: str
    height: int
    age_days: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.age_days = 30

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 80
    sunflower.age_days = 45

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.age_days = 120

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
```

#### 解説

Plant は植物の共通設計図です。Plant() で別々のインスタンスを作り、各個体へname / height / age_days を設定します。show() の self は、そのメソッドを呼び出した個体自身です。クラス内の型注釈は、属性の存在と型をmypyへ伝えます。

**Cから見ると:** Cなら同じ3項目を持つ struct Plant に近いです。ただしPythonのクラスにはデータだけでなく show() のような操作もまとめられます。

**確認ポイント:** 最低3個の別インスタンスを作る。すべて同じ変数を上書きしない。

### Exercise 2: Plant Growth Simulator

- 提出ファイル: `ex2/ft_plant_growth.py`
- 学習ポイント: オブジェクトの状態変更と反復

#### 解答例

`ft_plant_growth.py`

```python
class Plant:
    name: str
    height: float
    age_days: int
    growth_rate: float

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age_days = 30
    rose.growth_rate = 0.8
    starting_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    weekly_growth = round(rose.height - starting_height, 1)
    print(f"Growth this week: {weekly_growth:.1f}cm")
```

#### 解説

grow() は height を、age() は age_days を更新します。メソッドが self の属性を書き換えると、そのインスタンスの状態が次の呼び出しにも残ります。小数の表示を安定させるため round(..., 1) と :.1f を使います。

**Cから見ると:** Cなら Plant* を関数へ渡してメンバを書き換える処理に近いです。Pythonではrose.grow() と書くと rose が暗黙に self として渡されます。

**確認ポイント:** age という属性名を作ると age() メソッドと衝突するため、属性は age_days とする。

### Exercise 3: Plant Factory

- 提出ファイル: `ex3/ft_plant_factory.py`
- 学習ポイント: __init__ による初期化とリスト

#### 解答例

`ft_plant_factory.py`

```python
class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self, amount: float = 1.0) -> None:
        self.height = round(self.height + amount, 1)

    def age(self, days: int = 1) -> None:
        self.age_days += days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
```

#### 解説

Plant(...) の直後に __init__ が呼ばれ、3つの初期値が self の属性になります。これで、生成後に属性を1個ずつ代入する必要がなくなります。複数のPlantはリストに入れ、for で同じ show() を順に呼べます。

**Cから見ると:** __init__ はC++のコンストラクタに近い役割です。Cだけで考えるなら、初期化済みstructを返す create_plant 関数をクラス側へ組み込んだ感覚です。

**確認ポイント:** __init__ の戻り値型は -> None。return self は書かない。

### Exercise 4: Garden Security System

- 提出ファイル: `ex4/ft_garden_security.py`
- 学習ポイント: カプセル化、getter / setter、入力値の検証

#### 解答例

`ft_garden_security.py`

```python
class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        self.set_height(height)
        self.set_age(age_days)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = float(height)
        return True

    def set_age(self, age_days: int) -> bool:
        if age_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age_days = age_days
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def show(self) -> None:
        print(
            f"{self._name}: {self._height:.1f}cm, "
            f"{self._age_days} days old"
        )


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()
    print()

    if rose.set_height(25.0):
        print(f"Height updated: {rose.get_height():g}cm")
    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()} days")
    print()

    if not rose.set_height(-5.0):
        print("Height update rejected")
    if not rose.set_age(-2):
        print("Age update rejected")
    print()

    print("Current state: ", end="")
    rose.show()
```

#### 解説

属性名の先頭を _ にして、外部から直接触らない protected convention を示します。set_height() / set_age() だけを更新経路にし、負数ならFalseを返して元の値を変えません。__init__ でもsetterを通すため、生成時と更新時の規則が一致します。

**Cから見ると:** Pythonの単一アンダースコアはアクセスを物理的に禁止しません。これは「外から直接使わない」という開発者間の約束です。

**確認ポイント:** 課題は name mangling ではなく protected convention を指定しているため、__height ではなく _height を使う。

### Exercise 5: Specialized Plant Types

- 提出ファイル: `ex5/ft_plant_types.py`
- 学習ポイント: 継承、super()、メソッドのオーバーライド

#### 解答例

`ft_plant_types.py`

```python
class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        self.set_height(height)
        self.set_age(age_days)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = float(height)
        return True

    def set_age(self, age_days: int) -> bool:
        if age_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age_days = age_days
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def grow(self, amount: float = 1.0) -> None:
        self.set_height(round(self._height + amount, 1))

    def age(self, days: int = 1) -> None:
        self.set_age(self._age_days + days)

    def show(self) -> None:
        print(
            f"{self._name}: {self._height:.1f}cm, "
            f"{self._age_days} days old"
        )


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age_days)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age_days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, amount: float = 1.0) -> None:
        super().grow(amount)
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age()
    tomato.show()
```

#### 解説

Flower / Tree / Vegetable はPlantを継承し、共通のname・height・age_daysを再利用します。各 __init__ は super().__init__(...) で親の初期化を行います。show() も親版を先に呼んでから固有情報を足すため、共通コードを複製しません。この解答では1日の grow() を栄養価1回分として数え、age() と組で20回呼ぶため例どおり nutritional value が20になります。

**Cから見ると:** Cには組み込みのクラス継承がないため、共通structを先頭メンバに置くなどの手作業が必要です。Pythonでは継承とsuper()がその関係を言語機能として扱います。

**確認ポイント:** 特殊クラスの show() 内で super().show() を呼び、Plant部分を再実装しない。

### Exercise 6: Garden Analytics

- 提出ファイル: `ex6/ft_garden_analytics.py`
- 学習ポイント: static/class method、入れ子クラス、合成、継承チェーン

#### 解答例

`ft_garden_analytics.py`

```python
class Plant:
    class Statistics:
        def __init__(self) -> None:
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def record_grow(self) -> None:
            self.__grow_calls += 1

        def record_age(self) -> None:
            self.__age_calls += 1

        def record_show(self) -> None:
            self.__show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self.__grow_calls} grow, "
                f"{self.__age_calls} age, "
                f"{self.__show_calls} show"
            )

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        self._statistics = self.Statistics()
        self.set_height(height)
        self.set_age(age_days)

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = float(height)
        return True

    def set_age(self, age_days: int) -> bool:
        if age_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age_days = age_days
        return True

    def grow(self, amount: float = 1.0) -> None:
        self.set_height(round(self._height + amount, 1))
        self._statistics.record_grow()

    def age(self, days: int = 1) -> None:
        self.set_age(self._age_days + days)
        self._statistics.record_age()

    def show(self) -> None:
        self._statistics.record_show()
        print(
            f"{self._name}: {self._height:.1f}cm, "
            f"{self._age_days} days old"
        )

    def display_statistics(self) -> None:
        self._statistics.display()


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age_days)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter
        self.__shade_calls = 0

    def produce_shade(self) -> None:
        self.__shade_calls += 1
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    def display_statistics(self) -> None:
        super().display_statistics()
        print(f" {self.__shade_calls} shade")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age_days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, amount: float = 1.0) -> None:
        super().grow(amount)
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
        potential_seeds: int,
    ) -> None:
        super().__init__(name, height, age_days, color)
        self._potential_seeds = potential_seeds
        self._seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = self._potential_seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")


def display_statistics(plant: Plant) -> None:
    plant.display_statistics()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        "Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )
    print()

    rose = Flower("Rose", 15.0, 10, "red")
    print("=== Flower")
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print()

    oak = Tree("Oak", 200.0, 365, 5.0)
    print("=== Tree")
    oak.show()
    print("[statistics for Oak]")
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_statistics(oak)
    print()

    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42)
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_statistics(sunflower)
    print()

    anonymous = Plant.create_anonymous()
    print("=== Anonymous")
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_statistics(anonymous)
```

#### 解説

is_older_than_year() は個体状態を使わないstatic methodです。create_anonymous() は cls を受け取って個体を作るclass method、つまり別名コンストラクタです。Plant.Statistics は各Plantが内部に1個持つ部品で、grow /age / show の呼び出し回数を記録します。Treeは統計表示をオーバーライドしてshade回数を追加し、Seedは Flower -> Plant の継承チェーンを使います。クラス外の display_statistics() は実際の型に応じたメソッドを呼ぶため、同じ関数でFlower、Tree、Seed、Plantを扱えます。

**Cから見ると:** ここはC経験だけでは自動的に埋まらない部分です。関数ポインタよりも、「同じ呼び出しが実体の型によって別の実装へ進む」という多態性に注目します。

**確認ポイント:** show() の回数は特殊クラスでも1回だけ増やす。子show()から親show()を1回だけ呼べば自然に達成できる。

# 最後に: どこまで理解したら次へ進んでよいか

次の5点をコードを見ながら説明できれば、これらの課題に長く留まる必要はありません。

1. input() はstrを返し、数値計算前にint()が必要。
2. rangeの終端は含まれず、Pythonはインデントでブロックを表す。
3. selfは呼び出したインスタンスで、__init__は生成直後の初期化を行う。
4. 継承先からsuper()で共通処理を再利用し、overrideで固有処理を足せる。
5. staticmethod、classmethod、通常メソッドの受け取るものの違いを言える。

とくにExercise 6を、クラス図を頭に描きながら一度だけ自分で小さく改造して（例: WaterPlantを追加する）、期待どおり統計が増えるところまで見れば十分です。
