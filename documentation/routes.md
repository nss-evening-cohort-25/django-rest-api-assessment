I'm writing a ticket for each of the following routes:
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

Can you fill out this ticket templaet for each route?

# TITLE OF TICKET

## Description

## Request
- **Method:**

- **Path:**

- **Body**

  ```json
  ```

## Response

- **Body**

  ```json
  ```

- **Status Code:**


### 🎶 Songs







### Update a Song

# Update an existing song

## Description
This ticket requests the implementation of a route that allows updating an existing song.

## Request
- **Method:** PUT
- **Path:** /songs/{songId}
- **Body**
  ```json
  {
    "title": "Updated Song Title",
    "artist_id": 123,
    "album": "Updated Album Name",
    "length": 240
  }
  ```

## Response
- **Body**
  ```json
  {
    "id": {songId},
    "title": "Updated Song Title",
    "artist_id": 123,
    "album": "Updated Album Name",
    "length": 240
  }
  ```
- **Status Code:** 200 OK


### View a List of all the Songs

# Retrieve a list of all songs

## Description
This ticket requests the implementation of a route that retrieves a list of all songs.

## Request
- **Method:** GET
- **Path:** /songs

## Response
- **Body**
  ```json
  {
    "songs": [
      {
        "id": 123,
        "title": "Song 1",
        "artist_id": 456,
        "album": "Album 1",
        "length": 180
      },
      {
        "id": 789,
        "title": "Song 2",
        "artist_id": 456,
        "album": "Album 2",
        "length": 240
      }
    ]
  }
  ```
- **Status Code:** 200 OK


### Details view of a single Song and its associated genres and artist details

# Retrieve details of a single song with associated genres and artist details

## Description
This ticket requests the implementation of a route that retrieves the details of a single song, including its associated genres and artist details.

## Request
- **Method:** GET
- **Path:** /songs/{songId}

## Response
- **Body**
  ```json
  {
    "id": {songId},
    "title": "Song Title",
    "artist": {
      "id": 456,
      "name": "Artist Name",
      "age": 30,
      "bio": "Artist Bio"
    },
    "album": "Album Name",
    "length": 180,
    "genres": [
      {
        "id": 789,
        "description": "Genre 1"
      },
      {
        "id": 123,
        "description": "Genre 2"
      }
    ]
  }
  ```
- **Status Code:** 200 OK


### Search songs by genre

# Search songs by genre

## Description
This ticket requests the implementation of a route that allows searching songs by genre.

## Request
- **Method:** GET
- **Path:** /songs?genre={genreId}

## Response
- **Body**
  ```json
  {
    "songs": [
      {
        "id": 123,
        "title": "Song 1",
        "artist_id": 456,
        "album": "Album 1",
        "length": 180
      },
      {
        "id": 789,
        "title": "Song 2",
        "artist_id": 456,
        "album": "Album 2",
        "length": 240
      }
    ]
  }
  ```
- **Status Code:** 200 OK




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
