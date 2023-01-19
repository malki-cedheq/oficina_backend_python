# app.py
'''
Tarefas Assíncronas
--Sugerido uso de Celery--
'''

from flask import Flask
import asyncio
from datetime import datetime

app = Flask(__name__)


async def some_async_task():
    await asyncio.sleep(1)
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return {"async message": now}


@app.route("/", methods=["GET"])
async def home():
    result = await some_async_task()
    return result


if __name__ == "__main__":
    app.run(debug=True, port=8081)
