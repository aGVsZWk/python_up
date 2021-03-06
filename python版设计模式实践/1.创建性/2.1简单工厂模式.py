# -*- coding: utf-8 -*-
# author: Luke

# 工厂模式：可以通过工厂类创建产品
import random


class BasicCourse(object):
    """
    基础课程
    """

    def get_labs(self):
        return 'basic_course: labs'

    def __str__(self):
        return 'BasicCourse'


class ProjectCourse(object):
    """
    项目课
    """

    def get_labs(self):
        return 'project_course: labs'

    def __str__(self):
        return 'ProjectCourse'


class SimpleCourseFactory(object):
    """简单工厂， 用于创建课程"""

    @staticmethod
    def create_course(type):
        if type == 'bc':
            return BasicCourse()
        elif type == 'pc':
            return ProjectCourse()


if __name__ == '__main__':
    t = random.choice(['bc', 'pc'])
    course = SimpleCourseFactory.create_course(t)
    print(course.get_labs())
