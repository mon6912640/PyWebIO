class AbstractSession:
    """
    由Task在当前Session上下文中调用：
        get_current_session
        get_current_task_id

        send_task_message
        next_client_event
        on_task_exception

    由Backend调用：
        send_client_event
        get_task_messages

    Task和Backend都可调用：
        close
        closed

    .. note::
        后端Backend在相应on_session_close时关闭连接时，需要保证会话内的所有消息都传送到了客户端
    """

    @staticmethod
    def get_current_session() -> "AbstractSession":
        raise NotImplementedError

    @staticmethod
    def get_current_task_id():
        raise NotImplementedError

    def __init__(self, target, on_task_message=None, on_session_close=None, **kwargs):
        raise NotImplementedError

    def send_task_message(self, message):
        raise NotImplementedError

    def next_client_event(self):
        raise NotImplementedError

    def send_client_event(self, event):
        raise NotImplementedError

    def get_task_messages(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def closed(self):
        raise NotImplementedError

    def on_task_exception(self):
        raise NotImplementedError
