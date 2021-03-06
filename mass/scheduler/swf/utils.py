#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Helper functions to register SWF domain, workflow type and activity type.
"""

# built-in modules
import math

# 3rd-party modules
from botocore.client import Config
from botocore.exceptions import ClientError
import boto3

# local modules
from mass.scheduler.swf import config


def register_domain(domain=None, region=None):
    client = boto3.client(
        'swf',
        region_name=region or config.REGION,
        config=Config(connect_timeout=config.CONNECT_TIMEOUT,
                      read_timeout=config.READ_TIMEOUT))

    # register domain for Mass
    try:
        res = client.register_domain(
            name=domain or config.DOMAIN,
            description='The SWF domain for Mass',
            workflowExecutionRetentionPeriodInDays=str(
                int(math.ceil(float(config.WORKFLOW_EXECUTION_START_TO_CLOSE_TIMEOUT) / 60 / 60 / 24)))
        )
    except ClientError:
        # DomainAlreadyExists
        pass


def register_workflow_type(domain=None, region=None):
    client = boto3.client(
        'swf',
        region_name=region or config.REGION,
        config=Config(connect_timeout=config.CONNECT_TIMEOUT,
                      read_timeout=config.READ_TIMEOUT))

    # register workflow type for Job
    try:
        res = client.register_workflow_type(
            domain=domain or config.DOMAIN,
            name=config.WORKFLOW_TYPE_FOR_JOB['name'],
            version=config.WORKFLOW_TYPE_FOR_JOB['version'],
            description='The SWF workflow type for Job of Mass.',
            defaultTaskStartToCloseTimeout=str(config.WORKFLOW_EXECUTION_START_TO_CLOSE_TIMEOUT),
            defaultExecutionStartToCloseTimeout=str(config.WORKFLOW_EXECUTION_START_TO_CLOSE_TIMEOUT),
            defaultTaskList={'name': config.DECISION_TASK_LIST},
            defaultTaskPriority='1',
            defaultChildPolicy=config.WORKFLOW_CHILD_POLICY
        )
    except ClientError:
        # TypeAlreadyExists
        pass

    # register workflow type for Task
    try:
        res = client.register_workflow_type(
            domain=domain or config.DOMAIN,
            name=config.WORKFLOW_TYPE_FOR_TASK['name'],
            version=config.WORKFLOW_TYPE_FOR_TASK['version'],
            description='The SWF workflow type for Job of Mass.',
            defaultTaskStartToCloseTimeout=str(config.WORKFLOW_EXECUTION_START_TO_CLOSE_TIMEOUT),
            defaultExecutionStartToCloseTimeout=str(config.WORKFLOW_EXECUTION_START_TO_CLOSE_TIMEOUT),
            defaultTaskList={'name': config.DECISION_TASK_LIST},
            defaultTaskPriority='1',
            defaultChildPolicy=config.WORKFLOW_CHILD_POLICY
        )
    except ClientError:
        # TypeAlreadyExists
        pass


def register_activity_type(domain=None, region=None):
    client = boto3.client(
        'swf',
        region_name=region or config.REGION,
        config=Config(connect_timeout=config.CONNECT_TIMEOUT,
                      read_timeout=config.READ_TIMEOUT))

    # register activity type for Cmd
    try:
        res = client.register_activity_type(
            domain=domain or config.DOMAIN,
            name=config.ACTIVITY_TYPE_FOR_ACTION['name'],
            version=config.ACTIVITY_TYPE_FOR_ACTION['version'],
            description='The SWF activity type for Cmd of Mass.',
            defaultTaskStartToCloseTimeout=str(config.ACTIVITY_TASK_START_TO_CLOSE_TIMEOUT),
            defaultTaskHeartbeatTimeout=str(config.ACTIVITY_HEARTBEAT_TIMEOUT),
            defaultTaskList={'name': config.ACTIVITY_TASK_LIST},
            defaultTaskPriority='1',
            defaultTaskScheduleToStartTimeout=str(config.ACTIVITY_TASK_START_TO_CLOSE_TIMEOUT),
            defaultTaskScheduleToCloseTimeout=str(config.ACTIVITY_TASK_START_TO_CLOSE_TIMEOUT)
        )
    except ClientError:
        # TypeAlreadyExists
        pass
