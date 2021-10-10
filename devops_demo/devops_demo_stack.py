from aws_cdk import core as cdk

from alb_asg_ec2.platform import AutoscaleInfra


class DevopsDemoStack(cdk.Stack):

    def __init__(
        self,
        scope: cdk.Construct,
        construct_id: str,
        *,
        vpc_name: str,
        asg_name: str,
        lb_name: str,
        list_name: str,
        **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        infra = AutoscaleInfra(self, construct_id, vpc_name, asg_name, lb_name, list_name)
