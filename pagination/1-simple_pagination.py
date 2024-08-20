#!/usr/bin/env python3
"""Module for server pagination using a CSV file."""

import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a dataset of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of the dataset based on pagination parameters.
        Args:
        page (int): The page number (1-indexed). Default is 1.
        page_size (int): The number of items per page. Default is 10.
        Returns:
        List[List]: A list of rows corresponding to the requested page."""
        assert isinstance(page, int) and page > 0,
        assert isinstance(page_size, int) and page_size > 0,

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        return dataset[start_index:end_index]
