
## 第一章

### 1.  回文数

- 来源： leetcode 9
- 题目： 给定一个整数，判断该数是否为回文数？

- 思路1： 先转化为字符串，然后遍历对比首尾字符， 时间复杂度为O(n)，它的边界条件会很恶心

### 2.  两数之和
- 来源：**leetcode 1**
- 题目： 给定一个数组arr， 一个整数aim， 请返回哪两个位置的数可以加出aim来。
- 举例： arr = [2, 7, 11, 15], target = 9. 返回 [0, 1]

- 思路1： 先排序， 然后用两个指针（头，尾）依次遍历， 但是由于要返回下标， 因此还需要记录每个元素下标的位置。-- 最佳方法
- 思路2： 采用哈希表{num:下标}， 依次遍历数组，查看 target - nums[i] 有没有出现过

- **引申1**： 给定一个有重复数字的数组arr， 一个整数target， 返回所有两个数和为target的数
- 思路： 依旧先排序， 然后维护一个pre_left, pre_right， 来避免输出重复数组

- **引申2**： 三数之和： 给定一个包含n个整数的数组nums， 判断nums中是否存在三个元素，使得 a + b + c = 0， 找出所有满足条件且不重复的三元组。
- 要求： 答案中不包含重复的三元组
-  类似：**leetcode 15**
- 思路：先固定第一个数nums[i]， 然后判断后续的数之和能不能 == target-nums[i]。 需要注意的是为了排除重复三元组，需要维护pre_num, pre_left, pre_right 三个数据。


### 3.  链表调整

给定一个链表list，
如果：
list = 1 调整之后1。
list = 1->2 调整之后1->2
list = 1->2->3 调整之后1->2->3
list = 1->2->3->4 调整之后1->3->2->4
list = 1->2->3->4->5 调整之后1->3->2->4->5
list = 1->2->3->4->5->6 调整之后1->4->2->5->3->6
list = 1->2->3->4->5->6->7 调整之后1->4->2->5->3->6->7
根据上面的规律，调整一个任意长度的链表。

- 思路1： 先将链表转化为数组，然后调整，最后再重新连接成链表。 调整的规律需要探索发现

### 4. 搜索二叉树->有序链表

- 题目： 把一棵搜索二叉树，转化成有序的双向链表。
无权限 leetcode 426


### 5. 

- 题目： **给定数组arr和整数num，共返回有多少个子数组满足如下情况：max(arr[i..j]) - min(arr[i..j]) <= num**

- 要求： 时间复杂度为O(n)

- 思路： 滑动窗口思路， 采用两个双端序列， 一个最大值双端序列，一个最小值双端序列分别记录滑动窗口的最大值和最小值。




### 6. 单词接龙 2
- 来源： **leetcode 126**
- 题目： 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
> - 每次转换只能改变一个字母。
> - 转换过程中的中间单词必须是字典中的单词。

- 说明:
> - 如果不存在这样的转换序列，返回一个空列表。
> - 所有单词具有相同的长度。
> - 所有单词只由小写字母组成。
> - 字典中不存在重复的单词。
> - 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

- 举例：
```
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
```

- 思路：
  > - 第一步： 采用一个hashmap来存储所有单词的邻居{word:[neibors]}
  > - 第二步： 采用宽度优先遍历，设置每个word 到 beginword(0) 的距离


### 7. 最近回文数

- 来源：**leetcode 564**
- 题目: 给定一个整数 n ，你需要找到与它最近的回文数（不包括自身）。“最近的”定义为两个整数差的绝对值最小。
- 说明1：n 是由字符串表示的正整数，其长度不超过18。
- 说明2：如果有多个结果，返回最小的那个。

- 思路： 找到比它大的离它最近的数， 再找到比它小的离它最近的数。
  > - 比它大： 

--- 

## 第二章

### 1. 丑数 2
- 来源：**leetcode 264**
- 题目：编写一个程序，找出第 n 个丑数。丑数就是**只包含**质因数 2, 3, 5 的正整数。假设1是第一个丑数。

