"""
需求
提取 treedata 中的 label 到一个 list 中去

"""

treedata = [{
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

def extract_labels_old(treedata, output):
    print("++treedata++", treedata)
    label = treedata.get('label')
    if label:
        output.append(label)

    children = treedata.get('children')
    print("-children---", label, children)

    if children and type(children) is list:
        for i in range(len(children)):
            print(children[i])
            return extract_labels_old(children[i], output)
    else:
        return output

def extract_labels(treedata, output):
    print("---output--", output)
    #print("*****treedata******", treedata)
    if type(treedata) is list:
        if len(treedata) == 1:
            print("1&&&&&",output)
            return extract_labels(treedata[0], output)
        else:
            print("2&&&&&",output)
            return extract_labels(treedata[0], output) + extract_labels(treedata[1:], output)
    elif type(treedata) is dict:
        label = treedata.get('label')
        print("----label----", label)
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
