

import asyncio
import logs.flightreview as fr
import drone.connect_drone as cd


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(fr.run(cd))