from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """
    LFU (Least Frequently Used) caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the LFU cache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Store an item in the cache, applying the LFU and LRU algorithms as needed.

        Args:
            key: The key for the cache entry.
            item: The item to be stored in the cache.

        Note:
            If 'key' or 'item' is None, this method does nothing.
            If the number of items exceeds BaseCaching.MAX_ITEMS, it applies LFU and LRU.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find and discard the LFU item(s)
            lfus = [(k, v['count']) for k, v in self.cache_data.items()]
            lfus.sort(key=lambda x: x[1])
            min_count = lfus[0][1]
            lfu_items = [k for k, v in self.cache_data.items() if v['count'] == min_count]

            if len(lfu_items) > 1:
                # If there is a tie for LFU, apply LRU and discard the least recently used among the LFU items
                lru_item = min(lfu_items, key=lambda x: self.cache_data[x]['access_time'])
                lfu_items.remove(lru_item)
                print(f"DISCARD: {lru_item}\n")

            for lfu_item in lfu_items:
                del self.cache_data[lfu_item]

        self.cache_data[key] = {'item': item, 'count': 0, 'access_time': self.access_time}
        self.access_time += 1

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with 'key' if it exists, or None if 'key' is None or not found in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Increment the access count for the accessed item
        self.cache_data[key]['count'] += 1
        return self.cache_data[key]['item']

