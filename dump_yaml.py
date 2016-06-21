Python 2.6.9 (unknown, Nov 19 2014, 15:44:49)
[GCC 4.3.4 [gcc-4_3-branch revision 152973]] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import yaml
>>>
>>>
>>> srv = """apiVersion: v1
... kind: Service
... metadata:
...   name: nodejshttp
... spec:
...   selector:
...     oscontainer: myolitcontainer
...   ports:
...   - nodePort: 0
...     port: 8080
...     protocol: TCP
...     targetPort: 8080"""
>>> srv
'apiVersion: v1\nkind: Service\nmetadata:\n  name: nodejshttp      \nspec:\n  selector:                  \n    oscontainer: myolitcontainer  \n  ports:\n  - nodePort: 0\n    port: 8080              \n    protocol: TCP\n    targetPort: 8080'
>>> yaml.load(srv)
{'kind': 'Service', 'spec': {'ports': [{'protocol': 'TCP', 'targetPort': 8080, 'nodePort': 0, 'port': 8080}], 'selector': {'oscontainer': 'myolitcontainer'}}, 'apiVersion': 'v1', 'metadata': {'name': 'nodejshttp'}}
>>> dict  = yaml.load(srv)
>>> import pprint
>>> pprint.pprint dict
  File "<stdin>", line 1
    pprint.pprint dict
                     ^
SyntaxError: invalid syntax
>>> pprint.pprint(dict)
{'apiVersion': 'v1',
 'kind': 'Service',
 'metadata': {'name': 'nodejshttp'},
 'spec': {'ports': [{'nodePort': 0,
                     'port': 8080,
                     'protocol': 'TCP',
                     'targetPort': 8080}],
          'selector': {'oscontainer': 'myolitcontainer'}}}
>>> pprint.pprint(dict, indent=4)
{   'apiVersion': 'v1',
    'kind': 'Service',
    'metadata': {   'name': 'nodejshttp'},
    'spec': {   'ports': [   {   'nodePort': 0,
                                 'port': 8080,
                                 'protocol': 'TCP',
                                 'targetPort': 8080}],
                'selector': {   'oscontainer': 'myolitcontainer'}}}