- 举例： n = 10, 输出12 （1, 2, 3, 4, 5, 6, 8, 9, 10, 12)
- 思路1： 从1开始试， 判断每一个数是否为丑数
- 思路2： 第i 个丑数 = 0-i-1个丑数中某三个数 *2， *3， *5 中最小的那个得到的

### 2. 回文对

- 来源： leetcode 336
- 题目：给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

- 思路： 
> - 第一步： 
> - 第二步：
> - 第三步：


### 4.  字母异位词分组

- 来源： leetcode 49
- 题目： 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
- 思路1： 先对每个字符串排序， 然后再进行分组， 采用hashmap来帮助存储
- 思路2： 对每个字符串查看a-z这些字符分别出现了多少次， 然后以此连接， 如"abcd" 就用"1_1_1_1_0_0_..."来表示， 然后用hashmap存储。


### 5.  矩阵中的最长递增路径

- 来源：** leetcode 329**
- 题目：给定一个整数矩阵，找出最长递增路径的长度。对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
```
输入: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
输出: 4 
解释: 最长递增路径为 [1, 2, 6, 9]。
```

### 6. 路径交叉

- 来源： **leetcode 335**
- 题目： 给定一个含有 n 个正数的数组 x。从点 (0,0) 开始，先向北（上）移动 x[0] 米，然后向西（左）移动 x[1] 米，向南（下）移动 x[2] 米，向东（右）移动 x[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。

- 要求：编写一个 O(1) 空间复杂度的一趟扫描算法，判断你所经过的路径是否相交。

---

## 第三章

### 1. 将有序数组转换为二叉搜索树

- 来源： leetcode 108
- 题目： 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

```
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
```

### 2. 二叉树的序列化与反序列化

- 来源： leetcode 297
- 题目： 请设计一个算法来实现二叉树的序列化与反序列化。
- 要求： 采用先序，层序的方法分别进行序列化

### 3. 字符串转化为整数

- 来源： leetcode 8
- 注意： 边界条件很多


### 4. 跳跃游戏

- 来源：leetcode 55 -- can_jump
- 来源：leetcode 45 -- jump， 要求： 时间复杂度为O(N)， 空间复杂度为O(1)


### 5. 


### 6. 斐波那契数列问题

**需要熟练动态规划**

---

## 第四章

### 1. 只用位运算不用算术运算实现整数的加减乘除运算

- 题目：给定两个32位整数a和b，可正、可负、可0。不能使用算术运算符，分别实现a和b的加减乘除运算。
- 要求：如果给定的a和b执行加减乘除的某些结果本来就会导致数据的溢出，那么你实现的函数不必对那些结果负责

- 思路：跳过了

### 2. 调整[0,x) 的数出现的概率

- 假设函数Math.random()等概率随机返回一个在[0,1)范围上的数，那么我们知道，在[0,x)区间上的数出现的概率为x
（0<x≤1）。给定一个大于0的整数k，并且可以使用Math.random()函数，请实现一个函数依然返回在[0,1)范围上的数，但是在[0,x)区间上的数出现的概率为xk(0<x≤1)。

- 思路： 进行k次 Math.random()， 并取大的那个返回。

### 3. 根据后序数组重建搜索二叉树

- 题目1： 给定一个整型数组arr，已知其中没有重复值，判断arr是否可能是节点值类型为整型的搜索二叉树后序遍历的结果。
- 引申题目：如果整型数组arr中没有重复值，且已知是一棵搜索二叉树的后序遍历结果，通过数组arr重构二叉树。

### 4. 打印N个数组整体最大的Top k

- 问题：有N个长度不一的数组，所有的数组都是有序的，请从大到小打印这N个数组整体最大的前K个数。
- 思路1： 对每行准备一个指针，则找到前k个数的时间复杂度为 O(nk), 且边界问题很复杂
- 思路2： 采用长度为N的堆来实现


### 5. 最大正方形

- 来源： leetcode 221
- 题目：在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

```
输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
```



### 6. 数组中未出现最小正整数

- 来源：** leetcode 41**
- 题目： 给定一个无序整型数组arr，找到数组中未出现的最小正整数。
- 要求： 时间复杂度O(n)， 空间复杂度O(1)
- 思路：主要是边界问题


## 第五章

### 1.  括号配对
- 问题：爱编程的小易发现，当自己代码中的括号较多时，如果括号未成对出现，或者出现的顺序错误，他的编辑器 总是能立马给出错误提示。好奇的小易决定自己尝试实现该功能。 对于一行代码(字符串)，里面可能出现大括号"{}"、中括号"[]"和小括号"()"，请编程判断该行代码的括号嵌 套是否正确。

- 举例："()","({})","print ('Hello Netease')"等都是括号的正确使用方法，"(]","print (Hello Netease]"则是错误的范例

- 思路： 采用栈， 遇到 '(', '[', "{" 就压栈， 遇到 "}", "]", ")" 就出栈比对。 其余一律忽略。

### 2. 卡牌游戏

- 问题：某游戏是一个卡牌类游戏，玩家通过战斗或抽牌可以拿到一些技能牌，每张技能牌都有对应的伤害值(伤 害值>=0)，当你有了组合技属性之后，你可以在自己手头上选择任意张技能牌，以组合技的方式来攻击 boss，组合技的总伤害将等于所组合的各张技能牌的伤害值的乘积(只有一张牌时，组合技伤害值等于这张牌 本身的伤害值)，但是能发动组合技必须有个前提:所有被选择的技能牌的伤害系数之和必须等于m(m>0) 以解开封印;
你为了能赢得最终胜利，需要在所有技能牌中挑出若干张技能牌触发组合技(每张牌只能用一 次)，以形成最大威力的组合技攻击效果。 

- 例如:你有伤害值分别为1,2,3,4,5的五张牌，给定的解开封印的阈值(m)为10，那形成最大组合攻击效果 的组合为30(5*3*2)，而不是24(4*3*2*1)，也不是20(5*4*1)，需要输出的结果即30。

- 思路1： 采用回溯法， 但是可能通不过
- 思路2： 将回溯改为动态规划

### 3. 屠龙

- 问题：你的王国里有n条龙，你希望雇佣一些勇士把它们杀死，王国里一共有m个骑士可以雇佣。假定，一个能力值 为x的骑士可以打败战斗力不超过x的恶龙，且需要支付x个金币。已知勇士可以重复雇佣，且重复雇佣需要重 复支付金币，请求出打败所有的恶龙需要的最小金币数目。
- 举例： knights = [1, 5, 10], dragons = [3, 8, 6]
- 思路：

- 引申题目：**如果一条龙可以被勇士合力杀死，求付出的金币数**
- 思路： 采用动态规划来做

### 4. 压缩字符串

- 题目：某位程序想出了一个压缩字符串的方法，压缩后的字符串如下:3{a}2{bc}，3{a2{c}}，2{abc}3{cd}ef，现在 需要你写一个解压的程序，还原原始的字符串。如: s = "3{d}2{bc}", return"dddbcbc". s = "3{a2{d}}", return "addaddadd". s ="2{efg}3{cd}ef", return "efgefgcdcdcdef". 重复次数可以确保是一个正整数。

- 思路：用栈或递归做， 注意理清边界

### 5.  组成种数

- **题目**：给定一个只由0（假）、1(真)、&(逻辑与)、|（逻辑或）和^(异或)五种字符组成的字符串express，再给定一个布尔值desired。返回express能有多少种组合方式，可以达到 desired的结果。

- 举例： express="1^0|0|1"，desired=false： 只有1^((0|0)|1)和1^(0|(0|1))的组合可以得到false，返回2。

- 思路：首先判断字符是否有效


### 6. 完美矩形

- 来源：**leetcode 391**

---

## 第六章

### 1. 最大子序和

- 来源：**leetcode 53**
- 思路：动态规划

- 引申题目：15年阿里原题：给定一个数组arr，返回两个不相容子数组的最大累加和。
- 举例：两个数组，
  > - 数组1 记录[:i+1](i=0, ..., n-1) 这个子数组中的最大子数组和
  > - 数组2记录[i:n](i = n-1, ..., 0)这个子数组中的最大子数组和
  > - 两个数组对应相加，返回最大的那个（意义就是以i为划分时，左边的最大子数组和与右边的最大子数组和 )

