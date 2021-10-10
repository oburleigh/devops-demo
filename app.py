#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

import constants
from devops_demo.devops_demo_stack import DevopsDemoStack

app = cdk.App()
DevopsDemoStack(
    app, 
    f"{constants.CDK_APP_NAME}-Production",
    env=constants.ENV_PROD,
    vpc_name = "vpcdemo",
    asg_name = "asgdemo",
    lb_name = "lbdemo",
    list_name = "listdemo",
)

app.synth()
