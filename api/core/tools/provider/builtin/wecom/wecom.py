from core.tools.provider.builtin.wecom.tools.wecom_group_bot import WecomRepositoriesTool
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController


class GaodeProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: dict) -> None:
        WecomRepositoriesTool()
        pass
