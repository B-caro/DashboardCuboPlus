from fastapi import FastAPI
import subprocess
import json 

app = FastAPI()

@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
    
@app.get("/test")
async def root():
    container_name = "lnd-lnd-1"  
    flag = "listaddresses"
    json_output = execCommand(container_name, flag)
    return json_output

@app.get("/api/getInfo")
async def root():
    container_name = "lnd-lnd-1"  
    flag = "getinfo"
    json_output = execCommand(container_name, flag)
    return json_output

@app.get("/api/walletBalance")
async def root():
    container_name = "lnd-lnd-1"  
    flag = "walletbalance"
    json_output = execCommand(container_name, flag)
    return json_output

@app.get("/api/getChannels")
async def root():
    container_name = "lnd-lnd-1"  
    flag = "listchannels"
    json_output = execCommand(container_name, flag)
    return json_output

@app.get("/api/getNodeInfo")
async def root():
    container_name = "lnd-lnd-1"  
    flag = "listchannels"
    json_output = execCommand(container_name, flag)
    return json_output

@app.get("/api/getChannelBalance")
async def root():
    container_name = "lnd-lnd-1"  
    flag = "channelbalance"
    json_output = execCommand(container_name, flag)
    return json_output


def execCommand(container_name, command):
    command = ["docker", "exec", "-it", container_name, "lncli", "-n", "signet", command]
    output = subprocess.check_output(command)
    clean_output = output.decode().replace("\n", "").replace("\t", "").replace("\r", "")
    json_output = json.loads(clean_output)
    return json_output