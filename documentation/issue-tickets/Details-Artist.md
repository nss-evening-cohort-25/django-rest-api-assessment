# Retrieve details of a single artist with associated songs

## Description
This ticket requests the implementation of a route that retrieves the details of a single artist, including the songs associated with them.

## Request
- **Method:** GET
- **Path:** /artists/{artistId}

## Response if Artist exists
- **Body**
  ```json
  {
    "id": {artistId},
    "name": "Artist Name",
    "age": 25,
    "bio": "Artist Bio",
    "song_count": 9,
    "songs": [
      {
        "id": 123,
        "title": "Song 1",
        "album": "Album 1",
        "length": 180
      },
      {
        "id": 456,
        "title": "Song 2",
        "album": "Album 2",
        "length": 240
      }
    ]
  }
  ```
- **Status Code:** 200 OK

## Response if Artist doesn't exist
- **Status Code:** 404 Not Found
