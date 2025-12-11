import os
import re
import pytest
import requests
import yaml
import json
from pathlib import Path
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def _expand_env_vars(config_str):
    pattern = re.compile(r"\${([^}:]+):-([^}]+)}")
    return pattern.sub(lambda m: os.getenv(m.group(1), m.group(2)), config_str)

def load_yaml_config():
    config_path = Path(__file__).parent / 'config.yml'
    if not config_path.exists():
        raise FileNotFoundError("config.yml not found")
    
    with config_path.open() as f:
        try:
            content = f.read()
            expanded_content = _expand_env_vars(content)
            return yaml.safe_load(expanded_content)
        except yaml.YAMLError as e:
            raise RuntimeError(f"Error parsing YAML: {e}")

@pytest.fixture(scope='session')
def config():
    return load_yaml_config()

@pytest.fixture
def load_endpoint_test_data():
    def _load(path):
        with open(path, 'r') as f:
            return json.load(f)
    return _load

@pytest.fixture
def merged_test_data(config, load_endpoint_test_data):
    def _merge(path):
        endpoint_data = load_endpoint_test_data(path)
        config_data = config.get('test_data', {})
        merged_data = {**config_data, **endpoint_data}
        return merged_data
    return _merge

class APIClient:
    def __init__(self, base_url, timeout=5, retries=3):
        self.base_url = base_url.strip()
        self.session = requests.Session()
        retries = Retry(total=retries, backoff_factor=0.1)
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.timeout = timeout

    def make_request(self, endpoint, method="GET", headers=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, headers=headers, timeout=self.timeout, **kwargs)
        response.raise_for_status()
        return response

    def get(self, endpoint, **kwargs):
        return self.make_request(endpoint, method="GET", **kwargs)

    def post(self, endpoint, **kwargs):
        return self.make_request(endpoint, method="POST", **kwargs)

    def put(self, endpoint, **kwargs):
        return self.make_request(endpoint, method="PUT", **kwargs)

    def patch(self, endpoint, **kwargs):
        return self.make_request(endpoint, method="PATCH", **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.make_request(endpoint, method="DELETE", **kwargs)

@pytest.fixture
def api_client(config):
    base_url = config['api']['host']
    return APIClient(base_url=base_url)

@pytest.fixture
def get_config(config):
    def _get_config(key):
        keys = key.split('.')
        value = config
        for k in keys:
            value = value.get(k)
            if value is None:
                break
        return value
    return _get_config

def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: mark test as part of the smoke suite")
