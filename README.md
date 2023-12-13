# SparrowTenGame

> 此文件由 HackMD 撰寫，若有排版錯誤，請移駕到此連結閱讀。
> https://hackmd.io/@poyu39/SparrowTenGame

```
1. 簡介
    本章中需要說明你專題的主要目標與功能，研究動機、以及人力分配與工作時程
2. 文獻，本章中請介紹幾個與你專題相關的作品，這些作品的功能，與你專題成品的差異等
3. 方法
    a. 你須將整個系統切割成數個子模組，並介紹子模組的主要功能、模組之間的關係及界面
    b. 說明 Client 及 Server 運作的流程
    c. 以循序圖來說明 Client 與 Server 之間訊息傳遞的流程
4. 成果，請介紹你們專題的成果
5. 結論
6. 參考文獻
```

## 成員
- 邱柏宇	D1009212	admin@poyu39.com
- 吳念澤	D1049174	matt920404@gmail.com

## 簡介
### 研究動機
藉由實作網路應用系統，進一步熟悉 Client/Server 程式在生活中如何應用，如何選擇目前所需及了解哪種網路協議可以符合當下使用場景。

### 主要目標
利用 Python 中的 Pygame 和 RPC，實作以 Client / Server 為架構的多人闖關 遊戲，遊戲目標為玩家操控 sparrow 一起合作將 sparrow 們寶貴的蛋，送至目的地，途中會遭遇各種怪物和燒腦的機關，俗話說三個臭皮匠勝過諸葛亮，遇到複雜的機關，最多可以連線 10 隻 sparrow 合作。

### 人力分配
使用 Trello，把工作進度可視化，將專案分代定、需求列表、代辦事項、進行中、完成與有些項目需要後續確認的確認，每個卡片中都有日期能與執行者，能避免混亂及工作重複。


## 文獻
> 相關的作品：[Fireboy & Watergirl](https://official-fireboy-watergirl.fandom.com/wiki/Official_Fireboy_%26_Watergirl_Wiki)、[PICO PARK](https://picoparkgame.com/en/)

### 成品的差異
森林冰火人較專注於雙人解謎與利用地圖上的機關解謎，我們希望以 PICO PARK 為目標不僅利用地圖上的機關解謎還能利用玩家手上的道具來幫助夥伴闖關，達成通關目的。


## 方法
### python 套件

#### pygame
pygame 是跨平台 Python 套件，專為電子遊戲設計。包含圖像、聲音，建立在SDL基礎上。

#### Pillow
用於處理影像相關的 Python 套件

#### Numpy
NumPy是 Python 語言的一個擴充程式庫。支援高階大規模的多維陣列與矩陣運算，此外也針對陣列運算提供大量的數學函數函式庫。


### 系統與子模組

#### 概略類別圖
![entities](https://hackmd.io/_uploads/rybhmDdV6.png)

我們以pygame主程式建立main，控制主要遊戲運行、控制更新率、及控制 debug 選項，在物件子模組中，我們先繼承Pygame中的Sprite，這是用來建立遊戲中物件的基本類別，將Sprite繼承改為後續使用方便的類別，並分別建立地圖區塊與人物物件，在制作遊戲的過程為了加快地圖開發，我們開發了地圖子模組，用來將已經畫好的地圖圖片，轉換為遊戲場景，變為地圖物件。

### Sprite 
繼承 pygame 中提供的 Sprite 型別
```
pos： 即時座標
r_pos： 上次座標
t_pos：目標座標
asset：渲染材質
rect：碰撞箱
move_hsp：移動的基礎水平速度
move_vsp：移動的基礎垂直速度
hsp：即時水平速度
vsp：即時垂直速度
```


### Player
![player_default](https://hackmd.io/_uploads/H1SiVD_4p.png)

繼承至 Sprite，玩家扮演 Sparrow （麻雀）的角色。
- `update` 函式
    - 呼叫 `move` 函式來監聽 WASD 事件來操作角色
    - 呼叫 `physics` 中的 `apply_gravity` 演算重力
    - 呼叫 `physics` 中的 `apply_friction` 演算摩擦
    - 呼叫 `physics` 中的 `check_ground` 判斷與地面關係，來決定是否可以跳躍。（避免二段跳）


### Map


### Client / Server 的運作

### non-blocking循序圖
![image](https://hackmd.io/_uploads/rysBZqXU6.png)

#### 概略循序圖
![image](https://hackmd.io/_uploads/HJ2ob9XUT.png)






#### Server
整個遊戲世界都是由 Server 去處理，包括物理碰撞、互動物件、玩家事件等等，利用 multithread 持續更新每個玩家的資料，並且傳送給 Client 需要渲染的資料。

#### Client
監聽玩家的按鍵事件，並且收集打包成封包後，傳送給 Server ，採用 non-blocking 的方式去傳送和接受，有接受到封包時，會對玩家的畫面更新。

## 成果
- [自製物理引擎 Demo](https://www.youtube.com/watch?v=qPZ0lB5t4h0)
- [鏡頭修正算法 Demo]()


## 結論
藉由本次的專題實作，更深入了解網路程式的應用，不同的應用場景間，如何選擇適合專案的網路協議，學習到許多關於遊戲設計、系統架構和開發流程的知識。在遊戲設計方面，我學會了如何設計具有新意的遊戲玩法，並結合合作元素，讓遊戲更加有趣。在系統架構方面，我學會了如何使用Client / Server模式來實現多人遊戲，並提高遊戲的流暢度。在開發流程方面，我學會了如何使用Trello來進行工作進度管理，有效避免混亂及工作重複。


## 參考文獻

> [Git 開發流程](https://wadehuanglearning.blogspot.com/2019/05/commit-commit-commit-why-what-commit.html)

> [Pygame doc](https://www.pygame.org/docs/)

