rename_process("rmi2s")
vr("opts", be.api.xarg())
be.api.setvar("return", "1")
if len(vr("opts")["w"]):
    vr("dev", vr("opts")["w"][0])
    if vr("dev").startswith("/dev/i2s"):
        vr("dev", vr("dev")[5:])
        vr("node", vr("dev"))
        vr("ok", False)
        be.api.subscript("/bin/stringproccessing/devid.py")
        if (
            vr("ok")
            and "i2s" in be.devices.keys()
            and vr("dev_name") == "i2s"
            and vr("dev_id") in be.devices["i2s"].keys()
        ):
            be.devices["i2s"][vr("dev_id")].stop()
            be.devices["i2s"][vr("dev_id")].deinit()
            del be.devices["i2s"][vr("dev_id")]
            be.api.setvar("return", "0")
        else:
            term.write("Invalid I2S bus!")
    else:
        term.write("Invalid I2S bus!")
else:
    term.write("No bus specified.")
