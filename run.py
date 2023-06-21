from browser import Browser
import yaml


data = yaml.load(open('/test/test.yaml', encoding='UTF-8'),
                 Loader=yaml.BaseLoader)
print(data)
try:
    for item in enumerate(data['spec']):
        b = Browser(item[1]['headers'])
        for i in enumerate(item[1]['cases']):
            b.get(item[1]['host']+i[1]['request']['url'], i[1]['name'], i[1]['request'].get(
                'headers')).want(i[1]['want'])
except ValueError as err:
    print(err)
