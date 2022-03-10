"""
    タイトルと文章を入力すると
    HTMLタグとして画面に出力するプログラム
"""
 
# タイトルと文章を入力
title = input("タイトルは？ ")
naiyo = input("内容は？ ")
 
# HTML生成
html = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>{}</title>
    </head>
    <body>
        <h1>{}</h1>
        <p>{}</p>
    </body>
</html>
"""
 
# 画面出力
print(html.format(title, title, naiyo))