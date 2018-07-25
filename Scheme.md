#  Notes from book <Yet Another Scheme Tutorial>

## Comments

**;** comment out a line

**\#;** comment out a whole procedure

## 加减乘除

lisp 中的 / 返回的是一个分子/分母的表达形式，而非真正的除法后得到的“浮点数”.

```
(/ 2 6) 返回的是 1/3

这种 1/3的表示形式倒也方便
```

如果要获得除后的结果

```
(exact->inexact (/ 2 6))
```

## 指数、对数

```
(expt 2 3): 2 的 三次方
```

```
(log 100 10): 以10为底，100的对数
(log 100)
```

## list

### cons cell

就是一对内存地址，分别指向 (cons x y)中的 x 和 y在内存中的位置

The Little Schemer 中提过

```
**The Second Commandment**

Use cons to build lists. 
```

看来scheme中用来构建列表的常用就是cons了

如果要构建诸如 (1 2 3 4)的列表：

```
(cons 1 (cons 2 (cons 3 (cons 4 '())))
```

有点点不太能接受，为什么要搞成这么复杂。似乎是这样的话，cons本身就是递归的了。不过还是没太get递归的强大思想意义。

也有简单的写法：

```
(list 1 2 3 4)
```

比较：

```
(list 1 2 3 4)
(list '(1 2 3 4))
(list '(1 2) '(3 4))
```

输出分别是：

```
> '(1 2 3 4)
> '((1 2 3 4))
> '((1 2) (3 4))
```

```'(1 2 3 4)'``` 本身就是一个列表了， 相当于(list 1 2 3 4)

问题：啥时候用list, 或 cons， 或```'```呢？

### 空列表

```
'()
```

或者

```
list()
```



## 字符

### 单个字符

```
#\a: 表示字符a
```

### 字符串

```
"hello world"
```



# Notes from book <The Little Schemer>

## atom

atom 字面上蕴含最小实体的意思。lisp中atom类似python的string，number等原始变量数据。

但在lisp中他们都是字符串

比如 hello, 12345

## list

一组数据，可以是atom, 也可以是list of atoms

比如```(hello 123456)```, ```((hello 1) 12345)```

## S 表达式

所有的atoms， lists 都是S表达式

## tup

原来lisp也有tuple类型，只是tup只限于数字

(1 2 3 4 5), 而且不能包含列表

## cons, car, cdr

### cons

(cons x y): 表示由x和y组成的一对，称为pair。

x 是任意S表达式

y 是任意list

将x添加到list y的最前面，返回值是list

### car

非空 list 中的第一个元素，是atom类型

### cdr

非空 list 中除了第一个元素之外的所有其他元素组成的list，是list类型

## null?

判断是否为空，只适用于list数据类型

## atom?

判断是否是atom，只适用于atom

## eq?

判断两个非数字的atom是否相同

## lat?

判断list中的所有元素是否都是atom类型

## member?

is it a memeber of lat.

```
(member? a (cdr l))
```



## Ask questions - cond

(cond

​	(______, ____)

​	(______, ____)

​	(else, _____)

)

## Summary From The Book

### The Ten Commandments

#### **The First Commandment**

- When recurring on a list of atoms, lat, ask two questions about it: (null? lat) and else. 
- When recurring on a number, n, ask two questions about it: (zero? n) and else. 
- When recurring on a list of S-expressions, l, ask three question about it: (null? l), (atom? (car l)), and else. 

**The Second Commandment**

Use cons to build lists. 

#### The Third Commandment

When building a list, describe the first typical element, and then cons it onto the natural recursion. 

#### The Fourth Commandment 

Always change at least one argument while recurring. 

- When recurring on a list of atoms, lat, use (cdr lat). 

- When recurring on a number, n, use (sub1 n). 

- And when recurring on a list of S-expressions, l, use (carl) and (cdr l) if neither (null? l) nor (atom? (carl)) are true. 

  It must be changed to be closer to termination. The changing argument must be tested in the termination condition: 

  - when using cdr, test termination with null? 
  - and when using sub1, test termination with zero?. 

#### The Fifth Commandment 

- When building a value with + ,always use 0 for the value of the terminating line, for adding 0 does not change the value of an addition. 
- When building a value with x, always use 1 for the value of the terminating line, for multiplying by 1 does not change the value of a multiplication. 
- When building a value with cons, always consider () for the value of the terminating line. 

#### The Sixth Commandment 

- Simplify only after the function is correct. 

#### The Seventh Commandment 

Recur on the subparts that are of the same nature:

- On the sublists of a list. 
- On the subexpressions of an arithmetic expression. 

#### The Eighth Commandment 

Use help functions to abstract from representations. 

#### The Ninth Commandment 

Abstract common patterns with a new function. 

#### The Tenth Commandment 

Build functions to collect more than one value at a time.  



### The Five Rules

#### The Law of Car 

The primitive car is defined only for nonempty lists.

####  The Law of Cdr 

The primitive cdr is defined only for nonempty lists. 

The cdr of any non-empty list is always another list. 

#### The Law of Cons 

The primitive cons takes two arguments. 

The second argument to cons must be a list. The result is a list. 

#### The Law of Null? 

The primitive null? is defined only for lists. 

#### The Law of Eq? 

The primitive eq'l takes two arguments. Each must be a non-numeric atom. 