### 2. 子矩阵的最大累加和问题

类似： leetcode 363
- **问题：给定一个矩阵matrix，其中的值有正、有负、有0，返回子矩阵的最大累加和。**
- 举例：

```
-90 48 78
64 -40 64
-81 -7 66
其中，最大累加和的子矩阵为：
48 78
-40 64
-7 66
所以返回累加和209。
```

### 3. 子数组最大累乘积

- 类似： **leetocede 152**
- 题目：给定一个double类型的数组arr，其中的元素可正、可负、可0，返回子数组累乘的最大乘积。
- 例如，arr=[-2.5，4，0，3，0.5，8，-1]，子数组[3，0.5，8]累乘可以获得最大的乘积12，所以返回12。
- 思路：

### 4. 最大矩形

- 来源： **leetcode 85**

### 5. 分割回文串 II

- 来源： leetcode 132
- 思路： 动态规划

### 6. 画匠问题

- 题目：给定一个整型数组arr，数组中的每个值都为正数，表示完成一幅画作需要的时间，再给
定一个整数num表示画匠的数量，每个画匠只能画连在一起的画作。所有的画家并行工作，请返回完成所有的画作需要的最少时间。

- 举例： arr=[3,1,4]，num=2。最好的分配方式为第一个画匠画3和1，所需时间为4。第二个画匠画4，所需时间为4。因为并行工作，所以最少时间为4。如果分配方式为第一个画匠画3，所需时间为3。第二个画匠画1和4，所需的时间为5。那么最少时间为5，显然没有第一种分配方式好。所
以返回4。

