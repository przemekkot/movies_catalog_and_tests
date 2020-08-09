import pytest
import tmdb_client
from unittest.mock import Mock



def test_get_movies_list(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list


def test_get_single_movie(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_single_movie = ['title', 'overview', 'budget', 'genre', 'cast']
    
    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    # Dla przykładu bierzemy movie_id 497, to jest "Zielona Mila"
    single_movie = tmdb_client.get_single_movie(movie_id=497)
    assert single_movie == mock_single_movie


def test_get_movie_images(monkeypatch):
    # Przygotowanie danych
    poster_api_path = "some-poster-path"
    #expected_default_size = 'w780'
    expected_default_size = 'w342'
    # Wywołanie kodu, który testujemy
    #poster_url = tmdb_client.get_movie_images(movie_id=497)
    poster_url = tmdb_client.get_poster_url(poster_api_path, size="w342")
    # Porównanie wyników
    assert expected_default_size in poster_url


def test_get_single_movie_cast(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    #mock_actor_details = ['name', 'character']
    mock_actor_details = ['cast_id', 'character', 'credit_id', 'gender']
    #mock_actor_details = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = {'cast': mock_actor_details}
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    # Dla przykładu bierzemy movie_id 497, to jest "Zielona Mila"
    actor_details = tmdb_client.get_single_movie_cast(movie_id=497, number=10)
    assert actor_details == mock_actor_details
