import cv2

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread('./input.jpg')

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
cv2.imwrite('./outputA.jpg', img)

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
####################################
# 第三引数(任意) : リスト型にてパラメータを指定する。
# cv2.IMWRITE_JPEG_QUALITY : JPEG画像の場合に、画像の品質を変更するもの。0から100までの値を設定でき、品質を変更できます（値が高いほど良い）。 デフォルト値は95。
####################################
# ※ JPEG画像は非可逆圧縮なので、元画像と保存した画像とでは画素値が異なります。元の画像をそのまま保存したい場合は、PNGやBMPなどで保存することをおすすめします。
# 画素値とは? : https://algorithm.joho.info/image-processing/digital-imaging/
# 非可逆圧縮とは? : https://e-words.jp/w/%E9%9D%9E%E5%8F%AF%E9%80%86%E5%9C%A7%E7%B8%AE.html#:~:text=%E9%9D%9E%E5%8F%AF%E9%80%86%E5%9C%A7%E7%B8%AE%E3%81%A8%E3%81%AF,%E5%AE%8C%E5%85%A8%E3%81%AB%E3%81%AF%E4%B8%80%E8%87%B4%E3%81%97%E3%81%AA%E3%81%84%E3%80%82
cv2.imwrite('./outputB.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 10])