- 思路：将arr划分为num块(num-1切分)， 使得每块之间的差值最小

### 7. 正则表达式匹配

- 来源： leetcode 10
- 思路： 动态规划


## 第七章

### 1. 扰乱字符串

- 来源： leetcode 87


### 2. 平衡二叉树
 
- 来源： leetcode 110  ， leetcode 98

> - 第一步：分析可能性
> - 第二步： 根据可能性找出需要的返回值
> - 第三步：默认左树，右树均满足信息
> - 第四步： 如何根据左树，右树返回值决策
> - 第五步： 返回需要的信息

### 3. 最大搜索二叉子树

- 给定一棵二叉树的头节点head，已知所有节点的值都不一样，求最大的搜索二叉子树的节点数量。


### 4. 

### 5.  二叉树最大距离

- 题目：二叉树中由节点a往上或者往下走到节点b，最短路径上节点的数量叫做a到b的距离。给定一棵二叉树的头节点head，求整棵树中的最大距离。


---

## 第八章

### 1. 完美洗牌问题

- 问题： 有一个长度为偶数的数组arr，左边一半叫做左半区，右边一半叫做右半区。记为：[L1,L2,...,LK,R1,R2,...,RK]，请调整为[L1,R1,L2,R2,...,LK,RK]
- 举例： [1, 2, 3, 4] 调整为[1， 3， 2， 4]； [1, 2, 3, 4, 5, 6] 调整为[1, 4, 2, 3, 5,6]
- 要求： 时间复杂度 O(n)， 空间复杂度O(1)


### 2. 

- 题目1： 数组中有一个数出现了奇数次，剩下的数出现了偶数次，打印这个出现奇数次的数
- 思路： 采用异或操作， 返回最终异或后的结果

- 题目2： **数组中有两个数出现了奇数次，剩下的数出现了偶数次，打印这两个出现奇数次的数**
- 思路：

- 题目3：数组中有一个数出现1次，剩下的数出现了k次，打印这个出现k次的数
- 思路：将每个数变为3进制， 然后所有的数按位相加，然后将和按位 %3 就得到了出现一次的数 


- 要求： 额外空间复杂度O(1)， 时间复杂度O(n)

### 3. 俄罗斯套娃信封问题

- 来源：leetcode 354
- 思路：将数组按照长度升序，再按照宽度降序排列，然后将宽度单独拿出组成一个数组，再求该数组的最大递增子序列

### 4. 