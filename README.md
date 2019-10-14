# ddtree

fantastic dodekamin tree project  
触ったことあるからっていうだけでDjango使うことにしたけど、  
この小ささの規模で書くならもっと適した言語や方法がある気がしてならない、  
が、とりあえずこれで進めていく  

## 重要なファイルたち

`static`: CSS,JS,画像などが入るらしい </br>
`templates`: 中には見た目(htmlファイル)が入っている。viewsから動的な値を受け取って返される </br>
（`pika`: メインのアプリ） </br>
`pika/urls.py`: ルーティングについて（ほぼ直接viewsに渡してるからあまり関係ない） </br>
`pika/views.py`: ロジックが書いてある。大体の処理はここで書いている </br>
`pika/models.py`: DBのモデルが書いてある </br>
