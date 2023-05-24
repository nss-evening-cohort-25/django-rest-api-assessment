# Self-Assess Your Django Competencies

## 🐟 Tuna Piano API

This API enables developers to create applications that provide song recommendations based on genre. It manages artists, their songs, and the associated genre for each song.

Let's make millions! 💰 💰 💰

### Setup

1. Clone the template repository.
2. Navigate to the created directory using `cd`.
3. Activate the Pipenv environment with `pipenv shell`.
4. Install the dependencies using `pipenv install`.
5. Open the project in Visual Studio Code.
6. Ensure that the correct interpreter is selected.
7. Implement the code.

### MVP Routes by Entity

These are all the available routes for this API. Each route has an associated ticket containing the following information:
- Route description.
- Request structure:
    - HTTP method.
    - Route path.
    - JSON body (if applicable).
- Response structure:
    - JSON body (if applicable).
    - Status code.

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

These are examples of stretch goals that you can tackle once you have been MVP approved for the above features!

- Plan and Build the Frontend for the MVP routes
- [Popular genres: Retrieve a list of genres based on the number of associated songs](./documentation/issue-tickets/Popular-genres.md)
- [Related artists: Retrieve artists with similar genres](./documentation/issue-tickets/Related-artists.md)
- [Search songs by genre](./documentation/issue-tickets/Search-songs-by-genre.md)
- [Search artists by genre](./documentation/issue-tickets/Search-artists.md)
- Search all entities by (name/title/description)

## Data Design

![ERD Picture](https://github.com/TrinityChristiana/django-api-assessment/assets/31781724/a39bab27-bc1e-4a42-9ecc-ab96130bb509)
- [Link to ERD Docs](https://dbdocs.io/trinitycterry/Tuna-Piano-API?view=relationships)
