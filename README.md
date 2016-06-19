# surugayaparser

駿河屋( http://www.suruga-ya.jp/ )の商品一覧ページを簡単にスクレイピングするためのライブラリです。

## Installation

```bash
pip install git+https://github.com/takeshi0406/surugayaparser
```

## Usage

このようなコードで、簡単に商品情報を取得することができます。

デフォルト引数では、1ページ分を1秒間隔で取得する設定になっています。

```python
from surugayaparser import SurugayaParser

instance = SurugayaParser()

# 欲しい商品一覧ページのGETパラメータを設定("page="のパラメータは消しておいてください)
getparam = 'category=11010200&search_word=&adult_s=1&' +\
           'grid=t&rankBy=modificationTime%3Adescending&' +\
           'restrict[]=hendou(text)=%E6%96%B0%E5%85%A5%E8%8D%B7'
instance.set_target_url(getparam)

# 3ページ分(pages=3まで)取得する
items = instance.request_items(pages=3)
print(items)
```

このような商品情報の辞書が、リストに入って返ってきます。

```python
{
  'title': 'Silly Walkerなりのポップナンバー｡ / Silly Walker',
  'maker': 'Silly Walker',
  'price': '￥300税込',
  'link': 'http://www.suruga-ya.jp/product/detail/186101549001',
  'picture': 'http://www.suruga-ya.jp/database/photo.php?shinaban=186101549001&size=l',
  'price_teika': None
}
```

