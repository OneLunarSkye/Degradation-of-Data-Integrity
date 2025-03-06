# Degradation-of-Data-Integrity
This project solves a system of linear differential equations representing the data flow between two processors, A and B, each with 100MB of memory. The data is pumped between the two processors, where processor A gains 3MB/sec from processor B and loses 2MB/sec to processor B, and vice versa.

## Project Overview

- **Problem**: The system simulates data flow in two processors over time, using a system of differential equations.
- **Objective**: Solve and plot the evolution of data in both processors over time.
- **Key Components**: 
    - Processor A (x1)
    - Processor B (x2)
    - Differential Equations Governing Data Flow

## Mathematical Model

The system of differential equations representing the data flow is given by:

- \( \dot{x1}(t) = 3x2(t) - 2x1(t) \)
- \( \dot{x2}(t) = -3x2(t) + 2x1(t) \)

Where:
- \( x1(t) \) represents the amount of data in processor A at time t.
- \( x2(t) \) represents the amount of data in processor B at time t.

## Project Structure

1. **Define the differential equations**: Define the equations for the rate of change of data in both processors.
2. **Initial Conditions**: Set initial values for \( x1 \) and \( x2 \), such as \( x1(0) = 1 \) and \( x2(0) = 1 \).
3. **Solve the System**: Use numerical integration to solve the system using `odeint` from the `scipy.integrate` library.
4. **Plot the Results**: Plot the evolution of data in processors A and B over time.
5. **Animation (Optional)**: Animate the results to visualize the data flow more dynamically.

## Requirements

- Python 3.x
- `numpy` (for numerical operations)
- `matplotlib` (for plotting)
- `scipy` (for solving the differential equations)

You can install the necessary packages using:

```bash
pip install numpy matplotlib scipy
