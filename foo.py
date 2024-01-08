import pytest
import asyncio


@pytest.fixture(scope='session')
async def foo():
    print(asyncio.get_running_loop())
    yield asyncio.get_running_loop()


async def test_foobar(foo):
    print(asyncio.get_running_loop())
    print(foo)
    assert foo == asyncio.get_running_loop()
