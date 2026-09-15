def offTOon (dict):
    
    if dict["status"] == "offline":
        dict["status"] = "online"
        return dict
    else:
        return dict
servers= {
    "name": "0024Server",
    "storge": "64 Gg",
    "status": "offline"

}

status=offTOon(servers)
print(status)