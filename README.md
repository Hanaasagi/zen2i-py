# zen2i-py

兆までの漢数字を半角数字に変換します。 漢数字が続いていたらそれぞれ変換します。

**This project was inspired by [yoshitsugu/zen_to_i](https://github.com/yoshitsugu/zen_to_i)**

### Usage

```Python
In [1]: zen2i('hoge')
Out[1]: 'hoge'

In [2]: zen2i('一二三')
Out[2]: '123'

In [3]: zen2i('百三')
Out[3]: '103'

In [4]: zen2i('三兆五十二万四十八')
Out[4]: '3000000520048'
```

### License
MIT
