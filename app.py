# coding:utf-8
from flask import Flask, render_template
app = Flask(__name__)

#视频解析网站1
@app.route('/')
def video_analysis():
    return render_template('video1.html')

#视频解析网站2
# @app.route('/video2')
# def video_analysis():
#     return render_template('video1.html')

if __name__ == '__main__':
    app.run(debug=True)
