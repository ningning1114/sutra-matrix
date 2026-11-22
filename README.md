# 佛經字雨 · Sutra Matrix

以佛經漢字呈現 cmatrix 風格的終端機字雨。分束落下的佛經漢字瀑布，保留黑色留白。遠景暗而慢、中景柔和、近景明亮而快，以三層速度與明暗營造景深。預設象牙白色、密度 1、速度 2。

獨立 Python 實作，沒有使用 cmatrix 原始碼，也不需要安裝 cmatrix。中文字佔兩格，整體風格接近 cmatrix；字型與實際顏色由終端機決定。

## 執行

需要 Python 3.9 以上、支援 UTF-8／中文與色彩的終端機。macOS / Linux 使用 Python 標準函式庫，不必 pip 安裝套件。Windows 請在 WSL 裡執行；原生 Windows Python 不在支援範圍。

下載專案 ZIP 並解壓縮，開啟終端機，輸入 `cd `（後面留一個空格），把專案資料夾拖進終端機，再按 Enter。接著執行：

```sh
python3 sutra_matrix.py
```

macOS 也附有 `start.command`。若下載後雙擊無法開啟，使用上述終端機方式即可。

視覺效果以黑色背景、關閉透明度的終端機為佳；可全螢幕並縮小字體，增加字雨的層次。畫面不顯示工具列或說明。

| 按鍵 | 功能 |
| --- | --- |
| `q` / `Esc` | 離開 |
| 空白鍵 | 暫停／繼續 |
| `+` / `-` | 加速／減速 |
| `Ctrl+C` | 離開 |

較稀疏、緩慢：

```sh
python3 sutra_matrix.py --density 0.55 --speed 0.7
```

較密集、快速：

```sh
python3 sutra_matrix.py --density 1 --speed 3
```

`--density` 設定啟用欄位的比例（0.1–1），不是畫面填滿比例。每束字流之間有黑色間隔，不會鋪滿暗字背景。`--speed` 為 0.1–5。視窗大小改變時會重新分配字雨。

## 參考圖風格與色調

預設為象牙白色，亮字與灰暗尾跡形成前後層次：

```sh
python3 sutra_matrix.py
```

青綠色版本：

```sh
python3 sutra_matrix.py --theme teal
```

經典綠色：

```sh
python3 sutra_matrix.py --theme green
```

字流分為遠、中、近三層，亮度、速度與長度不同；每束落完後會留出空白再出現。背景保持純黑，沒有滿版文字底層。使用 256 色終端機呈現六層明暗；只有基本色的終端機會降級顯示。終端機格線限制每個漢字大小相同，無法重現參考圖片的大小變化與書法字形；字型可自行在終端機偏好設定中調整。

## 選擇經文版本

所有版本預設象牙白、三層景深、密度 1、速度 2；只更換隨機抽字的經文來源。

| 版本 | 啟動命令 |
| --- | --- |
| 心經 | `python3 sutra_matrix.py` |
| 觀無量壽經 | `python3 sutra_matrix.py --sutra contemplation` |
| 金剛經 | `python3 sutra_matrix.py --sutra diamond` |
| 大勢至菩薩念佛圓通章 | `python3 sutra_matrix.py --sutra mahasthamaprapta` |
| 阿彌陀經 | `python3 sutra_matrix.py --sutra amitabha` |

也接受表格中的中文名稱，例如：

```sh
python3 sutra_matrix.py --sutra 金剛經
python3 sutra_matrix.py --sutra 大勢至菩薩念佛圓通章
```

按 `q` 退出後，再輸入另一部經的命令即可切換。用 `python3 sutra_matrix.py --list` 查看全部版本。色調、速度和密度參數可以與 `--sutra` 搭配使用。

## 更換經文

將經文存成 UTF-8 純文字檔，再指定路徑：

```sh
python3 sutra_matrix.py --text "我的經文.txt"
```

只取漢字，略過標點與空白；隨機抽字，不依經文順序，也不是誦讀模式。字元出現頻率會受到原文出現次數影響。請使用終端機字型能顯示的漢字，罕見字可能顯示為方框。

## 放上自己的 GitHub

1. 登入 GitHub，建立名稱為 `sutra-matrix` 的空儲存庫。不要預先新增 README、License 或 .gitignore，本專案已附上。
2. 在本專案資料夾的終端機執行以下命令，把 `ningning1114` 換成你的帳號：

```sh
git init -b main
git add .
git commit -m "Initial release of Sutra Matrix"
git remote add origin https://github.com/ningning1114/sutra-matrix.git
git push -u origin main
```

推送前需完成 GitHub 的命令列驗證。HTTPS 請使用 GitHub 支援的驗證方式，例如 personal access token，不是帳號密碼。若 Git 要求作者資料，先依提示設定 `user.name` 與 `user.email`，再重試 commit。

不使用 Git 命令，也可在 GitHub 網頁建立儲存庫後，以「uploading an existing file」或「Add file → Upload files」上傳專案內的檔案（不是 ZIP）。

官方說明：[將本機程式碼加入 GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)。

公開後，其他人可以下載 ZIP，或將下方帳號換成你的 GitHub 帳號：

```sh
git clone https://github.com/ningning1114/sutra-matrix.git
cd sutra-matrix
python3 sutra_matrix.py
```

## 來源與授權

- 程式碼與本專案說明：MIT License，見 `LICENSE`。
- 五種經文取自 CBETA 電子佛典集成 Version 2026.R2 的 PDF 正文，來源與擷取範圍見 `NOTICE.md`。經文電子資料不包含於程式碼的 MIT 授權。
- 視覺靈感來自 cmatrix；本專案與 cmatrix 無隸屬關係。

## 驗證範圍

已在 macOS 的偽終端機做啟動、輸出與自動退出測試。實際字型呈現仍依使用者終端機而異；Linux／WSL 尚未做實機測試。
