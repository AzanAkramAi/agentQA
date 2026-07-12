# Backend

This folder contains the Python calculator API.

## What it does
- Exposes a `/calculate` endpoint.
- Accepts JSON input from the frontend.
- Performs arithmetic and scientific calculations.
- Returns results as JSON.

## Supported operations
- add
- subtract
- multiply
- divide
- sin
- cos
- tan
- sqrt
- square
- cube

## Notes
- Trigonometric functions use degrees.
- Square root rejects negative numbers.
- Division by zero is blocked with an error response.
