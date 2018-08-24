# zen2i-py

兆までの漢数字を半角数字に変換します。 漢数字が続いていたらそれぞれ変換します。

**This project is inspired by [yoshitsugu/zen_to_i](https://github.com/yoshitsugu/zen_to_i), only working in Python 3.6 and above**

### Install

```Bash
pip install git+https://github.com/Hanaasagi/zen2i-py.git
```

### Usage

```Python
In [1]: from zen2i import zen2i

In [2]: zen2i('hoge')
Out[2]: 'hoge'

In [3]: zen2i('一二三')
Out[3]: '123'

In [4]: zen2i('百三')
Out[4]: '103'

In [5]: zen2i('三兆五十二万四十八')
Out[5]: '3000000520048'
```

### License
MIT
