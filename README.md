＃study_python  
速習 python3 による学習の記録

# オブジェクトとメソッド
**オブジェクト**  = データの塊+処理  
オブジェクトはメモリ上に存在し、変数はそのメモリを参照しているだけなので同一のオブジェクトを持っているという点に注意する  
同一のメモリを参照している変数Aと変数Bのどちらかを更新しようとして意図しない動きをするトラブルが発生する

## オブジェクトの属性の確認
dirで属性(メソッド）の確認ができる

## テキスト処理
in = 存在の確認  
find = 位置の確認  

text = 'hello world python'  
* 'wor' in text  -> True  
* 'w0r' in text -> False  
* text.find('w0r') ->-1  
* text.find('o') -> 4  

__startswith(最初が一致),endswith(最後が一致),rfind(右から検索）__

## 文字列の生成
+でも文字の生成はできるが、Pythonはformat目祖度を主流としていく  

これが一番好き  

* print('{ user} : {age}'. format( user =' taro', age = 35))  
#taro : 35  
  
formatはVBとかのFormat見たいにも使える  
右寄せするときとか0埋めの例  
* print('{:5}'.format(50))  -> '&nbsp;&nbsp;&nbsp;50'  
* print('{:5}'.format(123)) -> '&nbsp;&nbsp;123'  
* print('{:.5}.format(50)) -> '00050'  

位置情報、キーワードとの併用  
* print('{ab:05} {cd:05}'.format(ab=50,cd=255))  
#'00050 00255'

整数型の表示の調整
* print('{:d}, {:f}'.format(5,5.5))  
#'5, 5.500000'
* print('{:.3f},{:.5f}.fomat(5.5,5.5))  
#'5.500, 5.50000'
* print('{:,}, {:10,}, {:010,}'.format(111111,111111,111111))  
#'111,111,   111,111, 00,111,111'
* print('{0:b}, {0:o}, {0:d}, {0:x}'.format(100))  
#'1100100, 144, 100, 64'

書式化演算子(%)  
* text = 'hello %s' % 'HELLO'  
#hello HELLO
* text= 'hello %s python %s' % ('HELLO',1)  
#hello HELLO python 1
