
# RESTful Task Management API (Python)

## Overview
This project is a high-performance **Microservices-based API** designed for task management. It demonstrates the ability to build scalable web services using **Python** and **FastAPI**, with a strong focus on **automated testing** and **Object-Oriented Design (OOAD)**.

## Technical Highlights
* **Microservices Architecture:** Built with **FastAPI**, utilizing asynchronous request handling to ensure high scalability and low latency.
* **Automated xUnit Testing:** Implements a robust test suite using **Pytest** to perform automated unit tests, ensuring endpoint reliability and system stability.
* **Object-Oriented Design (OOAD):** Leverages **Pydantic** models for strict data schema validation, ensuring type safety and clean data handling.
* **Complexity Analysis:** * **GET /tasks**: $O(1)$ time complexity to return the task list.
    * **POST /tasks**: $O(1)$ time complexity for adding new records to the in-memory data store.
* **Interactive Documentation:** Automatically generates **OpenAPI (Swagger UI)** for seamless documentation and testing by platform contributors.



## Project Structure
* `main.py`: The core API logic, defining RESTful endpoints and data schemas.
* `test_main.py`: Automated xUnit-style test cases verifying the system's core functionality.

## How to Run
1.  **Install dependencies**:
    ```powershell
    pip install fastapi uvicorn pytest httpx
    ```
2.  **Start the API Server**:
    ```powershell
    uvicorn main:app --reload
    ```
3.  **Run Automated Tests**:
    ```powershell
    pytest
    ```

## Skills Demonstrated
`Python` `Microservices` `REST APIs` `Automated Testing (xUnit)` `OOAD` `Complexity Analysis`
