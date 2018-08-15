# 缘起

读SICP的过程中，不断的见识到贯穿全书(lisp)的递归思想，虽然递归的定义（调用自己）看起来很简单，但总觉得还没有get到，为什么要这么频繁的用递归，递归是否是那种大道至简的方法之一？我们的生活中是否也遍布递归现象或思想？为什么现代语言却又在规避使用递归，等等问题。

希望通过阅读sicp以及其他相关的书籍对递归有更深一层的理解。

之前看过一点<The Little Schemer>, 传达递归思想的神书，奈何目前还不太看得进去；今天翻GEB目录，发现第五章<Recursive Structures and Process>，眼前一亮，正是理解递归的入门篇章啊，略微翻了下，讲了很多生活中的递归现象的例子，接下来准备先细读本章，以后再找其他书继续读。

## GEB：Recursive Structures and Processes

### 生活中有哪些递归现象

下面几个是在看书前想到的，留在这，待读完再界。

- 老和尚讲故事应该算一下，这个还比较好理解
- 树形结构
- 语言的组成：从字符->单词->句子->段落->文章->书。。。这个算么？
- 做梦：梦中有梦，梦中知道自己在做梦，然后梦醒
- 轮回算么

## 各路分析理解

### from @thxiami [关于递归函数返回值的问题（本周作业碰到的问题） · Issue #23 · AIHackers/Py101-004](https://github.com/AIHackers/Py101-004/issues/23#issuecomment-323377521)

