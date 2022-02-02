from abc import ABC, abstractmethod


class AISession(ABC):
    def today_session(self):
        print("In Today's session")


class Feb2session(AISession):
    def today_session(self):
        print('OOPs concept Covered')


class Feb1session(AISession):
    def today_session(self):
        print('Flask concept Covered')


# Using Super() abstract method can also be invoked
class Jan31session(AISession):
    def today_session(self):
        super().today_session()
        print('CNN concept Covered')


# Driver Code
# Instance creation
Feb1_topic = Feb1session()
Feb1_topic.today_session()

Feb2_topic = Feb2session()
Feb2_topic.today_session()



Jan31_topic = Jan31session()
Jan31_topic.today_session()
