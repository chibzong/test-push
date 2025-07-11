from selenium import webdriver #用于操作浏览器
from selenium.webdriver.chrome.options import Options #用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service #用于管理驱动
from selenium.webdriver.common.by import By
import time
#设置启动浏览器
def shezhi():
    # 设置浏览器对象
    q1=Options()
    #禁用沙盒模式（增加兼容性)
    q1.add_argument('--no-sandbox')
    #保持浏览器打开状态（默认代码执行完关闭）
    q1.add_experimental_option('detach',True)
    #创建启动浏览器
    a1=webdriver.Chrome(service=Service('chromedriver.exe'),options=q1) #绑定一下浏览器驱动的路径，这里是相对路径，绑定一下应用的设置
    a1.implicitly_wait(3)
    return a1

a1=shezhi()
#打开指定网址
# a1.get("https://sahitest.com/demo/alertTest.htm")
# a1.get("https://sahitest.com/demo/confirmTest.htm")
#a1.get("https://sahitest.com/demo/promptTest.htm")
# a1.get("https://sahitest.com/demo/iframesTest.htm")
#a1.get("https://www.peopleapp.com/column/30048843468-500006213567")
a1.get("https://www.baidu.com/")
# a1.get("https://www.bilibili.com/")
#time.sleep(2)
#关闭当前标签页
#a1.close()
#退出浏览器并释放驱动
#a1.quit()

#浏览器最大化 maximize_window()
#浏览器最小化 minimize_window()

a1.maximize_window()
# a1.minimize_window()

#设置浏览器的打开位置
#a1.set_window_position(0,0)
#设置浏览器打开尺寸
# a1.set_window_size(600,600)
time.sleep(2)

#浏览器截图
#a1.get_screenshot_as_file('1.png')
#刷新当前网页
#a1.refresh()

#定位一个元素
#a2=a1.find_element(By.ID,'kw')
# print(a2)
#定位多个元素
# a3=a1.find_elements(By.ID,'kw1')
# print(a3)
#浏览器查找多个元素：document.getElementById('元素')
#元素定位导包：from selenium.webdriver.common.by import By

#元素交互操作

#元素输入
# a2.send_keys('nihao')
# a3 = a1.find_element(By.ID,'su')
#元素点击
# a3.click()
# time.sleep(2)
#元素清空
# a2.clear()

#通过id定位元素，一般比较准确；并不是所有网页元素都有id
#a2=a1.find_element(By.ID,'kw').send_keys('nihao')
#通过name定位元素，一般比较准确；并不是所有网页元素都有id,比id出现还要低
#a2=a1.find_elements(By.NAME,'wd')
#通过class定位元素,class值不能为空格否则报错；class值重复的有很多需要切片操作,不切片就会找第一个；有的网站是随机的
#a1.find_element(By.CLASS_NAME,'s_ipt').send_keys('nihao')
#a1.find_element(By.CLASS_NAME,'channel-icons__item').click()
#元素定位 TAG_NAME;找出<开头标签名字>基本不可能唯一
#a1.find_elements(By.TAG_NAME,'a')[3].click()
#元素定位 LINK_TEXT;通过精准链接文本找到a标签的元素；有可能有重复的需要切片
#a1.find_element(By.LINK_TEXT,'新闻').click()
#元素定位 PARTIAL_LINK_TEXT;通过模糊链接文本找到a标签的元素；有可能有重复的需要切片
#a1.find_elements(By.PARTIAL_LINK_TEXT,'图')[1].click()
# 元素定位 CSS_SELECTOR;要记得value加上单引号包起来
# 1.可以通过id定位：#id=井号+id值；
# 2.通过class定位：.class=点+class值；
# 3.不加修饰符=标签头;
# 4.通过任意类型定位:"[类型='精准值']"
# 5.通过任意类型定位:"[类型*='模糊值']"
# 6.通过任意类型定位:"[类型^='开头值']"
# 7.通过任意类型定位:"[类型$='结尾值']"
#以上这些方法都属于理论定位法，父标签和子标签的定位方式
#8.更简单的定位方式，在谷歌控制台直接右键复制selector（个别元素定位值比较长）
#a1.find_element(By.CSS_SELECTOR,"#s-top-left > a:nth-child(6)").click()
# a1.find_element(By.CSS_SELECTOR,"[onclick='showAlert()']").click()
# 元素定位 XPATH;
#1.复制谷歌浏览器xpath，通过属性+路径定位，属性如果是随机的，可能定位不到
#2.复制谷歌浏览器full xpath，缺点定位值比较长，优点是基本100%准确
#3.用艾特属性来定位比如value: '//标签(input)[@类型名（placeholder）="请输入账号"]'
#a1.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/a[1]').click()


#警告框（alert)元素交互
#演示地址：https://sahitest.com/demo/alertTest.htm

# a1.find_element(By.XPATH,'/html/body/form/input[1]').clear()
# time.sleep(2)
# a1.find_element(By.XPATH,'/html/body/form/input[1]').send_keys('nihao')
# time.sleep(2)
# a1.find_element(By.XPATH,'/html/body/form/input[3]').click()
# #获取弹框内的文本内容
# print(a1.switch_to.alert.text)
# #点击弹框确定按钮
# a1.switch_to.alert.accept()

#确认框的元素交互
#点击弹框取消按钮
#a1.switch_to.alert.dismiss()

#提示框prompt元素交互
#弹框输入内容
# a1.switch_to.alert.send_keys('nihao')
# time.sleep(2)
# a1.switch_to.alert.accept()

# #获取iframe元素
# a2=a1.find_element(By.XPATH,'/html/body/iframe')
# #进入iframe嵌套页面
# a1.switch_to.frame(a2)
# time.sleep(2)
# #进入iframe页面操作元素点击
# a1.find_element(By.XPATH,'/html/body/table/tbody/tr/td[1]/a[1]').click()
# time.sleep(2)
# #iframe嵌套页面退出,返回默认页面
# a1.switch_to.default_content()
# a1.find_element(By.XPATH,'/html/body/input[2]').click()

#获取元素文本内容
# a2=a1.find_element(By.XPATH,'//*[@id="newsContent"]/p[1]').text
# print(a2)
# #元素是否可见,看得到的是True,看不见的就是False
# a3=a1.find_element(By.XPATH,'/html/body/script[4]').is_displayed()
# print(a3)

#网页的前进和后退
a1.find_element(By.XPATH,'//*[@id="kw"]').send_keys('nihao')
time.sleep(2)
a1.find_element(By.XPATH,'//*[@id="su"]').click()
time.sleep(2)
#网页后退
a1.back()
time.sleep(2)
#网页前进
a1.forward()