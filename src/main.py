from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/')
async def test_get():
    return {"message": "ok"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)

