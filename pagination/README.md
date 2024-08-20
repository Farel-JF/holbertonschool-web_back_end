Pagination and Hypermedia Pagination in Python
This project includes several Python scripts that demonstrate pagination techniques for handling datasets. The goal is to paginate data efficiently and handle edge cases such as data deletion and hypermedia pagination. The project consists of four modules:

Simple Helper Function
Simple Pagination
Hypermedia Pagination
Deletion-Resilient Hypermedia Pagination
1. Simple Helper Function
File: 0-simple_helper_function.py

This module provides a helper function for calculating index ranges for pagination.

index_range(page: int, page_size: int) -> tuple
Arguments:
page: The page number (1-indexed).
page_size: The number of items per page.
Returns: A tuple containing the start and end index for pagination.
Example Usage:

python
Copy code
from 0-simple_helper_function import index_range

print(index_range(1, 7))  # Output: (0, 7)
print(index_range(3, 15)) # Output: (30, 45)
2. Simple Pagination
File: 1-simple_pagination.py

This module defines a Server class that uses the CSV file Popular_Baby_Names.csv for pagination.

Server Class
Methods:
dataset() -> List[List]: Loads and caches the dataset from the CSV file.
get_page(page: int = 1, page_size: int = 10) -> List[List]: Retrieves a page of data based on the page number and page size.
Example Usage:

python
Copy code
from 1-simple_pagination import Server

server = Server()
print(server.get_page(1, 3)) # Retrieves the first page with 3 items per page
3. Hypermedia Pagination
File: 2-hypermedia_pagination.py

This module extends the Server class to include hypermedia pagination features.

Server Class
Additional Method:
get_hyper(page: int = 1, page_size: int = 10) -> Dict[str, Any]: Retrieves pagination information and data for the specified page.
Example Usage:

python
Copy code
from 2-hypermedia_pagination import Server

server = Server()
print(server.get_hyper(1, 2)) # Retrieves hypermedia information for page 1 with 2 items per page
4. Deletion-Resilient Hypermedia Pagination
File: 3-hypermedia_del_pagination.py

This module provides a deletion-resilient hypermedia pagination technique, handling cases where rows might be deleted between queries.

Server Class
Additional Methods:
indexed_dataset() -> Dict[int, List]: Returns a dataset indexed by position.
get_hyper_index(index: int = None, page_size: int = 10) -> Dict[str, Any]: Retrieves a page of data starting from the given index and handles deletions gracefully.
Example Usage:

python
Copy code
from 3-hypermedia_del_pagination import Server

server = Server()
print(server.get_hyper_index(3, 2)) # Retrieves data starting from index 3 with 2 items per page
CSV Data File
File: Popular_Baby_Names.csv
This CSV file contains data about popular baby names. It includes columns such as Year of Birth, Gender, Ethnicity, Child's First Name, Count, and Rank.
Running Tests
To test the functionality of each module, you can run the corresponding main script:

Simple Pagination:

sh
Copy code
python3 1-main.py
Hypermedia Pagination:

sh
Copy code
python3 2-main.py
Deletion-Resilient Hypermedia Pagination:

sh
Copy code
python3 3-main.py
