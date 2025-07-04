# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0
import os
import logging

log = logging.getLogger('custodian.config')


class Bag(dict):
    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(k)

    def __setattr__(self, k, v):
        self[k] = v


class Config(Bag):

    def copy(self, **kw):
        d = {}
        d.update(self)
        d.update(**kw)
        return Config(d)

    @classmethod
    def empty(cls, **kw):
        d = {}
        d.update({
            'region': os.environ.get('AWS_DEFAULT_REGION', 'us-east-1'),
            'regions': (),
            'cache': '',
            'profile': None,
            'account_id': None,
            'assume_role': None,
            'session_policy': None,
            'external_id': None,
            'log_group': None,
            'tracer': 'default',
            'metrics_enabled': False,
            'metrics': None,
            'output_dir': '',
            'cache_period': 0,
            'dryrun': False,
            'authorization_file': None,
            's3_log_sse': 'default',  # Added default for s3-log-sse
        })
        d.update(kw)
        return cls(d)
