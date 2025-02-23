from hyper_fetch.types import Plugin, DownloadRequest, DownloadResult


class CompressionPlugin(Plugin):
    """Plugin for handling compressed responses"""

    async def initialize(self) -> None:
        pass

    async def pre_request(self, request: DownloadRequest) -> DownloadRequest:
        if request.headers is None:
            request.headers = {}
        request.headers["Accept-Encoding"] = "gzip, deflate"
        return request

    async def post_response(self, result: DownloadResult) -> DownloadResult:
        return result

    async def cleanup(self) -> None:
        pass
