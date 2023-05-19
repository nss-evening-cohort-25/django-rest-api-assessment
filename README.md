# Self-Assess Your Django Competencies

## 🐟 Tuna Piano API

In this assessment, you will be building the backend for an existing React frontend application. The frontend consists of features related to Songs, Artists, and Genres. Your task is to implement the backend functionality to support these features.

We'll make millions 💰 💰 💰


### Setup

1. Clone the template repository
2. `cd` to the directory it creates
3. `pipenv shell`
4. `pipenv install`
5. Open in VS Code
6. Make sure the correct interpreter is selected
7. Implement the code


Routes by Entity

### 🎶 Songs
- Create a Song:
    - Route: POST /songs
- Delete a Song:
    - Route: DELETE /songs/{songId}
- Update a Song:
    - Route: PUT /songs/{songId}
- View a List of all the Songs:
    - Route: GET /songs
- Details view of a single Song and its associated genres and artist details:
    - Route: GET /songs/{songId}
- Search songs by genre:
    - Route: GET /songs?genre={genreId}

### 👩🏾‍🎤 Artists
- Create an Artist:
    - Route: POST /artists
- Delete an Artist:
    - Route: DELETE /artists/{artistId}
- Update an Artist:
    - Route: PUT /artists/{artistId}
- View a List of all the Artists:
    - Route: GET /artists
- Details view of a single Artist and the songs associated with them:
    - Route: GET /artists/{artistId}
- See related artists with similar genres:
    - Route: GET /artists/{artistId}/related
- Search artists by genre:
    - Route: GET /artists?genre={genreId}

### 🎸 Genres
- Create a Genre:
    - Route: POST /genres
- Delete a Genre:
    - Route: DELETE /genres/{genreId}
- Update a Genre:
    - Route: PUT /genres/{genreId}
- View a List of all the Genres:
    - Route: GET /genres
- Details view of a single Genre and the songs associated with it:
    - Route: GET /genres/{genreId}
- Popular genres to see a list of genres based on the number of songs associated with each genre:
    - Route: GET /genres/popular

The artist response should include the total number of songs in the database for the artist. It should also include a serialized list of all related songs _(see example below)_.

## Data Design

### Artists

The following information should be captured for each artist.

1. Name
2. Age
3. Bio

### Songs

The following information should be captured for each song.

1. Title
2. Artist
3. Genre
4. Album name
5. Length

### Genres

The genre model only needs to have the name of the genre on it.

## JSON Responses

Set up your serializers to produce the following JSON responses for getting songs and artists.

## Song

```json
{
    "id": 1,
    "title": "Song Title",
    "album": "Album Title",
    "length": 342,
    "genre": {
        "description": "Pop"
    },
    "artist": {
        "name": "Yerena Gonzalez"
    }
}
```

## Artist

```json
{
    "id": 1,
    "name": "Yerena Gonzalez",
    "age": 26,
    "bio": "Accusamus maxime sed illo doloribus minus. Quaerat et sed et. Harum consequatur hic ut magnam consequatur labore culpa tempore.",
    "songs": [
        {
            "id": 1,
            "title": "Song Title",
            "album": "Album Title"
        }
    ],
    "song_count": 1
}
```
