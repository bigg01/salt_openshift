
{% set namespace = 'default' %}
{% set AccountName = 'olitest' %}
oc create ServiceAccount {{ AccountName }}":
  cmd.run:
    - name: "echo '{\"kind\":\"ServiceAccount\",\"apiVersion\":\"v1\",\"metadata\":{\"name\":\"{{ AccountName }}\"}}' | oc create --namespace={{namespace}} -f -"
    - unless: oc get sa --namespace={{namespace}} {{title}}


