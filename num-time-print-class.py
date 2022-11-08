import asyncio
from random import randint
from typing import Generator

async def number( value: int ) -> int:
    await asyncio.sleep( value )
    print( value )
    return value

class NumPrinter:

    def __init__( self, count: int ) -> None:
        self._count = count

    def __await__( self ) -> Generator[ None, None, list[ int ] ]:
        async def num_printer() -> list[ int ]:
            return await asyncio.gather( *(
                number( randint( 0, self._count ) ) for _ in range( self._count )
            ) )
        return num_printer().__await__()

async def main():
    print( await NumPrinter( 30 ) )

asyncio.run( main() )
