import uvicorn
from fastapi import FastAPI
from database.database import DBConnection

app = FastAPI()

@app.get('/')
async def root():
    return {'message':'backend'}

@app.get('/test')
async def test():
    dbconn = DBConnection()

    engine = dbconn.get_engine(
        dbconn.creds['pguser'],
        dbconn.creds['pgpasswd'],
        dbconn.creds['pghost'],
        dbconn.creds['pgport'],
        dbconn.creds['pgdb']
    )
    print(engine.has_table('test'))
    return(engine.has_table('test'))


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)