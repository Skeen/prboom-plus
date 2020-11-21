from fastapi import FastAPI, Form
import json
import asyncio

with open("e1m1tas.json", "r") as f:
    pload = json.load(f)

tics = pload['tics']


app = FastAPI()


@app.post("/tick")
async def root(f: int = Form(None), x: int = Form(None), y: int = Form(None), z: int = Form(None), a: int = Form(None)):
    print("f", "=", f)
    print("x", "=", x)
    print("y", "=", y)
    print("z", "=", z)
    print("a", "=", a)

    try:
        forward, side, angle, buttons = tics[f]
    except:
        forward, side, angle, buttons = (0,0,0,0)
    exit = 0
    angle = angle * 256

    print()
    print("FRAME", f)
    print("forward", forward)
    print("side", side)
    print("angle", angle)
    print("buttons", buttons)
    print("exit", exit)

    if f == 1000:
        exit = 1
    return f"{forward} {side} {angle} {buttons} {exit}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5123)
