"""A Python Pulumi program"""

import pulumi
import pulumi_docker as docker

config = pulumi.Config()

# Build the Flask Image and Push it to Dockerhub
flaskImage = docker.Image(
    "pulumi_flask_alpine",
    build=docker.DockerBuild(context="flask"),
    image_name="dhanushreddy29/pulumi_flask_alpine",
    registry=docker.ImageRegistry(
        config.require("server"), config.require("username"), config.require("password")
    ),
    local_image_name="dhanushreddy29/pulumi_flask_alpine"
)

# Start the container
flask_container = docker.Container(
    "flask",
    image=flaskImage.base_image_name,
    ports=[{"internal": 5000, "external": 5000}],
)
