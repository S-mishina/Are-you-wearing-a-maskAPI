# Are-you-wearing-a-maskAPI
Yoloのデータを可視化する為のテストプログラム.<br>
詳細には,ストームを利用したsocket通信のテスト用プログラムになります.<br>
実行方法.
一つ目のターミナルで,<br>
$python server.py<br>
二つ目のターミナルで<br>
$python client.py<br>
# データベースの構成
databasename:mask<br>
table:mask-ok-or-ng1<br>
カラム:3<br>
|name      |format 
|:----------|-----:|
|day       | day   | 
|time      | time  | 
|ok-or-ng  | text  | 

Are-you-wearing-a-mask側でマスクを検知するとsqlok()を実行<br>
ngだとsqlng()を実行する.
# 音声の出力
Are-you-wearing-a-mask側でマスクを検知するとok.wavを再生<br>
ngだとnomask.wavを再生する.
