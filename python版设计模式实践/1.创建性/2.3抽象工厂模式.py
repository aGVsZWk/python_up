# -*- coding: utf-8 -*-


import random
import abc


class BasicCourse(object):
    """
    基础课程
    """

    def get_labs(self):
        return "basic course: labs"

    def __str__(self):
        return "BasicCourse"


class ProjectCourse(object):
    """
    项目课
    """

    def get_labs(self):
        return "project_course: labs"

    def __str__(self):
        return "ProjectCourse"


class Factory(metaclass=abc.ABCMeta):
    """
    抽象工厂类
    """
    @abc.abstractmethod
    def create_course(self):
        pass


class BasicCourseFactory(Factory):
    """
    基础课程工厂类
    """

    def create_course(self):
        return BasicCourse()


class ProjectCourseFactory(Factory):
    """
    项目课程工厂类
    """

    def create_course(self):
        return ProjectCourse()


def get_factory():
    """
    随机获取一个工厂类
    """
    return random.choice([BasicCourseFactory, ProjectCourseFactory])()


if __name__ == '__main__':
    factory = get_factory()
    course = factory.create_course()
    print(course.get_labs())


# 两种类型的课程
class BasicCourse(object):
    """
    基础课程
    """

    def get_labs(self):
        return "basic course: labs"

    def __str__(self):
        return "BasicCourse"


class ProjectCourse(object):
    """
    项目课
    """

    def get_labs(self):
        return "project_course: labs"

    def __str__(self):
        return "ProjectCourse"


class LinuxVm(object):
    """
    Linux 虚拟机
    """

    def start(self):
        return "Linux vm running"


class MacVm(object):
    """
    Mac OSX 虚拟机
    """

    def start(self):
        return "Mac OSX vm running"


class Factory(metaclass=abc.ABCMeta):
    """
    抽象工厂类
    """
    @abc.abstractmethod
    def create_course(self):
        pass

    @abc.abstractmethod
    def create_vm(self):
        pass


class BasicCourseLinuxFactory(Factory):
    """
    基础课程工厂类
    """

    def create_course(self):
        return BasicCourse()

    def create_vm(self):
        return LinuxVm()


class ProjectCourseMacFactory(Factory):
    """
    项目课程工厂类
    """

    def create_course(self):
        return ProjectCourse()

    def create_vm(self):
        return MacVm()


def get_factory():
    """
    随机获取一个工厂类
    """
    return random.choice([BasicCourseLinuxFactory, ProjectCourseMacFactory])()

if __name__ == '__main__':
    factory = get_factory()
    course = facotry.create_course()
    vm = factory.create_vm()
    print(course.get_labs())
    print(vm.start())
