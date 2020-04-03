import asyncio
#import asyncio_dgram
try:
    from .aio import DatagramStream, DatagramServer, DatagramClient, Protocol
except Exception: #ImportError
    from aio import DatagramStream, DatagramServer, DatagramClient, Protocol
import time
try:
    from .wizlight import wizlight, PilotBuilder
except Exception: #ImportError
    from wizlight import wizlight, PilotBuilder
import logging
import sys

# python3 -m wiz_light.test

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

_LOGGER = logging.getLogger(__name__)

async def testbulb(bulb):
	wait_secs=10

	state = await bulb.updateState()

	if state.get_state(): # check if on
		await asyncio.wait_for(bulb.turn_off(), wait_secs)
	await asyncio.sleep(0.5)
	await asyncio.wait_for(bulb.lightSwitch(), wait_secs)
	await asyncio.sleep(0.5)
	await asyncio.wait_for(bulb.turn_off(), wait_secs)
	await asyncio.sleep(0.5)
	await asyncio.wait_for(bulb.turn_on(PilotBuilder(brightness = 255)), wait_secs)
	await asyncio.sleep(0.5)
	await asyncio.wait_for(bulb.turn_on(PilotBuilder(brightness = 50)), wait_secs)
	await asyncio.sleep(0.5)
	await asyncio.wait_for(bulb.turn_on(PilotBuilder(rgb = (50, 100, 200))), wait_secs)
	await asyncio.sleep(0.5)
	await asyncio.wait_for(bulb.turn_on(PilotBuilder(colortemp = 4000)), wait_secs)
	await asyncio.sleep(0.5)
	await asyncio.wait_for(bulb.turn_on(PilotBuilder(colortemp = 6500)), wait_secs)
	await asyncio.sleep(0.5)
	await asyncio.wait_for(bulb.turn_on(PilotBuilder(scene = 14)), wait_secs)
	await asyncio.sleep(0.5)
	await asyncio.wait_for(bulb.turn_on(PilotBuilder(scene = 24)), wait_secs)
	await asyncio.sleep(0.5)
	await asyncio.wait_for(bulb.turn_off(), wait_secs)

	state = await bulb.updateState()
	print(state.get_state())
	print(state.get_scene())
	print(state.get_scene())
	print(state.get_warm_white())
	print(state.get_speed())
	print(state.get_cold_white())
	print(state.get_rgb())
	print(state.get_brightness())
	print(state.get_colortemp())
		

async def run_bulb_automation():
	loop = asyncio.get_event_loop()
	bulb1 = wizlight('192.168.15.64')
	# await asyncio.gather(testbulb(bulb1), testbulb(bulb2), loop = loop)
	state = await bulb1.updateState()
	await bulb1.turn_on(PilotBuilder(scene = 14))
	state = await bulb1.updateState()
	await asyncio.sleep(0.5)
	await bulb1.turn_on(PilotBuilder()) #rhythm
	state = await bulb1.updateState()

if __name__ == '__main__':	
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_bulb_automation())
        loop.close()
