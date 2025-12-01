import os
import pytest
import requests
import yaml
from pathlib import Path
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Helper function to expand environment variables in strings
def _expand_env_in_string(value):
    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
        var_name, _, default = value[2:-1].partition(":-")
        return os.getenv(var_name, default)
    return value

# Load configuration from config.yml
def load_config():
    config_file_path = Path(__file__).parent / "config.yml"
    try:
        with open(config_file_path, 'r') as file:
            config = yaml.safe_load(file)
            # Expand environment variables in the config
            for key, value in config.items():
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        config[key][sub_key] = _expand_env_in_string(sub_value)
                else:
                    config[key] = _expand_env_in_string(value)
            return config
    except Exception as e:
        raise RuntimeError(f"Failed to load configuration: {e}")

@pytest.fixture(scope='session')
def config():
    return load_config()

@pytest.fixture(scope='session')
def host(config):
    return config['api']['host'].strip()

@pytest.fixture(scope='session')
def auth(config):
    return config['auth']['ApiKeyAuth'].strip()

@pytest.fixture(scope='session')
def config_test_data(config):
    return config['test_data']

class APIClient:
    def __init__(self, base_url, auth):
        self.base_url = base_url
        self.auth = auth
        self.session = requests.Session()
        retries = Retry(total=3, backoff_factor=0.3, status_forcelist=[500, 502, 503, 504])
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        self.session.mount('http://', HTTPAdapter(max_retries=retries))

    def make_request(self, endpoint, params=None, headers=None, method='GET'):
        url = f"{self.base_url}/{endpoint}".strip()
        headers = headers or {}
        headers['Authorization'] = self.auth
        try:
            response = self.session.request(method=method, url=url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {e}")

    def get(self, endpoint, headers=None, params=None):
        return self.make_request(endpoint, params=params, headers=headers, method='GET')

    def post(self, endpoint, headers=None, params=None, data=None):
        return self.make_request(endpoint, params=params, headers=headers, method='POST')

    def put(self, endpoint, headers=None, params=None, data=None):
        return self.make_request(endpoint, params=params, headers=headers, method='PUT')

    def delete(self, endpoint, headers=None, params=None):
        return self.make_request(endpoint, params=params, headers=headers, method='DELETE')

    def patch(self, endpoint, headers=None, params=None, data=None):
        return self.make_request(endpoint, params=params, headers=headers, method='PATCH')

@pytest.fixture(scope='session')
def api_client(host, auth):
    return APIClient(base_url=host, auth=auth)

def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: mark test as a smoke test")
