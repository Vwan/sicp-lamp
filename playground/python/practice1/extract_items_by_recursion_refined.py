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

def extract_labels(treedata, output=None):
    """
    extract all the labels value from treedata
    :param treedata: tree-structure list
    :param output: new list containing all label values
    :return: list
    """
    def list_recursive(lst, output):
        if len(lst) == 1:
            return extract_labels(lst[0], output)
        else:
            return extract_labels(lst[1:], extract_labels(lst[0], output))

    if output == None:
        output = []

    if type(treedata) is list:
        list_recursive(treedata, output)
    elif type(treedata) is dict:
        label = treedata.get('label')
        output.append(label)
        children = treedata.get('children')
        if children:
            list_recursive(children, output)

    print("output before return is ", output)
    return output

if __name__ == "__main__":
    output = extract_labels(treedata)
    print("output after return is : ", output)
