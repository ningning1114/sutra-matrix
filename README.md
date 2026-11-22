# 佛經字雨 · Sutra Matrix

在終端機中播放佛經漢字瀑布。黑色背景、象牙白字流，透過遠、中、近三層的亮度、速度與長度變化呈現景深。

內建《心經》《觀無量壽經》《金剛經》《大勢至菩薩念佛圓通章》《阿彌陀經》，也可載入自己的文字檔。字元隨機排列，不依經文順序，適合作為視覺動畫。

## 下載與執行

需要 Python 3.9 以上，以及支援 UTF-8、中文和色彩的終端機。macOS／Linux 使用 Python 標準函式庫，不需安裝額外 Python 套件或 cmatrix。Windows 可在 WSL 環境中使用；不支援原生 Windows Python。

在專案頁面點選 **Code → Download ZIP**，解壓縮後，在終端機進入解壓縮的資料夾，執行：

```sh
python3 sutra_matrix.py
```

macOS 使用者可先在終端機輸入 `cd `（後面留一個空格），將解壓縮後的資料夾拖進終端機，再按 Enter。

也可以使用 Git 下載：

```sh
git clone https://github.com/ningning1114/sutra-matrix.git
cd sutra-matrix
python3 sutra_matrix.py
```

## 操作

| 按鍵 | 功能 |
| --- | --- |
| `q` / `Esc` / `Ctrl+C` | 離開 |
| 空白鍵 | 暫停／繼續 |
| `+` / `-` | 加速／減速 |

## 選擇經文

預設播放《心經》。其他版本可用中文名稱啟動：

```sh
python3 sutra_matrix.py --sutra 觀無量壽經
python3 sutra_matrix.py --sutra 金剛經
python3 sutra_matrix.py --sutra 大勢至菩薩念佛圓通章
python3 sutra_matrix.py --sutra 阿彌陀經
```

每次執行一行。按 `q` 退出後，再執行另一部經的命令即可切換。

| 中文名稱 | 英文代號 |
| --- | --- |
| 心經 | `heart` |
| 觀無量壽經 | `contemplation` |
| 金剛經 | `diamond` |
| 大勢至菩薩念佛圓通章 | `mahasthamaprapta` |
| 阿彌陀經 | `amitabha` |

`--sutra` 同樣接受英文代號。用 `python3 sutra_matrix.py --list` 查看內建版本。

## 色調、速度與密度

預設象牙白（`ivory`）、速度倍率 `2`、欄位密度 `1`。可將以下選項與 `--sutra` 搭配使用：

```sh
# 青綠色
python3 sutra_matrix.py --theme teal

# 經典綠色
python3 sutra_matrix.py --theme green

# 稀疏、緩慢
python3 sutra_matrix.py --density 0.55 --speed 0.7

# 保持全部欄位、加快速度
python3 sutra_matrix.py --density 1 --speed 3
```

`--density` 範圍為 0.1–1，控制啟用欄位的比例。每束字流之間仍保留黑色間隔。`--speed` 範圍為 0.1–5。調整視窗大小時，字流會重新分配。

使用 256 色終端機可呈現六層明暗。可在終端機設定中調整字型與字級；所有漢字使用相同字級。黑色背景與關閉透明度可讓字流更清晰。

## 自訂文字

將經文存為 UTF-8 純文字檔，再指定路徑：

```sh
python3 sutra_matrix.py --text "我的經文.txt"
```

`--text` 與 `--sutra` 擇一使用。程式只抽取漢字，略過標點與空白；原文出現較多次的字也較容易被抽中。罕見字是否能顯示，取決於終端機字型。

## 相容性

已在 macOS 偽終端機測試五種經文的啟動、輸出與自動退出。Linux／WSL 尚未完成實機測試。只有基本色的終端機會使用簡化配色。

若出現 `python3: command not found`，請先安裝 Python 3；若出現方框或字元錯位，請確認終端機使用 UTF-8，並選擇支援中文的字型。

## 來源與授權

- 程式碼與專案說明採用 [MIT License](LICENSE)。本專案為獨立 Python 實作，視覺靈感來自 cmatrix。
- 經文電子資料取自 CBETA 電子佛典集成 Version 2026.R2，另適用來源資料的使用條件，不包含於程式碼的 MIT 授權。完整來源與擷取範圍見 [NOTICE.md](NOTICE.md)。
