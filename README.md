# pharmaML

# PharmaML API

This FastAPI application provides endpoints to fetch product demand for the current or a specified week and to calculate the reorder point for products.

## Available Routes

# PharmaML API

This FastAPI application provides various endpoints to manage and analyze product demand, supplier scores, reorder points, and other inventory-related data.

## Available Routes

### 1. Home Page
- **Endpoint**: [`GET /`](https://pharma-ml.vercel.app/)
- **Description**: Displays a welcome message on the home page.
- **Example Request**: [https://pharma-ml.vercel.app/](https://pharma-ml.vercel.app/)
- **Example Response**:
  ```plaintext
  Welcome to Home Page


### 2. Get Product Demand for the Current or Specified Week
- **Endpoint**: [`GET /product-demand`](https://pharma-ml.vercel.app/product-demand)
- **Description**: Fetches the product demand for the current week if no query parameter is specified. You can also specify a week number (from 1 to 18) to retrieve demand for that week.
- **Query Parameter**:
  - `week` (optional, integer): The week number for which you want to fetch demand. Must be between 1 and 18.
- **Example Request**: [https://pharma-ml.vercel.app/product-demand?week=3](https://pharma-ml.vercel.app/product-demand?week=3)
- **Example Response**:
  ```json
  {
    "Paracetamol": {"demand": 500},
    "Aspirin": {"demand": 300}
  }
