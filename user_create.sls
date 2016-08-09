
{% set namespace = 'default' %}
{% set AccountName = 'olitest' %}

# https://docs.saltstack.com/en/latest/ref/renderers/all/salt.renderers.jinja.html
{% set data = {
    'foo': True,
    'bar': 42,
    'baz': [1, 2, 3],
    'qux': 2.0
} %}

{% set json = {{ data|json }} %}

{% load_json as ServiceAccount %}
{
  "kind": "ServiceAccount",
  "apiVersion: "v1",
  "metadata": {
    "name":"{{ AccountName }}"
    }
}
{% endload %}


oc create ServiceAccount {{ AccountName }}":
  cmd.run:
    - name: "echo '{\"kind\":\"ServiceAccount\",\"apiVersion\":\"v1\",\"metadata\":{\"name\":\"{{ AccountName }}\"}}' | oc create --namespace={{namespace}} -f -"
    - unless: oc get sa --namespace={{namespace}} {{title}}


