import json

base_template = open("dashboard.json").read()
interface_template = open("interface_panel.json").read()

base_template = base_template.replace("{{ dashboard_title }}", "grafana-demo-device")

interface_templates = []
for interface in ["Gi1/0/10", "Gi1/0/11", "Gi1/0/23", "Gi1/0/24"]:
    _t = interface_template
    replace_values = {"{{ host }}": "192.168.0.252", "{{ interface }}": interface, "{{ panel_title }}": interface}
    for k,v in replace_values.items():
        _t = _t.replace(k,v)
    interface_templates.append(json.loads(_t))

base_template = json.loads(base_template)
base_template["panels"] = interface_templates

with open("template_example.json","w") as exampleFile:
    exampleFile.write(json.dumps(base_template, indent=4))
