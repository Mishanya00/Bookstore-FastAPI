# Bookstore-FastAPI

## Project to practice from DeepSeek

**Final Project:**
Build a Bookstore API with:

- [ ] User auth
- [ ] CRUD for books
- [ ] Search by title/author
- [ ] Purchase system
- [ ] Automated docs

**Bonus:**

- Add Redis caching
- Implement WebSocket notifications

---

## Resources:

- Official Docs: https://fastapi.tiangolo.com/
- Testing Guide: https://testdriven.io/blog/fastapi-crud/
- Deployment: https://fastapi.tiangolo.com/deployment/

---

To launch application:

```bash
uvicorn src.main:app --reload
```

Note that *uvicorn src.main:app* will not work on Windows OS due to psycopg limitations
