## Line_Counter

## 概要
フォルダを指定して、そのフォルダ内にある.js .css .html .py ファイルの行数を数えてくれる。 +
出力は、指定したフォルダの中にテキストファイルで出力される。 +

check_extの中に数えてほしいファイルの拡張子を入れることでその拡張子のファイルの行数も数えられる。 +
exclude_extの中に数えてほしくないファイルの拡張子を入れることで数えるファイルから省くことができる。 +

例：
check_ext=[".css"], exclude_ext=[".map.css"]とすることで、cssのファイルの行数を数えるが.map.cssのファイルの行数は数えないことができる。（あまり使わないかも....）

## 開発環境
|||
|---|---|
|開発プラットフォーム|Visual Studio Code|
|開発言語|Python 3.10.8|

## 使用方法
main.pyをリポジトリから取ってきて、main.pyを実行。 +
ターミナルでディレクトリパスを入力し、Enterを押す。 +
成功すると入力したディレクトリパスに```count_lines.txt```が生成されている。 +
失敗すると、ターミナルに```Not exist directly.```と出力される。 +
