# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0
import pytest
from c7n.config import Config
import argparse


def test_s3_log_sse_default_in_config():
    config = Config.empty()
    assert hasattr(config, 's3_log_sse')
    assert config.s3_log_sse == 'default'


def test_s3_log_sse_override():
    # Simulate argparse.Namespace as used in cli.py
    args = {
        's3_log_sse': 'aws:kms',
        'output_dir': 's3://mybucket/logs',
        'region': 'us-east-1',
        'regions': ['us-east-1'],
    }
    config = Config.empty(**args)
    assert config.s3_log_sse == 'aws:kms'


def test_s3_log_sse_choices():
    for value in ['default', 'aws', 'aws:kms']:
        config = Config.empty(s3_log_sse=value)
        assert config.s3_log_sse == value


def test_s3_log_sse_invalid():
    # The CLI parser enforces choices, but config does not, so this is allowed
    config = Config.empty(s3_log_sse='invalid')
    assert config.s3_log_sse == 'invalid'
