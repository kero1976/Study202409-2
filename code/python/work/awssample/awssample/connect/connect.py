"""
AWS Connnector.

create boto3.resource and boto3.client
"""
from logging import getLogger

import boto3

# ロガーの作成
logger = getLogger(__name__)


class Connect():
    """AWS Connnector.

    create boto3.resource and boto3.client
    """

    def __init__(self, service: str, profile_name: str = None, region_name: str = None):
        """コンストラクタ

        Args:
            service (str): サービス名
        """
        self.service = service
        self.profile_name = profile_name
        self.region_name = region_name

    def get_resource(self):
        """resourceの取得

        Returns:
            _type_: resource
        """
        if self.profile_name:
            return self._get_session().resource(self.service)
        return boto3.resource(self.service)

    def get_client(self):
        """clientの取得

        Returns:
            _type_: client
        """
        if self.profile_name:
            return self._get_session().client(self.service)
        return boto3.client(self.service)

    def _get_session(self):
        """profile_nameを使用してセッションを作成する
        """
        logger.info({
            "status": "start",
            "param": {
                "self.service": self.service,
                "self.profile_name": self.profile_name,
                "self.region_name": self.region_name
            }
        })
        session = boto3.Session(profile_name=self.profile_name, region_name=self.region_name)
        logger.info({"status": "success", "result": session})
        return session
