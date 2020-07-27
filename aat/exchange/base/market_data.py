from abc import ABCMeta


class _MarketData(metaclass=ABCMeta):
    '''internal only class to represent the streaming-source
    side of a data source'''

    def instruments(self):
        '''get list of available instruments'''
        return []

    async def tick(self):
        '''return data from exchange'''
