#  Artificial Pancreas System

A simplified Python model simulating **data-driven glucose regulation**, designed to represent how an **artificial pancreas** might monitor and adjust glucose levels based on food intake, exercise, and insulin response.

>  **Note:** This version includes only the implementation of the `ArtificialPancreasSystem` class.
> Unit tests using **pytest** will be implemented in a later stage.

---

##  Project Structure

```
main/
│
├── __init__.py
├── artificial_pancreas.py     # Contains the ArtificialPancreasSystem class
│
tests/
│
├── __init__.py
├── test_artificial_pancreas.py  # (To be implemented later)
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

##  Overview

The **ArtificialPancreasSystem** simulates glucose regulation by modeling the relationship between **carbohydrate intake**, **physical activity**, and **insulin dosage**.

It helps demonstrate:

* Basic **OOP (Object-Oriented Programming)** in Python
* Simple **data-driven decision logic**
* Good software structure (using `main/` and `tests/` directories)
* Foundation for future **unit testing (pytest)**

---

## ⚙️ Class: `ArtificialPancreasSystem`

### Class Constants

```python
GLUCOSE_PER_CARB = 0.5       # Increase in glucose per carb unit
GLUCOSE_BURN_PER_MIN = 0.3   # Decrease in glucose per exercise minute
min_glucose_level = 50       # Minimum glucose level cap
```

### Attributes

| Attribute             | Type  | Description                  |
| --------------------- | ----- | ---------------------------- |
| `glucose_level`       | float | Current glucose reading      |
| `insulin_sensitivity` | float | Strength of insulin’s effect |
| `target_glucose`      | float | Ideal glucose target         |
| `tolerance`           | float | Acceptable deviation range   |

---

## 🔍 Methods

### `__init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10)`

Initializes the system with given parameters.

---

### `meal(self, carbs)`

Simulates a meal event and increases glucose level.

**Example:**

```python
controller.meal(40)
# Output: Glucose level after eating is <new_value>
```

**Validation:** Raises `ValueError` if carbs input is not numeric.

---

### `exercise(self, duration)`

Simulates an exercise event and decreases glucose level.

**Example:**

```python
controller.exercise(20)
# Output: Glucose level after exercising is <new_value>
```

* Ensures glucose does not fall below 50 (safety cap).
* Raises `ValueError` if duration is not numeric.

---

### `predict_action(self)`

Predicts whether to:

* **Deliver insulin** (if glucose > target + tolerance)
* **Warn of low glucose** (if glucose < target + tolerance)
* **Maintain** (if within target range)

**Returns:**

```python
("deliver_insulin", new_glucose_level)
```

or a string message like `"Warning low glucose!!!"`

---

### `Total_insulin_delivered (property)`

Reports the total insulin administered based on dosage and sensitivity.

**Example:**

```python
controller.Total_insulin_delivered
# Output: Administered <value> dosage of insulin
```

---

## Example Run

```python
print("=============Testing code===================")

controller = ArtificialPancreasSystem(100, 1.0, 100, 10)
controller.meal(40)
controller.exercise(20)
action, level = controller.predict_action()
controller.Total_insulin_delivered
print(action, level)
```

**Sample Output:**

```
=============Testing code===================
Glucose level after eating is 120.0
Glucose level after exercising is 114.0
The insulin dose is 14.0
Total insulin delivered is 14.0
deliver_insulin 100.0
```

---

##  Next Steps (Planned)

* [ ] Implement unit tests in `tests/test_artificial_pancreas.py` using **pytest**
* [ ] Automate testing via GitHub Actions CI
* [ ] Add input validation enhancements

---

##  Setup Instructions

### 1. Create & Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate       # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Program

```bash
python main/artificial_pancreas.py
```

---

##  requirements.txt

```text
pytest
```

---

##  .gitignore

```text
__pycache__/
*.pyc
.venv/
.env
.ipynb_checkpoints/
```

---

##  Git Workflow Summary

1. Create a public repo named:

   ```
   de-week2-unittest-<yourname>
   ```

2. Initialize on `main`, then create a branch:

   ```bash
   git checkout -b feature/week2-unittest
   ```

3. Commit changes with clear messages:

   ```bash
   git add .
   git commit -m "feat: implement ArtificialPancreasSystem class"
   ```

4. Push your branch:

   ```bash
   git push -u origin feature/week2-unittest
   ```

5. Open a Pull Request:
   `feature/week2-unittest → main`

6. Merge when complete (optional).

---

## Author

**Name:** Salome Akpan
**GitHub:** [Sallie25](https://github.com/Sallie25)
**Project:** Week 2 — Unit Testing Assignment


