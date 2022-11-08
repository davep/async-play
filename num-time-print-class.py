import asyncio
from random import randint
from typing import Generator

async def number( value: int ) -> None:
    await asyncio.sleep( value )
    print( value )

class NumPrinter:

    def __init__( self, count: int ) -> None:
        self._count = count

    def __await__( self ) -> Generator[ None, None, None ]:
        async def num_printer() -> None:
            await asyncio.gather( *(
                number( randint( 0, self._count ) ) for _ in range( self._count )
            ) )
        return num_printer().__await__()

async def main():
    await NumPrinter( 30 )

asyncio.run( main() )
