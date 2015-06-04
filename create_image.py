# -*- coding:utf-8 -*-

__author__ = 'thiswind'

from docker.client import Client
# from docker.utils import kwargs_from_env
from io import BytesIO
import json


# kwargs = kwargs_from_env()
# kwargs['tls'].assert_hostname = False
# cli = Client(**kwargs)

cli = Client(base_url='tcp://323studio.com:0323')

STATUS = {}


def build_image_from_dockerfile_str(dockerfile_str, tag):
    dockerfile_str = str(dockerfile_str)

    f = BytesIO(dockerfile_str.encode('utf-8'))
    output = cli.build(fileobj=f, rm=True, tag=tag)
    response = [line for line in output]

    result_str = json.loads(response[-1])['stream']
    if 'Successfully built' in result_str:
        image_id = str(result_str.split(' ')[-1]).strip()
        return image_id

    return None


def build_bind9_image():
    dockerfile = '''
        FROM ubuntu:here
        ENV DEBIAN_FRONTEND=noninteractive
        RUN apt-get install -y -q bind9
    '''

    image_id = build_image_from_dockerfile_str(dockerfile, 'bind9')

    STATUS['bind9_image_id'] = image_id

    return image_id


def build_dns_server_image():
    dockerfile = '''
        FROM bind9
    '''

    image_id = build_image_from_dockerfile_str(dockerfile, 'dns_server')

    STATUS['dns_server_image_id'] = image_id

    return image_id


def run_dns_server():
    dns_server_image_id = STATUS['dns_server_image_id']

    if dns_server_image_id:
        output = cli.start(dns_server_image_id)

    pass


def stop_dns_server():
    images = cli.images()
    dns_id = ''

    pass


def remove_none_tag_images():
    images = cli.images()
    for img in images:
        tag = img['RepoTags'][-1]
        if 'none' in tag:
            img_copy = img
            cli.remove_image(img_copy, force=True)
        pass


if __name__ == '__main__':
    pass


