## Write VMD data
Vocaloid Motion Data (.vmd) ファイルへ、データを書き込む Python スクリプト。

<br>

### Usage
`vmdwritefunctions.py` で定義されている各関数を使用します。

```python
with open("converted.vmd", "wb") as result:
    # Header
    header = VMD_HEADER("Vocaloid Motion Data 0002", "Some model")
    writeheader(result, header)

    # Motion Data Count
    motioncount = VMD_MOTION_COUNT(0)
    writemotioncount(result, motioncount)
```

<br>

### Sample
サンプルとして、fbx形式のシェイプキーアニメーションを vmd形式に変換するスクリプト `fbxshapetovmd.py` を用意しました。引数の `mesh name` には、シェイプキーアニメーションを含むメッシュの名前を一つ指定してください。

```bash
python fbxshapetovmd.py <fbx filepath> <mesh name>
```



<br>

### Note
- vmd ファイルの仕様は、t_tetosuki様の [ブログ](https://blog.goo.ne.jp/torisu_tetosuki/e/bc9f1c4d597341b394bd02b64597499d) から拝借しました

- `vmd.py` については、別リポジトリ [Output_vmd_data](https://github.com/Ndgt/Output_vmd_data) のソースと同じものです
