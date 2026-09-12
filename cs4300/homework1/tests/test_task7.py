import sys, os
from unittest.mock import patch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from task7 import get_status_code

# fake the internet request so the test doesn't need real wifi
def test_status_code():
    with patch("task7.requests.get") as fake_get:
        fake_get.return_value.status_code = 200
        result = get_status_code("http://example.com")
        assert result == 200