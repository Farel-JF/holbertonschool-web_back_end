#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """Retrieves a page of the dataset starting from the given index."""
        start_index = index if index is not None else 0
        end_index = start_index + page_size - 1
        size_data = len(self.dataset())

        assert start_index >= 0
        assert end_index < size_data

        current_page = [self.dataset()[i] for i in range(start_index,
                                                         min(end_index + 1,
                                                             size_data))]

        next_index = end_index + 1

        return {
            'index': start_index,
            'data': current_page,
            'page_size': page_size,
            'next_index': next_index
        }
