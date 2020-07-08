from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
import os


from applitools.selenium import (
    logger,
    VisualGridRunner,
    Eyes,
    Target,
    BatchInfo,
    BrowserType,
    DeviceName,
)

test_url_v2 = "https://demo.applitools.com/gridHackathonV2.html"


def set_up(eyes):
    eyes.configure.set_api_key("3j06RRiK1c2pjjfw98uCO3I9bgpjCmiNSa100QhnVKRznk110")
    eyes.configure.set_batch(BatchInfo("Ultrafast Batch"))
    (
        eyes.configure.add_browser(800, 600, BrowserType.CHROME)
        .add_browser(700, 500, BrowserType.FIREFOX)
        .add_browser(1600, 1200, BrowserType.IE_11)
        .add_browser(1024, 768, BrowserType.EDGE_CHROMIUM)
        .add_browser(800, 600, BrowserType.SAFARI)
        .add_device_emulation(DeviceName.iPhone_X)
        .add_device_emulation(DeviceName.Pixel_2)
    )


def ultra_fast_test(web_driver, eyes):
    try:
        web_driver.get(test_url_v2)
        eyes.open(
            web_driver, "Demo App", "Task 1"
        )
        web_driver.maximize_window()
        eyes.check("", Target.window().fully())
        eyes.close_async()
    except Exception as e:
        eyes.abort_async()
        print(e)


def tear_down(web_driver, runner):
    web_driver.quit()
    all_test_results = runner.get_all_test_results(False)
    print(all_test_results)


web_driver = Chrome(ChromeDriverManager().install())
consecutive_runs = 10
runner = VisualGridRunner(consecutive_runs)
eyes = Eyes(runner)
set_up(eyes)

try:
    ultra_fast_test(web_driver, eyes)
finally:
    tear_down(web_driver, runner)
