import os
import pytest
import requests
import yaml
from pathlib import Path
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def _expand_env_in_string(value):
    import re
    pattern = re.compile(r'\${([^}:-]+)(:-([^}]+))?}')
    def replace(match):
        env_var = match.group(1)
        default_value = match.group(3)
        return os.getenv(env_var, default_value)
    return pattern.sub(replace, value)

@pytest.fixture(scope='session')
def config():
    config_path = Path(__file__).parent / 'config.yml'
    with open(config_path, 'r') as file:
        config_data = yaml.safe_load(file)
    
    # Expand environment variables in the config
    for key, value in config_data.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                config_data[key][sub_key] = _expand_env_in_string(sub_value)
        else:
            config_data[key] = _expand_env_in_string(value)
    
    return config_data

@pytest.fixture(scope='session')
def api_client(config):
    class APIClient:
        def __init__(self, base_url, auth):
            self.base_url = base_url.strip()
            self.auth = auth
            self.session = requests.Session()
            retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
            self.session.mount('https://', HTTPAdapter(max_retries=retries))
            self.session.mount('http://', HTTPAdapter(max_retries=retries))

        def make_request(self, endpoint, params=None, headers=None, method='GET'):
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            headers = headers or {}
            if self.auth:
                headers.update(self.auth)
            response = self.session.request(method, url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            return response

        def get(self, endpoint, headers=None, params=None):
            return self.make_request(endpoint, params=params, headers=headers, method='GET')

        def post(self, endpoint, headers=None, params=None, data=None):
            return self.make_request(endpoint, params=params, headers=headers, method='POST', data=data)

        def put(self, endpoint, headers=None, params=None, data=None):
            return self.make_request(endpoint, params=params, headers=headers, method='PUT', data=data)

        def delete(self, endpoint, headers=None, params=None):
            return self.make_request(endpoint, params=params, headers=headers, method='DELETE')

        def patch(self, endpoint, headers=None, params=None, data=None):
            return self.make_request(endpoint, params=params, headers=headers, method='PATCH', data=data)

    api_config = config['api']
    auth_config = config['auth']
    auth_headers = {'Authorization': f"Bearer {auth_config['ApiKeyAuth']}"} if auth_config['ApiKeyAuth'] else {}
    return APIClient(api_config['host'], auth_headers)

@pytest.fixture(scope='session')
def config_test_data(config):
    return config.get('test_data', {})

@pytest.fixture(scope='session')
def host(config):
    return config['api']['host']

@pytest.fixture(scope='session')
def auth(config):
    return config['auth']

def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: mark test as smoke test for success scenarios")
