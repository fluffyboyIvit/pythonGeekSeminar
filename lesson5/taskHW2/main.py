import copy

site = {
'html': {
'head': {
'title': 'Куплю/продам телефон недорого'
},
'body': {
'h2': 'У нас самая низкая цена на iPhone',
'div': 'Купить',
'p': 'Продать'
}
}
}

def changeValue(struct,key,value):
    if key in struct:
        struct[key] = value
    else:
        for subStruct in struct.values():
            if isinstance(subStruct,dict):
                changeValue(subStruct,key,value)
    return struct

def printStruct(struct,space=1):
    for key,value in struct.items():
        if isinstance(value,dict):
            print(" " * space, key)
            printStruct(value,space + 3)
        else:
            print(f"{" " * space}{key} : {value}")

def makeSite(name):
    structSite = copy.deepcopy(site)
    newTitle = 'Куплю/продам {} недорого'.format(name)
    structSite = changeValue(structSite,'title',newTitle)
    newH2 = 'У нас самая низкая цена на {}'.format(name) 
    structSite = changeValue(structSite, 'h2', newH2)
    return structSite

sites=[]
siteCount = int(input("Введите кол-во нужных сайтов: "))
for sitecreate in range(siteCount):
    productName = input("Введите название продукта: ")
    newSite = makeSite(productName)
    sites.append(newSite)
    for i in sites:
        printStruct(i)