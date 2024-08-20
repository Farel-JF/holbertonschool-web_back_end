#!/usr/bin/env python3
"""Module for server pagination using a CSV file."""

import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """Calculates the start and end index for a given page and page size.
    Args:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.
    Returns:
    tuple: A tuple containing the start index and end index for pagination."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, stop = index_range(page, page_size)
        dataset = self.dataset()

        if len(dataset) <= start:
            return []

        return dataset[start:stop]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Retrieves hypermedia pagination information for a page of the dataset.
        Args:
        page (int): The page number (1-indexed). Default is 1.
        page_size (int): The number of items per page. Default is 10.
        Returns:
        Dict[str, Any]: A dictionary containing pagination information."""
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
