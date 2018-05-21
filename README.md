# SICP Learning Notes

在阅读本书之前，学过也写过一些程序如Python，以为对程序的基础要素已经蛮熟悉了，因为每学一门语言，都是从这些基本语言特性开始的：变量类型、运算符、逻辑控制、循环等等。但是每个语言都浅尝辄止，一没体会到太多编程的乐趣（掉的坑太多，要么爬不出，要么满心伤痕）；二不太会融会贯通，java collections\多线程、python collections\多线程、blahblah每种都在独立的学习，编程在各种语言相同功能的不同方法中迷失了；三无抽象思维能力，也很少深入思考。

听闻SICP是基础的基础，学完不一定会编程能力大涨，但可大大开阔思维。尤其是书中用的语言是LISP（开发语言之母），另外还有一本SICP In Python，如果结合着看（看不过来），更厉害。想的很美好。

曾经被大妈怼过我满篇的“复杂度”恐惧：

> - 要知道无论多复杂的系统/知识/理论/代码/...
> - 都是由最基础的元件组合而成的
> - 不存在独立的完全不可分解的复杂度...

背道而驰，我经常将简单的事情复杂化，而事情一复杂了，又未能分解之。MVP于我实施起来之难，可想而知。其背后的一个原因是，我对“简单的事情”并未有真正的理解，或即使理解了，但没有有效的运用起来。希望通过SICP的学习和练习，帮助自己不迷失在复杂的编程世界中。

以第一章开篇结尾：

> The acts of the mind, wherein it exerts its power over simple ideas, are chiefly these three: 1.   Combining several simple ideas into one compound one, and thus all complex ideas are made. 
>
> 2. The second is bringing two ideas, whether simple or complex, together, and setting them by one another so as to take a view of them at once, without uniting them into one, by which it gets all its ideas of relations. 
> 3. The third is separating them from all other ideas that accompany them in their real existence: this is called abstraction, and thus all its general ideas are made.
>
> —John Locke, An Essay Concerning Human Understanding(1690)

# Scheme Environment

按照这个教程[Scheme 编程环境的设置](http://www.yinwang.org/blog-cn/2013/04/11/scheme-setup)，配好后，打开一个sample scm文件：

```
(define s 123)
s
```

按F5运行报错：

```Symbol's function definition is void: fine```

毫无头绪现在

# Emacs 基本操作

M x: alt + x

# **本书地址：**

[Structure and Interpretation of Computer Programs, 2e: Top](file://localhost/Users/wanjia/Library/Application%20Support/Zotero/Profiles/h6gwndqs.default/zotero/storage/98VGGP3G/index.html)

# **参考书：**

[SICP in Python | Pedro Kroger](https://pedrokroger.net/sicp-python/)