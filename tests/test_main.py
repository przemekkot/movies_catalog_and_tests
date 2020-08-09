import pytest
from main import app
import tmdb_client
from tmdb_client import call_tmdb_api
from unittest.mock import Mock


@pytest.mark.parametrize('n, result', (
   ('movie/top_rated', 200),
   ('movie/upcoming', 200),
   ('movie/popular', 200),
   ('movie/now_playing', 200)
))
def test_homepage(monkeypatch, n, result):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       #assert response.status_code == 200
       assert response.status_code == result
       #api_mock.assert_called_once_with(n)




