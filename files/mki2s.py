rename_process("mki2s")
be.api.setvar("return", "1")
vr("opts", be.api.xarg())
vr("i2sbus", None)
vr("bck", None)
vr("ws", None)
vr("dout", None)

if "b" in vr("opts")["o"]:
    vr("bck", vr("opts")["o"]["b"])
elif "bck" in vr("opts")["o"]:
    vr("bck", vr("opts")["o"]["bck"])
if vr("bck") is not None:
    vr("bck", be.devices["gpiochip"][0].pin(vr("bck"), force=True))

if "w" in vr("opts")["o"]:
    vr("ws", vr("opts")["o"]["w"])
elif "ws" in vr("opts")["o"]:
    vr("ws", vr("opts")["o"]["ws"])
if vr("ws") is not None:
    vr("ws", be.devices["gpiochip"][0].pin(vr("ws"), force=True))

if "d" in vr("opts")["o"]:
    vr("dout", vr("opts")["o"]["d"])
elif "dout" in vr("opts")["o"]:
    vr("dout", vr("opts")["o"]["dout"])
if vr("dout") is not None:
    vr("dout", be.devices["gpiochip"][0].pin(vr("dout"), force=True))


if vr("bck") is None:
    term.write("Invalid BCK pin!")
if vr("ws") is None:
    term.write("Invalid WS pin!")
if vr("dout") is None:
    term.write("Invalid DOUT pin!")

if vr("bck") is not None and vr("ws") is not None and vr("dout") is not None:
    import audiobusio

    try:
        vr("i2sbus", audiobusio.I2SOut(vr("bck"), vr("ws"), vr("dout")))
    except:
        term.write("Failed to create I2S bus!")
    del audiobusio

if vr("i2sbus") is not None:
    be.based.run("mknod i2s")
    vr("node", be.api.getvar("return"))
    be.api.subscript("/bin/stringproccessing/devid.py")
    be.devices["i2s"][vr("dev_id")] = vr("i2sbus")
    dmtex("I2S bus registered at /dev/i2s" + str(vr("dev_id")))
    be.api.setvar("return", "0")
