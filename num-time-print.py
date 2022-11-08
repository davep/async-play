import asyncio
from random import randint

async def number( value: int ) -> int:
    await asyncio.sleep( value )
    print( value )
    return value

async def num_printer( count: int ) -> list[ int ]:
    return await asyncio.gather( *(
        number( randint( 0, count ) ) for _ in range( count )
    ) )

print( asyncio.run( num_printer( 30 ) ) )
