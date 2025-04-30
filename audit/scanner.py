import yaml
from kubernetes import client, config

def load_rules(path="audit/rules.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def scan_pods():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces(watch=False)
    return pods.items