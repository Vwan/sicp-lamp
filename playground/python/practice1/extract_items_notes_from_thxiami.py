# 为了减低debug难度，把数据的嵌套层数缩减，此时原来问题仍然存在，但是debug难度降低
treedata1 = [{
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

treedata = treedata = [{
    'label': '1',
    'children': [{
        'label': '1.1',
        'children': [{
            'label': '1.1.1',
            'children': ''
        }, {
            'label': '1.1.2',
            'children': ''
        }, {
            'label': '1.1.3',
            'children': ''
        }],
    }, {
        'label': '1.2',
        'children': [{
            'label': '1.2.1',
            'children': ''
        }, {
            'label': '1.2.2',
            'children': ''
        }, {
            'label': '1.2.3',
            'children': ''
        }],
    }, ]
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

def extract_labels_refined(treedata, output):
    if type(treedata) is list:
        if len(treedata) == 1:
            return extract_labels_refined(treedata[0], output)
        else:
            t1 = extract_labels_refined(treedata[0], output)
            t2 = extract_labels_refined(treedata[1:], t1)
            return  t2
    elif type(treedata) is dict:
        label = treedata.get('label')
        output.append(label)

        children = treedata.get('children')
        if children and type(children) is list:
            output1 = extract_labels_refined(children[0], output)
            output2 = extract_labels_refined(children[1:], output1)

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
            return output2
            # return extract_labels(children[0], output) + extract_labels(children[1:], output)

    print("output before return is ", output)
    return output

def extract(treedata):
    return extract_labels_refined(treedata, [''])


final_output = extract(treedata)
print("output after return is : ", final_output)