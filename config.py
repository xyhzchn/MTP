# -*- coding: utf-8 -*-
import os

class Config:
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost:3306/websnail'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)),'data.sqlite')
    SECRET_KEY = 'what does the fox say?'
    WTF_CSRF_SECRET_KEY = "whatever"
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__),"app/static/uploads")
    CASE_FOLDER = os.path.join(os.path.dirname(__file__),"testcases")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    APPIUM_LOG_LEVEL = "debug"

    db_host = os.environ.get("DB_HOST")
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    db_database = os.environ.get("DB_DATABASE")
    db_port = os.environ.get("DB_PORT")

    SHAIRED_CAPABILITIES = {
        "newCommandTimeout" : 120,
        "noSign" : True,
        "unicodeKeyboard":True,
        "resetKeyboard":True,
	#"noReset":True
    }

    #系统权限弹框中允许/拒绝按钮的id
    system_alerts = [
    	('me.sui.arizona:id/btn_right','me.sui.arizona:id/btn_left'),
        ('com.lbe.security.miui:id/accept','com.lbe.security.miui:id/reject'),
        ('com.huawei.systemmanager:id/btn_allow','com.huawei.systemmanager:id/btn_forbbid'),
        ('android:id/button1','android:id/button'),
        ('flyme:id/accept','flyme:id/reject'),
	('com.miui.securitycenter:id/allow_button','com.miui.securitycenter:id/deny_button')
    ]

    log_path = os.path.join(os.path.dirname(__file__),"logs")
    snapshot_path = os.path.join(os.path.dirname(__file__),"snapshots")


    ci_monkeyconfig = {
        "actioncount":3000,
        "actiondelay":300,
        "touchpercent":40,
        "motionpercent":20,
        "pinchzoompercent":5,
        "majornavpercent":10,
        "syskeyspercent":15,
        "appswitchpercent":10
    }


    case_template = \
'''
# -*- coding: utf-8 -*-
import sys
if "app/main/defender/main" not in sys.path:
    sys.path.append("app/main/defender/main")
from android.basecase import AndroidDevice
{% for lib in libs %}{{lib}};{% endfor %}

class TestCase(AndroidDevice):
    desc = "{{ desc }}"

    def __init__(self,ce,dc):
        self.dc = dc
        self.appium_port = ce['port']
        self.bootstrap_port = ce['bootstrap_port']
        self.device_name = dc['deviceName']
        self.appium_url = ce['url']
        self.filename = str(self.__class__).split('.')[0].split("\'")[1]
        self.casename = '%s_%s_%s' %(dc['deviceName'].replace('.','_').replace(":","_"),ce['port'],self.filename)

    def __call__(self,conflict_datas):
        super(TestCase,self).__init__(conflict_datas,command_executor=self.appium_url,desired_capabilities=self.dc)
        return self

    def __repr__(self):
        return "<Testcase:%s>" %self.filename

    def run(self):
        self.implicitly_wait(10)
        for i in range(3):
            self.sleep(1)

{% for action in actions %}
        {{ action }}
{% endfor %}
'''


    @staticmethod
    def init_app(app):
        pass


if __name__ == '__main__':
    print(os.path.dirname(__file__))
