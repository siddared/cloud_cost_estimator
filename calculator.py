EC2_PRICING = {

    "t2.micro": 0.0116,

    "t2.small": 0.023,

    "t3.micro": 0.0104,

    "t3.small": 0.0168,

    "t3.medium": 0.0336
}


S3_PRICE = 0.023

RDS_PRICE = 0.017

TRANSFER_PRICE = 0.09


def estimate_cost(
        ec2_type,
        ec2_hours,
        s3_storage,
        rds_instances,
        transfer):

    ec2_rate = EC2_PRICING.get(ec2_type, EC2_PRICING["t2.micro"])

    ec2_cost = (
        ec2_rate
        * ec2_hours
    )

    s3_cost = (
        s3_storage
        * S3_PRICE
    )

    rds_cost = (
        rds_instances
        * 730
        * RDS_PRICE
    )

    transfer_cost = (
        transfer
        * TRANSFER_PRICE
    )

    total = (
        ec2_cost +
        s3_cost +
        rds_cost +
        transfer_cost
    )

    return round(total, 2)