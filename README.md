# Algorithm Python

## Reading List:
1. [十大经典排序算法动画与解析，看我就够了！（配代码完全版）](https://mp.weixin.qq.com/s/vn3KiV-ez79FmbZ36SX9lg)
2. [十大经典排序算法（动图演示）](https://www.cnblogs.com/onepixel/articles/7674659.html)
3. [LeetCodeAnimation](https://github.com/MisterBooo/LeetCodeAnimation/blob/master/Readme.md)
4. [python的面试题](https://github.com/kenwoodjw/python_interview_question)
5. [算法复杂度速查表](https://mp.weixin.qq.com/s/fGh04uCu0tVX7ttoy2cXYQ)
6. [30 张图弄懂「图的两种遍历方式」](https://mp.weixin.qq.com/s/hwx6R8z8tkK7q1oSze7uNA)
7. [代码随想录](https://programmercarl.com/)

## Terms
1. 稳定排序：如果 a 原本在 b 的前面，且 a == b，排序之后 a 仍然在 b 的前面，则为稳定排序。

2. 非稳定排序：如果 a 原本在 b 的前面，且 a == b，排序之后 a 可能不在 b 的前面，则为非稳定排序。

3. 原地排序：原地排序就是指在排序过程中不申请多余的存储空间，只利用原来存储待排数据的存储空间进行比较和交换的数据排序。

4. 非原地排序：需要利用额外的数组来辅助排序。

5. 时间复杂度：一个算法执行所消耗的时间。

6. 空间复杂度：运行完一个算法所需的内存大小。

![数据结构操作](http://mmbiz.qpic.cn/mmbiz/foPACGrddJ3ib5Tg6K5ak8SZ1ToqAj2AeQvtHAXic0d7rrJy2TsvF9oHcic1fR3oWnLUyCyzfKxd1rGy0KgL08WJw/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![大O复杂度图表](http://mmbiz.qpic.cn/mmbiz/foPACGrddJ3ib5Tg6K5ak8SZ1ToqAj2AecXFKfLTicfLDXnE8QTpPpBHrvQkVoKyTuKbesswR4ibc0gEiaekPhAj3Q/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 基本数据结构
### 参考
* [数据结构基础概念篇](https://blog.csdn.net/qq_31196849/article/details/78529724)
### 线性表
* 把线性表的结点按**逻辑顺序**依次存放在一组地址连续的存储单元里。用这种方法存储的线性表简称**顺序表**。是一种**随机存取**的存储结构。```顺序存储指内存地址是一块的，随机存取指访问时可以按下标随机访问，存储和存取是不一样的。```如果是存储，则是指按顺序的，如果是存取，则是可以随机的，可以利用元素下标进行。数组比线性表速度更快的是：原地逆序、返回中间节点、选择随机节点。
### 链表
* 用一组任意的存储单元来依次存放线性表的结点，这组存储单元即可以是连续的，也可以是不连续的，甚至是零散分布在内存中的任意位置上的。因此，链表中结点的逻辑次序和物理次序不一定相同。为了能正确表示结点间的逻辑关系，在存储每个结点值的同时，还必须存储指示其后继结点的地址。data域是数据域，用来存放结点的值。next是指针域（亦称链域），用来存放结点的直接后继的地址（或位置）。不需要事先估计存储空间大小。
* 链表只能顺序查找，定位一个元素的时间为O(N)，删除一个元素的时间为O(1)。

### 栈（Stack）
* 限制在表的一端进行插入和删除运算的**线性表**。
* 通常称插入、删除的这一端为栈顶(Top)，另一端为栈底(Bottom)。**先进后出**。
### 队列（Queue）
* 是一种运算受限的**线性表**。
* 它只允许在表的一端进行插入，而在另一端进行删除。允许删除的一端称为队头(front)，允许插入的一端称为队尾(rear)。**先进先出**。
### 堆
### 树
### 图