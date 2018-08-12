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
print("output after return is : ", output1)
