import asyncio
from unittest import TestCase

import cat

async def herd(cat, direction):
    cat.pet()
    return await cat.move(direction)


class Tests(TestCase):

    def test_forward(self):
        garfield = cat.Cat('Garfield')
        result = asyncio.run(herd(garfield, 'forward'))
        self.assertTrue(result)





