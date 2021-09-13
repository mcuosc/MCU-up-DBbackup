# MCU-up-DBbackup

事前準備
---
1. clone專案
```
git clone https://github.com/mcuosc/MCU-up-DBbackup.git
```
2. 安裝套件
```
pip install -r requirments.txt
```

建立流程
---
1. 建立`.env`檔，填入相應資訊
2. 執行`docker -t backup .`
3. 執行`docker run -d --name backup backup`


