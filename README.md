# CinemaScope

<div style="color: red;">This is an experiment branch.</div>

The aim is to:

1. Shift the backend to Go **for faster performance & scalability**.
2. Introduce Vue (signals) in the frontend **for performance and ease**.
3. Improve ML solution **for making product actually useful**.
    - Use a quality data-set
    - Include more multi-media.
    - Use real-world algorithm.
    - Add account management.

> [!NOTE]
> May use `SurrealDB` for everthing.

**Takeaways** (or benefits):

Getting to learn these things are highly valuable:-

1. Working with Signals in JavaScript.
2. Creating backend with Go.
3. Streamlining data-collection and auto-updating relevant data.
4. Knowing how to work with Vector database.

## But what about the python code?

The core Python functions will remain as it, **Python code will not be obselete**; infact they will be improved to meet quality.

**It will be integrated as a microservice**. This is because the ML development still very much relies on Python due its mature echo-system. Hence, the Python functions will be consumed via APIs; which will be exposed via [FastAPI](https://fastapi.tiangolo.com/).

However,
**Flask will be removed** as FastAPI offers much developer-friendly experience on top of being faster and offering asynchronous functions.

## Roadmap

The below planning is divided into phases. It's a high-level overview.

Each phase should take maximum 1-2 months.

### #1 Architecture

Concurrently proceed with:

1. Replacing `Flask` with `Go`.
2. Expose existing Python functions as API; using `FastAPI`.

> [!NOTE]
> No need to modify `html` files, as `Go`'s templating syntax is almost same as `Jinja`.

#### Project Structure

```bash
.
├── core
├── microservice
├── main.go
├── README.md
└── templates
    ├── support
    └── addons
```

The project structure is different from usual. I went ahead and structured it according to what made most sense to me. **It represents how I think of the project.**

1. `core/`: contains controller or main program modules.
2. `microservice/`: virtual environment for FastAPI code.
3. `main.go`: binary for the application (entry point).
4. `templates/`: contains webpages to show.
    - `support/`: contains the static elements such as javascript and css files.
    - `addons`: contains stuff like images and fonts.

### #2 ML Solution

1. Create custom data-set by Streamlining the process of data-collection & automating its updation.
2. Use `Qdrant` as vector database; for training ML model. (NOT FINAL).
3. Research on improving algorithm; improve the algorithm for a single-user experience.

### #3 User Experience

1. Add `Vue` Signals to the frontend.
    - Break frontend into components to achieve better frontend code organisation.
    - Handle revelant things client-side with ease, as uptil now all things were being done by the server (WHICH IS ANNOYING).
2. Use `SurrealDB` for database and caching (NOT FINAL).
3. Implement account management for multi-user experience.

### #4 Polishing

Look for more improvements along the way, then implement them.

---

This can be a great final-year project.
