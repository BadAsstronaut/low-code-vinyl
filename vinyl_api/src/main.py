'''
FastAPI entrypoint
'''

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Works!'}


@app.get('/health')
async def health():
    return
