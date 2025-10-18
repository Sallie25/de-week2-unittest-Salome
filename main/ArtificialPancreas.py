class ArtificialPancreasSystem:

    GLUCOSE_PER_CARB = 0.5      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise
    min_glucose_level = 50

    """A simplified model for data-driven glucose regulation.

    Attributes:
    glucose_level (float): The current glucose reading of the person. Defaults to 100, but can be set to a different starting value.

    insulin_sensitivity (float): How strongly insulin affects the glucose drop. Higher values indicate more sensitivity. Defaults to 1.0.

    target_glucose (float): The ideal glucose level the system is trying to maintain. Defaults to 100.

    tolerance (float): The small range above or below the target where the glucose level is considered stable. Defaults to 10.
    """

    def __init__(self, glucose_level:float, insulin_sensitivity:float=1.0, target_glucose:float=100, tolerance:float=10):
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance


    def meal(self, carbs: float):

        """Simulate a meal event (input feature: carbs)."""
        if not isinstance(carbs, (float,int)):
          raise ValueError("Type in a Number!")

        else:
          self.glucose_level += float(carbs) * self.GLUCOSE_PER_CARB

          print(f"Glucose level after eating is {self.glucose_level}")

          return self.glucose_level


    def exercise(self, duration: float):
        """Simulate physical activity (input feature: duration).

        -- glucose_level -= duration * GULCOSE_BURN_PER_MIN

        -- make sure glucose never goes unrealistically low, you can cap it at 50"""

        if not isinstance(duration, (float,int)):
          raise ValueError("Type in a Number!")

        else:
          self.glucose_level -= float(duration) * self.GLUCOSE_BURN_PER_MIN

        # We do not want to report an unreasonably low Glucose level - glucose level capped at 50
          if self.glucose_level < 50:
            self.glucose_level = self.min_glucose_level

          print(f"Glucose level after exercising is {self.glucose_level}")

          return self.glucose_level


    def predict_action(self):
            """
            Predict and apply an appropriate system action.
            Acts like a decision function in a model.
            """
            if self.glucose_level > self.target_glucose + self.tolerance:

              # the insulin dose is based on how much above the target the glucose is
              self.dosage = abs(self.glucose_level - self.target_glucose)

              print(f"The insulin dose is {self.dosage}")

              # After giving insulin, subtract the dose from the current glucose level
              self.glucose_level = self.glucose_level - self.dosage

              return "deliver_insulin", self.glucose_level

            elif self.glucose_level < self.target_glucose + self.tolerance:
              return "Warning low glucose!!!"

            else:
              return "maintain"

            return self.glucose_level

    @property
    def Total_insulin_delivered(self):
      print(f"Total insulin delivered is {self.dosage * self.insulin_sensitivity}")
      return f"Administered {self.dosage * self.insulin_sensitivity} dosage of insulin"

print("=============Testing code===================")

controller = ArtificialPancreasSystem(100, 1.0, 100, 10)
controller.meal(40)
controller.exercise(20)
action, level = controller.predict_action()
controller.Total_insulin_delivered
print(action, level)