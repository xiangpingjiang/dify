from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool


class WecomRepositoriesTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]
                ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        """
            invoke tools
        """
        content = tool_parameters.get('content', '')
        if not content:
            return self.create_text_message('Invalid parameter content')

        hook_key = tool_parameters.get('hook_key', '')
        if not hook_key:
            return self.create_text_message('Invalid parameter hook_key')

        msgtype = 'text'
        api_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send'
        headers = {
            'Content-Type': 'application/json',
        }
        params = {
            'key': hook_key,
        }
        payload = {
            "msgtype": msgtype,
            "text": {
                "content": content,
            }
        }

        try:
            res = httpx.post(api_url, headers=headers, params=params, json=payload)
            if res.is_success:
                return self.create_text_message("Text message sent successfully")
            else:
                return self.create_text_message(
                    f"Failed to send the text message, status code: {res.status_code}, response: {res.text}")
        except Exception as e:
            return self.create_text_message("Failed to send message to group chat bot. {}".format(e))
