from aws_cdk import aws_autoscaling as autoscaling
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from aws_cdk import core as cdk


class AutoscaleInfra(cdk.Construct):
# still need to replace many more hardcoded values 
    def __init__(
        self,
        scope: cdk.Construct,
        id_: str,
        vpc_name: str,
        asg_name: str,
        lb_name: str,
        list_name: str
    ) -> None:
        super().__init__(scope, id_)

        vpc = ec2.Vpc(self, vpc_name)

        asg = autoscaling.AutoScalingGroup(
            self,
            asg_name,
            vpc=vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2)
        )

        lb = elbv2.ApplicationLoadBalancer(
            self, lb_name,
            vpc=vpc,
            internet_facing=True)

        listener = lb.add_listener(list_name, port=80)
        listener.add_targets("Target", port=80, targets=[asg])
        listener.connections.allow_default_port_from_any_ipv4("Open to the world")

        asg.scale_on_request_count("AModestLoad", target_requests_per_second=1)
        cdk.CfnOutput(self,"LoadBalancer",export_name=lb_name,value=lb.load_balancer_dns_name)
