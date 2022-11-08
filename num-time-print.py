import asyncio
from random import randint

async def number( value: int ) -> None:
    await asyncio.sleep( value )
    print( value )

async def num_printer( count: int ) -> None:
    await asyncio.gather( *(
        number( randint( 0, count ) ) for _ in range( count )
    ) )

asyncio.run( num_printer( 30 ) )
