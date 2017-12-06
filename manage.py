from jobplus.app import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run()
    # 使用 gevent 提供的 WSGI 服务器，并启用 WebSocket 支持
    import pywsgi
    # 创建一个 WSGIServer，包含我们的 app 和 gevent 的 WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app)
    server.serve_forever()