> 对递归的评估
>
> - 健壮性(Robustness)
>   - 根据搜索，代码的健壮性主要指其面对各种异常情景时能否正常处理，输出出错信息。递归会存在栈溢出的潜在问题（学术名词: stack overflow ,这个名词我也不是特别懂，应该跟记录函数运行的记录有关），当递归次数超过一定数量时（我这里默认1000次，使用sys.getrecursionlimit()查看），程序会被终止，并抛出 1 个异常:RuntimeError: maximum recursion depth exceeded 。因此，当不确定函数需要调用的次数时，这会影响程序运行的稳定性。如果直至报错，递归仍然没有获得结果，那这时的代码就不够健壮，不如使用循环。
> - 效率
>   - 写代码的效率：递归更接近于一些算法问题的描述，比如（阶乘，斐波那契数列），相对循环来说更容易编写，出问题时也容易 debug
>   - 运行效率：递归的速度（一般情况）会比循环要慢,占用内存更多（Python中没有对尾递归进行优化，即便使用尾递归也不能缓解内存占用的问题）。但在某一些问题上，改变递归的实现方式（结合一些数据结构），会给速度带来提升，甚至速度比循环更快(例子可参见: Recursive Functions)
> - 可读性
>   - 算法问题：一般来说，递归更易读，易 debug
>   - ch0，ch1 作业中的获得用户输入的问题：对初学者，递归可读性比循环差
> - 其他可能发生的问题
>   - 目前不知道
>
> Recuision or Loop
>
> - 根据上面分析的递归的优劣，阅读好几个类似问题下的答案，基本上大家的观点都比较一致：
>
>   - 一个算法如果能通过递归实现，循环也可以实现
>
>   - ###### 当递归易写但低效时，那么选择哪种方法解决问题，其实就是选择花更多的时间用 loop 实现，还是花更多的钱提升机器性能
>
> Reference
>
> - [wisc大学cs课程教案](http://pages.cs.wisc.edu/~vernon/cs367/notes/6.RECURSION.html)
> - [Guido's blog:Tail Recursion Elimination](http://neopythonic.blogspot.jp/2009/04/tail-recursion-elimination.html)
> - [Recursive Functions](http://www.python-course.eu/recursive_functions.php)
> - [What are the advantages and disadvantages of recursion?](https://stackoverflow.com/questions/5250733/what-are-the-advantages-and-disadvantages-of-recursion)
> - [recursion versus iteration](https://stackoverflow.com/questions/15688019/recursion-versus-iteration)

## 实际操练1

### 需求

> ```
> """
> 需求
> 提取 treedata 中的 label 到一个 list 中去
> 
> """
> 
> treedata = [{
>     'label': '1',
>     'children': [{
>         'label': '1.1',
>         'children': [{
>             'label': '1.1.1',
>             'children': ''
>         }, {
>             'label': '1.1.2',
>             'children': ''
>         }, {
>             'label': '1.1.3',
>             'children': ''
>         }],
>     }, {
>         'label': '1.2',
>         'children': [{
>             'label': '1.2.1',
>             'children': ''
>         }, {
>             'label': '1.2.2',
>             'children': ''
>         }, {
>             'label': '1.2.3',
>             'children': ''
>         }],
>     }, ]
> }]
> ```

### 分析

谢谢@thxiami同学提供的实际项目需求，花了好长好长时间研究怎么用递归来实现，最终还是很傻的代码，加上奇诡的输出，果然理论看过了不操练就是眼高手低。

对我来说，这个需求**几大难点**：

1. 判断递归退出条件

- 满足什么条件应该退出递归，否则无穷循环
  - 我现在的代码并没有明确的指出退出条件，似乎并不太好

2. 判断递归的最小单元

- 数据treedata是list表示的树结构，list item是字典，内含子项children是包含多个字典项的列表
- 我很长时间卡在是以字典为单元递归，还是列表为单元
- 后来想通应该以列表为单元，因为重复的结构是list结构啊

3. 如何保存所需的新列表

- 递归的时候，取出label值需要放到一个列表中，
  - 但如果这个列表作为函数的局部变量，就会被不断的重写
    - 我的解决方法是，将新列表变量作为函数的参数。但这样的问题是，实现的函数是迭代式的，虽然其定义上看还是递归。不过好像看起来是尾递归，虽然我还分不清尾递归和迭代的具体区别（这里的迭代不是指for loop, 而是SICP中第一章里面的迭代）
  - 如果在函数外设置一个全局变量，似乎可以解决重写问题，但实际项目中一般不会这么做吧？

4. 如何通过递归来遍历children list的各个子项：

- 因为我是以list为单元来递归，所以当children list有多项的时候，总是在第一项做完就退出了（可能是我不会处理），google搜索了一下，参考：[list - Basics of recursion in Python - Stack Overflow](<https://stackoverflow.com/questions/30214531/basics-of-recursion-in-python>)，解决。

  

  ```
  >>> def listSum(ls):
  ...     # Base condition
  ...     if not ls:
  ...         return 0
  ...
  ...     # First element + result of calling `listsum` with rest of the elements
  ...     return ls[0] + listSum(ls[1:])
  ```

  ```return ls[0] + listSum(ls[1:])```, 看着很眼熟的感觉，其思路很像lisp中的pair，ls[0]相当于car, ls[1:]相当于cdr

  参考之，我用了以下：

  ```
  return extract_labels(treedata[0], output) + extract_labels(treedata[1:], output)
  ```

### 实现思路

本需求中treedata是包含一个字典项的列表，考虑到实际生产中可能会包含多个字典项，比如label: 2等，所以将treedata作为多个字典项的列表来实现：

- 定义一个extract_labels方法，参数：treedata, output

  - output 将为最终返回的新列表

- 方法体：

  - 如果treedata是list，则递归调用

    - 这里做了一下判断treedata的长度

      - 如果是1， 则

      ```
      return extract_labels(treedata[0], output)
      ```

      - 否则

      ```
      return extract_labels(treedata[0], output) + extract_labels(treedata[1:], output)
      ```

  - 如果treedata是dict，则取其“label”和"children"

    - 如果children是list，则递归调用
      - 【问题】：如果children的长度是1的话，此处代码会报错。

### 代码

```
def extract_labels(treedata, output):
    if type(treedata) is list:
        if len(treedata) == 1:
            return extract_labels(treedata[0], output)
        else:
            return extract_labels(treedata[0], output) + extract_labels(treedata[1:], output)
    elif type(treedata) is dict:
        label = treedata.get('label')
        output.append(label)

        children = treedata.get('children')
        if children and type(children) is list:
            return extract_labels(children[0], output) + extract_labels(children[1:], output)
    
    print("output before return is ", output)
    return output

def extract(treedata):
    return extract_labels(treedata, [''])

output1 = extract(treedata)
print("output after return is : ", output1)
```

### 运行结果

出问题了，不明白，为什么返回前和返回后输出不一样呢？这中间没有其他操作了啊。[原因：我以为的"print("output before return is ", output)" 这一行其实并不是函数最终的返回行，应该是在那几个递归行呢]

```
output before return is  ['', '1', '1.1', '1.1.1', '1.1.2', '1.1.3', '1.2', '1.2.1', '1.2.2', '1.2.3']
output after return is :  ['', '1', '1.1', '1.1.1', '1.1.2', '1.1.3', '', '1', '1.1', '1.1.1', '1.1.2', '1.1.3', '', '1', '1.1', '1.1.1', '1.1.2', '1.1.3', '', '1', '1.1', '1.1.1', '1.1.2', '1.1.3', '1.2', '1.2.1', '1.2.2', '1.2.3', '', '1', '1.1', '1.1.1', '1.1.2', '1.1.3', '1.2', '1.2.1', '1.2.2', '1.2.3', '', '1', '1.1', '1.1.1', '1.1.2', '1.1.3', '1.2', '1.2.1', '1.2.2', '1.2.3']

```

#### [@thxiami的debug调试结果](https://github.com/DebugUself/du4proto/commit/c2ba6ee4a59789ba4326496ffd99839d744d75f5#commitcomment-30059252)

```
# 为了减低debug难度，把数据的嵌套层数缩减，此时原来问题仍然存在，但是debug难度降低
treedata = [{
    'label': '1',
    'children': [{
        'label': '1.1',
        'children': '',
    },
        {
        'label': '1.2',
        'children': '',
    },
    ]
}]


def extract_labels(treedata, output):
    if type(treedata) is list:
        if len(treedata) == 1:
            return extract_labels(treedata[0], output)
        else:
            return extract_labels(treedata[0], output) + extract_labels(treedata[1:], output)
    elif type(treedata) is dict:
        label = treedata.get('label')
        output.append(label)

        children = treedata.get('children')
        if children and type(children) is list:
            output1 = extract_labels(children[0], output)
            output2 = extract_labels(children[1:], output)
            
            # 明确两个信息：
            # 1、操作的 output 始终对应于内存中同一块地址，任何时候通过任意途径修改了 output，在其他地方引用的 output 也会发生对应变化
            # 2、output1 和 output2 都是 return output 得到的，也就是 output1 和 output2 都是 output 的引用，二者对应同一块内存地址
            # 可以通过下面表达式验证
            print('**debug id(output1) == id(output):', id(output1) == id(output))
            print('**debug id(output2 == id(output):', id(output2) == id(output))
            
            # 接着理清递归的过程
            # 先进行递归操作 output 得到 output1，此时 output=output1 = ['', '1', '1.1']
            # 再进行递归操作 output 得到 output2，操作前 output = ['', '1', '1.1']，操作后 output2 = output = ['', '1', '1.1', '1.2']
            # 此时 output1 其实就是 output 的引用，所以 output1 = ['', '1', '1.1', '1.2']
            # 最后相当于 output + output
            #          ['', '1', '1.1', '1.2'] + ['', '1', '1.1', '1.2']
            return output1 + output2
            # return extract_labels(children[0], output) + extract_labels(children[1:], output)

    print("output before return is ", output)
    return output


def extract(treedata):
    return extract_labels(treedata, [''])


final_output = extract(treedata)
print("output after return is : ", final_output)
print的结果

output before return is  ['', '1', '1.1']
output before return is  ['', '1', '1.1', '1.2']
**debug id(output1) == id(output): True
**debug id(output2 == id(output): True
output after return is :  ['', '1', '1.1', '1.2', '', '1', '1.1', '1.2']
```

#### 解决方案

原因找着了，现在就是如何解决的问题了，按thxiami的提示，两种方法：

- 从拷贝而非引用的角度探索. 拷贝又分为深拷贝和浅拷贝,目前我们的情况深拷贝和浅拷贝没有区别.
- 始终操作同一个output，并返回

个人感觉始终操作同一个output应该可行，现在看出错点主要是在：

```
output1 = extract_labels(children[0], output)
output2 = extract_labels(children[1:], output)
```

output1 和 output2 都指向了 output, 就是说， extract_labels(children[0], output) 的返回结果其实并没有传入后面的操作extract_labels(children[1:], output)，只需要改成这样即可：

```
output1 = extract_labels(children[0], output)
return extract_labels(children[1:], output1)
```

### 进一步思考

1. 需求中的treedata其实就是json格式的数据，为什么不直接用json处理而是要用递归？

2. 用递归实现的时候结合for loop是否可行？

   试了一下，貌似比我前面的实现简单多了， 而且结果正确

   ```
   output = []
   def extract_labels(treedata):
       for data in treedata:
           label = data.get('label')
           output.append(label)
           children = data.get('children')
           if type(children) is list:
               extract_labels(children)
       return output
   
   output1 = extract_labels(treedata)
   print("output is : ", output1)
   ```

   看了thxiami同学的实现，思路差不多，但是比我的专业多多了，先后两版：

   **版本1**：

   ```
   def get_label(des_ls, data_ls):
       if not isinstance(data_ls, list):
           print("return")
           return
   
       for i in data_ls:
           print("*"*20)
           print("**debug data['children']:", i['children'])
           print("**debug data['label']:", i['label'])
           print("**debug type(data['children']", type(i['children']))
   
           des_ls.append(i['label'])
           if 'children' in i.keys():
               get_label(des_ls, i['children'])
   
   
   if __name__ == '__main__':
       des_ls = []
       get_label(des_ls, treedata)
       print("des_ls:", des_ls)
   ```

   **版本2:**

   改进：
   1、只用传 需要解析的 treedata，函数的入口更简单，只用关心传什么
   2、解析完生成的list会 return 回来，函数的出口更明确，不像之前那样不 return 东西，只是在内部隐式操作。

   ```
   def get_label(data_ls, des_ls=None):
       if des_ls is None:
           des_ls = []
   
       if not isinstance(data_ls, list):
           print("return")
           return
   
       for i in data_ls:
           print("*"*20)
           print("**debug data['children']:", i['children'])
           print("**debug data['label']:", i['label'])
           print("**debug type(data['children']", type(i['children']))
   
           des_ls.append(i['label'])
           if 'children' in i.keys():
               get_label(i['children'], des_ls)
       return des_ls
   
   
   if __name__ == '__main__':
       des_ls = get_label(treedata)
       print("des_ls:", des_ls)
   ```

    **几点收获：**

   - 以后代码尽量写的专业点，不局限于写函数。

   - 关于用type()还是isinstance()来判断是否列表或字典，主要区别应该在于后者可以用于继承类的判断

     [python - What are the differences between type() and isinstance()? - Stack Overflow](https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance)

   - 局部变量和全局变量

     - 我的for loop实现中 output是全局变量，这种做法不妥
     - 取而代之将output作为函数参数

   - 参数默认值的使用

     - 列表output需要有个初始值，不然无法append, 但傻傻的放个空列表做函数参数值的话，不好看，而且面向用户的函数入口不清爽。
     - 给output参数一个默认值None，如果是None则在函数体内设为空。这样用户只需要传treedata即可。

   ```
   def get_label(data_ls, des_ls=None):
       if des_ls is None:
           des_ls = []
   ```

   

3. 现在的实现还能不能进一步模块化？

   分析需求，主要有两步操作：

   - 遍历
   - 筛选label

   如果treedata数据变化，比如增加新的节点并取出来呢？如果尽可能少的代码变动以应对不同的treedata？