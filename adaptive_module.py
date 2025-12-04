# # adaptive_engine.py

# import math
# import random
# from collections import defaultdict, deque

# DIFFICULTY_MAP = {
#     "easy": -1.0,
#     "medium": 0.0,
#     "hard": 1.0
# }

# class AdaptiveEngine:
#     """
#     Adaptive Engine for CAT-lite.
#     Handles:
#       - theta (ability) updates
#       - dynamic difficulty control
#       - topic balancing
#     """

#     def __init__(self, 
#                  initial_theta=0.0, 
#                  K=0.2, 
#                  topic_history_limit=5):

#         self.theta = initial_theta
#         self.K = K

#         # kept for compatibility, but not used in new logic
#         self.topic_usage = defaultdict(int)

#         # cooldown topic memory
#         self.recent_topics = deque(maxlen=topic_history_limit)


#     # -------------------------------
#     # 1) THETA UPDATE
#     # -------------------------------


#     # def update_theta(self, difficulty, result):
#     #     expected = self.compute_expected(difficulty)
#     #     self.theta += self.K * (result - expected)
#     #     return self.theta


#     def compute_expected(self, difficulty):
#         return 1 / (1 + math.exp(difficulty - self.theta))

#     def update_theta(self, difficulty, result):
#         # difficulty will be string ("easy", "medium", "hard")
#         difficulty_value = self.DIFFICULTY_MAP[difficulty]

#         expected = self.compute_expected(difficulty_value)
#         self.theta += self.K * (result - expected)
#         return self.theta

#     # -------------------------------
#     # 2) DIFFICULTY CONTROL
#     # -------------------------------
#     def select_difficulty(self):
#         if self.theta < -0.5:
#             return "easy"
#         elif self.theta < 0.5:
#             return "medium"
#         else:
#             return "hard"


#     # -------------------------------
#     # 3) TOPIC BALANCING (UPDATED)
#     # -------------------------------
#     def select_topic(self, available_topics):
#         """
#         New topic balance: ONLY cooldown avoidance.
#         """

#         # Try selecting a topic not recently used
#         filtered = [t for t in available_topics if t not in self.recent_topics]

#         if filtered:
#             selected = random.choice(filtered)
#         else:
#             # fallback if all topics recently used
#             selected = random.choice(available_topics)

#         # store in cooldown history
#         self.recent_topics.append(selected)

#         return selected

#     # -------------------------------
#     # 4) NEXT QUESTION CONTROL
#     # -------------------------------
#     def get_next_question_spec(self, available_topics):
#         difficulty = self.select_difficulty()
#         topic = self.select_topic(available_topics)

#         return {
#             "difficulty": difficulty,
#             "topic": topic,
#             "theta": self.theta
#         }




import math
import random
from collections import defaultdict, deque

class AdaptiveEngine:

    DIFFICULTY_MAP = {
        "easy": -1.0,
        "medium": 0.0,
        "hard": 1.0
    }

    def __init__(self, initial_theta=0.0, K=0.2, topic_history_limit=5):
        self.theta = initial_theta
        self.K = K
        self.topic_usage = defaultdict(int)
        self.recent_topics = deque(maxlen=topic_history_limit)

    def compute_expected(self, difficulty_value):
        return 1 / (1 + math.exp(difficulty_value - self.theta))

    def update_theta(self, difficulty, result):
        difficulty_value = self.DIFFICULTY_MAP[difficulty]
        expected = self.compute_expected(difficulty_value)
        self.theta += self.K * (result - expected)
        return self.theta

    def select_difficulty(self):
        if self.theta < -0.5:
            return "easy"
        elif self.theta < 0.5:
            return "medium"
        else:
            return "hard"

    def select_topic(self, available_topics):
        filtered = [t for t in available_topics if t not in self.recent_topics]
        if filtered:
            selected = random.choice(filtered)
        else:
            selected = random.choice(available_topics)
        self.recent_topics.append(selected)
        return selected

    def get_next_question_spec(self, available_topics):
        difficulty = self.select_difficulty()
        topic = self.select_topic(available_topics)
        return {
            "difficulty": difficulty,
            "topic": topic,
            "theta": self.theta
        }
