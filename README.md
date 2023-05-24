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

- [Create a Song](./documentation/issue-tickets/Create-Song.md)
- [Delete a Song](./documentation/issue-tickets/Delete-Song.md)
- [Update a Song](./documentation/issue-tickets/Update-Song.md)
- [View a List of all the Songs](./documentation/issue-tickets/List-Songs.md)
- [Details view of a single Song and its associated genres and artist details](./documentation/issue-tickets/Details-Song.md)

#### 👩🏾‍🎤 Artists

- [Create an Artist](./documentation/issue-tickets/Create-an-Artist.md)
- [Delete an Artist](./documentation/issue-tickets/Delete-an-Artist.md)
- [Update an Artist](./documentation/issue-tickets/Update-an-Artist.md)
- [View a List of all the Artists](./documentation/issue-tickets/List-Artists.md)
- [Details view of a single Artist and the songs associated with them](./documentation/issue-tickets/Details-Artist.md)

#### 🎸 Genres

- [Create a Genre](./documentation/issue-tickets/Create-Genre.md)
- [Delete a Genre](./documentation/issue-tickets/Delete-Genre.md)
- [Update a Genre](./documentation/issue-tickets/Update-Genre.md)
- [View a List of all the Genres](./documentation/issue-tickets/List-Genres.md)
- [Details view of a single Genre and the songs associated with it](./documentation/issue-tickets/Details-Genre.md)


### Stretch Goals
- [Plan out and Build out the Frontend for the MVP routes](url)
- [Popular genres to see a list of genres based on the number of songs associated with each genre](./documentation/issue-tickets/Popular-genres.md)
- [See related artists with similar genres](./documentation/issue-tickets/Related-artists.md)
- [Search songs by genre](./documentation/issue-tickets/Search-songs-by-genre.md)
- [Search artists by genre](./documentation/issue-tickets/Search-artists.md)
- [Search all entities by (name/title/description)](url)*

## Data Design

![ERD Picture](https://github.com/TrinityChristiana/django-api-assessment/assets/31781724/a39bab27-bc1e-4a42-9ecc-ab96130bb509)
- [Link to ERD Docs](https://dbdocs.io/trinitycterry/Tuna-Piano-API?view=relationships)
