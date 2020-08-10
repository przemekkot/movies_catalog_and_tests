import pytest
from main import app
import tmdb_client
from tmdb_client import call_tmdb_api
from unittest.mock import Mock


@pytest.mark.parametrize('n, result', (
   ('top_rated', 200),
   ('upcoming', 200),
   ('popular', 200),
   ('now_playing', 200)
))
def test_homepage(monkeypatch, n, result):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get(f'/?list_type={n}')
       #assert response.status_code == 200
       assert response.status_code == result
       api_mock.assert_called_once_with(f'movie/{n}')




