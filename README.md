# apkTW網頁自動簽到
運用windows工作排程器執行自動簽到動作
![image](https://user-images.githubusercontent.com/87114199/125604512-070404ad-102c-42d7-aaf2-f8ff0d4b1cbe.png)
## 需求
1.python虛擬環境(使用anaconda3安裝環境)  
![image](https://user-images.githubusercontent.com/87114199/125605533-e36c9a3e-61e3-4870-8043-5533f4cfd113.png)
2.Python selenium安裝(python環境下安裝)  
3.chromedriver驅動(依照chrome版本選擇)  
![image](https://user-images.githubusercontent.com/87114199/125605663-04c75498-7f3c-4010-bbcc-308d530f8d47.png)

## 步驟
### step 1 anaconda3
下載anaconda並完成安裝，記得在advanced options將Add Anaconda3 to my PATH environment variable選項打勾
![image](https://user-images.githubusercontent.com/87114199/125606264-b26831d8-fa2b-465a-8bf4-f75417d06071.png)
### step 2 python虛擬環境  
打開CMD創建一個python虛擬環境  
輸入指令:conda create --name myenv  
myenv可以改成自己想要的名字  
Proceed ([y]/n)?輸入y後按enter即可  
![image](https://user-images.githubusercontent.com/87114199/125607004-a7d44b49-91d3-449a-b180-057b555f67be.png)  
  
開啟anaconda檢查Applications on是否有myenv  
![image](https://user-images.githubusercontent.com/87114199/125608248-7822c22f-0890-4c66-ab08-22e928b971c6.png)  
  
選擇myenv並且安裝jupyter notebook，安裝完畢後執行  
![image](https://user-images.githubusercontent.com/87114199/125608339-d023dc7f-c312-4826-b5b9-d5b94bec5e67.png)  
### step 3 selenium安裝  
啟動myenv虛擬環境
輸入指令:conda activate myenv
![image](https://user-images.githubusercontent.com/87114199/125607453-5daf6f99-b8f7-4bc2-9af8-2bbe6c35eb63.png)  
安裝selenium
輸入指令:pip install selenium
![image](https://user-images.githubusercontent.com/87114199/125607631-d478d1a1-9a70-42f3-b113-0f3cb3c9f6df.png)  
### step 4 chromedriver
下載chromedriver並解壓縮  
將chromedriver.exe檔案移至虛擬環境的scripts資料夾  
<img width="773" alt="螢幕擷取畫面 2021-07-14 183807" src="https://user-images.githubusercontent.com/87114199/125608747-ffe21471-2d99-4619-97b4-41742e2c8897.png">  
### step 5 下載腳本並設定帳密
將apkTW.py及autoSign.bat下載並移至虛擬環境的scripts資料夾  
![image](https://user-images.githubusercontent.com/87114199/125609249-d3549c55-aaf5-4441-a295-62e06c5ba2ba.png)  
  
以記事本開啟apkTW.py，將userName = "XXXX"的XXXX改成帳號，將userPassword = "zzzz"的zzzz改成密碼，完成後儲存
![image](https://user-images.githubusercontent.com/87114199/125612469-d452050c-d65b-440f-9a96-59e79d3c3010.png)
![image](https://user-images.githubusercontent.com/87114199/125612519-7cd0ca92-0947-409b-af06-f9b39a4630f3.png)  
  
以記事本開啟autoSign.bat，將路徑改成你的路徑，圈起來的都要改  
<img width="787" alt="螢幕擷取畫面 2021-07-14 191437" src="https://user-images.githubusercontent.com/87114199/125613208-ea6af868-ab63-4ea7-81a9-a5a84daa7205.png">  

### step 6 工作排程器設定
windows搜尋欄搜尋工作排程器並開啟  
  
右邊動左點選建立工作  
![image](https://user-images.githubusercontent.com/87114199/125609716-bedcef37-e683-4992-a001-e8b4352e2eaa.png)  
  
名稱自訂，記得勾選以最高權限執行  
<img width="476" alt="螢幕擷取畫面 2021-07-14 184758" src="https://user-images.githubusercontent.com/87114199/125609903-88d532da-c69f-4387-bf8c-4620f629d23e.png">  
  
觸發程序按下新增，勾選每天  
![image](https://user-images.githubusercontent.com/87114199/125610024-ead23d5e-b086-461b-953c-b7a481fb28e2.png)
  
動作區按下新增，瀏覽至myenv環境下的scripts選擇autoSign.bat，按下確定  
<img width="812" alt="螢幕擷取畫面 2021-07-14 185323" src="https://user-images.githubusercontent.com/87114199/125610571-7f382a90-0d78-43e6-abb6-1d58f0f41840.png">

## 完成
  


