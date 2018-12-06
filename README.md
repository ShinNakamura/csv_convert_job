# What is this? #

業務上必要になったので作ったプログラム

項目なしのCSVに項目を指定する設定を与えて、項目ありのCSVで出力する


## サンプル ##

* このようにデータだけが並んでいるCSVがある

data.csv
```
"red","15mm","seamaster"
"Omega","John","15-00-9"
```

* 何行目の何列目が何(項目名)なのかを設定ファイル(CSV)に書く

config.csv
```
row,column,name
1,1,color
1,2,size
1,3,brand
2,1,company
2,2,person
2,3,orderNum
```

* 上記2つを元に下記のようなCSVを出す

out.csv
```
color,size,brand,company,person,orderNum
red,15mm,seamaster,Omega,John,15-00-9
```


## Usage ##

```sh
python3 conv.py config.csv data.csv >out.csv
```

* 各CSVは全て UTF-8 (LF) である前提
