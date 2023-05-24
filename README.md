# Self-Assess Your Django Competencies

## 🐟 Tuna Piano API

This API will allow developers to build applications that recommend songs based on a provided genre. It will manage artists, songs produced by those artists, and the genre for each song.

We'll make millions 💰 💰 💰


### Setup

1. Clone the template repository
2. `cd` to the directory it creates
3. `pipenv shell`
4. `pipenv install`
5. Open in VS Code
6. Make sure the correct interpreter is selected
7. Implement the code


### MVP Routes by Entity

Here are all the possible routes for this API.

Each route has a ticket associated with it that lists the following information:
- Description of the route,
- What the request should look like
    - Method Verb
    - Route Path
    - JSON Body - (if applicable)
- What the response should look like
    - JSON Body (if applicable)
    - Status Code

#### 🎶 Songs

- Create a Song
- Delete a Song
- Update a Song
- View a List of all the Songs
- Details view of a single Song and its associated genres and artist details

#### 👩🏾‍🎤 Artists

- Create an Artist
- Delete an Artist
- Update an Artist
- View a List of all the Artists
- Details view of a single Artist and the songs associated with them

#### 🎸 Genres

- Create a Genre
- Delete a Genre
- Update a Genre
- View a List of all the Genres
- Details view of a single Genre and the songs associated with it


### Stretch Goals
- Plan out and Build out the Frontend for the MVP routes
- Popular genres to see a list of genres based on the number of songs associated with each genre
- See related artists with similar genres
- Search artists by genre
- Search songs by genre
- Search all entities by (name/title/description)*


The artist response should include the total number of songs in the database for the artist. It should also include a serialized list of all related songs _(see example below)_.

## Data Design

![ERD Picture](https://github.com/TrinityChristiana/django-api-assessment/assets/31781724/a39bab27-bc1e-4a42-9ecc-ab96130bb509)
- [Link to ERD Docs](https://dbdocs.io/trinitycterry/Tuna-Piano-API?view=relationships)
