# -*- coding: utf-8 -*-

import os
os.environ['BLOG_SETTINGS'] = 'blog.config.DevelopmentConfig'


from blog import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)
